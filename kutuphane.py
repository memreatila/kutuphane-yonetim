from datetime import datetime, timedelta
from veritabani import Veritabani

class Odunc:
    def __init__(self, kitap, uye):
        self.kitap = kitap
        self.uye = uye

    def odunc_al(self):
        tarih = datetime.today().date()
        Veritabani.query('INSERT INTO oduncler (uyeid, kitap, tarih) VALUES(?, ?, ?)', (self.uye.id, self.kitap.ad, tarih))
        self.kitap.durumguncelle('Mevcut Değil')

    def iade(self):
        Veritabani.query('DELETE FROM oduncler WHERE uyeid = ? and kitap = ?', (self.uye.id, self.kitap.ad))
        self.kitap.durumguncelle('Mevcut')


class Uye:
    def __init__(self, id, kullaniciadi, sifre, ad, soyad, telefon):
        self.id = id
        self.kullaniciadi = kullaniciadi
        self.sifre = sifre
        self.ad = ad
        self.soyad = soyad
        self.telefon = telefon

    @staticmethod
    def kayitol(kullaniciadi, sifre, ad, soyad, telefon):
        Veritabani.query('INSERT INTO kullanicilar (kullaniciadi, sifre, ad, soyad, telefon) VALUES(?, ?, ?, ?, ?)', (kullaniciadi, sifre, ad, soyad, telefon))
    
class Kitap:
    def __init__ (self, id, ad, yazar, tur, fotograf, aciklama, durum):
        self.id = id
        self.yazar = yazar
        self.ad = ad
        self.tur = tur
        self.fotograf = fotograf
        self.aciklama = aciklama
        self.durum = durum
        
    def durumguncelle(self, yenideger):
        self.durum = yenideger
        Veritabani.query('UPDATE kitaplar SET durum = ? WHERE ad = ?', (yenideger, self.ad))
