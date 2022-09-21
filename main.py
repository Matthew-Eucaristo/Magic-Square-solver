from functools import cache
import itertools


@cache
def main():
    n = int(input('masukkan n: '))
    magic_table: list = []

    kump_angka = [x for x in range(1, n*n+1)]

    kumpulan_jawaban: list = []
    for combo in itertools.permutations(kump_angka):
        magic_table = []

        index = 0
        for _ in range(n):
            temp = []
            for _ in range(n):
                temp.append(combo[index])
                index += 1
            magic_table.append(temp)

        if cek(magic_table):
            print(magic_table)
            kumpulan_jawaban.append(magic_table)

    print('total penyelesaian: ')
    print(len(kumpulan_jawaban))


def cek(table):
    horizontal: bool = False
    vertical: bool = False
    diagonal: bool = False

    kumpulan_horizontal: list = []
    kumpulan_vertical: list = []
    kumpulan_diagonal: list = []

    # cek horizontal
    for baris in table:
        kumpulan_horizontal.append(sum(baris))

    if len(set(kumpulan_horizontal)) == 1:
        horizontal = True

    # cek vertical
    for i in range(len(table[0])):
        kumpulan_vertical.append(sum([x[i] for x in table]))

    if len(set(kumpulan_vertical)) == 1:
        vertical = True

    # cek diagonal
    temp = []
    for i in range(len(table)):
        temp.append(table[i][i])
    kumpulan_diagonal.append(sum(temp))

    temp = []
    for i in range(len(table)):
        temp.append(table[len(table)-i-1][i])
    kumpulan_diagonal.append(sum(temp))

    if len(set(kumpulan_diagonal)) == 1:
        diagonal = True

    # cek all
    if horizontal and vertical and diagonal:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
