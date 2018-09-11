
import requests
import datetime
import time
import names
import os
import random
import proxymanager

#############EDIT HERE ONLY############
email = ('') # put END Clothing username
requested = 1 # amount that you want
password = '' # put your END Clothing password
size = 'UK 6'   # Please only put sizes that the website has avalible. check at the url
street1 = ''  # address line 1
city = ''   # city
state= ""   # state REMOVE IF OUTSIDE OF US
postcode = ''  # postcode
country = ''   # country
cardNumber = ''   # card number
cardMonth = '' # expiry month
cardYear = ''   # expiry year
cvv = '' # cvv
print(
    #ENDCLOTHING RAFFLE SCRIPT#
    #####MADE BY @Chaselazarian#####
)

proxy_manager = ProxyManager('proxies.txt')

def header():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

header()
catchall = 1
emaildomain = email
if '@' in email:
    emailname = email.split('@') [0]
    emaildomain = '@' + email.cplit('@') [1]
    catchall = 0
header()
headers = {
    'origin': 'https://launches.endclothing.com',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'accept': '*/*',
    'referer': 'https://launches.endclothing.com/product/nike-air-max-97-miami-921826-102',
    'authority': 'https://launches.endclothing.com',
    'x-requested-with': 'XMLHttpRequest',
    'request-source': 'freight',
}
registered = 0
s = requests.Session()

while registered < requested :
    fName = names.get_first_name()
    lName = names.get_last_name()
    s.cookies.clear()
    if catchall == 0:
        email = emailname + "+" + str(random.randomint(1, 999999)) + emaildomain
    else:
        email = names.get_first_name() + names.get_last_name() + "@" + emaildomain
    phone = "(" + str(random.randint(111, 999)) + ") " + str(random.randint(111, 999))
    data = [
        ('userEmail', email),
        ('firstName', fName),
        ('lastName', lName),
        ('password', password),
        ('s-launches-pdp__form__size__dropdown', size),
        ('telephone', phone),
        ('street1', street1),
        ('city', city),
        ('postCode', postcode),
        ('countryId', country),
        ('cardDetails', cardNumber),
        ('expirationMonth', cardMonth),
        ('expirationYear', cardYear),
        ('cvv', cvv),
        ('c-input-control__input', on)
    ]
    a = s.get('https://launches.endclothing.com/product/nike-x-undercover-react-element-87-bq2718-400', headers=headers)
    if a.status_code == 403:
        print("IP banned, RIP")
        input("")
        sys.exit()
    a = s.get('https://launches.endclothing.com/product/nike-x-undercover-react-element-87-bq2718-400', headers=headers)
    a = s.post('https://launches.endclothing.com/product/nike-x-undercover-react-element-87-bq2718-400', headers=headers, data=data)
    registered += 1
    header()
    print("Registered account #" + str(registered))
    time.sleep(0.1)
