from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import threading
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

def test_logic():
    driver = webdriver.Chrome(options=options)
    driver.get("https://rsport.ria.ru/20231219/boss-of-year-2023-1911702814.html")
    time.sleep(2)
    try:
        no = driver.find_element(By.XPATH, '//*[@id="endless"]/div[1]/div/div/div/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[4]/div[2]/div[1]/div[1]').click()
        no = driver.find_element(By.XPATH, '//*[@id="endless"]/div/div/div/div/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[5]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]').click()
        no = driver.find_element(By.XPATH, '//*[@id="endless"]/div/div/div/div/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[6]/div/div/div[1]').click()
        time.sleep(2)
    except:
        driver.quit()
    finally:
        driver.quit()

inp = input(f"""Введите кол-во браузеров запущенных одновременно: 
Учти, что при большом количестве браузеров компу может прийти пизда)))""")

while True:
    N = int(inp)   # Number of browsers to spawn
    thread_list = list()
# Start test
    for i in range(N):
        t = threading.Thread(name='Браузер {}'.format(i), target=test_logic)
        t.start()
        time.sleep(1)
        print(t.name + ' запущен')
        thread_list.append(t)

    # Wait for all threads to complete
    for thread in thread_list:
        thread.join()