# Encode from text to ASCII
def encode(input_string : str):
    encoded_string = ""
    for character in input_string : 
        encoded_string += str(ord(character)) + " " # Adding a space to separate each character's ASCII expression
    return encoded_string.strip()

# Decode from ASCII to text 
def decode(encoded_string : str):
    decoded_string = ""
    for code in encoded_string.split():
        decoded_string += chr(int(code))  # Convert the ASCII code back to char using char() function
    return decoded_string


input_string = "Hello, world"
encoded = encode(input_string=input_string)
decoded = decode(encoded_string=encoded)
print(f"Input String: {input_string}")
print(f'Encoded String : {encoded}')
print(f'Decoded String : {decoded}')