import tkinter as tk
from tkinter import messagebox
import json
import random
import os

# --- COLORS ---
COLOR_DEFAULT = "#B1DDC6"
COLOR_MASC = "#AEC6CF"     # Blue (Der)
COLOR_FEM = "#FFB3BA"      # Pink (Die)
COLOR_NEUT = "#77DD77"     # Green (Das)
COLOR_VERB = "#FDFD96"     # Yellow (Verbs)
CARD_FRONT_COLOR = "#FFFFFF"

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🇩🇪 German Mastery")
        self.root.config(padx=40, pady=40, bg=COLOR_DEFAULT)

        # 1. Load Data
        self.full_vocab_list = self.load_data()
        
        # 2. Get Unique Categories for Dropdown
        self.categories = ["All"] + sorted(list(set(w.get("category", "General") for w in self.full_vocab_list)))
        
        # 3. Setup Logic
        self.current_category = "All"
        self.learning_list = []
        self.current_card = {}

        # --- UI LAYOUT ---
        
        # CARD (Left - Column 0)
        self.canvas = tk.Canvas(width=800, height=526, bg=CARD_FRONT_COLOR, highlightthickness=0)
        self.title_text = self.canvas.create_text(400, 150, text="German", font=("Arial", 35, "italic"))
        self.word_text = self.canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
        self.details_text = self.canvas.create_text(400, 400, text="", font=("Arial", 20))
        
        self.canvas.grid(row=0, column=0, rowspan=6, padx=20)

        # SIDEBAR (Right - Column 1)
        
        # Row 0: Label
        tk.Label(text="Select Category:", bg=COLOR_DEFAULT, font=("Arial", 10, "bold")).grid(row=0, column=1, sticky="s")

        # Row 1: Dropdown Menu
        self.cat_var = tk.StringVar(root)
        self.cat_var.set("All") 
        self.cat_menu = tk.OptionMenu(root, self.cat_var, *self.categories, command=self.change_category)
        self.cat_menu.config(width=15, font=("Arial", 12))
        self.cat_menu.grid(row=1, column=1, pady=(0, 20))

        # Row 2: Counter
        self.count_label = tk.Label(text="Cards", bg=COLOR_DEFAULT, font=("Arial", 14, "bold"))
        self.count_label.grid(row=2, column=1, pady=10)

        # Row 3: Reveal Button
        self.flip_button = tk.Button(text="🔍 Reveal", command=self.flip_card, font=("Arial", 15, "bold"), bg="#FFB347", fg="white", width=15)
        self.flip_button.grid(row=3, column=1, pady=10)

        # Row 4: Check Button
        self.known_button = tk.Button(text="✅ I Know It", command=self.is_known, font=("Arial", 15), bg="#77DD77", fg="white", width=15)
        self.known_button.grid(row=4, column=1, pady=5)

        # Row 5: Cross Button
        self.unknown_button = tk.Button(text="❌ I Forgot", command=self.next_card, font=("Arial", 15), bg="#FF6961", fg="white", width=15)
        self.unknown_button.grid(row=5, column=1, pady=5, sticky="n")

        # Initialize
        self.filter_words()
        self.next_card()

    def load_data(self):
        if not os.path.exists('vocab.json'): return []
        try:
            with open('vocab.json', 'r', encoding='utf-8') as f: return json.load(f)
        except: return []

    def change_category(self, selection):
        self.current_category = selection
        self.filter_words()
        self.next_card()

    def filter_words(self):
        if self.current_category == "All":
            self.learning_list = self.full_vocab_list.copy()
        else:
            self.learning_list = [w for w in self.full_vocab_list if w.get("category") == self.current_category]
        
        if not self.learning_list:
             messagebox.showinfo("Info", f"No cards found for {self.current_category}!")
             self.current_category = "All"
             self.cat_var.set("All")
             self.learning_list = self.full_vocab_list.copy()

    def next_card(self):
        self.root.config(bg=COLOR_DEFAULT)
        self.count_label.config(bg=COLOR_DEFAULT, text=f"Remaining: {len(self.learning_list)}")
        
        if not self.learning_list:
            self.canvas.itemconfig(self.title_text, text="Done!", fill="black")
            self.canvas.itemconfig(self.word_text, text="Category Finished", fill="green")
            self.canvas.itemconfig(self.details_text, text="Select another category")
            return

        self.current_card = random.choice(self.learning_list)
        
        german = self.current_card.get('singular', 'Unknown')
        self.canvas.itemconfig(self.title_text, text="German", fill="black")
        self.canvas.itemconfig(self.word_text, text=german, fill="black")
        self.canvas.itemconfig(self.details_text, text="")
        self.canvas.config(bg=CARD_FRONT_COLOR)
        
        self.flip_button["state"] = "normal"
        self.known_button["state"] = "disabled"
        self.unknown_button["state"] = "disabled"

    def flip_card(self):
        if not self.current_card: return

        article = self.current_card.get('article', '').lower().strip()
        singular = self.current_card.get('singular', '')
        plural = self.current_card.get('plural', '')
        meaning = self.current_card.get('meaning', '')
        sentence = self.current_card.get('sentence', '') # Added!
        
        bg_color = COLOR_VERB
        if article == "der": bg_color = COLOR_MASC
        elif article == "die": bg_color = COLOR_FEM
        elif article == "das": bg_color = COLOR_NEUT

        self.canvas.config(bg=bg_color)
        self.root.config(bg=bg_color)
        self.count_label.config(bg=bg_color)

        full = f"{article} {singular}" if article else singular
        
        # Logic to stack Plural -> Meaning -> Sentence
        details = ""
        if plural: 
            details += f"Plural: die {plural}\n"
        
        details += f"Meaning: {meaning}"
        
        if sentence:
            details += f"\n\n\"{sentence}\""

        self.canvas.itemconfig(self.title_text, text="Answer", fill="black")
        self.canvas.itemconfig(self.word_text, text=full, fill="black")
        self.canvas.itemconfig(self.details_text, text=details, fill="black")

        self.flip_button["state"] = "disabled"
        self.known_button["state"] = "normal"
        self.unknown_button["state"] = "normal"

    def is_known(self):
        self.learning_list.remove(self.current_card)
        self.next_card()

if __name__ == "__main__":
    window = tk.Tk()
    app = FlashcardApp(window)
    window.mainloop()
