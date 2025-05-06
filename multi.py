from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from supabase import create_client, Client
from threading import Thread, Event
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv
import string
import random
import sys
import os

SUPABASE_URL = "https://cqakrownxujefhtmsefa.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNxYWtyb3dueHVqZWZodG1zZWZhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzIyNjMyMzMsImV4cCI6MjA0NzgzOTIzM30.E9jJxNBxFsVZsndwhsMZ_2hXaeHdDTLS7jZ50l-S72U"
SUPABASE_TABLE_NAME = "aet"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)



def random_string(count):
    string.ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    return "".join(random.choice(string.ascii_letters) for x in range(count))

    # return random.choice(string.ascii_letters)


# Fungsi membaca CSV dengan rentang baris tertentu
def read_csv_range(filename, start, end):
    with open(filename, newline='', encoding='utf-8') as f:
        rows = [row[0] for i, row in enumerate(csv.reader(f)) if start <= i < end]
    return rows

# Rentang data yang diproses (misal dari baris 1 sampai 50)
start_row =0  # Baris pertama (0-based index)
end_row = 50  # Baris terakhir yang ingin diproses

# Deklarasi akun tunggal
email = "cwickgcobiebu"
password = "@@Eskepal123"

# Baca judul video sesuai rentang yang diinginkan
titles = read_csv_range("x.csv", start_row, end_row)

# Inisialisasi WebDriver


# Proses upload
for title in titles:
    try:
        kw = title

        username =  kw.replace(" ", "-")

        fix_username = username+'_'+random_string(5)

        judul =f'{kw} Leaked Onlyfans New Files Update - ({random_string(5)})' 

        slug = f'{username}-leaked-onlyfans-new-files-2025-{random_string(5)}'
        gmailnya = f'{fix_username}@gmail.com'
        print(judul)


        driver = webdriver.Chrome()
        driver.maximize_window()

        

        driver.get(f"https://aetherhub.com/Account/Register")
       
        time.sleep(5)

        driver.find_element(By.CSS_SELECTOR, '#Username').send_keys(slug)
        time.sleep(1)


        driver.find_element(By.CSS_SELECTOR, '#Email').send_keys(gmailnya)
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, '#Password').send_keys('CobaGas123OKx')
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, '#ConfirmPassword').send_keys('CobaGas123OKx')
        time.sleep(1)

        #angre

        driver.find_element(By.CSS_SELECTOR, '#Consent').click()
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, '#Newsletter').click()
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
        time.sleep(5)
        

        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[1]/form/div[16]/div/a').click()
        time.sleep(2)


        iframe = driver.find_element(By.ID, "profiledescription_ifr")

        # Pindah ke dalam iframe
        driver.switch_to.frame(iframe)

        konten = f'''
        {judul}<br><br> LINK ⏩⏩  <a href="https://clipsfans.com/{username}&ref=aet">https://clipsfans.com/{username}</a> 
    '''



        # Gunakan execute_script dengan argumen terpisah
        driver.execute_script("document.querySelector('#tinymce').innerHTML = arguments[0];", konten)


        time.sleep(3)

        driver.switch_to.default_content()
        

        driver.find_element(By.CSS_SELECTOR, '#descriptionSubmit').click()
        time.sleep(5)



        urlnya = f'https://aetherhub.com/User/{fix_username}'

        response = (
            supabase.table(SUPABASE_TABLE_NAME)
            .insert({"result": urlnya})
            .execute()
        )

     
        time.sleep(5)
        driver.close()
    except:
        driver.quit()

        
