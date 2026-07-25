import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Scanner;
import os
import random
import string

def generate_otp(length):
    return ''.join(random.choice(string.digits) for _ in range(length))

def main():
    print("OTP Generator")
    print("============")
    print("Author: R3zytH3cker")
    print("------------")
    length = int(input("Masukkan panjang OTP: "))
    otp = generate_otp(length)
    print("OTP:", otp)

if __name__ == "__main__":
    main()
    
public class OTPScraper {
    public static void main(String[] args) throws Exception {
        String apiUrl = "https://api.simulasi.com/otp";
        OTPScraper otpScraper = new OTPScraper(apiUrl);
        otpScraper.simulasiOTP();
    }

    public void simulasiOTP() throws Exception {
        while (true) {
            String otp = getOTP(apiUrl);
            if (otp != null) {
                System.out.println("OTP: " + otp);
            } else {
                System.out.println("Gagal mengakses API");
            }
            Thread.sleep(1000);
        }
    }

    public String getOTP(String apiUrl) throws Exception {
        URL url = new URL(apiUrl);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("GET");
        int responseCode = connection.getResponseCode();
        if (responseCode == 200) {
            BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            String inputLine;
            StringBuffer content = new StringBuffer();
            while ((inputLine = in.readLine()) != null) {
                content.append(inputLine);
            }
            in.close();
            return content.toString();
        } else {
            return null;
        }
    }
}
