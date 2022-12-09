tekst = input("Podaj słowo do zaszyfrowania:")

def szyfrowanie():
    zaszyfrowane = ""
    for i in range(len(tekst)):
        klucz = i+1
        if ord(tekst[i]) > 122 - klucz:
            zaszyfrowane += chr(ord(tekst[i]) + klucz - 26)
        else:
            zaszyfrowane += chr(ord(tekst[i]) + klucz)
    return zaszyfrowane

def rozszyfrowanie():
    odszyfrowane = ""
    for i in range(len(szyfrowanie())):
        klucz = i+1
        if ord(szyfrowanie()[i]) > 122 + klucz:
            odszyfrowane += chr(ord(szyfrowanie()[i]) - klucz - 26)
        else:
            odszyfrowane += chr(ord(szyfrowanie()[i]) - klucz)
    print("Odszyfrowany tekst to: ", odszyfrowane)

print("Rozszyfrowany tekst to: ", szyfrowanie())

rozszyfrowanie()

