tekst = input("Podaj słowo do zaszyfrowania:")
szyfr = ""
for i in range(len(tekst)):
    klucz = i+1
    if ord(tekst[i]) > 122 - klucz:
        szyfr += chr(ord(tekst[i]) + klucz - 26)
    else:
        szyfr += chr(ord(tekst[i]) + klucz)
print("Zaszyfrowany tekst to: ", szyfr)