import random
import string

def generate_otp(length):
    return ''.join(random.choice(string.digits) for _ in range(length))

def main():
    print("OTP Generator")
    print("-------------")
    length = int(input("Masukkan panjang OTP: "))
    otp = generate_otp(length)
    print(f"OTP: {otp}")

if __name__ == "__main__":
    main()
    
