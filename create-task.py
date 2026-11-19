def encode_message(message, key_list):
    message = message.lower()
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    encoded_message = ""
    current_key = key_list[0]
    for letter in message:
        if letter in alphabet:
            encoded_message = encoded_message + alphabet[(alphabet.index(letter)+current_key)%26]
            current_key = key_list[(key_list.index(current_key)+1)%len(key_list)]
        else:
            encoded_message = encoded_message + letter
    return encoded_message

plaintext = input("Enter a message to encode (to decode a message, enter it here and make all the keys negative): ")
num_of_keys = int(input("Enter how many keys you want to encode/decode your message with: "))
keys = []

for i in range(num_of_keys):
    keys.append(int(input("Key #" + str(i+1) + " (must be a number): ")))

ciphertext = encode_message(plaintext, keys)
print(ciphertext)