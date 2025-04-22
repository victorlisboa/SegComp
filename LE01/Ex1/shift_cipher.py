def shift_encrypt(plaintext, k):
    encrypted_text = ''
    for l in plaintext:
        if l.isalpha():
            encrypted_text += chr((ord(l) - 97 + k) % 26 + 97)
        else:
            encrypted_text += l
    return encrypted_text

def shift_decrypt(ciphertext, k):
    decrypted_text = ''
    for l in ciphertext:
        if l.isalpha():
            decrypted_text += chr((ord(l) - 97 - k) % 26 + 97)
        else:
            decrypted_text += l
    return decrypted_text

def main():
    plaintext = input('Texto a ser cifrado: ').lower()
    k = int(input('Chave k: '))
    ciphertext = shift_encrypt(plaintext, k)
    decrypted_text = shift_decrypt(ciphertext, k)
    print(f'Texto criptografado por deslocamento com o k=3: {ciphertext}')
    print(f'Texto descriptografado por deslocamento com o k=3: {decrypted_text}')

if __name__ == '__main__':
    main()