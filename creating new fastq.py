inp = open('DRR127195.fastq')
out = open('new.fastq', 'w')
f = open('indexes.txt')
for s in f:
    S = s
indexes = S[1:-1].split(', ')
f.close()
inlist = []
for s in inp:
    inlist.append(s)

for i in indexes:
    for n in range(4):
        rec = inlist[ int(i) * 4 + n]
        out.write(rec)
inp.close()
out.close()
        
