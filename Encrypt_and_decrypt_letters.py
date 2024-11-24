Alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Direction = input(f"Type 'encode' to encrypt the data, type 'decode' to decrypt: \n").lower()
Text = input("Type your message: \n").lower()
shift = int(input("Enter the shift number: \n"))

def encrypt(original_text, shift_number):
    cipher_text = ""
    for letter in original_text:
        if letter in Alphabets:  # Only shift alphabetic characters
            shifted_position = Alphabets.index(letter) + shift_number
            shifted_position %= len(Alphabets)  # Use modulo to wrap around
            cipher_text += Alphabets[shifted_position]
        else:
            cipher_text += letter  # Keep non-alphabet characters as is

    print(f"Here is the encoded result: {cipher_text}")

def decrypt(original_text, shift_number):
    deciphered_text = ""
    for letter in original_text:
        if letter in Alphabets:  # Only shift alphabetic characters
            shifted_position = Alphabets.index(letter) - shift_number
            shifted_position %= len(Alphabets)  # Use modulo to wrap around
            deciphered_text += Alphabets[shifted_position]
        else:
            deciphered_text += letter  # Keep non-alphabet characters as is

    print(f"Here is the decoded result: {deciphered_text}")

# Choose whether to encode or decode
if Direction == 'encode':
    encrypt(Text, shift)
elif Direction == 'decode':
    decrypt(Text, shift)
else:
    print("Invalid input. Please type 'encode' or 'decode'.")
