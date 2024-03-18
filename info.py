import requests

# Seu nome de usuário do GitHub
username = "Alexpiltzz"

# URL da API para obter estatísticas de contribuição
url = f"https://api.github.com/users/{username}/stats/contributors"

# Faça a solicitação GET para a API do GitHub
response = requests.get(url)

# Verifique se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Extrai os dados de resposta em formato JSON
    data = response.json()

    # Se houver dados disponíveis
    if data:
        # Extraia estatísticas de contribuição
        total_commits = sum(contributor["total"] for contributor in data)
        total_additions = sum(contributor["weeks"][-1]["a"] for contributor in data)
        total_deletions = sum(contributor["weeks"][-1]["d"] for contributor in data)

        # Formate os dados em Markdown
        markdown_content = f"""
        ## Estatísticas de Contribuição do GitHub
        
        - Total de Commits: {total_commits}
        - Total de Adições de Linhas: {total_additions}
        - Total de Remoções de Linhas: {total_deletions}
        """

        # Imprima o conteúdo Markdown
        print(markdown_content)
    else:
        print("Não há dados disponíveis para exibir estatísticas de contribuição.")
else:
    print(
        f"Falha ao obter estatísticas de contribuição. Código de status: {response.status_code}"
    )
