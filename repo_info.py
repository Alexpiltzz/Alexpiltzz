import requests


# Função para obter as principais linguagens de todos os repositórios de um usuário
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
    top_languages = {
        language: (bytes_count / total_bytes) * 100
        for language, bytes_count in languages.items()
    }

    # Ordenar as linguagens por porcentagem de uso
    top_languages = dict(
        sorted(top_languages.items(), key=lambda item: item[1], reverse=True)
    )

    return top_languages


# Exemplo de uso
username = "Alexpiltzz"
top_languages = get_top_languages(username)

# Exibir as principais linguagens
for language, percentage in top_languages.items():
    print(f"{language}: {percentage:.2f}%")
