seq = [0,1]
def fibseq(maxnum, item=1):
    (item <= maxnum and
        (seq.append(item), fibseq(maxnum, item + seq[-2])))

fibseq(input('Max. Element.: '))
print(seq)
