import requests
from bs4 import BeautifulSoup as soup

page = "https://www.myip.com/"

my_city_request = requests.get("https://www.iplocation.net/")
my_ip_request = requests.get(page)
get_page = soup(my_ip_request.content,'html.parser')
get_city_page = soup(my_city_request.content, 'html.parser')
my_city = get_city_page.find('span',attrs={'class':'ipinfo--location'}).text
my_country = get_page.find('div',attrs={'class':'info_2'}).text
provider_and_IP_elements = get_page.find_all('div', attrs={'class':'texto_1'})
my_provider_and_IP = [provider.text for provider in provider_and_IP_elements]

print("Your current IP: {}".format(my_provider_and_IP[0].replace("copy","").strip()))
print("Your current country: {}".format(my_country))
print("Your current city: {}".format(my_city.strip()).replace("[Details]",""))
print("Your current provider: {}".format(my_provider_and_IP[1].strip()))
print("\nProvided by: myip.com and iplocation.net")
print("github.com/g3th")


