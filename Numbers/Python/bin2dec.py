def bin2dec(num):
    '''
    Exemplo de um simples conversor de binário para decimal.
    bit => bit do numero binário
    pos => posição
    >>> bin2dec(1010)
    10
    >>> bin2dec(1011011)
    91
    >>> bin2dec(1010010)
    82
    '''
    return sum([int(bit)*2**pos for pos, bit in enumerate(str(num)[::-1])])
