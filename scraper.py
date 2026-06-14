import requests
from bs4 import BeautifulSoup

def get_trending_repos():
    url = "https://github.com/trending"
    response = requests.get(url)
    if response.status_code != 200:
        return "Failed to fetch trending repositories."

    soup = BeautifulSoup(response.text, 'html.parser')
    repos = []
    
    # GitHub trending repos are in <article> tags
    for article in soup.select('article'):
        h2 = article.select_one('h2')
        if h2 and h2.a:
            repo_name = h2.a.text.strip().replace('\n', '').replace(' ', '')
            repos.append(repo_name)
    
    return repos[:5]

if __name__ == "__main__":
    print("--- Top 5 Trending Repositories on GitHub ---")
    trending = get_trending_repos()
    for i, repo in enumerate(trending, 1):
        print(f"{i}. {repo}")
