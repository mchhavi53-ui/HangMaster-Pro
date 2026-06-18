import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:

    def __init__(self, root):
        self.root = root
        self.root.title("🎯 HangMaster Pro")
        self.root.geometry("700x550")
        self.root.configure(bg="#1e1e2f")
        self.root.resizable(False, False)

        self.score = 0

        self.categories = {
            "Technology": {
                "python": "Popular programming language",
                "laptop": "Portable computer",
                "coding": "Writing computer programs"
            },
            "Animals": {
                "tiger": "Big striped wild cat",
                "rabbit": "Loves carrots",
                "elephant": "Largest land animal"
            },
            "Sports": {
                "cricket": "Very popular in India",
                "football": "Played with a round ball",
                "tennis": "Uses rackets"
            }
        }

        self.start_game()

    def start_game(self):

        category = random.choice(list(self.categories.keys()))
        self.category = category

        self.word = random.choice(
            list(self.categories[category].keys())
        )

        self.hint = self.categories[category][self.word]

        self.guessed_letters = []
        self.wrong_guesses = 0
        self.max_wrong = 6

        for widget in self.root.winfo_children():
            widget.destroy()

        title = tk.Label(
            self.root,
            text="🎯 HangMaster Pro",
            font=("Arial", 24, "bold"),
            fg="gold",
            bg="#1e1e2f"
        )
        title.pack(pady=10)

        self.score_label = tk.Label(
            self.root,
            text=f"🏆 Score: {self.score}",
            font=("Arial", 14, "bold"),
            fg="white",
            bg="#1e1e2f"
        )
        self.score_label.pack()

        category_label = tk.Label(
            self.root,
            text=f"📂 Category: {self.category}",
            font=("Arial", 14),
            fg="cyan",
            bg="#1e1e2f"
        )
        category_label.pack(pady=5)

        self.word_label = tk.Label(
            self.root,
            text=self.display_word(),
            font=("Courier", 30, "bold"),
            fg="white",
            bg="#1e1e2f"
        )
        self.word_label.pack(pady=20)

        self.attempt_label = tk.Label(
            self.root,
            text=f"❤️ Attempts Left: {self.max_wrong}",
            font=("Arial", 14),
            fg="lightgreen",
            bg="#1e1e2f"
        )
        self.attempt_label.pack()

        self.guessed_label = tk.Label(
            self.root,
            text="Guessed Letters: None",
            font=("Arial", 12),
            fg="white",
            bg="#1e1e2f"
        )
        self.guessed_label.pack(pady=10)

        self.entry = tk.Entry(
            self.root,
            font=("Arial", 18),
            width=5,
            justify="center"
        )
        self.entry.pack(pady=10)

        guess_btn = tk.Button(
            self.root,
            text="Guess",
            font=("Arial", 14, "bold"),
            bg="#4CAF50",
            fg="white",
            command=self.check_guess
        )
        guess_btn.pack(pady=5)

        hint_btn = tk.Button(
            self.root,
            text="💡 Hint",
            font=("Arial", 12, "bold"),
            bg="orange",
            command=self.show_hint
        )
        hint_btn.pack(pady=5)

        restart_btn = tk.Button(
            self.root,
            text="🔄 Restart",
            font=("Arial", 12, "bold"),
            bg="#2196F3",
            fg="white",
            command=self.start_game
        )
        restart_btn.pack(pady=5)

        self.status_label = tk.Label(
            self.root,
            text="Let's begin!",
            font=("Arial", 12),
            fg="yellow",
            bg="#1e1e2f"
        )
        self.status_label.pack(pady=15)

    def display_word(self):
        result = ""

        for letter in self.word:
            if letter in self.guessed_letters:
                result += letter + " "
            else:
                result += "_ "

        return result

    def show_hint(self):
        messagebox.showinfo(
            "Hint",
            f"💡 {self.hint}"
        )

    def check_guess(self):

        guess = self.entry.get().lower().strip()
        self.entry.delete(0, tk.END)

        funny_messages = [
            "😅 Oops! Wrong letter.",
            "🐵 Monkey disagrees with that guess.",
            "🚀 That letter flew into space.",
            "🍕 Wrong! Have a pizza and retry.",
            "🤦 Better luck next guess."
        ]

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning(
                "Invalid Input",
                "Enter one alphabet letter."
            )
            return

        if guess in self.guessed_letters:
            messagebox.showinfo(
                "Already Used",
                "You already guessed this letter."
            )
            return

        self.guessed_letters.append(guess)

        if guess in self.word:
            self.status_label.config(
                text="✅ Nice! Correct Guess."
            )
        else:
            self.wrong_guesses += 1
            self.status_label.config(
                text=random.choice(funny_messages)
            )

        self.word_label.config(
            text=self.display_word()
        )

        self.attempt_label.config(
            text=f"❤️ Attempts Left: {self.max_wrong - self.wrong_guesses}"
        )

        self.guessed_label.config(
            text="Guessed Letters: " +
            ", ".join(sorted(self.guessed_letters))
        )

        if all(
            letter in self.guessed_letters
            for letter in self.word
        ):
            self.score += 10

            messagebox.showinfo(
                "🎉 You Won!",
                f"Congratulations!\n\nWord: {self.word}\n\n+10 Points"
            )

            self.start_game()

        elif self.wrong_guesses >= self.max_wrong:

            messagebox.showerror(
                "💀 Game Over",
                f"You Lost!\n\nThe word was: {self.word}"
            )

            self.start_game()


root = tk.Tk()
game = HangmanGame(root)
root.mainloop()
