# Gmail hesaplarını kontrol eder gmail hesabına github hesabı varsa ismini gösterir

import requests

def check_mail_validity(email):
    url = "https://mailcheck.co/api/checkMail"
    headers = {"Content-Type": "application/json"}
    data = {"email": email}

    try:
        response = requests.post(url, headers=headers, json=data)

        if response.ok:
            result = response.json()
            smtp_exists = result.get("smtpExists", False)

            if smtp_exists:
                print(f"E-posta geçerli: {email}")
                return True
            else:
                print(f"E-posta geçerli değil: {email}")
                return False
        else:
            print(f"HTTP Hata ({response.status_code}): {email}")
            return False
    except Exception as e:
        print(f"Bir hata oluştu: {email}, {e}")
        return False

def save_valid_emails(file_path, valid_emails_file):
    try:
        with open(file_path, "r") as file:
            emails = file.readlines()

            with open(valid_emails_file, "w") as valid_file:
                for email in emails:
                    if check_mail_validity(email.strip()):
                        valid_file.write(email)

    except FileNotFoundError:
        print("Belirtilen dosya bulunamadı.")

# Kullanım örneği:
file_path = "email_list.txt"  # Okunacak dosyanın yolu
valid_emails_file = "valid_emails.txt"  # Geçerli e-posta adreslerinin kaydedileceği dosyanın adı
save_valid_emails(file_path, valid_emails_file)
