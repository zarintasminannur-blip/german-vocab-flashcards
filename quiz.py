import json
import random
import os

if not os.path.exists('vocab.json'):
    print("No words found.")
    exit()

with open('vocab.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

if not data:
    print("List is empty.")
    exit()

card = random.choice(data)

print("\n" + "="*30)
print(f"🇩🇪  TEST: {card['singular']}")
print("="*30)
input("Press Enter...")

full_word = f"{card['article']} {card['singular']}"
print(f"📝 Answer:  {full_word}")
print(f"📚 Plural:  die {card['plural']}")
print(f"🇬🇧 Meaning: {card['meaning']}")
print("-" * 30 + "\n")