def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches
        
x = []

f = open('cluster.txt')
x = 0
S = str()
for s in f:
    S = s

indexes = list(find_all(S, '4'))
print(indexes)




