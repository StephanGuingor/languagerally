def BinaryToDecimal(binary):
    return int(binary, base=2)


test_str = """
Lately I'm feeling lonely, 
I am getting bored of torturing primates all of the time.

At least I'm doing the world a favor my punishing them.

Just remember we are good. Not Cruel
"""
res = ''.join('{0:08b}'.format(ord(i), 'b') for i in test_str)
print(res)

str_data = ''
for i in range(0, len(res), 8):
    temp_data = res[i:i + 8].lstrip('0')
    decimal_data = BinaryToDecimal(temp_data)
    str_data += chr(decimal_data)

print(str_data)
