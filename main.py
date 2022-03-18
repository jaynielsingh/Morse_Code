ALPHABET = {
    "a": ".- ", "b": "-... ", "c": "-.-. ", "d": "-.. ", "e": ". ", "f": "..-. ", "g": "--. ", "h": ".... ", "i": ".. ",
    "j": ".--- ", "k": "-.- ", "l": ".-.. ", "m": "-- ", "n": "-. ", "o": "--- ", "p": ".--. ", "q": "--.- ",
    "r": ".-. ",
    "s": "... ", "t": "- ", "u": "..- ", "v": "...- ", "w": ".-- ", "x": "-..- ", "y": "-.-- ", "z": "--.. ",
    "1": ".---- ",
    "2": "..--- ", "3": "...-- ", "4": "....- ", "5": "..... ", "6": "-.... ", "7": "--... ", "8": "---.. ",
    "9": "----. ", "0": "-----", " ": ", "
}


def encrypt(message):
    """Returns the morse code version of the character"""
    morse_code = ""
    for char in message:
        char_code = ALPHABET[char]
        morse_code += char_code
    print(morse_code)


is_on = True

while is_on:
    print("Welcome to the morse code generator! ")
    text = input("Enter text: ")
    encrypt(text)
    play_again = input("Type 'yes' if you want to try again. Otherwise 'no' ")
    if play_again == "no":
        is_on = False
        print('Goodbye')
