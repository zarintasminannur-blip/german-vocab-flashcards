# 🇩🇪 Deutsch Flashcards: Interactive Vocabulary Trainer

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

A smart, visual desktop application designed to help learners master German vocabulary, specifically focusing on the difficult "Der, Die, Das" gender rules using visual color association psychology.

![App Screenshot](screenshot.png)
*(Add a screenshot of your app here if you have one)*

## 🌟 Key Features

### 🎨 Visual Gender Coding
German nouns are notoriously hard to memorize because of the three genders. This app uses color psychology to reinforce memory:
* **🟦 Der (Masculine):** The card turns **Blue**.
* **🟥 Die (Feminine):** The card turns **Pink**.
* **🟩 Das (Neutral):** The card turns **Green**.
* **🟨 Verbs/Adjectives:** The card turns **Yellow**.

### 📚 Structured Learning
* **Category Filtering:** Choose to study specific topics (e.g., "Fruits", "Travel", "Furniture") via a dropdown menu.
* **Contextual Learning:** Cards display the Article, Singular, Plural, Meaning, and an **Example Sentence**.
* **Spaced Repetition:** Mark cards as "I Know It" to remove them from the current session, or "I Forgot" to reshuffle them back in.

### ⚡ Easy Vocabulary Management
Includes a dedicated **Vocabulary Manager Dashboard** (`vocab_manager.py`) that allows:
* **Manual Entry:** Add words one by one via a form.
* **Bulk Import:** Paste JSON data directly from AI tools (like ChatGPT/Gemini) to add 50+ words instantly.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **GUI Framework:** Tkinter (Standard Python Interface)
* **Data Storage:** JSON (Human-readable `vocab.json`)
* **Version Control:** Git & GitHub

## 🚀 Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/german-vocab-flashcards.git](https://github.com/YOUR_USERNAME/german-vocab-flashcards.git)
    cd german-vocab-flashcards
    ```

2.  **Run the Flashcard App**
    ```bash
    python flashcard_gui.py
    ```

3.  **Run the Vocabulary Manager (To add words)**
    ```bash
    python vocab_manager.py
    ```

## 📂 Project Structure

| File | Description |
| :--- | :--- |
| `flashcard_gui.py` | The main application window where you study. |
| `vocab_manager.py` | The dashboard to add new words or categories. |
| `vocab.json` | The database storing all words, meanings, and categories. |
| `add.py` | (Legacy) Simple command-line script for adding words. |

## 📝 How to Bulk Import Words
To add many words at once using the **Manager**:
1.  Ask an AI (Gemini/ChatGPT): *"Give me 20 German words for 'Kitchen' in JSON format with keys: category, article, singular, plural, meaning, sentence."*
2.  Copy the JSON code block.
3.  Open `vocab_manager.py`.
4.  Click **"Import from Clipboard"**.

## 🔮 Future Roadmap
* [ ] Add Audio/Pronunciation support (Text-to-Speech).
* [ ] Add a "Night Mode" toggle.
* [ ] Create a scorecard to track long-term progress.

## 👤 Author
**Zarin Tasmin An Nur**
* Research Assistant | Aspiring PhD Researcher
* International Student in Germany

---
*Created with ❤️ and Python.*
