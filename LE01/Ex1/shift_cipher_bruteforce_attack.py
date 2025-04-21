import sys
from shift_cipher import shift_encrypt, shift_decrypt

def bruteforce_breaker(ciphertext):
    print('Plaintexts:')
    for k in range(26):
        print(f'- {shift_decrypt(ciphertext, k)}')

def main():
    plaintext = sys.argv[1]
    k = 3
    if len(sys.argv) > 2:
        k = int(sys.argv[2])
    ciphertext = shift_encrypt(sys.argv[1], k)
    bruteforce_breaker(ciphertext)

if __name__ == '__main__':
    main()
