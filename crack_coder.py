from random import randint, choice

letters = "abcdefghijklmnopqrstuvwxyz"
capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "symbols"

length_id = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"

def encode (decoded_str: str, length: int) -> str:

    if length > len(length_id):
        length = len(length_id) - 1
    
    else:
        length -= 1

    has_letters = False
    has_capitals = False
    has_numbers = False
    has_symbols = False

    for i in decoded_str:
        if i in letters:
            has_letters = True

        elif i in capitals:
            has_capitals = True

        elif i in numbers:
            has_numbers = True

        elif i in symbols:
            has_symbols = True

    possible_chars = ""

    if has_letters:
        possible_chars += letters

    if has_capitals:
        possible_chars += capitals
    
    if has_numbers:
        possible_chars += numbers
    
    if has_symbols:
        possible_chars += symbols
    
    encoded_str = decoded_str[0]
    x = 1

    while x < len(decoded_str):

        y = 0

        while y <= length:

            encoded_str += choice(possible_chars)
            y += 1
        
        encoded_str += decoded_str[x]
        x += 1

    return encoded_str + length_id[length]
            


def decode (encoded_str: str) -> str:
    pass

# # # # # # # # # #

if __name__ == "__main__":

    a = input('Enter \'encode\' to encode a string, and \'decode\' to decode an encoded string.  ')
    b = None

    while b == None:

        if a == 'encode':

            b = input('Please input an encoded string to decode.  ')
            c = input('Please input the strength of the encoding.  ')
            c_c = False

            while not c_c:

                try:
                    int(c)

                except:
                    c = input('That isn\'t a number.  Please input the strength of the encoding.  ')

                else:
                    length = int(c)
                    c_c = True

            print('Your encoded string is \'' + encode(b, length) + "'")

        elif a == 'decode':

            b = input('Please input a string to decode.  ')
            
            print('Your decoded string is \'' + decode(b) + "'")

        else:
            a = input('Sorry, please either input \'encode\' or \'decode\'.  ') 