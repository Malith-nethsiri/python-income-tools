import requests
from datetime import datetime

API_KEY = "e9e23ad33152a87acabf52bf45abc8a2"  
def get_news():
    url = f"https://gnews.io/api/v4/top-headlines?lang=en&country=us&max=10&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    headlines = []
    for article in data.get("articles", []):
        headlines.append(article["title"])
    return headlines

def save_to_file(headlines):
    today = datetime.now().strftime("%Y-%m-%d")
    with open(f"headlines_{today}.txt", "w", encoding="utf-8") as f:
        for line in headlines:
            f.write(f"- {line}\n")

def main():
    news = get_news()
    save_to_file(news)
    print(f"{len(news)} headlines saved.")

if __name__ == "__main__":
    main()
