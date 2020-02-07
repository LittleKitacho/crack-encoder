import crack_coder

string = "testing string"
length = 1

encoded_string = crack_coder.encode(string, length)
decoded_string = crack_coder.decode(encoded_string)

print(string)
print(str(length))
print(encoded_string)
print(decoded_string)