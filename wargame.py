import random
import time

class Canavar:
    def __init__(self,isim,hp,sp,position):
        self.isim=isim
        self.hp=hp
        self.sp=sp
        self.position=position
    def saldir(self):
        saldiri=self.sp
        kritik_vurus=random.randrange(1,4)
        if(kritik_vurus==2):
            print("KRİTİKKKKKKKK SALDIRIIIIIIII!!!!!!!!")
            print("Saldırı iki kat arttırıldı")
            saldiri=self.sp*2
        return saldiri
    def savun(self,sp):
        self.hp-=sp
        if(self.hp<0):
            print("Bir DÜŞMANI Öldürdün")
class Heroes:
    def __init__(self,isim,hp,sp,position):
        self.isim=isim
        self.hp=hp
        self.sp=sp
        self.position=position
    def saldir(self):
        saldiri=self.sp


        return saldiri
    def savun(self,sp):
        kritik_savunma=random.randrange(1,3)
        if(kritik_savunma==2):
            sp=sp/2
            print("ÇELİİİİİİİKKKKK SAVUNMAAAA!!!!!!!!!")
            print("Saldırı gücünün yarısı bloke edildi")
        self.hp-=sp
        if(self.hp<0):
            print("Bir ADAMIN Öldü")


canavarlar=[]
i=0
while(i<3):
    random_canavar_ismi="Canavar"+str(i+1)
    random_canavar_sp=random.randrange(35,50)
    random_canavar_hp=random.randrange(80,100)
    random_position=random.randrange(1,6)
    yeni_canavar=Canavar(random_canavar_ismi,random_canavar_hp,random_canavar_sp,random_position)
    canavarlar.append(yeni_canavar)
    i+=1
heroes=[]
i=0
while(i<3):
    hero_ismi="ALİ BARUTCU"
    random_hero_sp = random.randrange(35, 50)
    random_hero_hp = random.randrange(80, 100)
    position=int(input("Hangi konuma koyacaksınız"))
    yeni_hero=Heroes(hero_ismi,random_hero_hp,random_hero_sp,position)
    heroes.append(yeni_hero)
    i+=1


while(True):
    if (len(canavarlar) == 0):
        print("ZAFEERRRRRRR!!!")
        break
    if (len(heroes) == 0):
        print("KAYBETTİN!!!!!!")
        break
    flag_1=0
    print("Sıra Sende")
    print("Atak yapacağın konumu seç")
    att_position=int(input())
    for canavar in canavarlar:
        if(att_position==canavar.position):
            print("HEDEFFFFF VURULDUUUUUU")
            canavar.savun(heroes[0].saldir())
            if(canavar.hp<=0):
                canavarlar.pop()
            flag_1=1
    if(flag_1==0):
        print("KARAVANAAAA")
    time.sleep(2)
    flag_2=0
    print("Sıra karşı tarafta")
    time.sleep(2)
    random_att_position=random.randrange(1,6)
    for hero in heroes:
        if(random_att_position==int(hero.position)):
            print("VURULDUUUUUUUNNNNNNNNNNNNNN!!!!!!!!!")
            hero.savun(canavarlar[0].saldir())
            if(hero.hp<=0):
                heroes.pop()
            flag_2=1
    if(flag_2==0):
        print("GÜZEL SAVUNMAAAAA!!!!!!")
    time.sleep(2)

















