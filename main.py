from cipher.caesar_cipher import encrypt, decrypt

def main():
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? (e/d): ").lower()
        if choice not in ('e', 'd'):
            print("Invalid choice. Please choose 'e' for encryption or 'd' for decryption.")
            continue

        text = input("Enter the message: ")
        try:
            shift = int(input("Enter the shift value: "))
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
            continue

        if choice == 'e':
            result = encrypt(text, shift)
            print(f"Encrypted message: {result}")
        else:
            result = decrypt(text, shift)
            print(f"Decrypted message: {result}")

        another = input("Do you want to encrypt/decrypt another message? (y/n): ").lower()
        if another != 'y':
            break

if __name__ == "__main__":
    main()
