import random
import time
import threading

def randon_number():
    return random.randint(100000, 999999)

def generation_number():
    while not exit_flag.is_set():
        random_number = randon_number()
        set_random_number(random_number)
        print("Doğrulama Kodu:", random_number)
        time.sleep(10)

def user_input():
    while True:
        user_input = input("Doğrulama kodunu girin: ")

        try:
            user_input = int(user_input)
            if user_input == current_random_number:
                print("Giriş başarılı!")
                set_random_number(None)
                exit_flag.set()
                break  
            else:
                print("Hatalı giriş. Yeni doğrulama kodu oluşturuluyor...")
                set_random_number(randon_number())
        except ValueError:
            print("Geçersiz giriş. Lütfen bir sayı girin.")

def set_random_number(value):
    global current_random_number
    current_random_number = value

exit_flag = threading.Event()
current_random_number = randon_number()

generation_number = threading.Thread(target=generation_number)
generation_number.start()

get_user_input_thread = threading.Thread(target=user_input)
get_user_input_thread.start()

get_user_input_thread.join()
generation_number.join()
