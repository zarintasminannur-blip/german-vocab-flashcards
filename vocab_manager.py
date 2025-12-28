import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

# --- CONFIGURATION ---
FILE_NAME = 'vocab.json'
COLOR_BG = "#f0f0f0"
COLOR_ACCENT = "#4a90e2" 

class VocabManager:
    def __init__(self, root):
        self.root = root
        self.root.title("📚 Vocabulary Manager")
        self.root.geometry("600x530") # Made slightly taller
        self.root.config(bg=COLOR_BG, padx=20, pady=20)

        # Load Data
        self.data = self.load_data()
        self.categories = sorted(list(set(d.get('category', 'General') for d in self.data)))

        # --- LEFT SIDE: MANUAL ENTRY ---
        self.frame_manual = tk.LabelFrame(root, text="Add Single Word", bg=COLOR_BG, font=("Arial", 12, "bold"), padx=15, pady=15)
        self.frame_manual.place(x=0, y=0, width=320, height=490)

        # 1. Category Input
        tk.Label(self.frame_manual, text="Category:", bg=COLOR_BG).pack(anchor="w")
        self.cat_var = tk.StringVar()
        self.cat_box = ttk.Combobox(self.frame_manual, textvariable=self.cat_var, values=self.categories)
        self.cat_box.pack(fill="x", pady=(0, 10))

        # 2. Article Input (UPDATED to Dropdown)
        tk.Label(self.frame_manual, text="Article:", bg=COLOR_BG).pack(anchor="w")
        self.art_var = tk.StringVar()
        # "None" is for Verbs/Adjectives
        self.art_box = ttk.Combobox(self.frame_manual, textvariable=self.art_var, values=["der", "die", "das", "None (Verb/Adj)"], state="readonly")
        self.art_box.pack(fill="x", pady=(0, 10))

        # 3. Word Details
        tk.Label(self.frame_manual, text="Singular Word:", bg=COLOR_BG).pack(anchor="w")
        self.entry_singular = tk.Entry(self.frame_manual)
        self.entry_singular.pack(fill="x", pady=(0, 10))

        tk.Label(self.frame_manual, text="Plural Form (optional):", bg=COLOR_BG).pack(anchor="w")
        self.entry_plural = tk.Entry(self.frame_manual)
        self.entry_plural.pack(fill="x", pady=(0, 10))

        tk.Label(self.frame_manual, text="Meaning:", bg=COLOR_BG).pack(anchor="w")
        self.entry_meaning = tk.Entry(self.frame_manual)
        self.entry_meaning.pack(fill="x", pady=(0, 10))

        tk.Label(self.frame_manual, text="Example Sentence:", bg=COLOR_BG).pack(anchor="w")
        self.entry_sentence = tk.Entry(self.frame_manual)
        self.entry_sentence.pack(fill="x", pady=(0, 10))

        # Save Button
        self.btn_save = tk.Button(self.frame_manual, text="💾 Save Word", bg=COLOR_ACCENT, fg="white", font=("Arial", 11, "bold"), command=self.save_word)
        self.btn_save.pack(fill="x", pady=20)


        # --- RIGHT SIDE: BULK IMPORT ---
        self.frame_bulk = tk.LabelFrame(root, text="Bulk Import (from AI)", bg=COLOR_BG, font=("Arial", 12, "bold"), padx=15, pady=15)
        self.frame_bulk.place(x=340, y=0, width=220, height=490)

        info_text = (
            "1. Ask Gemini for words\n"
            "   in JSON format.\n\n"
            "2. Copy the JSON code.\n\n"
            "3. Click Import below."
        )
        tk.Label(self.frame_bulk, text=info_text, bg=COLOR_BG, justify="left", font=("Arial", 10)).pack(anchor="w")

        # Import Button
        self.btn_import = tk.Button(self.frame_bulk, text="📋 Import from\nClipboard", bg="#2ecc71", fg="white", font=("Arial", 11, "bold"), height=3, command=self.import_from_clipboard)
        self.btn_import.pack(fill="x", pady=30)
        
        self.status_label = tk.Label(self.frame_bulk, text="Ready", bg=COLOR_BG, fg="gray")
        self.status_label.pack(side="bottom")

    def load_data(self):
        if not os.path.exists(FILE_NAME): return []
        try:
            with open(FILE_NAME, 'r', encoding='utf-8') as f: return json.load(f)
        except: return []

    def save_to_file(self):
        with open(FILE_NAME, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)

    def save_word(self):
        # 1. Get Values
        cat = self.cat_var.get().strip().capitalize()
        
        # Article Logic: If "None (Verb/Adj)" is selected, save as empty string ""
        raw_art = self.art_var.get()
        if "None" in raw_art or raw_art == "":
            art = ""
        else:
            art = raw_art.strip().lower()

        sing = self.entry_singular.get().strip()
        plu = self.entry_plural.get().strip()
        mean = self.entry_meaning.get().strip()
        sent = self.entry_sentence.get().strip()

        if not sing or not mean:
            messagebox.showwarning("Missing Data", "Please enter at least the Word and Meaning.")
            return

        if not cat: cat = "General"

        new_entry = {
            "category": cat,
            "article": art,
            "singular": sing,
            "plural": plu,
            "meaning": mean,
            "sentence": sent
        }

        self.data.append(new_entry)
        self.save_to_file()
        
        # Clear Inputs (Keep Category for speed)
        self.entry_singular.delete(0, 'end')
        self.entry_plural.delete(0, 'end')
        self.entry_meaning.delete(0, 'end')
        self.entry_sentence.delete(0, 'end')
        self.art_box.set('') # Reset article dropdown
        
        messagebox.showinfo("Success", f"Saved: {sing}")
        self.status_label.config(text=f"Total Words: {len(self.data)}")

    def import_from_clipboard(self):
        try:
            content = self.root.clipboard_get()
            new_items = json.loads(content)
            
            if not isinstance(new_items, list):
                raise ValueError("Clipboard data is not a list!")

            count = 0
            for item in new_items:
                if 'singular' in item and 'meaning' in item:
                    if 'category' not in item:
                        item['category'] = 'Imported'
                    self.data.append(item)
                    count += 1
            
            self.save_to_file()
            messagebox.showinfo("Import Success", f"Successfully added {count} words!")
            self.status_label.config(text=f"Total Words: {len(self.data)}")
            
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Clipboard does not contain valid JSON.\nCheck the code block!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    window = tk.Tk()
    app = VocabManager(window)
    window.mainloop()
