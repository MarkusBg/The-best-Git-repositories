import requests

# Функция для поиска репозиториев на GitHub по ключевому запросу
def get_github_repos(query, num_repos=3):
    url = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        repos = data['items'][:num_repos]

        print(f"\nTop {num_repos} repositories for '{query}':\n")
        for repo in repos:
            name = repo['name']
            owner = repo['owner']['login']
            stars = repo['stargazers_count']
            description = repo['description'] if repo['description'] else "No description"
            html_url = repo['html_url']

            print(f"Repo: {name}")
            print(f"Owner: {owner}")
            print(f"Stars: {stars}")
            print(f"Description: {description}")
            print(f"URL: {html_url}")
            print("-" * 60)
    else:
        print(f"Error fetching data for '{query}' from GitHub API.")

# Получение топ-3 репозиториев по Python
get_github_repos("Python")

# Получение топ-3 репозиториев по Machine Learning
get_github_repos("Machine Learning")

