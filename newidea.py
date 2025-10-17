print("salam, zəhmət olmasa kartınızın kodunu daxil edin: ")
kk = input("")
kklen = len(kk)
if kklen == 13:
    borc = 0
    gedsay = 0
    bal = 1
    gunluk_toplam_artim = 0
    son_emeliyyatlar = []
    gunluk_gedishler = 0
    gunluk_odenish = 0
    gunluk_endirim = 0
    gunluk_artim = 0
    gunluk_limit = 100
    endirim_rejimi = "normal"
    cehd_sayi = 0
    pin_duzgun = False
    
    while cehd_sayi < 3:
        pa = input("zəhmət olmasa kartınıza şifrə təyin edin: ")
        pas = input("zəhmət olmasa şifrəni daxil edin: ")
        
        if pa == pas:
            pin_duzgun = True
            print("hesaba uğurla daxil oldunuz.")
            break
        else:
            cehd_sayi += 1
            print(f"Şifrə yanlışdır. {cehd_sayi} cəhd hüququnuz qaldı.")

    if pin_duzgun == False:
        print("3 dəfə səhv şifrə daxil edildi. Proqram dayandırılır.")
        exit()
    
    while True:
        print("ne etmək istəyirsiniz? (1) balansa baxmaq, (2) balans artirmaq, (3) gedish et, (4) son emeliyyata bax, (5) gunluk statistika, (6) parametrler, (0) çıxış")
        sec = input().lower()
        
        if sec == "1":
            print(f"balansınız: {bal} Azn, borc: {borc} Azn")
            print("davam etmək istəyirsiniz? (y/n)")
            ans = input().lower()
            if ans != "y":
                print("hesabdan çıxılır.")
                break
        elif sec == "2":
            print(f"balans: {bal} Azn, borc: {borc} Azn")
            casho_input = input("balansa nə qədər pul daxil etmek istəyirsiniz? ")
            if casho_input.isdigit():
                casho = int(casho_input)
            else:
                print("xəta: yalnız ədəd daxil edin.")
                continue
            if casho <= 0:
                print("xəta: yalnız müsbət məbləğ daxil edin.")
                continue
            if gunluk_artim + casho > gunluk_limit:
                print(f"gundelik balans artirma limiti {gunluk_limit} azn-dir. Bugün {gunluk_artim} AZN artırmısınız.")
                continue
            if borc > 0:
                if casho >= borc:
                    casho -= borc
                    borc = 0
                    print(f"Borcunuz silindi. Qalan məbləğ: {casho} AZN")
                else:
                    borc -= casho
                    casho = 0
                    print(f"Borcunuzun bir hissəsi silindi. Qalan borc: {borc} AZN")
            if casho > 0:
                bal += casho
                gunluk_artim += casho
                son_emeliyyatlar.append(("Balans artırma", casho, 0, bal))
                print(f"balansınıza pul daxil etdikden sonra balansiniz {bal} Azn oldu.")
        
        elif sec == "3":
            if endirim_rejimi == "telebe":
                qiymet = 0.20
            elif endirim_rejimi == "pensiyaçı":
                qiymet = 0.15
            else:  # normal
                if gedsay == 0:
                    qiymet = 0.40
                elif 1 <= gedsay <= 3:
                    qiymet = 0.36
                else:
                    qiymet = 0.30
            
            endirim_meblegi = 0.40 - qiymet
            if bal < 0.30:
                print("balansda kifayet qeder vesait yoxdur.")
            elif 0.30 <= bal < 0.40 and endirim_rejimi == "normal":
                print("tecili kecidden istifade etmek isteyirsiz? 0.10 man borc yazilacaq! (y/n)")
                ans3 = input().lower()
                if ans3 == "y":
                    borc += 0.10
                    bal -= 0.30
                    gedsay += 1
                    gunluk_gedisler += 1
                    gunluk_odenis += 0.30
                    son_emeliyyatlar.append(("Gediş", 0.30, 0, bal))
                    print("Təcili keçid edildi. 0.10 AZN borc yazıldı.")
                else:
                    print("Keçid ləğv edildi.")
            else:
                if bal >= qiymet:
                    bal -= qiymet
                    gedsay += 1
                    gunluk_gedisler += 1
                    gunluk_odenis += qiymet
                    gunluk_endirim += endirim_meblegi
                    son_emeliyyatlar.append(("Gediş", qiymet, endirim_meblegi, bal))
                    print(f"Gediş edildi. {qiymet} AZN tutuldu. Endirim: {endirim_meblegi} AZN")
                else:
                    print("balansda kifayet qeder vesait yoxdur.")
        elif sec == "4":
            n_input = input("Neçə son əməliyyata baxmaq istəyirsiniz? ")
            if n_input.isdigit():
                n = int(n_input)
            else:
                print("xəta: yalnız ədəd daxil edin.")
                continue
            if n <= 0:
                print("xəta: müsbət ədəd daxil edin.")
                continue
            print(f"Son {n} əməliyyat:")
            say = 1
            baslangic = len(son_emeliyyatlar) - n
            if baslangic < 0:
                baslangic = 0
            
            for i in range(baslangic, len(son_emeliyyatlar)):
                tip, mebleg, endirim, yeni_balans = son_emeliyyatlar[i]
                print(f"{say}. {tip}: {mebleg} AZN, Endirim: {endirim} AZN, Yeni balans: {yeni_balans} AZN")
                say += 1
        elif sec == "5":
            print("=== Günlük Statistika ===")
            print(f"Gediş sayı: {gunluk_gedisler}")
            print(f"Ümumi ödəniş: {gunluk_odenis} AZN")
            print(f"Ümumi endirim: {gunluk_endirim} AZN")
            print(f"Ümumi artırım: {gunluk_artim} AZN")
            print(f"Günlük limit: {gunluk_artim}/{gunluk_limit} AZN")
        elif sec == "6":
            print("=== Parametrlər ===")
            print(f"1. Gündəlik balans artırma limiti: {gunluk_limit} AZN")
            print(f"2. Endirim rejimi: {endirim_rejimi}")
            
            param_sec = input("Hansı parametri dəyişmək istəyirsiniz? (1/2/0 - heç biri): ")
            
            if param_sec == "1":
                yeni_limit_input = input("Yeni gündəlik limit daxil edin: ")
                if yeni_limit_input.isdigit():
                    yeni_limit = int(yeni_limit_input)
                else:
                    print("xəta: yalnız ədəd daxil edin.")
                    continue
                if yeni_limit > 0:
                    gunluk_limit = yeni_limit
                    print(f"Gündəlik limit {gunluk_limit} AZN olaraq təyin edildi.")
                else:
                    print("xəta: müsbət ədəd daxil edin.")
            elif param_sec == "2":
                print("Endirim rejimi seçin:")
                print("1. Normal")
                print("2. Tələbə")
                print("3. Pensiyaçı")
                rejim_sec = input("Seçim (1/2/3): ")
                if rejim_sec == "1":
                    endirim_rejimi = "normal"
                elif rejim_sec == "2":
                    endirim_rejimi = "telebe"
                elif rejim_sec == "3":
                    endirim_rejimi = "pensiyaçı"
                else:
                    print("Yanlış seçim!")
                print(f"Endirim rejimi {endirim_rejimi} olaraq təyin edildi.")
        elif sec == "0":
            print("hesabdan çıxılır.")
            break
        else:
            print("yanlış seçim! Zəhmət olmasa 0-6 arası rəqəm daxil edin.")
else:
    print("zəhmət olmasa mövcud bir kart kodu daxil edin")
