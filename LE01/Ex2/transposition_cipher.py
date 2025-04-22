import math

def transposition_encrypt(plaintext, k):
    plaintext = plaintext.lower()
    
    col_num = len(k)
    row_num = math.ceil(len(plaintext) / col_num)
    
    # preenche a matriz com o texto
    matrix = [['' for _ in range(col_num)] for _ in range(row_num)]
    idx = 0
    for row in range(row_num):
        for col in range(col_num):
            if idx < len(plaintext):
                matrix[row][col] = plaintext[idx]
                idx += 1

    # ordem das colunas usando a chave
    order = sorted(list(enumerate(k)), key=lambda x: x[1])
    sorted_idxs = [i for i, _ in order]

    encrypted_text = ''
    for idx in sorted_idxs:
        for row in range(row_num):
            if matrix[row][idx]:
                encrypted_text += matrix[row][idx]

    return encrypted_text

def transposition_decrypt(ciphertext, k):
    col_num = len(k)
    row_num = math.ceil(len(ciphertext) / col_num)
    num_chars = len(ciphertext)

    # numero de colunas completas
    whole_col_num = num_chars % col_num

    # ordena indices da chave
    order_k = sorted(list(enumerate(k)), key=lambda x: x[1])
    indices_ordenados = [i for i, _ in order_k]

    matrix = [['' for _ in range(col_num)] for _ in range(row_num)]

    # preenche colunas na ordem
    idx = 0
    for col_order in indices_ordenados:
        col_size = row_num
        if col_order >= whole_col_num and num_chars % col_num != 0:
            col_size -= 1  # ultima linha incompleta

        for row in range(col_size):
            if idx < num_chars:
                matrix[row][col_order] = ciphertext[idx]
                idx += 1

    decrypted_text = ''
    for row in matrix:
        for char in row:
            if char:
                decrypted_text += char

    return decrypted_text

def main():    
    plaintext = 'amor eh fogo que arde sem se ver'
    k = 'zebras'
    ciphertext = transposition_encrypt(plaintext, k)
    decrypted_text = transposition_decrypt(ciphertext, k)
    print(f'Texto criptografado por deslocamento com o k=zebras: {ciphertext}')
    print(f'Texto descriptografado por deslocamento com o k=zebras: {decrypted_text}')

if __name__ == '__main__':
    main()