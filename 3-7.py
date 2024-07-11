with open('sample.txt', 'r') as f:
    line = f.readlines()
print(line)
f.close()

with open('sample.txt', 'r') as f:
    for line in f:
        print(line.strip())
