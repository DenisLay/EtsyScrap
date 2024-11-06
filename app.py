from bs4 import BeautifulSoup
import requests
from scraper import Scraper


user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
]

def wrap_to_search_url(url, query):
    return f'{url}/search?q={query.replace(" ", "%20").replace("\n", "")}&ref=search_bar'

base_url = 'https://www.etsy.com'

url = wrap_to_search_url(base_url, 'leather box')
link = 'https://www.etsy.com/c/clothing/boys-clothing/costumes?ref=pagination&explicit=1&page=1'

scraper = Scraper(user_agents=user_agent_list, urls=[link], fail_download_content_patterns=[r"https://ct\.captcha-delivery\.com/c\.js"])

scraper.start_downloading()



# headers = {
#     "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
#     "Accept": '*/*',
#     "Accept-Language": 'uk,ru-RU;q=0.9,ru;q=0.8,en-US;q=0.7,en;q=0.6',
#     "Content-Type": 'application/json'
# }

