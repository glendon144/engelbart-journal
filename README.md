# Engelbart Journal — DemoKit Revival

**Engelbart Journal** is a fork of *DemoKit 5.1*, reimagined as a clean, AI-assisted hypertext environment for thinking, journaling, research, and experimentation. It runs on minimal hardware, supports X11 forwarding, and preserves a lineage of inspired computing going back to Doug Engelbart’s original vision of augmenting human intellect.

---

## 🌟 What It Is

Engelbart Journal is a Python/Tkinter application that integrates:

- 🧠 **AI interaction** (via the `ASK` and `IMAGE` commands)
- 🔗 **Hypertext-style navigation** with permanent links and backtracking
- 📄 **SQLite-based document storage**, with support for text, logs, and Base64-encoded image artifacts
- 🧰 A GUI interface for exploring, querying, and visually mapping your ideas

Originally revived on a cloud-hosted system named **Jazz** and remotely accessed via X11 in Tucson, Engelbart Journal is now ready for public sharing, backup, and future refinement.

---

## 💡 Why This Exists

This project was built out of a desire to:

- Preserve a working fork of DemoKit 5.1 in a *clean, merge-free repository*
- Explore the intersection of AI, journaling, and creative research
- Reflect on Engelbart’s philosophy through modern tools and small hardware
- Enable local-first workflows — no cloud required after setup

---

## 🚀 Features

- ✅ ASK: Send a query to an AI model and insert the reply into your workspace
- ✅ BACK: Return to the previous document and scroll to the clicked anchor
- ✅ IMAGE: Trigger DALL·E-style image generation and view results inline
- ✅ DIRECTORY IMPORT: Bulk-import plain text files as documents
- ✅ GREEN LINKS™: Hyperlinked references between ideas, anchored in context
- ✅ .gitignore: Clean separation of code and cache, no `.pyc` or `__pycache__` pollution

---

## 🛠️ Installation

Clone the repository:

```bash
git clone git@github.com:glendon144/engelbart-journal.git
cd engelbart-journal
```

Set up a Python virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then launch the main GUI:

```bash
python3 main.py
```

---

## 🖥️ Platform Notes

- Runs well on Raspberry Pi (tested on Pi 3 and 4)
- Remote GUI supported via X11 forwarding
- Originally bootstrapped on a 20 GB Cometera VPS named **Jazz**
- Compatible with Linux, macOS, and some thin clients

---

## 🧬 Background & Acknowledgments

This project is part of a larger conversation about the future of personal computing, AI-augmented creativity, and document-centric knowledge tools. The name *Engelbart Journal* is a tribute to Doug Engelbart, whose “Mother of All Demos” helped define the foundation of modern computing interfaces.

This codebase was salvaged, refined, and restructured collaboratively — with a balance of hands-on debugging, Git forensics, and philosophical intent.

> “We’re not just building software. We’re trying to amplify the evolution of thought.” — Inspired by Engelbart’s vision

---

## 📜 License

MIT License. Free to use, fork, remix, and reflect upon.

---

## ✍️ Author

**Glen Gross** — musician, thinker, and coder of resilient software  
**ChatGPT-4o** — co-developer, debugger, and enthusiastic collaborator  
GitHub: [glendon144](https://github.com/glendon144)
