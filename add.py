import json
import os

def load_data():
    if not os.path.exists('vocab.json'): return []
    try:
        with open('vocab.json', 'r', encoding='utf-8') as f: return json.load(f)
    except: return []

def save_data(data):
    with open('vocab.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

print("--- 🇩🇪 Add a New German Word 🇩🇪 ---")

# 1. Ask for Category
category = input("Category (e.g. Food, Travel, Animals): ").strip().capitalize()
if not category: category = "General"

# 2. Ask for Word Details
article = input("Article (der/die/das): ").strip().lower()
singular = input("Singular Word: ").strip()
plural = input("Plural Form: ").strip()
meaning = input("English Meaning: ").strip()
sentence = input("Example Sentence: ").strip()

new_entry = {
    "category": category,
    "article": article,
    "singular": singular,
    "plural": plural,
    "meaning": meaning,
    "sentence": sentence
}

data = load_data()
data.append(new_entry)
save_data(data)

print(f"\n✅ Saved to ['{category}']: {article} {singular}")