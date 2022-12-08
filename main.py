import requests as requests
from bs4 import BeautifulSoup
import random


def find_restaurants(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    new = soup.find_all("a", {"class": "css-1m051bw"})
    temp = []
    for i in range(2, 12):
        temp.append(new[i].text.strip())

    return temp


def main():
    yelp_links = []
    # (starting index, ending index, incrementer)
    for i in range(0, 51, 10):
        url = "https://www.yelp.com/search?find_desc=Restaurants&find_loc=29.566096%2C+-98.520598&l=g%3A-98.57173919677734%2C29.52118926983812%2C-98.46942901611328%2C29.61077466268004&attrs=RestaurantsPriceRange2.1%2CRestaurantsPriceRange2.2&start={}".format(
            i)
        yelp_links.append(url)

    final_list = []
    for links in yelp_links:
        results = find_restaurants(links)
        final_list = final_list + results

    random_num = random.randint(0, len(final_list))
    print(len(final_list))
    print(random_num)
    print(final_list[random_num])
    # print("Costco")


if __name__ == "__main__":
    main()
