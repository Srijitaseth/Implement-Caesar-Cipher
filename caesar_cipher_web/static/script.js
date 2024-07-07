function encrypt(text, shift) {
    let encryptedText = "";
    for (let i = 0; i < text.length; i++) {
        let char = text[i];
        if (char.match(/[a-z]/i)) {
            let code = text.charCodeAt(i);
            if (code >= 65 && code <= 90) {
                char = String.fromCharCode(((code - 65 + shift) % 26) + 65);
            } else if (code >= 97 && code <= 122) {
                char = String.fromCharCode(((code - 97 + shift) % 26) + 97);
            }
        }
        encryptedText += char;
    }
    return encryptedText;
}

function decrypt(text, shift) {
    return encrypt(text, -shift);
}

function encryptMessage() {
    let message = document.getElementById("message").value;
    let shift = parseInt(document.getElementById("shift").value);
    let result = encrypt(message, shift);
    document.getElementById("result").value = result;
}

function decryptMessage() {
    let message = document.getElementById("message").value;
    let shift = parseInt(document.getElementById("shift").value);
    let result = decrypt(message, shift);
    document.getElementById("result").value = result;
}
