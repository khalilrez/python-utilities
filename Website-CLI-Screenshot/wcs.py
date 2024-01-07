from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


from time import sleep
import os
import random

def insert():
    os.system('cls' if os.name == 'nt' else 'clear')
    website_url = input("Enter the URL of the page : (format: https://[www.]example.com ) \n")
    file_name = input("What should I save it as ? (Press Enter for random name)")
    random_names = ["solstice", "cascade", "enigma", "meteorite", "cacophony", "serendipity", "glimmer", "tapestry", "nostalgia", "kaleidoscope", "reverie", "monolith", "firmament", "effervescent", "ephemeral", "chasm", "silhouette", "crescendo", "reverie", "citadel", "azure", "ebony", "embark", "serenade", "constellation", "epiphany", "equilibrium", "symphony", "penumbra", "quixotic", "gossamer", "chimera", "elegy", "dunescape", "turquoise", "serpentine", "mausoleum", "effervescent", "celestial", "ambrosia", "meander", "reverence", "effigy", "solstice", "nebula", "symphony", "chimera", "firmament", "cascady", "enigmo"]

    if file_name == "":
        file_name = random.choice(random_names) + "-" + random.choice(random_names) + str(int(random.random()*9999))
    return website_url, file_name

def screenCapture(website_url,file_name):
    options = Options()
    service = Service(executable_path='./geckodriver')
    browser = webdriver.Firefox(options=options,service=service)

    browser.get(website_url)
    sleep(1)
    
    browser.save_screenshot(f"{file_name}.png")
    browser.quit()
    print("Done ! Saved as :" + file_name+".png")

website_url,file_name = insert()
print("Just a sec! ")
screenCapture(website_url,file_name)