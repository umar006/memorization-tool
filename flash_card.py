from typing import Tuple


class FlashCard:

    def __init__(self) -> None:
        self.flash_cards = {}

    def main_menu(self) -> None:
        print("1. Add flashcards")
        print("2. Practice flashcards")
        print("3. Exit")

    def add_flash_card_menu(self) -> None:
        print("\n1. Add a new flashcard")
        print("2. Exit")

    def add_flash_card_field(self) -> Tuple[str, str]:
        print("\nQuestion:")
        question = input()
        print("Answer:")
        answer = input()

        return question, answer

    def add_flash_card(self, question, answer) -> None:
        self.flash_cards[question] = answer

    def __practice_flash_card_field(self, question: str) -> str:
        print(f"Question: {question}")
        print('Please press "y" to see the answer or press "n" to skip:')
        choice = input()

        return choice

    def practice_flash_card(self) -> None:
        for flash_card in self.flash_cards:
            choice = self.__practice_flash_card_field(flash_card)
            if choice == 'y':
                print(f"\nAnswer: {self.flash_cards[flash_card]}")
            elif choice == 'n':
                print("\n\n")
