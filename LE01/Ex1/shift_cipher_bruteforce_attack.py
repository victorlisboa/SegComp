import sys
from shift_cipher import shift_encrypt, shift_decrypt

def bruteforce_shift(ciphertext):
    print('Plaintexts:')
    for k in range(26):
        print(f'- {shift_decrypt(ciphertext, k)}')

def main():
    plaintext = 'amor eh fogo que arde sem se ver'
    k = 3
    ciphertext = shift_encrypt(plaintext, k)
    bruteforce_shift(ciphertext)

if __name__ == '__main__':
    main()
