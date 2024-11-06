import time
import requests
import re

class Scraper:
    def __init__(self, user_agents = [], urls = [], fail_download_content_patterns=[]):
        self.proxy_list = []
        self.user_agents = user_agents
        self.urls = urls
        self.fail_download_content_patterns = fail_download_content_patterns

    def prepare_proxy(self):
        url = 'https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=country&sort_type=desc'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            for proxy in data['data']:  # Зазвичай дані містяться у ключі 'data'
                if proxy['country'] == 'US':
                    #self.proxy_list.append({'country': proxy['country'], 'ip': proxy['ip'], 'port': proxy['port']})
                    #print(f"IP: {proxy['ip']}, Country: {proxy['country']}, Port: {proxy['port']}")
                    self.proxy_list.append(f'{proxy['ip']}:{proxy['port']}')

        else:
            print('fail')

    def start_downloading(self):
        self.prepare_proxy()
        urls = self.urls

        for url in urls:
            for proxy in self.proxy_list:
                print(f'PROXY: {proxy}')

                for user_agent in self.user_agents:
                    headers = {
                        "User-Agent": user_agent,
                        "Accept": '*/*',
                        "Accept-Language": 'uk,ru-RU;q=0.9,ru;q=0.8,en-US;q=0.7,en;q=0.6',
                        "Content-Type": 'application/json'
                    }

                    if len(self.proxy_list) == 0:
                        pass

                    print(f'####### {url} DOWNLOAD #######')

                    response = requests.get(url, proxies={'http': proxy}, headers=headers)
                    page = response.text

                    if len(self.fail_download_content_patterns) > 0:
                        for pattern in self.fail_download_content_patterns:
                            if re.search(pattern, page):
                                print(f'####### FAIL #######')
                            else:
                                print(f'####### DONE #######')
                    else:
                        print(page)

                    time.sleep(3)




