from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from supabase import create_client, Client
from threading import Thread, Event
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv
import string
import random
import sys
import os

from concurrent.futures import (
    ThreadPoolExecutor,
    wait,
    FIRST_EXCEPTION,
)

SUPABASE_URL = "https://cqakrownxujefhtmsefa.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
SUPABASE_TABLE_NAME = "aet"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def random_string(count):
    string.ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return "".join(random.choice(string.ascii_letters) for x in range(count))


def load_data(start_data, end_data):
    script_dir = os.path.dirname(os.path.realpath("__file__"))
    data_file = os.path.join(script_dir, "x.csv")

    with open(data_file) as csv_data_file:
        data_account = list(csv.reader(csv_data_file, delimiter=","))

    return data_account[int(start_data):int(end_data)]


def run_bot(data_account, recover=1):
    kw = data_account[0]
    try:
        username = kw.replace(" ", "-")
        fix_username = username + '_' + random_string(5)

        judul = f'{kw} Leaked Onlyfans New Files Update - ({random_string(5)})'
        slug = f'{username}-leaked-onlyfans-new-files-2025-{random_string(5)}'
        gmailnya = f'{fix_username}@gmail.com'
        print(judul)

        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get("https://aetherhub.com/Account/Register")
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "Username")))

        driver.find_element(By.ID, 'Username').send_keys(slug)
        driver.find_element(By.ID, 'Email').send_keys(gmailnya)
        driver.find_element(By.ID, 'Password').send_keys('CobaGas123OKx')
        driver.find_element(By.ID, 'ConfirmPassword').send_keys('CobaGas123OKx')
        driver.find_element(By.ID, 'Consent').click()
        driver.find_element(By.ID, 'Newsletter').click()
        driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

        time.sleep(5)

        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[1]/form/div[16]/div/a').click()
        time.sleep(2)

        # Tunggu dan masuk ke iframe TinyMCE
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "profiledescription_ifr")))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tinymce")))

        konten = f'''
        {judul}<br><br> LINK ⏩⏩  <a href="https://clipsfans.com/{username}&ref=aet">https://clipsfans.com/{username}</a>
        '''

        try:
            driver.execute_script("document.querySelector('#tinymce').innerHTML = arguments[0];", konten)
        except Exception as e:
            print("JavaScript injection failed:", e)
            driver.save_screenshot("tinymce_error.png")
            driver.switch_to.default_content()
            return

        time.sleep(3)
        driver.switch_to.default_content()

        driver.find_element(By.ID, 'descriptionSubmit').click()
        time.sleep(5)

        urlnya = f'https://aetherhub.com/User/{slug}'

        supabase.table(SUPABASE_TABLE_NAME).insert({"result": urlnya}).execute()
        print(f"SUKSES CREATE: {kw}", file=sys.__stderr__)

        time.sleep(5)
        driver.quit()

    except Exception as e:
        if recover == 0:
            print(f"TERJADI ERROR: ${e}", file=sys.__stderr__)
            return e
        run_bot(data_account, recover - 1)


def main():
    if len(sys.argv) < 3:
        print('Params require "python script.py 0 5"')
        os._exit(1)

    start_data = int(sys.argv[1])
    end_data = int(sys.argv[2])

    if not start_data and not end_data:
        print('Params require "python script.py 0 5"')
        os._exit(1)

    data = load_data(start_data, end_data)

    with ThreadPoolExecutor(max_workers=1) as executor:
        futures = [
            executor.submit(run_bot, data[i])
            for i in range(len(data))
        ]
        wait(futures, return_when=FIRST_EXCEPTION)


if __name__ == "__main__":
    main()
