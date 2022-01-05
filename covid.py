import requests
from termcolor import colored
from bs4 import BeautifulSoup
URL = "https://www.worldometers.info/coronavirus/#countries"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
infos = soup.find_all("div", "maincounter-number")
cases = (infos[0].get_text())
deaths = (infos[1].get_text())
recoverd = (infos[2].get_text())
## Out put
print("COVID-19 \n")
print(colored("Cases: " + str(cases), "yellow"))
print(colored("Deahts: " + str(deaths), "red"))
print(colored("recoverd " + str(recoverd), "green"))