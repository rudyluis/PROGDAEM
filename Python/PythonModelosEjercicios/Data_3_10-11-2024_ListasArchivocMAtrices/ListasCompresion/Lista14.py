n = 7
vector = []

for i in range(1, n + 1):
    if i % 2 == 1:  
        vector.append(i)
    else:
        vector.insert(0, i)  

print(vector)

