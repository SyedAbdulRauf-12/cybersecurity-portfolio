# This code is for purely demonstration of how a caesars ciper works.
def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int) or isinstance(shift, bool): #checking the datatype of shift value.
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25: # shift value must not exceed 25 or lower than 1
        return 'Shift must be an integer between 1 and 25.' 

    alphabet = 'abcdefghijklmnopqrstuvwxyz' # define the alphabet for shifting

    if not encrypt: # for decrypting encrytped text
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift] # alphabets are shifted using string slicing 
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper()) # the normal alphabet and the shifted alphabet are mapped together
    return text.translate(translation_table) # Will return the cipher text of the plaintext

def encrypt(text, shift): # seperate function for encryption. By default the caesar function encrypts.
    return caesar(text, shift) 
    
def decrypt(text, shift): # separate function for decryption 
    return caesar(text, shift, encrypt=False) # here 3rd argument is changed to false for decrypting.
  
text = "Hello world" # hard coded text value
encrypted_text = encrypt(text, 13) # encrypting
decrypted_text = decrypt(encrypted_text, 13) # displays the decrypted text
print(encrypted_text)
print(decrypted_text)
