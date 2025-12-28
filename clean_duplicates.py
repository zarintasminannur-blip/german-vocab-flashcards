import json
import os

def clean_vocab():
    input_filename = 'vocab.json'
    output_filename = 'vocab_cleaned.json'

    if not os.path.exists(input_filename):
        print(f"❌ Error: {input_filename} not found.")
        return

    try:
        with open(input_filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        print(f"📂 Loaded {len(data)} words from {input_filename}...")

        unique_words = {}
        cleaned_list = []
        duplicates_count = 0

        for entry in data:
            # Normalize the word: lowercase and stripped of whitespace
            german_word = entry.get('singular', '').strip()
            
            # Create a unique key (Word + Meaning) to be safe, 
            # or just (Word) if you want strict unique German words.
            # Here we use just the German word to ensure no duplicate flashcards.
            unique_key = german_word.lower()

            if unique_key and unique_key not in unique_words:
                unique_words[unique_key] = True
                cleaned_list.append(entry)
            else:
                duplicates_count += 1
                print(f"   ⚠️ Removed Duplicate: {german_word} ({entry.get('category')})")

        # Save the new list
        with open(output_filename, 'w', encoding='utf-8') as f:
            json.dump(cleaned_list, f, indent=4, ensure_ascii=False)

        print("-" * 30)
        print(f"✅ Success! Created {output_filename}")
        print(f"📉 Original count: {len(data)}")
        print(f"📈 Cleaned count:  {len(cleaned_list)}")
        print(f"🗑️  Removed {duplicates_count} duplicates.")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    clean_vocab()