alphabet = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
    cipher_text=""
    for letter in text:
         pos = alphabet.index(letter)
         new_pos = pos + shift
         new_letter = alphabet[new_pos]
         cipher_text += new_letter
    print(f"the encoded text is {cipher_text}")

encrypt(text,shift)