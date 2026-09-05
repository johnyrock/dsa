# Templates

To start a new problem, copy `problem/` to `<difficulty>/<NNN>-<slug>/` and rename the three
`slug*` files to the problem's snake_case name, e.g. `two_sum.py`, `two_sum_annotated.py`,
`test_two_sum.py`. Run a test with `python3 <folder>/test_<slug>.py`.

```bash
cp -R templates/problem easy/002-valid-anagram
cd easy/002-valid-anagram
mv slug.py valid_anagram.py && mv slug_annotated.py valid_anagram_annotated.py && mv test_slug.py test_valid_anagram.py
```
