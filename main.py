import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#################################################################
###### OZON ### OZON ### OZON ### OZON ### OZON ### OZON ########
#################################################################
url = "https://www.ozon.ru/category/osveshchenie-15096"
driver.get(url)
time.sleep(5) # для загрузки страницы

carts = driver.find_elements(By.CLASS_NAME, "m5j_23")
parsed_data_oz = []
for cart in carts:
    try:
        name = cart.find_element(By.CSS_SELECTOR, "span.tsBody500Medium").text
        price = cart.find_element(By.CSS_SELECTOR, "span.c3015-a1").text.replace("\u2009", "").replace("₽", "") #compensation-text--kTJ0_rp54B2vNeZ3CTt2
        link = cart.find_element(By.CSS_SELECTOR, "a.tile-hover-target").get_attribute("href")
    except:
        print("Error")
        continue

    parsed_data_oz.append([name, price, link])

#################################################################
###### DIVAN ### DIVAN ### DIVAN ### DIVAN ### DIVAN ### OZON ###
#################################################################
driver.get("https://divan.ru/category/divany-i-kresla")
time.sleep(5)  # для загрузки страницы

carts = driver.find_elements(By.CLASS_NAME, "_Ud0k")
parsed_data_divan = []
for cart in carts:
    try:
        name = cart.find_element(By.CSS_SELECTOR, "span[itemprop='name']").text
        price = cart.find_element(By.CSS_SELECTOR, "span.ui-LD-ZU").text
        link = cart.find_element(By.CSS_SELECTOR, "link").get_attribute("href")
    except:
        print("Error")
        continue

    parsed_data_divan.append([name, price, link])

################# write in file #################################
driver.quit()

with open ("OZON_DIVAN.csv", "w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Наименование", "Цена", "ссылка"])
    writer.writerows(parsed_data_oz)
    writer.writerow([" ", " ", " "]) # просто разделяю в файлке озон и диван
    writer.writerow(["######", "######", "######"])
    writer.writerow([" ", " ", " "])
    writer.writerows(parsed_data_divan)