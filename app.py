import requests
import time


def search_ids():
    response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")
    id_info = response.json()
    id_30 = id_info[:30]
    return id_30


def search_info_url(id_30):
    last_30_list = {}
    for id in id_30:
        response = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty")
        info = response.json()
        if info["url"] is None:
            last_30_list["title"] = info["title"]
            last_30_list["link"] = "None"
            continue
        last_30_list["title"] = info["title"]
        last_30_list["link"] = info["url"]
        print(last_30_list)
        time.sleep(1)


def main():
    id_30 = search_ids()
    search_info_url(id_30)


if __name__ == "__main__":
    main()
