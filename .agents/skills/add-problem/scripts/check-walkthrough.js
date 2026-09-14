#!/usr/bin/env node
// Static + execution check for a walkthrough.html.
// Usage: node .agents/skills/add-problem/scripts/check-walkthrough.js <tier>/<NNN>-<slug>/walkthrough.html
// Fails (exit 1) on: script parse error, Python leaking into JS (e.g. `len(source)`),
// a data-state with no STATES entry, render() throwing for any state, an hl index
// outside CODE, CODE containing non-Solution boilerplate, leftover template title,
// generic boilerplate prose, or too few inline <code> references in the narration.
const fs = require("fs");
const f = process.argv[2];
if (!f) { console.error("usage: check-walkthrough.js <walkthrough.html>"); process.exit(2); }
const h = fs.readFileSync(f, "utf8");
const fail = (m) => { console.error("FAIL " + f + ": " + m); process.exit(1); };

const m = h.match(/<script>([\s\S]*)<\/script>/);
if (!m) fail("no <script> block");
const js = m[1];

// 1. Python leaking into JS (outside string literals).
const noStrings = js
  .replace(/"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'/g, '""')
  .replace(/\/\/[^\n]*/g, "")
  .replace(/\/\*[\s\S]*?\*\//g, "");
if (/\blen\(|\bNone\b|\bTrue\b|\bFalse\b|\belif\b/.test(noStrings)) fail("Python syntax in JS (len(/None/True/False/elif outside strings and comments)");

// 2. Leftover template text.
const title = (h.match(/<title>(.*?)<\/title>/) || [])[1] || "";
const h1 = (h.match(/<h1>(.*?)<\/h1>/) || [])[1] || "";
const h1Name = h1.replace(/,\s*narrated$/, "").trim();
if (!title.startsWith(h1Name)) fail("<title> '" + title + "' does not match <h1> '" + h1 + "' (leftover template title?)");
if (/A direct approach can repeatedly re-scan/.test(h)) fail("generic boilerplate STEP 2 prose");

// 3. data-state coverage.
const states = [...h.matchAll(/data-state="(\w+)"/g)].map((x) => x[1]);
if (states.length < 7) fail("only " + states.length + " steps; need 7–10");

// 4. Prose depth: inline <code> in the narration column.
const stepsHtml = (h.match(/<div class="steps">([\s\S]*?)<div class="code-final">/) || [null, ""])[1];
const codeRefs = (stepsHtml.match(/<code>/g) || []).length;
if (codeRefs < 15) fail("only " + codeRefs + " inline <code> references in steps; need >= 15 (010 has 26)");
for (const st of states) {
  const sec = h.match(new RegExp('<section class="step" data-state="' + st + '">([\\s\\S]*?)</section>'));
  const words = sec ? sec[1].replace(/<[^>]+>/g, " ").split(/\s+/).filter(Boolean).length : 0;
  if (words < 15) fail("step '" + st + "' has only " + words + " words of prose");
}

// 5. Execute the script under a DOM stub and render every state.
const ids = [...h.matchAll(/id="([\w-]+)"/g)].map((x) => x[1]);
const mk = () => ({
  style: {}, classList: { toggle() {}, add() {}, remove() {} }, setAttribute() {}, getAttribute() { return ""; },
  appendChild() { return this; }, removeChild() {}, get firstChild() { return null; },
  getBoundingClientRect() { return { top: 0, bottom: 0, height: 0 }; }, addEventListener() {},
  querySelector() { return mk(); }, querySelectorAll() { return []; }, textContent: "", innerHTML: "", hidden: false,
});
const stepEls = states.map((s) => Object.assign(mk(), { getAttribute() { return s; } }));
global.document = {
  getElementById(id) { return ids.includes(id) ? mk() : null; },
  createElementNS() { return mk(); }, createElement() { return mk(); },
  querySelector() { return mk(); }, querySelectorAll(sel) { return sel === ".step" ? stepEls : []; }, addEventListener() {},
};
global.window = { matchMedia() { return { matches: false }; }, innerHeight: 800, addEventListener() {} };
global.IntersectionObserver = function () { this.observe = function () {}; };
let CODE = null;
const src = js
  .replace(/function render\(name\)/, "global.__render = render; function render(name)")
  .replace(/var CODE = (\[[\s\S]*?\]);/, (all, arr) => all + " global.__CODE = CODE;")
  .replace(/var STATES = \{/, "global.__STATES = STATES; var STATES = global.__STATES = {");
try { new Function(src)(); } catch (e) { fail("script threw while loading: " + e.message); }
if (!global.__render) fail("could not find function render(name)");
CODE = global.__CODE;
if (!CODE) fail("could not find `var CODE = [...]`");
if (!/^class \w+:/.test(CODE[0])) fail("CODE[0] must be the class line (no imports / TreeNode boilerplate)");
if (CODE.some((l) => /^(from|import) /.test(l))) fail("CODE contains import lines");
for (const st of states) {
  try { global.__render(st); } catch (e) { fail("render('" + st + "') threw: " + e.message); }
}
const STATES = global.__STATES;
if (STATES) {
  for (const st of states) {
    if (!STATES[st]) fail("data-state '" + st + "' has no STATES entry");
    const hl = STATES[st].hl || [];
    for (const i of hl) if (i < 0 || i >= CODE.length) fail("state '" + st + "' hl index " + i + " outside CODE (" + CODE.length + " lines)");
  }
}
console.log("ok " + f + " — " + states.length + " states, " + CODE.length + " code lines, " + codeRefs + " inline code refs");
