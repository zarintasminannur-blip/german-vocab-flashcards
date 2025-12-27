import json
import random

# 1. Load data
try:
    with open('vocab.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    print("No words found! Run add.py first.")
    exit()

if not data:
    print("Vocabulary list is empty.")
    exit()

# 2. Pick a random card
card = random.choice(data)

# 3. THE TEST
print("\n" + "="*30)
print(f"🇩🇪  TEST: {card['singular']}")
print("="*30)
print("Think about: Article? Plural? Meaning?")
input("Press Enter to reveal...")

# 4. THE REVEAL
print("-" * 30)
if card['article']:
    print(f"📝 Full Form:  {card['article']} {card['singular']}")
else:
    print(f"📝 Word:       {card['singular']}")

if card['plural']:
    print(f"📚 Plural:     die {card['plural']}")

print(f"🇬🇧 Meaning:    {card['meaning']}")

if card['sentence']:
    print(f"🗣️  Context:    \"{card['sentence']}\"")
print("-" * 30 + "\n")