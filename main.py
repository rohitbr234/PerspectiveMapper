from agents.reddit_fetcher import RedditFetcher

if __name__ == "__main__":
    topic = "mindfulness and heart rate variability"
    fetcher = RedditFetcher(topic)
    posts = fetcher.fetch_posts()
    
    print(f"\nTop Reddit results for '{topic}':")
    for post in posts:
        print(f"→ {post['title']}\n  {post['url']}")
