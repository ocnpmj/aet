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

from concurrent.futures import (
    ProcessPoolExecutor,
    ThreadPoolExecutor,
    wait,
    FIRST_EXCEPTION,
)

SUPABASE_URL = "https://cqakrownxujefhtmsefa.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNxYWtyb3dueHVqZWZodG1zZWZhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzIyNjMyMzMsImV4cCI6MjA0NzgzOTIzM30.E9jJxNBxFsVZsndwhsMZ_2hXaeHdDTLS7jZ50l-S72U"
SUPABASE_TABLE_NAME = "aet"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def random_string(count):
    string.ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    return "".join(random.choice(string.ascii_letters) for x in range(count))

    # return random.choice(string.ascii_letters)


def load_data(start_data, end_data):

    script_dir = os.path.dirname(os.path.realpath("__file__"))
    data_file = os.path.join(script_dir, "x.csv")

    data_account = []

    with open(data_file) as csv_data_file:
        data_account = list(csv.reader(csv_data_file, delimiter=","))

    data_account = data_account[int(start_data) : int(end_data)]

    return data_account





def run_bot(data_account, recover=1):
    kw = data_account[0]



    try:

        
           
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

        print("SAMPE SINI")


    #     iframe = driver.find_element(By.ID, "profiledescription_ifr")

    #     # Pindah ke dalam iframe
    #     driver.switch_to.frame(iframe)

    #     konten = f'''
    #     {judul}<br><br> LINK ⏩⏩  <a href="https://clipsfans.com/{username}&ref=aet">https://clipsfans.com/{username}</a> 
    # '''



      
    #     driver.execute_script("document.querySelector('#tinymce').innerHTML = arguments[0];", konten)


        time.sleep(3)

        # driver.switch_to.default_content()
        

        # driver.find_element(By.CSS_SELECTOR, '#descriptionSubmit').click()
        # time.sleep(5)



        urlnya = f'https://aetherhub.com/User/{slug}'

        # driver.get(urlnya)


        response = (
            supabase.table(SUPABASE_TABLE_NAME)
            .insert({"result": urlnya})
            .execute()
        )

        time.sleep(5)

        print(f"SUKSES CREATE: {kw}", file=sys.__stderr__)

        time.sleep(5)
        driver.close()
    except Exception as e:
        if recover == 0:
            print(
                f"TERJADI ERROR: ${e}",
                file=sys.__stderr__,
            )
            #driver.close()
            return e

        run_bot(data_account, recover - 1)


def main():

    if len(sys.argv) < 3:
        print('Params require "node run.js 0 5"')
        os._exit(1)

    start_data = int(sys.argv[1])
    end_data = int(sys.argv[2])

    workers = 1

    if not start_data and not end_data:
        print('Params require "node run.js 0 5"')
        os._exit(1)

    data = load_data(start_data, end_data)

    futures = []
    line_count = 0
    with ThreadPoolExecutor(max_workers=workers) as executor:
        for index in range(start_data + 1, end_data + 1):
            try:
                futures.append(
                    executor.submit(
                        run_bot,
                        data[line_count],
                    )
                )
            except:
                pass
            line_count += 1

    wait(futures, return_when=FIRST_EXCEPTION)


if __name__ == "__main__":
    main()
