from main import text_to_morse, morse_to_text, play_morse

example = "Hello world this is Raul"
expected_morse = "....   .   .-..   .-..   ---       .--   ---   .-.   .-..   -..       -   ....   ..   ...       ..   ...       .-.   .-   ..-   .-.."
encoded_morse = text_to_morse(example)
decoded_morse = morse_to_text(encoded_morse)
print(f"Test string to encode: {example.upper()}")
print(f"Expected result: {expected_morse}")
print(f"Actual result:   {encoded_morse}")
print(f"Decoded result again:  {decoded_morse}")
play_morse(encoded_morse)
print("You also heard the code in actual bips")
