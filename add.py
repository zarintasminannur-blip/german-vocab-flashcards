import json
import os

# 1. Load existing data
if os.path.exists('vocab.json'):
    with open('vocab.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
else:
    data = []

print("--- 🇩🇪 Add a New German Word 🇩🇪 ---")
print("(Tip: If it's a verb, you can leave Article/Plural empty by pressing Enter)")

# 2. Ask for detailed input
article = input("1. Article (der/die/das): ").strip()
singular = input("2. Singular Word: ").strip()
plural = input("3. Plural Form: ").strip()
meaning = input("4. English Meaning: ").strip()
sentence = input("5. Example Sentence: ").strip()

# 3. Structure the data effectively
new_entry = {
    "article": article,
    "singular": singular,
    "plural": plural,
    "meaning": meaning,
    "sentence": sentence
}

# 4. Save to file
data.append(new_entry)
with open('vocab.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"\n✅ Saved: {article} {singular} (Pl: {plural})")