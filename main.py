from sound import dot, dash, space

morse_dict = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----',
        '.': '.-.-.-',
        ',': '--..--',
        '?': '..--..',
        '!': '-.-.--',
        '&': '.-...',
        }
reversed_morse_dict = {v: k for k, v in morse_dict.items()}

def text_to_morse(text: str):
    """
    Code text into Morse
    In morse, separations are like this:
    - Symbols of the same character, one unit
    - Letters of the same word, three units
    - Words, seven units
    Simplyfing, we will be using:
    - No space between the symbols of the same char
    - 3 spaces between the letters of the same word
    - 7 spaces between words
    """
    output = ""
    words = text.upper().split(" ")

    for word in words:
        for letter in word:
            output += morse_dict[letter] + "   "#3 spaces after each letter
        output += "    "#Add 4 extra spaces to make it 7 for the word
    return output.strip()


def morse_to_text(morse_text: str):
    """
    Decode Morse into text.
    In morse, separations are like this:
    - Symbols of the same character, one unit
    - Letters of the same word, three units
    - Words, seven units
    Unit can mean 'second' or whatever desired
    Simplyfing, we will be using:
    - No space between the symbols of the same char
    - 3 spaces between the letters of the same word
    - 7 spaces between words
    """
    output = ""

    #text_input = morse_text.split(" ")
    words = morse_text.split("       ")
    #print(words)
    for word in words:
        chars = word.split("   ")
        for char in chars:
            output += reversed_morse_dict[char]
        output += " "

    return output.strip()

def play_morse(morse_text: str):
    """
    Play the Morse sentence in the speaker
    """
    words = morse_text.split("       ")
    for word in words:
        chars = word.split("   ")
        for char in chars:
            for symbol in char:
                if symbol == ".":
                    dot()
                elif symbol == "-":
                    dash()
                else:
                    print("Exception!!")
                space(1)
            space(2)
        space(4)
