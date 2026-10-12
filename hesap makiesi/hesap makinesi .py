print("basit hesap makinesi

sayi1 = float(input("birinci sayiyi girin: "))
islem = input("islem secin (+, -, *, /): ")
sayi2 = float(input("ikinci sayiyi girin: "))

if islem == "+":
    sonuc = sayi1 + sayi2
    print(f"{sayi1} + {sayi2} = {sonuc}")
elif islem == "-":
    sonuc = sayi1 - sayi2
    print(f"{sayi1} - {sayi2} = {sonuc}")
elif islem == "*":
    sonuc = sayi1 * sayi2
    print(f"{sayi1} * {sayi2} = {sonuc}")
elif islem == "/":
    if sayi2 != 0:
        sonuc = sayi1 / sayi2
        print(f"{sayi1} / {sayi2} = {sonuc}")
    else:
        print("Hata: Sifira bolme hatasi!")
else:
    print("Gecersiz islem secimi.")