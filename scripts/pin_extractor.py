# This file is a workshop that tests my concepts in user defined and built in functions, strings, loops and conditionals

def pin_extractor(poems):
    secret_codes = [] # an empty list to store multiple pin codes.
    for poem in poems:
        secret_code = '' # An empty string that will get concatenated after pin extraction.
        lines = poem.split('\n') # splits the poem based on new line characters
        for line_index, line in enumerate(lines): # enumerating the poem lines to track their index and extract pin.
            words = line.split() # splitting each word in the line
            if len(words) > line_index:
                secret_code += str(len(words[line_index])) # Extracting the pin from the index and length of words and turning it into string.
            else:
                secret_code += '0' # edge case that handles if there are less words.
        secret_codes.append(secret_code) #append all coodes to empty list.
    return secret_codes    #return list of codes.

poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""
poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

print(pin_extractor([poem, poem2, poem3]))
