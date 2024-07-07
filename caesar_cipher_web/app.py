from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def encrypt(text, shift):
    encryptedText = ""
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            shift_amount = shift if char.islower() else shift
            start = ord('a') if char.islower() else ord('A')
            encryptedText += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            encryptedText += char
    return encryptedText

def decrypt(text, shift):
    return encrypt(text, -shift)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt_message():
    data = request.json
    message = data.get('message', '')
    shift = int(data.get('shift', 0))
    encrypted_text = encrypt(message, shift)
    return jsonify({'result': encrypted_text})

@app.route('/decrypt', methods=['POST'])
def decrypt_message():
    data = request.json
    message = data.get('message', '')
    shift = int(data.get('shift', 0))
    decrypted_text = decrypt(message, shift)
    return jsonify({'result': decrypted_text})

if __name__ == '__main__':
    app.run(debug=True)
