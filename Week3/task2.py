import csv
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def get_lottery_posts(page_url, file):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "cookie": "over18=1"
    }
    req = Request(page_url, headers=headers)
    try:
        response = urlopen(req)
        if response.status == 200:
            soup = BeautifulSoup(response.read(), "html.parser")
            posts = []
            for article in soup.find_all("div", class_="r-ent"):
                # Skip deleted articles
                if article.find("div", class_="title").text.strip() == "本文已刪除":
                    continue
                
                title = article.find("div", class_="title").text.strip()
                link = "https://www.ptt.cc" + article.find("div", class_="title").find("a")["href"]
                like_dislike_count = article.find("div", class_="nrec").text.strip()
                # If like/dislike count is empty, set it to 0
                if not like_dislike_count:
                    like_dislike_count = 0
                else:
                    like_dislike_count = like_dislike_count.strip()
                # Extract publish time
                publish_time = get_publish_time(link)
                if publish_time:
                    posts.append({"title": title, "like_dislike_count": like_dislike_count, "publish_time": publish_time})
            
            # Write to CSV file
            fieldnames = ["ArticleTitle", "Like/DislikeCount", "PublishTime"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            for post in posts:
                writer.writerow({"ArticleTitle": post["title"], "Like/DislikeCount": post["like_dislike_count"], "PublishTime": post["publish_time"]})
            
            # Return the URL of the next page
            next_page_url = get_next_page_url(soup)
            return next_page_url
        else:
            print("Failed to fetch posts")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    
def get_publish_time(link):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "cookie": "over18=1"
    }
    req = Request(link, headers=headers)
    try:
        response = urlopen(req)
        if response.status == 200:
            soup = BeautifulSoup(response.read(), "html.parser")
            time_elements = soup.find_all("span", class_="article-meta-value")
            if time_elements:
                publish_time = time_elements[-1].text.strip()
                return publish_time
            else:
                print(f"No publish time found for {link}")
                return ""
        else:
            print(f"Failed to fetch publish time for {link}")
            return ""
    except Exception as e:
        print(f"Error: {e}")
        return ""

def get_next_page_url(soup):
    prev_button = soup.find("a", text="‹ 上頁")
    if prev_button:
        return "https://www.ptt.cc" + prev_button["href"]
    else:
        return None

#確保單獨執行才進行：
if __name__ == "__main__":
    with open("article.csv", mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["ArticleTitle", "Like/DislikeCount", "PublishTime"])

        count = 0
        page_url = "https://www.ptt.cc/bbs/Lottery/index.html"
        while count < 3:
            page_url = get_lottery_posts(page_url, file)
            if page_url:
                count += 1
            else:
                break
