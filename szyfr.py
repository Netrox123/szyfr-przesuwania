tekst = input("Podaj słowo do zaszyfrowania:")
zaszyfrowane = ""
for i in range(len(tekst)):
    klucz = i+1
    if ord(tekst[i]) > 122 - klucz:
        zaszyfrowane += chr(ord(tekst[i]) + klucz - 26)
    else:
        zaszyfrowane += chr(ord(tekst[i]) + klucz)
print("Zaszyfrowany tekst to: ", zaszyfrowane)

odszyfrowane = ""
for i in range(len(zaszyfrowane)):
    klucz = i+1
    if ord(zaszyfrowane[i]) > 122 + klucz:
        odszyfrowane += chr(ord(zaszyfrowane[i]) - klucz - 26)
    else:
        odszyfrowane += chr(ord(zaszyfrowane[i]) - klucz)
print("Odszyfrowany tekst to: ", odszyfrowane)


