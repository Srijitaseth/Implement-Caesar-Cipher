def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                start = ord('a')
                encrypted_text += chr((ord(char) - start + shift_amount) % 26 + start)
            elif char.isupper():
                start = ord('A')
                encrypted_text += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)
