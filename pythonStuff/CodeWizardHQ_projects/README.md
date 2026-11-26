These are CodeWizardsHQ (CWHQ) projects.

## This will NOT run with plain `python index.py`

With all CWHQ projects, this is a **browser program**, not a normal
desktop Python program. Opening `index.py` in VS Code and pressing Run will
crash with an error like:

```
NameError: name 'document' is not defined
```

That is expected -> **nothing is broken**.

## Why it works on CodeWizardsHQ but not in VS Code

On the CodeWizardsHQ platform your Python code is **translated into JavaScript**
(using a tool called [Transcrypt](https://www.transcrypt.org/)) and then run
**inside a web page** — not by the Python interpreter.

The helper functions in `wizardlib.py` control a web page using *browser*
features like `document`, `window`, and `setInterval`. Plain Python (the kind
VS Code runs) has no web page and has never heard of `document`, so it errors
out the moment the code runs. The CWHQ platform provides the browser, which is
why it works there.

The `index.html` file runs a **compiled JavaScript copy** of the Python from a
`__target__/index.js` folder, not the `.py` file directly.

## How to actually see it run

- **Easiest:** open it on the CodeWizardsHQ platform, where the whole pipeline
  is already set up.
- **Locally (advanced):** install Transcrypt, compile `index.py` into a
  `__target__/index.js` folder, then serve the folder with a local web server
  (e.g. `python -m http.server`) and open `index.html` in a browser. The CWHQ
  pages also pull some styles/scripts from `projects.codewizardshq.com`, so this
  needs internet.

## Files (per frame)
- `index.py` — the program, main file to run
- `wizardlib.py` — the CWHQ library that draws and animates things in the browser
- `index.html` — the web page the program runs inside
- `*.png`, `*.jpg` — the images used by any viewed program
