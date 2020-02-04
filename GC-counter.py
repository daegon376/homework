# quantity of reads 4568785
# max length 40

x = []

f = open('DRR127195.fastq')
gcc = open('GCc.txt', 'w')


theline = False 
for s in f:
    if theline == True: #the sequence of read
        g_con = int(s.count('G'))
        c_con = int(s.count('C'))
        gc_content = (g_con + c_con) / len(s)
        gcc.write(str(gc_content) + '\n')
    if s.startswith('@DRR127195') == True: #1st line of the read
        theline = True
    else:
        theline = False

gcc.close()
f.close()
        
