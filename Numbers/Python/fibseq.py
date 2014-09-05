'''
Fibonacci Sequence -
Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
'''
seq = [0,1]
def fibseq(maxnum, item=1):
    (item <= maxnum and
        (seq.append(item), fibseq(maxnum, item + seq[-2])))

fibseq(input('Max. Element.: '))
print(seq)
