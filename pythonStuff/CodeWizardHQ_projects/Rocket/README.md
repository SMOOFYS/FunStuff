# Rocket Launch 🚀

A CodeWizardsHQ (CWHQ) project. You enter a launch code, a countdown runs, and
the rocket blasts off.

## ⚠️ This will NOT run with plain `python index.py`

This is a **browser program**, not a normal desktop Python program. If you open
`index.py` in VS Code and press Run, it will crash with an error like:

```
NameError: name 'document' is not defined
```

That is expected — **nothing is broken**. Here is why.

## Why it works on CodeWizardsHQ but not in VS Code

On the CodeWizardsHQ platform your Python code is **translated into JavaScript**
(using a tool called [Transcrypt](https://www.transcrypt.org/)) and then run
**inside a web page** — not by the Python interpreter.

The helper functions in `wizardlib.py` and `lesson_1_extras.py` control a web
page. They use *browser* features like `document`, `window`, and `setInterval`:

```python
def add_rocket():
    rocket_element = document.getElementById("rocket")  # 'document' only exists in a browser
    rocket_element.style.display = "block"
```

Plain Python (the kind VS Code runs) has no web page and has never heard of
`document`, so it errors out the moment the code runs. The CWHQ platform
provides the browser, which is why it works there.

You can see this in `index.html`, which loads a **compiled JavaScript copy** of
the Python — note the `__target__/index.js`:

```html
<script type="module">import * as index from './__target__/index.js';</script>
```

## How to actually see it run

- **Easiest:** open it on the CodeWizardsHQ platform, where the whole pipeline
  is already set up.
- **Locally (advanced):** install Transcrypt, compile `index.py` into a
  `__target__/index.js` folder, then serve the folder with a local web server
  (e.g. `python -m http.server`) and open `index.html` in a browser. Note: this
  copy is missing the `__target__` folder, and `index.html` also pulls some
  styles/scripts from `projects.codewizardshq.com`, so it needs internet.

## Files
- `index.py` — the program I wrote (the rocket-launch logic)
- `lesson_1_extras.py` — extra helper functions for this lesson
- `wizardlib.py` — the CWHQ library that draws and animates things in the browser
- `index.html` — the web page the program runs inside
- `*.png`, `*.jpg`, `*.mp3` — images and sound the program uses
