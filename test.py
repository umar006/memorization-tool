import unittest
from unittest.mock import patch

from flash_card import FlashCard


class TestFlashCard(unittest.TestCase):

    def test_len_flash_card_data(self):
        """
        Initial flash card should has zero length
        """
        fc = FlashCard()
        self.assertEqual(len(fc.flash_cards), 0)

    def test_add_new_flash_card(self):
        """
        Flash card data should has one length after add a new flash card
        """
        fc = FlashCard()
        fc.add_flash_card('question', 'answer')
        self.assertEqual(len(fc.flash_cards), 1)


if __name__ == "__main__":
    unittest.main()
