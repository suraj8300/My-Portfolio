

def caesar(original_text, shift_amount, choice):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cypher_text = ""
    for i in original_text:
        if i not in alphabet:
            cypher_text += i
        else:
            if choice == "encrypt":
                cypher_text += alphabet[(alphabet.index(i) + shift_amount) % 26]
            elif choice == "decrypt":
                cypher_text += alphabet[(alphabet.index(i) - shift_amount) % 26]
    return cypher_text