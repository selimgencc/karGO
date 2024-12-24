import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

# SMTP ayarları (Gmail örneği)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = ""  # Gönderici e-posta adresi
EMAIL_PASSWORD = ""  # Uygulama şifresi

def generate_random_six_digit_number():
    """Rastgele 6 haneli bir sayı üretir ve string olarak döner."""
    return str(random.randint(100000, 999999))

def send_email():
    try:
        # Sabit değerler
        recipient = "Recipient Email"
        subject = "karGO"
        body = f"Sayın müşterimiz siparişiniz kargoya verilmiştir. Doğrulama kodunuz: {generate_random_six_digit_number()}"

        # E-posta mesajı oluştur
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # SMTP sunucusuna bağlan ve mesajı gönder
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Şifrelemeyi etkinleştir
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        print("Email başarıyla gönderildi!")

    except Exception as e:
        print(f"Bir hata oluştu: {str(e)}")

if __name__ == "__main__":
    send_email()
