"""A class which converts between text and morse code"""

from morse_dict import MORSE_DICT


class TextConverter:

    def __init__(self):
        self.text = ""
        self.morse = ""

    def new_text(self):
        self.text = input("Enter the text you would like to be converted into morse code:\n"
                          "(Special char and punct  will be ignored.)\n")

    def convert_to_morse(self):
        self.morse = ""
        for char in self.text:
            if char == ".":
                self.morse += " "
                for letter in "STOP":
                    morse_char = MORSE_DICT[letter.upper()]
                    self.morse += morse_char + " "
            else:
                try:
                    morse_char = MORSE_DICT[char.upper()]
                    self.morse += morse_char + " "
                except AttributeError:
                    morse_char = MORSE_DICT[char]
                    self.morse += morse_char + " "
                except KeyError:
                    pass

    def new_morse(self):
        self.morse = input("Enter the morse code that you would like to convert to text.\n"
                           "Enter your code using '.' and '-',\n"
                           "No spaces between dots and dashes of the same letter,\n"
                           "One space between letters in a word,\n"
                           "and leave 3 spaces between words.\n")

    def convert_to_text(self):
        self.text = ""
        morse_words = self.morse.split("   ")
        for word in morse_words:
            morse_letters = word.split(" ")
            for morse_letter in morse_letters:
                for letter, morse in MORSE_DICT.items():
                    if morse == morse_letter:
                        self.text += letter
            self.text += " "
        print(f"\nHere is the text version of your morse input:\n\n"
              f"{self.text}\n")
