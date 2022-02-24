import modul as m

# 1. feladat:
menhely = m.kutya_lista()

# 2. feladat:
print(f'a menhelyen {m.vizslak_szam(menhely)} db vizsla él')

# 3. feladat:
print(f'a menhely legöregebb kutyája egy {m.legoregebb_fajta(menhely)}')

# 4. feladat:
k_fajta = input('milyen fajtájú kutyákat keresel? ')
m.adott_fajtaju_kutyak(menhely, k_fajta)