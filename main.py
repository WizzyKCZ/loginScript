import requests
from bs4 import BeautifulSoup

cookies = {
    'ZPUSOB_OVERENI': 'SOL',
    '__utma': '258762120.601741167.1631258897.1636097265.1636101210.4',
    '__utmz': '258762120.1636101210.4.4.utmcsr=aplikace.skolaonline.cz|utmccn=Logout|utmcmd=Logout',
    '__gads': 'ID=9fc72c915f35064c-22e843f30bc90002:T=1631258897:RT=1631258897:S=ALNI_MZREDCRNR3DTJW_LSZa2FbQSa6HEQ',
    '__gpi': '00000000-0000-0000-0000-000000000000&c2tvbGFvbmxpbmUuY3o=&Lw==',
    'cookieconsent_dismissed': 'yes',
    '__utmc': '258762120',
    'ASP.NET_SessionId': 'uosall3lhvy4amoxefd1wvsw',
    'SERVERID': 'apl-1',
    '__utmb': '202636225.11.10.1636100951',
    '.ASPXAUTH': 'CC1327B1C78D32613CF8D190733EF23888D5A202AFACD79D9482997715FC868B360400545479FA6EE617E9FACA245B9E851CA47A4F9B5CF797B9830006C43C374C3CD883175E6420F55DC4B88781D5D030DC2A83D8117C29D229FFBDD77C75B34C6A3C3596C4163C3E4E29752F89856E2CEFAE90',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
}

response = requests.get('https://aplikace.skolaonline.cz/SOL/App/Spolecne/KZZ010_RychlyPrehled.aspx#', headers=headers, cookies=cookies)

soup = BeautifulSoup(response.content, 'html.parser')

print(soup)