class Kutya:
    def __init__(self, nev, fajta, kor):
        self.nev = nev
        self.fajta = fajta
        self.kor = int(kor)


def kutya_lista():
    print('add meg rendre a kutyák adatait!')
    print('ha valamelyik adattagot üresen hagyod, a bekérés befejeződik')
    kutyak = []
    ssz = 1
    while True:
        print(f'Add meg a {ssz}. kutya adatait:')
        n = input('\tneve:     ')
        if len(n) == 0: break
        f = input('\tfajtája:  ')
        if len(f) == 0: break
        k = input('\téletkora: ')
        if len(k) == 0: break
        kutyak.append(Kutya(n, f, k))
        ssz += 1
    return kutyak


def vizslak_szam(kutyak):
    c = 0
    for k in kutyak:
        if k.fajta.lower() == 'vizsla':
            c += 1
    return c


def legoregebb_fajta(kutyak):
    maxi = 0
    for i in range(1, len(kutyak)):
        if kutyak[i].kor > kutyak[maxi].kor:
            maxi = i
    return kutyak[maxi].fajta


def adott_fajtaju_kutyak(kutyak, k_fajta):
    nevek = []
    for k in kutyak:
        if k.fajta.lower() == k_fajta.lower():
            nevek.append(k.nev)
    if len(nevek) == 0: print(f'nincs {k_fajta} fajtájú kutya')
    if len(nevek) == 1: print(f'csak {nevek[0]} {k_fajta}')
    else:
        print(f'{k_fajta} fajtájú kutyák:', end = ' ')
        for n in nevek:
            print(f'{n},', end=' ')