import unittest

from flash_card import FlashCard


class TestFlashCard(unittest.TestCase):

    def test_len_flash_card_data(self):
        """
        Initial flash card should has zero length
        """
        fc = FlashCard()
        self.assertEqual(len(fc.flash_cards), 0)


if __name__ == "__main__":
    unittest.main()
