import requests
from bs4 import BeautifulSoup as bs


class GetPttPost:
    def __init__(self, pages=1):
        self.pages = pages
        self.url = "https://www.ptt.cc/bbs/Gossiping/index.html"
        self.origin = requests.Session()
        self.payload = {
            'from': '/bbs/Gossiping/index.html',
            'yes': 'yes'
        }
        self.origin.post("https://www.ptt.cc/ask/over18", data=self.payload)

    def __iter__(self):
        for _ in range(self.pages):
            origin_data = self.origin.get(self.url)

            soup = bs(origin_data.text, "html.parser")
            posts = soup.select("div.r-ent")

            self.url = f"https://www.ptt.cc{soup.select('div.btn-group.btn-group-paging a')[1]['href']}"

            for post in posts:
                if '刪除' not in str(post.select('div.title')[0].text):
                    if '[公告]' not in str(post.select('div.title a')[0].text):
                        data = {"title": f"{post.select('div.title a')[0].text}",
                                "url": f"https://www.ptt.cc{post.select('div.title a')[0]['href']}",
                                "author": f"{post.select('div.meta div.author')[0].text}",
                                "date": f"{post.select('div.meta div.date')[0].text}",
                                "push": f"{post.select('div.nrec span.hl')[0].text if post.select('div.nrec')[0].text else ''}"}
                        yield data


if __name__ == "__main__":
    datas = GetPttPost(10)
    for i in datas:
        print(i)
        print("=" * 20)
