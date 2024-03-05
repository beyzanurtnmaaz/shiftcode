#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
# Harfleri tutan liste
harfler=["a","b","c","d","e","f","g","h","ı","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 
while True:
    # Kullanıcıdan seçenek girişi isteni
    print("-----------------------------------")
    secim = input("Lütfen (1,2,3) seçeneklerinden birini giriniz: ")

    if secim == "1":
        # Seçenek 1: Harfleri kaydıran şifreleme
        kelime = input("Lütfen ingilizce karakter içeren bir kelime giriniz.").lower()
        sayi = input("Sayi giriniz.")
        integer_deger = int(sayi)

        x = list(kelime)
        my_list = []
        
        for indeks, eleman  in enumerate(x):
        

            try:
                # Girilen sayıyı tamsayıya çevirme metodu
                aranan_eleman = x[indeks]
                x[indeks] = harfler.index(aranan_eleman)
                # Kaydırma değerini integer değer ile başlatma
                kaydirma_index= integer_deger
                # Kaydırma indeksini hesaplama
                kaydirma_index=x[indeks]+integer_deger
                #kaydırılan indeksin z den sonra a ya geri dönmesini sağlayan kod
                if kaydirma_index > 25:
                    kaydirma_index = kaydirma_index % 26
                    #Girilen sayıyı indekse ekleme
                    my_list.append(harfler[kaydirma_index])           
                else:
                    my_list.append(harfler[kaydirma_index])          
                #Girilen değerin listede bulunmadığı durumda alttaki kod çalışır
            except ValueError:
                aranan_eleman = x[indeks]
                print(f"{aranan_eleman} listede bulunamadı.")
            continue # Hata durumunda döngüye geri dön
               
        my_string = ''.join(my_list)
        print(my_string) 
        print("-----------------------------------")
            
    elif secim == "2":
        print("Seçenek 2'yi seçtiniz.")
        #Kullanıcı kelime giriniz yerine sayı girerse aşağıdaki döngü çalışır
        while True:
            kelime = input("Lütfen ingilizce karakter içeren bir kelime giriniz.").lower()

            if kelime.isalpha():
                break  # Harf girildiyse döngüden çıkma metodu

            print('Lütfen bir kelime giriniz.')
        
        sayi = input("Lütfen bir sayı giriniz ")
        integer_deger = int(sayi)

        x = list(kelime)
        my_list = []
        
        for indeks, eleman  in enumerate(x):
        

            try:# Girilen sayıyı tamsayıya çevirme
                aranan_eleman = x[indeks]
                x[indeks] = harfler.index(aranan_eleman)
                kaydirma_index= integer_deger
                kaydirma_index = x[indeks]-integer_deger # Negatifse düzelten kod satırı
                if kaydirma_index > 25:
                    kaydirma_index = kaydirma_index % 26 # İngilizcede 26 harf olduğu için kaydırma indeksini başa dönmek için mod 26 alırız.
                    my_list.append(harfler[kaydirma_index])           
                else:
                    my_list.append(harfler[kaydirma_index])          
                
                
            except ValueError:
                aranan_eleman = x[indeks]
                print(f"{aranan_eleman} listede bulunamadı.")
            continue # Hata durumunda döngüye geri dön
        my_string = ''.join(my_list)#Harfler listesinin elemanlarını birleştirmek için kullanılan kod satırı
        print(my_string) 
        print("-----------------------------------")
        
    elif secim == "3":
         #Programdan çıkma komutu
        exit()
        
        
    else:
        print("Geçersiz bir seçenek girdiniz. Lütfen tekrar deneyin.")
    
   


# In[ ]:





# In[ ]:




