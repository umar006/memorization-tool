from typing import Tuple


class FlashCard:

    def __init__(self) -> None:
        self.flash_cards = {}

    def main_menu(self) -> None:
        print("1. Add flashcards")
        print("2. Exit")

    def add_flash_card_menu(self) -> None:
        print("\n1. Add a new flashcard")
        print("2. Exit")

    def add_flash_card_form(self) -> Tuple[str, str]:
        print("\nQuestion:")
        question = input()
        print("Answer:")
        answer = input()

        return question, answer

    def add_flash_card(self, question, answer) -> None:
        self.flash_cards[question] = answer
