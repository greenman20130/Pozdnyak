from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service as ChromeService
import time
import threading



options = Options()
prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2,
                            'plugins': 2, 'popups': 2, 'geolocation': 2, 
                            'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2, 
                            'mouselock': 2, 'mixed_script': 2, 'media_stream': 2, 
                            'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2, 
                            'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2, 
                            'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2, 
                            'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2, 
                            'durable_storage': 2}}
options.add_experimental_option('prefs', prefs)
options.add_argument('--disable-dev-shm-usage')
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "eager"
service = ChromeService(desired_capabilities=caps)

def test_logic():
    driver = webdriver.Chrome(options=options, service=service)
    driver.get("https://rsport.ria.ru/20231219/boss-of-year-2023-1911702814.html")
    try:
        no = driver.find_element(By.XPATH, '//*[@id="endless"]/div[1]/div/div/div/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[4]/div[2]/div[1]/div[1]').click()
        no = driver.find_element(By.XPATH, '//*[@id="endless"]/div/div/div/div/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[5]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]').click()
        no = driver.find_element(By.XPATH, '//*[@id="endless"]/div/div/div/div/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[6]/div/div/div[1]').click()
        print("Голос отдан")
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