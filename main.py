from flash_card import FlashCard

if __name__ == "__main__":
    fc = FlashCard()
    while True:
        fc.main_menu()

        user_input = input()
        if user_input == '1':
            while True:
                fc.add_flash_card_menu()
                user_input = input()
                if user_input == '1':
                    question, answer = fc.add_flash_card_field()
                    fc.add_flash_card(question, answer)
                elif user_input == '2':
                    break
                else:
                    print(f"{user_input} is not an option")
        elif user_input == '2':
            fc.practice_flash_card()
        elif user_input == '3':
            print("Bye!")
            break
        else:
            print(f"{user_input} is not an option")

        print()
