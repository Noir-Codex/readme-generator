<div align="center">

# 🚀 README Generator

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logoColor=white&logo=python)
![License](https://img.shields.io/badge/license-MIT-brightgreen?style=for-the-badge)
![GitHub Stars](https://img.shields.io/github/stars/Noir-Codex/readme-generator?style=for-the-badge&color=yellow)
![GitHub Forks](https://img.shields.io/github/forks/Noir-Codex/readme-generator?style=for-the-badge&color=blue)

<br/>

<p>An interactive CLI tool that automatically generates a beautiful <code>README.md</code> for your GitHub projects. Supports Russian and English.</p>

🇷🇺 [Читать на русском](README_RU.md)

</div>

---

## 📋 Table of Contents

- [✨ Features](#-features)
- [⚡ Quick Start](#-quick-start)
- [📦 Installation](#-installation)
- [▶️ Usage](#️-usage)
- [📁 Project Structure](#-project-structure)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## ✨ Features

- ✅ **Bilingual interface** — Russian 🇷🇺 and English 🇬🇧, chosen at startup
- ✅ **Auto-generated badges** — language (with logo & color), license, GitHub Stars / Forks / Issues
- ✅ **Centered header** — `<div align="center">` like popular open-source projects
- ✅ **Project emoji icon** — pick from 10 options or type your own
- ✅ **Quick Start section** — `git clone` + install + run in one place
- ✅ **Contributing section** — standard guide for contributors
- ✅ **Beautiful footer** — author link + ⭐ call-to-action
- ✅ **Zero dependencies** — pure Python standard library only (Python 3.8+)

---

## ⚡ Quick Start

```bash
git clone https://github.com/Noir-Codex/readme-generator.git
cd readme-generator
```

```bash
python3 main.py
```

---

## 📦 Installation

No external packages needed — just **Python 3.8+**.

```bash
git clone https://github.com/Noir-Codex/readme-generator.git
cd readme-generator
python3 main.py
```

---

## ▶️ Usage

```bash
python3 main.py
```

The program walks you through a short interview:

```
Choose language / Выберите язык [ru/en]: en

╔══════════════════════════════════════════════╗
║        🚀  README Generator  v1.0            ║
║   Automatically creates a beautiful README.md ║
╚══════════════════════════════════════════════╝

📌 Project name: My Awesome App
📝 Short description: A tool that does awesome things
💻 Main programming language: Python

  1:🚀  2:⚡  3:🎯  4:🛠️  5:🌟  6:🔥  7:💡  8:🎨  9:📦  10:🤖
🎨 Project emoji icon (Enter for default 🚀): 2
🐙 GitHub username (Enter to skip): Noir-Codex
📂 GitHub repository name (Enter to skip): my-awesome-app

✨ Features (one per line, empty line to finish):
   ➤ Feature 1: Fast performance
   ➤ Feature 2: Easy to use
   ➤ Feature 3:

📦 Installation command: pip install -r requirements.txt
▶️  Usage example: python main.py
📄 License: MIT
👤 Author: Noir-Codex

✅ README.md has been created successfully in the current directory!
```

---

## 📁 Project Structure

```
readme-generator/
├── main.py         # Entry point: language picker, interview loop
├── generator.py    # Badge builder + Markdown template assembler
├── languages.py    # UI strings in RU / EN
├── README.md       # This file (English)
└── README_RU.md    # Russian version
```

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a **Pull Request**

---

## 📄 License

This project is licensed under the **MIT** license.
See the [LICENSE](https://github.com/Noir-Codex/readme-generator/blob/main/LICENSE) file for details.

---

<div align="center">

Made with ❤️ by **[Noir-Codex](https://github.com/Noir-Codex)**

⭐ Star this project if you found it helpful!

</div>
