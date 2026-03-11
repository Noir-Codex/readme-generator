from __future__ import annotations

from languages import STRINGS
from generator import ProjectInfo, build_readme, save_readme, _EMOJI_OPTIONS


# ─────────────────────────────── Helpers ───────────────────────────────────

def _ask(prompt: str, *, required: bool = True, default: str = "") -> str:
    """
    Print *prompt* and read a line from stdin.
    If *required* is True and there is no *default*, the field cannot be empty.
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        if not required or default:
            return default
        print("  ⚠️  This field cannot be empty. Please try again.")


def _ask_features(s: dict) -> list[str]:
    """Collect an open-ended list of features (one per line)."""
    print(s["q_features"])
    features: list[str] = []
    n = 1
    while True:
        item = input(s["q_feature_item"].format(n=n)).strip()
        if not item:
            if not features:
                print("  ⚠️  Please enter at least one feature.")
                continue
            break
        features.append(item)
        n += 1
    return features


def _ask_emoji(s: dict) -> str:
    """Let the user pick an emoji icon or accept the default 🚀."""
    hint = "  " + "  ".join(f"{i+1}:{e}" for i, e in enumerate(_EMOJI_OPTIONS))
    print(hint)
    raw = input(s["q_emoji"]).strip()
    if not raw:
        return "🚀"
    # Allow picking by number
    if raw.isdigit():
        idx = int(raw) - 1
        if 0 <= idx < len(_EMOJI_OPTIONS):
            return _EMOJI_OPTIONS[idx]
    return raw  # accept any emoji/text the user typed


def _separator() -> None:
    print("\n" + "─" * 48 + "\n")


# ───────────────────────────── Language picker ──────────────────────────────

def choose_language() -> dict:
    prompt = STRINGS["ru"]["choose_lang"]
    while True:
        choice = input(prompt).strip().lower()
        if choice in STRINGS:
            return STRINGS[choice]
        print(STRINGS["ru"]["invalid_lang"])


# ─────────────────────────── Main interview loop ───────────────────────────

def collect_info(s: dict) -> ProjectInfo:
    """Walk the user through all questions and return a ProjectInfo object."""
    info = ProjectInfo()

    info.name        = _ask(s["q_name"])
    info.description = _ask(s["q_description"])
    info.language    = _ask(s["q_language"])

    _separator()
    info.emoji_icon     = _ask_emoji(s)
    info.github_username = _ask(s["q_github_user"], required=False)
    if info.github_username:
        info.repo_name = _ask(s["q_repo_name"], required=False)

    _separator()
    info.features = _ask_features(s)

    _separator()
    info.install_cmd   = _ask(s["q_install"])
    info.usage_example = _ask(s["q_usage"])
    info.license_name  = _ask(s["q_license"], default="MIT")
    info.author        = _ask(s["q_author"])

    return info


# ──────────────────────────────────  Main  ─────────────────────────────────

def main() -> None:
    s = choose_language()

    print(s["welcome"])
    print(s["intro"])

    info = collect_info(s)

    print(s["saving"])
    readme_content = build_readme(info)
    save_readme(readme_content)

    _separator()
    print(s["success"])
    print(s["open_tip"])
    print()


if __name__ == "__main__":
    main()
