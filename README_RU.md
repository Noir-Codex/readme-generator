<div align="center">

# 🚀 README Generator

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logoColor=white&logo=python)
![License](https://img.shields.io/badge/license-MIT-brightgreen?style=for-the-badge)
![GitHub Stars](https://img.shields.io/github/stars/Noir-Codex/readme-generator?style=for-the-badge&color=yellow)
![GitHub Forks](https://img.shields.io/github/forks/Noir-Codex/readme-generator?style=for-the-badge&color=blue)

<br/>

<p>Интерактивный CLI-инструмент для автоматической генерации красивого <code>README.md</code> для GitHub-проектов. Поддерживает русский и английский языки.</p>

🇬🇧 [Read in English](README.md)

</div>

---

## 📋 Содержание

- [✨ Возможности](#-возможности)
- [⚡ Быстрый старт](#-быстрый-старт)
- [📦 Установка](#-установка)
- [▶️ Использование](#️-использование)
- [📁 Структура проекта](#-структура-проекта)
- [🤝 Участие в разработке](#-участие-в-разработке)
- [📄 Лицензия](#-лицензия)

---

## ✨ Возможности

- ✅ **Двуязычный интерфейс** — русский 🇷🇺 и английский 🇬🇧, выбирается при запуске
- ✅ **Автоматические badges** — язык (с логотипом и цветом), лицензия, GitHub Stars / Forks / Issues
- ✅ **Центрированный заголовок** — `<div align="center">` как у популярных open-source проектов
- ✅ **Emoji-иконка проекта** — выбор из 10 вариантов или свой символ
- ✅ **Секция Quick Start** — `git clone` + install + run в одном месте
- ✅ **Секция Contributing** — стандартный гайд для контрибьюторов
- ✅ **Красивый footer** — ссылка на автора + призыв поставить ⭐
- ✅ **Нет внешних зависимостей** — только стандартная библиотека Python 3.8+

---

## ⚡ Быстрый старт

```bash
git clone https://github.com/Noir-Codex/readme-generator.git
cd readme-generator
```

```bash
python3 main.py
```

---

## 📦 Установка

Внешних пакетов не требуется — только **Python 3.8+**.

```bash
git clone https://github.com/Noir-Codex/readme-generator.git
cd readme-generator
python3 main.py
```

---

## ▶️ Использование

```bash
python3 main.py
```

Программа проведёт через интерактивный опрос:

```
Выберите язык / Choose language [ru/en]: ru

╔══════════════════════════════════════════════╗
║        🚀  README Generator  v1.0            ║
║   Автоматически создаёт красивый README.md   ║
╚══════════════════════════════════════════════╝

📌 Название проекта: My Awesome App
📝 Краткое описание: Делает что-то крутое
💻 Основной язык программирования: Python

  1:🚀  2:⚡  3:🎯  4:🛠️  5:🌟  6:🔥  7:💡  8:🎨  9:📦  10:🤖
🎨 Эмодзи-иконка проекта (Enter — 🚀 по-умолчанию): 2
🐙 GitHub username (Enter — пропустить): Noir-Codex
📂 Название репозитория на GitHub (Enter — пропустить): my-awesome-app

✨ Возможности (каждая с новой строки, пустая строка — конец):
   ➤ Возможность 1: Быстрая работа
   ➤ Возможность 2: Простая установка
   ➤ Возможность 3:

📦 Команда установки: pip install -r requirements.txt
▶️  Пример запуска: python main.py
📄 Лицензия: MIT
👤 Автор: Noir-Codex

✅ Файл README.md успешно создан в текущей папке!
```

---

## 📁 Структура проекта

```
readme-generator/
├── main.py         # Точка входа: выбор языка, опрос, запуск генерации
├── generator.py    # Генерация badges + сборка Markdown-шаблона
├── languages.py    # Строки интерфейса на RU / EN
├── README.md       # Английская версия
└── README_RU.md    # Этот файл (русский)
```

---

## 🤝 Участие в разработке

Вклад в проект приветствуется! Как начать:

1. **Fork** репозиторий
2. Создай ветку для фичи: `git checkout -b feature/крутая-фича`
3. Зафиксируй изменения: `git commit -m 'Добавить крутую фичу'`
4. Запушь ветку: `git push origin feature/крутая-фича`
5. Открой **Pull Request**

---

## 📄 Лицензия

Этот проект распространяется под лицензией **MIT**.
Подробнее — в файле [LICENSE](https://github.com/Noir-Codex/readme-generator/blob/main/LICENSE).

---

<div align="center">

Сделано с ❤️ автором **[Noir-Codex](https://github.com/Noir-Codex)**

⭐ Поставь звезду, если проект оказался полезным!

</div>
