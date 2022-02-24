from flash_card import FlashCard

if __name__ == "__main__":
    fc = FlashCard()
    while True:
        fc.main_menu()

        user_input = input()
        if user_input == '1':
            fc.add_flash_card_menu()
            user_input = input()
            if user_input == '1':
                question, answer = fc.add_flash_card_field()
                fc.add_flash_card(question, answer)
        elif user_input == '2':
            fc.practice_flash_card()
        elif user_input == '3':
            print("Bye!")
            break

        print()
