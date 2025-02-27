import string

def mod_inverse(a):
    for i in range(1, 26):
        if (a * i) % 26 == 1:
            return i
    return None

def encrypt_func(plainText, a, b):
    msg = ""
    plainText = plainText.upper()
    for i in plainText:
        temp = ((a * (ord(i) - ord('A')) + b) % 26) + ord('A')
        msg +=  chr(temp)
    return msg

def decrypt_func(encryptedText, a_inv, a, b):
    decryptedText = ""
    for char in encryptedText:
        y = ord(char) - ord('A')
        x = (a_inv * (y - b)) % 26 + ord('A')
        decryptedText += chr(x)
    return decryptedText

def brute_force_decrypt(encryptedText, a_inv):
    encryptedText = encryptedText.upper() # in hoa hết

    a_array = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25] # những gt có thể của a
    # b in [0, 25]

    for a in a_array:
        for b in range(26):
            decrypted = decrypt_func(encryptedText, a_inv, a, b)
            print(f"With a = {a}, b = {b}: {decrypted}")


def main():
    print("Nhap 2 keys:")
    a = int(input())
    b = int(input())
    # 1: Xác định xem a có phải là số nguyên tố cùng với 26 hay không, không thì nhập lại
    a_inv = mod_inverse(a)
    if a_inv is None:
        print(a, "key is not coprime with 26. Please choose a different one")
        return
    
    print("Type your plaintext to encrypt:")
    plainText = input()
    # 2: Encrypt stage
    encryptedText = encrypt_func(plainText, a, b)
    print("Here is Encrypted Text:", encryptedText)

    # 3: Decrypt stage using brute-force, tức là coi như k biết a, b, ra nhiều kết quả, phải nhìn xem kết quả nào phù hợp
    brute_force_decrypt(encryptedText, a_inv)


if __name__== "__main__":
    main()