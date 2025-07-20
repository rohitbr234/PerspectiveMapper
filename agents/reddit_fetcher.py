import requests
from bs4 import BeautifulSoup

class RedditFetcher:
    def __init__(self, topic, limit=5):
        self.topic = topic
        self.limit = limit
        self.base_url = "https://www.reddit.com/search/?q="

    def fetch_posts(self):
        headers = {'User-Agent': 'PerspectiveMapper/0.1'}
        query_url = f"{self.base_url}{self.topic.replace(' ', '%20')}&sort=relevance"
        response = requests.get(query_url, headers=headers)

        if response.status_code != 200:
            print(f"[RedditFetcher] Failed to fetch. Status code: {response.status_code}")
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        posts = []

        for link in soup.find_all("a", href=True):
            href = link["href"]
            if "/r/" in href and "/comments/" in href:
                title = link.get_text(strip=True)
                if title:
                    posts.append({"title": title, "url": f"https://www.reddit.com{href}"})
                if len(posts) >= self.limit:
                    break

        return posts
