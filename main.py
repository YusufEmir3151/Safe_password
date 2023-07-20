from data import sql
from encryption import Encryption, reading


def show_menu():
    print("\n")
    print("1. Şifre Ekle")
    print("2. Şifre Sil")
    print("3. Şifreleri Görüntüle")
    print("4. Şifre Öğrenme")
    print("5. Şifre Değiştirme")
    print("6. Çıkış")


def add_password():
    inf = input("Şifre Başlığı: ")
    user = input("Kullanıcı adı/E-posta: ")
    password = input("Şifre: ")
    password_red = Encryption.calculate_password_red(password)
    sql.add_password(inf, user, password_red)
    print("Şifre başarıyla eklendi!")


def delete_password():
    inf = input("Silinecek şifrenin başlığını girin: ")
    sql.delete_password(inf)
    print("Şifre silindi!")


def display_passwords():
    print("\nKayıtlı Şifreler:\n")
    sql.display_passwords()


def get_password_by_title():
    title = input("Şifre başlığını giriniz: ")
    result = reading.get_password_by_title(title)
    print(result)


def change_password():
    inf = input("Şifresini değiştireceğiniz kaydın başlığını girin: ")
    new_password = input("Yeni şifre: ")
    new_password_red = Encryption.calculate_password_red(new_password)
    sql.change_password(inf, new_password_red)
    print("Şifre başarıyla değiştirildi!")


safe = input("Lütfen güvenlik şifresini giriniz: ")
if safe == 'YusufEmir2006':
    while True:
        show_menu()
        choice = input("Bir işlem seçin (1-5): ")

        if choice == "1":
            add_password()
        elif choice == "2":
            delete_password()
        elif choice == "3":
            display_passwords()
        elif choice == "4":
            get_password_by_title()
        elif choice == "5":
            change_password()
        elif choice == "6":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz bir seçim yaptınız. Tekrar deneyin.")
else:
    print("Hatalı giriş.")
    print(".")
    print(".")
    exit()
