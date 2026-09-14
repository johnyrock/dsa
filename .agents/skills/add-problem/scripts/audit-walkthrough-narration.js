#!/usr/bin/env node

// Deterministic audit for walkthrough structure and common narration mistakes.
// It deliberately avoids judging style beyond specific, easy-to-explain phrases.
const fs = require("fs");

const files = process.argv.slice(2);
if (files.length === 0) {
  console.error("usage: audit-walkthrough-narration.js <walkthrough.html> [...]");
  process.exit(2);
}

let failed = false;
let failedFiles = 0;
let issues = 0;

function stripNonNarrative(html) {
  return html
    .replace(/<!--[\s\S]*?-->/g, " ")
    .replace(/<pre\b[^>]*>[\s\S]*?<\/pre>/gi, " ")
    .replace(/<code\b[^>]*>[\s\S]*?<\/code>/gi, " ")
    .replace(/<[^>]+>/g, " ")
    .replace(/&(?:[a-z]+|#\d+|#x[\da-f]+);/gi, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function narrativeBlocks(html) {
  const patterns = [
    /<p\b[^>]*>([\s\S]*?)<\/p>/gi,
    /<li\b[^>]*>([\s\S]*?)<\/li>/gi,
    /<div\b(?=[^>]*\bclass=["'][^"']*\bcallout\b[^"']*["'])[^>]*>([\s\S]*?)<\/div>/gi,
  ];
  const blocks = [];
  for (const pattern of patterns) {
    for (const match of html.matchAll(pattern)) {
      const text = stripNonNarrative(match[1]);
      if (text) blocks.push({ index: match.index, text });
    }
  }
  return blocks.sort((a, b) => a.index - b.index);
}

function excerpt(text) {
  return text.length <= 160 ? text : `${text.slice(0, 157)}...`;
}

function hasFirstPersonBefore(text, boundary) {
  const sentenceStart = Math.max(
    text.lastIndexOf(".", boundary),
    text.lastIndexOf("!", boundary),
    text.lastIndexOf("?", boundary),
    text.lastIndexOf(";", boundary),
    text.lastIndexOf(":", boundary),
  ) + 1;
  return /\b(?:I|my|mine|myself)\b/i.test(text.slice(sentenceStart, boundary));
}

function addNarrationErrors(errors, blocks) {
  const manualVoice = /\b(?:you|your|we|our|notice)\b/i;
  const imperativeVerb = "(?:add|advance|append|avoid|build|check|choose|compare|create|define|drop|fill|find|follow|iterate|keep|look|make|move|pick|place|pop|process|push|put|read|record|remember|remove|reset|return|run|save|scan|set|skip|sort|start|store|swap|take|track|treat|try|turn|use|walk|write)";
  const leadingImperative = new RegExp(`^(?:please\\s+)?(?:only\\s+)?${imperativeVerb}\\b`, "i");
  // A manual instruction may begin after a sentence or explanatory clause,
  // not only at the start of its containing paragraph. The optional lead-ins
  // catch prose such as “So push ...”, while requiring a boundary prevents
  // matching first-person narration such as “I push ...”.
  const embeddedImperative = new RegExp(`(?:^|[.!?;:]\\s+)(?:(?:so|then|now)\\s+)?(?:please\\s+)?(?:only\\s+)?${imperativeVerb}\\b`, "i");
  const commaImperative = new RegExp(`,\\s+(?:(?:so|then|now)\\s+)?(?:please\\s+)?(?:only\\s+)?${imperativeVerb}\\b`, "ig");
  const awkwardNoThenFirstPerson = /\bno\b[^.!?]{0,100}\bI\s+(?:check|scan|test|look|need|want)\b/i;
  const awkwardSequenceLeadIn = /\ba\s+sequence\s+that\s+supports\b[^:]{0,120}:\s*I\b/i;
  const awkwardComplexityLeadIn = /\bI\s+first\s+scan\s+O\s*\(/i;
  const boilerplate = [
    ["repeated boilerplate 'I can improve'", /\bI\s+can\s+improve\b/i],
    ["repeated boilerplate 'This baseline is correct'", /\bThis\s+baseline\s+is\s+correct\b/i],
    ["repeated boilerplate 'My first correct baseline'", /\bMy\s+first\s+correct\s+baseline\b/i],
    ["generic opening 'I\'ll start with the direct approach'", /\bI(?:'|’)?ll\s+start\s+with\s+the\s+direct\s+approach\b/i],
    ["generic transition 'then improve it as I trace the running example'", /\bthen\s+improve\s+it\s+as\s+I\s+trace\s+the\s+running\s+example\b/i],
  ];

  for (const { text } of blocks) {
    if (manualVoice.test(text)) {
      errors.push(`manual voice (${text.match(manualVoice)[0]}): "${excerpt(text)}"`);
    }
    if (leadingImperative.test(text)) {
      errors.push(`paragraph-leading imperative: "${excerpt(text)}"`);
    } else if (embeddedImperative.test(text)) {
      errors.push(`sentence/clause imperative: "${excerpt(text)}"`);
    } else {
      let match;
      commaImperative.lastIndex = 0;
      while ((match = commaImperative.exec(text))) {
        if (!hasFirstPersonBefore(text, match.index)) {
          errors.push(`sentence/clause imperative: "${excerpt(text)}"`);
          break;
        }
      }
    }
    if (awkwardNoThenFirstPerson.test(text)) {
      errors.push(`awkward rewrite 'no ... I ...': "${excerpt(text)}"`);
    }
    if (awkwardSequenceLeadIn.test(text)) {
      errors.push(`awkward list lead-in 'a sequence that supports ...: I ...': "${excerpt(text)}"`);
    }
    if (awkwardComplexityLeadIn.test(text)) {
      errors.push(`awkward complexity lead-in 'I first scan O(...)': "${excerpt(text)}"`);
    }
    for (const [label, pattern] of boilerplate) {
      if (pattern.test(text)) errors.push(`${label}: "${excerpt(text)}"`);
    }
  }
}

for (const file of files) {
  let html;
  try {
    html = fs.readFileSync(file, "utf8");
  } catch (error) {
    console.error(`fail ${file}: ${error.message}`);
    failed = true;
    continue;
  }

  const sections = [...html.matchAll(/<section\b[^>]*class=["'][^"']*\bstep\b[^"']*["'][^>]*>[\s\S]*?<\/section>/gi)]
    .map((match) => match[0]);
  const problem = sections.find((section) => /data-state=["']problem["']/i.test(section)
    && /<h2>\s*The problem\s*<\/h2>/i.test(section));
  const instinct = sections.find((section) => /<h2>\s*First instinct(?:\s*:|\s*<|\s*$)/i.test(section));
  const errors = [];

  if (!problem) {
    errors.push("missing a data-state=problem section titled 'The problem'");
  } else {
    const problemText = stripNonNarrative(problem);
    const problemFirstPerson = /\b(?:I|me|my|mine|myself)\b/i;
    if (problemFirstPerson.test(problemText)) {
      errors.push(`The problem must stay neutral (first-person pronoun): "${excerpt(problemText)}"`);
    }
  }
  if (!instinct) {
    errors.push("missing a section titled 'First instinct'");
  } else {
    if (!/<pre\b[^>]*class=["'][^"']*\bcode\b[^"']*["'][^>]*>/i.test(instinct)) {
      errors.push("First instinct is missing a baseline <pre class=\"code\"> block");
    }
    const plain = instinct.replace(/<[^>]+>/g, " ").replace(/&[a-z]+;/gi, " ");
    if (!/O\s*\([^)]*\)\s*(?:time|running time)|(?:time|running time)[\s\S]{0,100}O\s*\(/i.test(plain)) {
      errors.push("First instinct is missing explicit time complexity");
    }
    if (!/O\s*\([^)]*\)\s*(?:extra )?space|(?:extra )?space[\s\S]{0,100}O\s*\(/i.test(plain)) {
      errors.push("First instinct is missing explicit space complexity");
    }
  }

  // The Problem section is intentionally neutral. Audit the header and every
  // later narration block, while stripping code examples to avoid false hits
  // from variables, comments, or string literals.
  const header = html.match(/<header\b[^>]*>([\s\S]*?)<\/header>/i);
  const blocks = [
    ...(header ? narrativeBlocks(header[1]) : []),
    ...sections
      .filter((section) => !/data-state=["']problem["']/i.test(section))
      .flatMap(narrativeBlocks),
  ];
  addNarrationErrors(errors, blocks);

  if (errors.length) {
    console.error(`fail ${file}: ${errors.join("; ")}`);
    failed = true;
    failedFiles += 1;
    issues += errors.length;
  } else {
    console.log(`ok ${file}`);
  }
}

const summary = `summary: ${failedFiles} file(s) failed, ${issues} issue(s)`;
if (failed) console.error(summary);
else console.log(summary);
process.exit(failed ? 1 : 0);
