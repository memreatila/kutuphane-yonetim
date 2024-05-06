import sqlite3

class veritabani:
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()

        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='kitaplar'")
        tablo_var_mi = self.cursor.fetchone()

        if not tablo_var_mi:  # Tablo yok
            self.cursor.execute('CREATE TABLE IF NOT EXISTS kitaplar (ID INTEGER PRIMARY KEY AUTOINCREMENT, ad TEXT, yazar TEXT, tur TEXT, Fotograf TEXT, Aciklama TEXT, Durum TEXT)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS kullanicilar (ID INTEGER PRIMARY KEY AUTOINCREMENT, kullaniciadi TEXT, sifre TEXT, ad TEXT, soyad TEXT, telefon TEXT)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS oduncler (ID INTEGER PRIMARY KEY AUTOINCREMENT, uyeid INTEGER, kitap TEXT, tarih TIMESTAMP)')

            kitaplar_tuple = [
                ("Sefiller", "Victor Hugo", "Trajedi", "sefiller.jpg", "Fransız yazarı Victor Hugo (1802-1885, Sefiller adlı dev romanının önsözünü şöyle bitirir: 'Yeryüzünde yoksulluk ve bilgisizliğin egemenliği sürdükçe, böylesi kitaplar gereksiz sayılmayabilir.' Victor Hugo, ateşli bir yurtseverdi. Yurdunun çıkarları adına siyasal kavgalardan hiç çekinmedi. Bu yüzden adına siyasal kavgalardan hiç çekinmedi. Bu yüzden de tam yirmi yıl sürgünde kaldı. Bu sürgün yılları, gerek şiir, gerek roman açısından onun en verimli dönemi oldu. Sefiller de bu yılların ürünüdür (1862). Bu dev romanı, genç okurlara yalınlaştırılmış, kısaltılmış biçimiyle sunarak, bu ölümsüz yapıta yeni okurlar kazandırmayı amaçlıyoruz.", "Mevcut"),
                ("Kürk Mantolu Madonna", "Sabahattin Ali", "Roman", "kurk.jpg", 'Her gün, daima öğleden sonra oraya gidiyor, koridorlardaki resimlere bakıyormuş gibi ağır ağır, fakat büyük bir sabırsızlıkla asıl hedefine varmak isteyen adımlarımı zorla zapt ederek geziniyor, rastgele gözüme çarpmış gibi önünde durduğum "Kürk Mantolu Madonna"yı seyre dalıyor, ta kapılar kapanıncaya kadar orada bekliyordum." Kimi tutkular rehberimiz olur yaşam boyunca. Kollarıyla bizi sarar. Sorgulamadan peşlerinden gideriz ve hiç pişman olmayacağımızı biliriz. Yapıtlarında insanların görünmeyen yüzlerini ortaya çıkaran Sabahattin Ali, bu kitabında güçlü bir tutkunun resmini çiziyor.', "Mevcut"),
                ("Tutunamayanlar", "Oğuz Atay", "Roman", "tutunamayanlar.jpg", 'Tutunamayanlar, Türk edebiyatının en önemli eserlerinden biridir. Berna Moran, Oğuz Atay\'ın bu ilk romanını "hem söyledikleri hem de söyleyiş biçimiyle bir başkaldırı" olarak niteler. Moran\'a göre "Oğuz Atay\'ın mizah gücü ve duyarlığı ve kullandığı teknik incelikler, Tutunamayanlar\'ı büyük bir yeteneğin ürünü yapmış, eserdeki bu yetkinlik Türk romanını çağdaş roman anlayışıyla aynı hizaya getirmiş ve ona çok şey kazandırmıştır. "Küçük burjuva dünyasını ve değerlerini zekice alaya alan Atay, "saldırısı tutunanların anlamayacağı, rededeceği türden bir romanla yazar."', "Mevcut"),
                ("Aşk-ı Memnu", "Halit Ziya Uşaklıgil", "Roman", "aşk.jpg", "Bihter hepsini unutmak isteyerek, kandili hala bütün bütüne yakmadığı için birtakım karartılar yansıtan aynanın karşısına geçiyor, çıplak gövdesine bakıyor, nergisçe bir tutumla hazdan sarsılıyordu. Başkaları ne düşünürdü bilmem, ama bu, kendi kendine tatmine giden yol, Bihter'i büsbütün yalnızlıkla sarıp sarmalardı. Hazlarda söze dökülemeyecek uçurumlar hissederdim. Romancı, Bihter için, 'Evet bu vücudu seviyor...' diye yazıyordu. Genç kadın ayna karşısındaydı, vücuduna sevgiler, vurgunluklar duyuyordu. Gülümsüyor, aynadaki aksinden sevda umuyordu.", "Mevcut"),
                ("80 Günde Devrialem", "Jules Verne", "Roman", "80.png", "Uçağın henüz icat edilmediği yıllar… Kısıtlı ulaşım koşulları, yolcuları bekleyen tehlikeler… Buna rağmen dünyanın etrafını seksen günde dönebileceğini iddia eden, dahası bütün servetini bu iddiaya yatıran bir adam… Seferlerin herhangi birinde yaşanabilecek en küçük bir gecikmenin her şeyi alt üst edeceği zamana karşı bu yarışı kazanabilecek mi? Phileas Fogg, uşağı Passepartout’yla birlikte kâh fırtınalarla boğuşan buharlı gemilerde, kâh birbirine bağlanmayan demiryolu hatlarında maceradan maceraya atılıyor.", "Mevcut"),
                ("Eylül", "Mehmet Rauf", "Dram", "eylul.jpg", "Her şey çürüyor, her şey... İnsanlar çürümeyecekler mi? Eylülde, sanki bahara hasret çeken hüzünlü bir tazelik, sanki üzerine çöken kışın kendisini yok etmek isteyen sonbahara rağmen devam etmek, yine bahar olmak mücadelesi vardır; fakat bunun için muhtaç olduğu şeylerden mahrumdur ve kendisinde de dayanma gücü kalmamıştır. Tabiat da bunu anlamış gibi acı bir düşünceyle üstüne çöken ıssızlığın, matemin altında ezilerek durur. Ne kadar uğraşırsa uğraşsın, ne kadar dayanabilirse dayansın kışın galip geleceğini, artık her şeyin, her ümidin bittiğini, buna dayanmak gerektiğini anlamaktan doğan bir güçsüzlük ile ağlar...", "Mevcut"),
                ("Kırmızı Başlıklı Kız", "Anonim", "Masal", "kırmızı.jpg", 'Adına yakışır şekilde kıpkırmızı giyinmeyi çok seven Kiraz, uzayın ta derinliklerinde, Sepet isimli bir galaksideki küçücük bir gezegende ailesiyle birlikte yaşıyordur. Günlerden bir gün, annesi Kiraz\'a önemli bir sorumluluk verir: Hasta büyükannesine bol vitaminli kurabiye götürmelidir. Tabii, yolda hiç oyalanmaması koşuluyla. Neden mi? Çünkü galakside bazı kötü kişilerin namı dolaşıyordur. Mesela Havkurt Gezegeni\'nin uydusunu birbirine katan murtlar gibi! Ve bu bol tüylü, korkunç yaratıkların göze alamayacakları şey yoktur...', "Mevcut"),
                ("Keloğlan", "Anonim", "Masal", "kel.jpg", 'Birçok masalın birinci kahramanı olan “Keloğlan”, başında saçı olmadığından dolayı bu adı almıştır. Genellikle hayatta yaşlı ve dul anasından başka kimsesi olmayan, doğuştan kel, fakir bir delikanlı olarak anlatılır fakat bazı masallarda kardeşleri vardır. Eğer masalda Keloğlan’ın kardeşleri varsa Keloğlan en küçükleridir ve kendisinden “deli oğlan” olarak bahsedilir. Birkaç masalda Keloğlan’ın babasından da bahsedilmiştir.', "Mevcut"),
                ("Romeo ve Juliet", "William Shakespeare", "Trajedi", "romeo.jpg", "Shakespeare'nin Romeo ve Juliet'i, 400 yıllık uzun bir süreçte değerini kaybetmeyen klasik eserler içerisinde yer alıyor. Önemli eser, birbirine düşman iki ailenin çocuklarının umutsuz aşkını işliyor. Yazar yapıtında romantik bir atmosfer yaratmayı başarıyor. William'ın romantik tragedya temalı eserini ölümsüzleştiren konusu, dili ve üslubu oluyor. Tipik bir Rönesans oyunu olan eserde yazıldığı dönemin toplumsal yapısının özellikleri de hissettiriliyor. Shakespeare, insan ilişkilerini gerçekçi ve dokunaklı bir şekilde işliyor. William Shakespeare'in gençlik yapıtları arasında yer alan bu eşsiz eser, yazıldığı dönemin ötesine geçerek tüm insanlığın üzerinde etki bırakmayı başarıyor.", "Mevcut")
            ]

            self.cursor.executemany('INSERT INTO kitaplar (ad, yazar, tur, fotograf, aciklama, durum) VALUES (?, ?, ?, ?, ?, ?)', kitaplar_tuple)
            self.cursor.execute("INSERT INTO kullanicilar (kullaniciadi, sifre, ad, soyad, telefon) VALUES ('enes', '123', 'Enes', 'Biçici', '5323184256')")
            self.connection.commit()

    def query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.connection.commit()
        return self.cursor
    
    def fetchall(self):
        return self.cursor.fetchall()
    
    def fetchone(self):
        return self.cursor.fetchone()
    
Veritabani = veritabani('sql.db')
