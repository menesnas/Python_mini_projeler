"""  class örneği  """
class HarfSayaci():
    def __init__(self):
        self.sesliharf = "aeiuo"
        self.sessizharf = "bcdfghjklmnprstvyz"
        self.sayac_sesli = 0
        self.sayac_sessiz = 0
    
    def kelime_sor(self):      # fonksiyon içinde self olarak parametre gönderilmesi,nesnenin bu sınıfın bir örneği olduğu ve bu örneğin bir özelliği olduğu anlamı taşır
        return input("Kelime girin : ")
    
    def seslidir(self,harf):
        return harf in self.sesliharf
    
    def sessizdir(self,harf):
        return harf in self.sessizharf
    
    def artir(self):
        for harf in self.kelime:
            if self.seslidir(harf):
                self.sayac_sesli += 1
            if self.sessizdir(harf):
                self.sayac_sessiz += 1
        return (self.sayac_sesli, self.sayac_sessiz)    # tuple[int,int] değeri döndürür. 'Type hinting'
    
    def ekran_yazdir(self):
        sesli, sessiz = self.artir()    # tuple[int,int] int değişkenlere atandı.
        mesaj = "{} kelimesinde {} adet sesli harf, {} adet sessiz harf bulunur..."
        print(mesaj.format(self.kelime,sesli,sessiz))
    
    def calistir(self):
        self.kelime = self.kelime_sor()
        self.ekran_yazdir()

instance = HarfSayaci()
instance.calistir()