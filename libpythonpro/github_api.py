import requests


def buscar_avatar(usuario):
    """
    Busca um avatar de um user no github
    :param usuario: str com o nome do usuario no Github
    :return:str com o link do avatar
    """

    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']
