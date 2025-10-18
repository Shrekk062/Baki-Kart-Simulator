#PIN_normal=1000


#Statistik deyisenler
u_umumi = 0
u_artirma = 0
u_endirim = 0
u_kecid = 0
balans = 0
#giris melumatlari ve limit
endirim = 0
giris = 1000
limit = 100
cehd = 3
normal_gedis = 0.40
telebe = 0.30
emekli = 0.15
#Motor deyisenleri
Durum = True
Durum_Proses = True

#motor
while Durum :
    PIN = int ( input ( "Pini daxil edin : " ))

#Yoxlanis
    if giris == PIN:

        #Menu ve Prosesler
        while Durum_Proses :
            print("""1) Balansı göstər 
                2) Balans artır 
                3) Gediş et (turniketi keç) 
                4) Son əməliyyatlara bax 
                5) Günlük statistika 
                6) Parametrlər
                0) Cixis """)
            proses=int ( input ("Prosesi yerinə yetirmək üçün göstərilən rəqəmi daxil edin : " ))
            if proses == 1 or 2 or 3 or 4 or 5 or 6 or 0 :

                if proses==0 :
                    Durum_Proses = False
                else :
                    #Cixis
                    if proses == 1 :
                        print("Sizini balansınız",balans,"Azn dir")


                    
                    #Balans artirma ve limit
                    elif proses == 2 :
                        artirma = int ( input ("Miqdarı Daxil edin: "))
                        if artirma > limit :
                            print("Sizin gündəlik balans artırma miqdarınız",limit,"Azndir")
                        else:
                            balans = balans + artirma
                            print("Sizini balansınız",balans,"Azn dir")
                        u_artirma = artirma + u_artirma



                    #Gedis haqqi ve endirimler
                    elif proses == 3 :
                        kecid = int ( input ("Keçid sayını girin : "))
                        if kecid == 1 :
                            balans = balans - normal_gedis
                            umumi = normal_gedis
                            print("Sizini balansınız",balans,"Azn dir")
                        elif kecid == 2 or 3 or 4 :
                            endirim = 0.36
                            umumi = (endirim*kecid-1) + normal_gedis
                            balans = balans - umumi 
                            print("Sizini balansınız",balans,"Azn dir")
                        elif kecid >= 5 :
                            endirim =0.30
                            umumi = normal_gedis + endirim*(kecid-1)
                            print("Sizini balansınız",balans,"Azn dir")
                        u_umumi = u_umumi + umumi
                        u_endirim = endirim*kecid + u_endirim
                        u_kecid = kecid + u_kecid
                        
                    #Son emeliyatlar tarixceler 


                    elif proses == 4 :
                        print("Sizini balansınız",balans,"Azn dir")
                        print("Balansini son defe",artirma,"artirilib")


                    #Statistika
                    elif proses == 5 :
                        print("Gün ərzində",u_kecid,"edilib")
                        print("Ümumi ödəniş",u_umumi,"Azn dir")
                        print("Edilən endirimlərin cəmi",u_endirim,"Azn dir")
                        print("Gün ərzində artırılan ümumi məbləğ",u_artirma,"Azn dir")
                    

                    elif proses == 6 :
                        print("L---->Artırma limitini dəyiş")
                        print("M----->1)Pensiyaner" \
                        "2)Tələbə","YAXINDA GƏLƏCƏK :)")
                    
                        alt_proses = input()
                        if alt_proses == "L" or alt_proses == "l" :
                            limit = int (input ("Artırma limitini daxil edin : "))

                        elif alt_proses == "M" or alt_proses == "m" :
                            mod = int(input("Modu seçin : "))
                            if mod == 1:
                                pass
                                
                            else :
                                pass


                        

                        else :
                            print("Göstəriciləri düzgün girin")
                            continue
                        





            else :
                print("Göstərilən rəqəmi girin : ")




            
    else :
        cehd = cehd-1
        print("PİNİ GOĞRU GİRİN")
        if cehd == 0 :
            print("Kartınız bloklandı daha sonra təkrar sınayın")
            Durum=False