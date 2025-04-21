import sys

def shift_encrypt(plaintext, k):
    encrypted_text = ''
    for l in plaintext:
        encrypted_text += chr((ord(l) - 97 + k) % 26 + 97)
    return encrypted_text

def shift_decrypt(ciphertext, k):
    decrypted_text = ''
    for l in ciphertext:
        decrypted_text += chr((ord(l) - 97 - k) % 26 + 97)
    return decrypted_text

def main():
    plaintext = sys.argv[1]
    k = 3
    if len(sys.argv) > 2:
        k = int(sys.argv[2])
    ciphertext = shift_encrypt(plaintext, k)
    decrypted_text = shift_decrypt(ciphertext, k)
    print(f'Texto criptografado por deslocamento com o k=3: {ciphertext}')
    print(f'Texto descriptografado por deslocamento com o k=3: {decrypted_text}')

if __name__ == '__main__':
    main()