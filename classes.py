import json

a = open(r"C:\Python\Acordes\acordes.txt", "r").read()
b = a.split('\n')
#print(b)
#for i in b:
#j =1
#print(b[1])
acordex = list()
for j in range(len(b)-1):
    #print(j)
    pos = b[j].index('=')
    chord_name = b[j][:pos-1]
    notes_str = b[j][pos+2:].split(' ')
    notex = list()
    for note in notes_str:
        if note == 'X':
            notex.append(-7)
        else:
            notex.append(int(note))
    #print(notex)
    #acordex.append(notex)
    notex.reverse()
    print(f'"{chord_name}": {notex},')
