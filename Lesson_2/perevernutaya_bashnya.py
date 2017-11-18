#N = input('Введите N: ')
N = 678

bashnya = [['.']*x for x in range(100) for y in range(x)]
bashnya = list(enumerate(bashnya, 1))

komnata = 1

for etazh in bashnya:
    for i in range(len(etazh[1])):
        etazh[1].remove('.')
        etazh[1].append(komnata)
        komnata += 1
#print(bashnya)

for etazh in bashnya:
    for k in etazh[1]:
        if k == N:
            komnata_po_poryadku = etazh[1].index(N) + 1
            print('Комната №', N, 'по счету', komnata_po_poryadku, 'слева на', etazh[0], 'этаже' )