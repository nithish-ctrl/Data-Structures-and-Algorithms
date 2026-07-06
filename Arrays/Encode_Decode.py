def encode(input_string : str):
    encoded_string = ""
    for character in input_string : 
        encoded_string += str(ord(character)) + " "
    return encoded_string.strip()

def decode(encoded_string : str):
    decoded_string = ""
    for code in encoded_string.split():
        decoded_string += chr(int(code))
    return decoded_string


input_string = "Hello, world"
encoded = encode(input_string=input_string)
decoded = decode(encoded_string=encoded)
print(f"Input String: {input_string}")
print(f'Encoded String : {encoded}')
print(f'Decoded String : {decoded}')