from text_converter import TextConverter
from morse_ascii import morse

text_converter = TextConverter()
running = True

while running:
    print("Hello and welcome to Morse Encryption/Decipher!")
    print(morse)
    while True:
        convert_to = input("Choose an option:\n"
                           "A) Convert text to morse code.\n"
                           "B) Convert morse code to text.\n"
                           "Type A or B to select your choicea. Type any other character to exit Morse Converter.\n")
        if convert_to.upper() == "A":
            text_converter.new_text()
            text_converter.convert_to_morse()
            # text_converter.play_morse_sound()
        elif convert_to.upper() == "B":
            text_converter.new_morse()
            text_converter.convert_to_text()
        else:
            running = False
            break
    print("Thank you for using Morse Converter, goodbye!")