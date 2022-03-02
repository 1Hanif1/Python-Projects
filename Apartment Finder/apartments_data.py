from pprint import pprint
from bs4 import BeautifulSoup
from requests import get

ZILLOW_URL = "https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55177535009766%2C%22east%22%3A-122.31488264990234%2C%22south%22%3A37.69926912019228%2C%22north%22%3A37.851235694487485%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"


class ApartmentsData():
    def __init__(self) -> None:
        self.header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15",
            "Accept-Language": "en-US"
        }

    def __fetch_data(self):
        response = get(url=ZILLOW_URL, headers=self.header)
        response.raise_for_status()
        self.response = response.text
        # pprint(response.text)

    def get_data(self):
        self.__fetch_data()
        soup = BeautifulSoup(self.response, 'html.parser')

        all_address = [add.getText().split("|")[-1] for add in soup.select(
            ".photo-cards.photo-cards_wow.photo-cards_short li .list-card-addr"
        )]
        all_prices = [price.getText() for price in soup.select(
            ".photo-cards.photo-cards_wow.photo-cards_short li .list-card-price")]
        all_links = []
        for link in soup.select(".list-card-top a"):
            anchor = link['href']
            if "http" not in anchor:
                all_links.append(f"https://www.zillow.com{anchor}")
            else:
                all_links.append(anchor)

        data = []
        if len(all_links) == len(all_address) == len(all_prices):
            for index in range(len(all_prices)):
                data.append(
                    (all_address[index], all_prices[index], all_links[index])
                )
        print(data)
        return data
