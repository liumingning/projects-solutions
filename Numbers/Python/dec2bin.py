'''
Binary to Decimal and Back Converter -
Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.
'''
conv = []
def dec2bin(num):
    '''
    Exemplo de um simples conversor de decimal para binário.
    '''
    (num/2 > 0 and (dec2bin(int(num/2)), conv.append(num%2)))

dec2bin(int(input('Decimal: ')))
print(''.join(map(str, conv)))
