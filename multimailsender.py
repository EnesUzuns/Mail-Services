import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# E-posta gönderen ve şifresini belirle
gonderen_mail = "metamaskcuzdan31@gmail.com"
gonderen_sifre = "ilkixfcoxsbtzdxc"

mesaj = MIMEMultipart()
mesaj['From'] = "Kimden gidecek olan email adresiniz"
mesaj['Subject'] = "Mail konu başlığınız"

# E-posta içeriğini belirle
icerik = """
<html>
<head>
    <title>Email HTML Örneği</title>
</head>
<body>
    <h1>Merhaba Dünya!</h1>
    <p>HTML ile e-posta içeriğine özel bir şey ekleyin.</p>
</body>
</html>
"""
mesaj_yapisi = MIMEText(icerik, 'html')
mesaj.attach(mesaj_yapisi)
# E-posta gönderilecek dosya yolu ve e-posta listesini oku
dosya_yolu = "C:\\Users\\enes.uzun\\Desktop\\email_list.txt"
with open(dosya_yolu, "r") as dosya:
    satir = dosya.readline()

    while satir:
        try:
            # SMTP ayarları ve bağlantısı
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login(gonderen_mail, gonderen_sifre)

            # E-postayı gönder
            mail.sendmail(mesaj['From'], satir.strip(), mesaj.as_string())
            print("{} adresine mail gönderildi".format(satir.strip()))
            mail.close()
        except Exception as e:
            print("{} adresine mail gönderilemedi. Hata: {}".format(satir.strip(), str(e)))

        # Sonraki satıra geç
        satir = dosya.readline()

# Dosyayı kapat
dosya.close()
