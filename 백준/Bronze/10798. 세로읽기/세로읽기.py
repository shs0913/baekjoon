table=[input() for _ in range(5)] 
for i in range(15):
    for q in range(5):
        if i< len(table[q]):
            print(table[q][i], end='')
            