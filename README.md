### Hello, I'm Matheus Alexander!

I'm a computer engineering student and backend developer based in Brazil. Currently, I'm learning pySpark to enhance my skills and knowledge in big data processing.

### 🔭 My GitHub Stats

<div align="center">
  <a href="https://github.com/Alexpiltzz">
    <img height="180em" src="https://github-readme-stats.vercel.app/api?username=Alexpiltzz&show_icons=true&theme=highcontrast&include_all_commits=true&count_private=true"/>
    <img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Alexpiltzz&layout=compact&langs_count=7&theme=highcontrast"/>
  </a>
</div>

### 📊 Top Languages (Average)

```python
import requests

def get_top_languages(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    repos = response.json()

    languages = {}

    for repo in repos:
        if not repo["private"]:
            repo_languages_url = repo["languages_url"]
            repo_languages_response = requests.get(repo_languages_url)
            repo_languages = repo_languages_response.json()

            for language, bytes_count in repo_languages.items():
                if language in languages:
                    languages[language] += bytes_count
                else:
                    languages[language] = bytes_count

    total_bytes = sum(languages.values())
    top_languages = {language: (bytes_count / total_bytes) * 100 for language, bytes_count in languages.items()}

    top_languages = dict(sorted(top_languages.items(), key=lambda item: item[1], reverse=True))

    return top_languages

username = "Alexpiltzz"
top_languages = get_top_languages(username)

for language, percentage in top_languages.items():
    print(f"{language}: {percentage:.2f}%")
```
