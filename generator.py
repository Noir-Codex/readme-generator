from __future__ import annotations
from dataclasses import dataclass, field
from typing import List


# ─────────────────────────────────── Data ──────────────────────────────────

@dataclass
class ProjectInfo:
    """All user-provided data about the project."""
    name: str = ""
    description: str = ""
    language: str = ""
    features: List[str] = field(default_factory=list)
    install_cmd: str = ""
    usage_example: str = ""
    license_name: str = "MIT"
    author: str = ""
    github_username: str = ""
    repo_name: str = ""
    emoji_icon: str = "🚀"


# ───────────────────────────────── Badges ──────────────────────────────────

# Well-known languages → shields.io colors + logos
_LANG_META: dict[str, tuple[str, str]] = {
    "python":     ("3776AB", "python"),
    "javascript": ("F7DF1E", "javascript"),
    "typescript": ("3178C6", "typescript"),
    "java":       ("ED8B00", "openjdk"),
    "kotlin":     ("7F52FF", "kotlin"),
    "swift":      ("F05138", "swift"),
    "rust":       ("DEA584", "rust"),
    "go":         ("00ADD8", "go"),
    "c":          ("555555", "c"),
    "c++":        ("00599C", "cplusplus"),
    "c#":         ("239120", "csharp"),
    "ruby":       ("CC342D", "ruby"),
    "php":        ("777BB4", "php"),
    "scala":      ("DC322F", "scala"),
    "dart":       ("0175C2", "dart"),
    "lua":        ("2C2D72", "lua"),
    "shell":      ("4EAA25", "gnubash"),
    "html":       ("E34F26", "html5"),
    "css":        ("1572B6", "css3"),
    "r":          ("276DC3", "r"),
}

_LICENSE_COLORS: dict[str, str] = {
    "mit":          "brightgreen",
    "apache-2.0":   "blue",
    "gpl-3.0":      "red",
    "bsd-2-clause": "orange",
    "bsd-3-clause": "orange",
    "unlicense":    "lightgrey",
}

_EMOJI_OPTIONS = ["🚀", "⚡", "🎯", "🛠️", "🌟", "🔥", "💡", "🎨", "📦", "🤖"]


def _language_badge(language: str) -> str:
    lang_lower = language.lower()
    color, logo = _LANG_META.get(lang_lower, ("blue", ""))
    label = language.replace(" ", "%20").replace("-", "--")
    logo_part = f"&logo={logo}" if logo else ""
    return (
        f"![{language}](https://img.shields.io/badge/"
        f"{label}-{color}?style=for-the-badge&logoColor=white{logo_part})"
    )


def _license_badge(license_name: str) -> str:
    lic_lower = license_name.lower()
    color = _LICENSE_COLORS.get(lic_lower, "lightgrey")
    label = license_name.replace(" ", "%20").replace("-", "--")
    return (
        f"![License](https://img.shields.io/badge/license-{label}"
        f"-{color}?style=for-the-badge)"
    )


def _github_badge(kind: str, username: str, repo: str) -> str:
    """Generate GitHub stars / forks / issues badges."""
    icons = {
        "stars":  ("GitHub Stars",  "stars",  "yellow"),
        "forks":  ("GitHub Forks",  "forks",  "blue"),
        "issues": ("GitHub Issues", "issues", "red"),
    }
    label, stat, color = icons[kind]
    return (
        f"![{label}](https://img.shields.io/github/{stat}/{username}/{repo}"
        f"?style=for-the-badge&color={color})"
    )


def build_badges(info: ProjectInfo) -> str:
    parts = [
        _language_badge(info.language),
        _license_badge(info.license_name),
    ]
    if info.github_username and info.repo_name:
        parts += [
            _github_badge("stars",  info.github_username, info.repo_name),
            _github_badge("forks",  info.github_username, info.repo_name),
            _github_badge("issues", info.github_username, info.repo_name),
        ]
    return "\n".join(parts)


# ──────────────────────────────── Helpers ──────────────────────────────────

def _features_list(features: List[str]) -> str:
    return "\n".join(f"- ✅ {f}" for f in features if f.strip())


def _repo_url(info: ProjectInfo) -> str:
    if info.github_username and info.repo_name:
        return f"https://github.com/{info.github_username}/{info.repo_name}"
    return "#"


# ──────────────────────────────── Template ─────────────────────────────────

def build_readme(info: ProjectInfo) -> str:
    """Assemble the full, beautiful README.md content."""
    badges   = build_badges(info)
    features = _features_list(info.features)
    repo_url = _repo_url(info)

    # Determine if we have a real GitHub repo for TOC links / clone section
    has_repo = bool(info.github_username and info.repo_name)
    clone_block = (
        f"```bash\ngit clone {repo_url}\ncd {info.repo_name}\n```\n\n"
        if has_repo else ""
    )

    toc = "\n".join([
        "- [✨ Features](#-features)",
        "- [⚡ Quick Start](#-quick-start)",
        "- [📦 Installation](#-installation)",
        "- [▶️ Usage](#️-usage)",
        "- [🤝 Contributing](#-contributing)",
        "- [📄 License](#-license)",
    ])

    readme = f"""\
<div align="center">

# {info.emoji_icon} {info.name}

{badges}

<br/>

<p>{info.description}</p>

</div>

---

## 📋 Table of Contents

{toc}

---

## ✨ Features

{features}

---

## ⚡ Quick Start

{clone_block}```bash
{info.install_cmd}
```

```bash
{info.usage_example}
```

---

## 📦 Installation

Make sure you have the required dependencies installed:

```bash
{info.install_cmd}
```

---

## ▶️ Usage

```bash
{info.usage_example}
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

This project is licensed under the **{info.license_name}** license.
See the [LICENSE]({repo_url}/blob/main/LICENSE) file for details.

---

<div align="center">

Made with ❤️ by **[{info.author}](https://github.com/{info.github_username or info.author})**

⭐ Star this project if you found it helpful!

</div>
"""
    return readme


def save_readme(content: str, path: str = "README.md") -> None:
    """Write README content to a file."""
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)
