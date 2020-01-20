a = [1, 2, 3, 4]
print(f'A:{a}')

b = a  # kopia przez referencje, kopia referencji tam gdzie jest ta lista a

b.pop()

print(f'Kopia referencji A po zmianie: {b}')
print(f'A po zmianie kopii referencji: {a}')  # zmienia a bo kopiowanie referencyjne, dla struktur/typów zlozonych
# zawsze jest reference, trzeba pamiętać

# copy
a = [1, 2, 3, ['a', 'b']]
print(f'\nA: {a}')
c = a.copy()  # kopia płytka, referuje tylko na poziom 1, zmiany w liscie w liscie wplyna na oryginal

c.append(True)
print(f'Kopia płytka A po zmienie struktury płytkiej: {c}')
print(f'A po zmianie płytkiej: {a}')

c[3].append('c')

print(f'\nKopia płytka A po zmienie struktury głębszej: {c}')
print(f'A po zmianie głębokiej: {a}')

from copy import deepcopy

a = [1, 2, 3, ['a', 'b']]
d = deepcopy(a)  # kopiowanie głebokie, pochodzi z modułu copy, czyli zmiany nawet w glebszych strukturach nie beda
# wplywaly na oryginal, jest to kopia wartosci

d.append(True)
d[3].append('c')

print(f'\nKopia głeboka A po zmianie struktury płytkiej i głebokiej: {d}')
print(f'A po zmianie płytkiej i głebokiej: {a}')


def f(arr):
    arr.append('x')  # kopia na podstawie refenrecji dlatego poczatkowe a sie zmienia
    return arr


a = [1, 2, 3]
print(f'\nOryginał {a}')
f(a)
print(f'Oryginał {a} został zmieniony przez funkcję, bo kopia byla to tylko przez referencję.')


def f(x):
    print(f'\nWartość wrzucona do funkcji: {x}')
    x = 2  # kopia
    print(f'Wartość wrzucona do funkcji po przekształceniu: {x}')
    return x


z = 10
a = f(z)
print(f'Zmienna prosta zawsze przekazywana jest jako kopia, więc oryginał: {z}, a po przekształceniu przez funkcję: {a}')
