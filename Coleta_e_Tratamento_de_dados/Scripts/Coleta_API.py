import requests


def enviar_arquivo():
    #Caminho do arquivo:
    caminho = 'C:/Users/user/Downloads/produtos_informatica.xlsx'

    # Chave da API
    api_key = 'Agx6uCczvTNugVVJyGt1Pz'

    # Enviar arquivo para a API
    with open(caminho, 'rb') as arquivo:
        requisicao = requests.post(
            url=f'https://www.filestackapi.com/api/store/S3?key={api_key}',
            files={'fileUpload': arquivo}
        )

    # Mostrar resposta bruta para debug
    print("Status:", requisicao.status_code)
    print("Resposta bruta:", requisicao.text)

    # Se a resposta for JSON, mostrar o link do arquivo
    if requisicao.status_code == 200:
        try:
            saida = requisicao.json()
            print("Arquivo enviado com sucesso! Link de acesso:", saida.get('url'))
        except ValueError:
            print("Não foi possível interpretar a resposta como JSON.")
    else:
        print("Erro ao enviar arquivo. Código:", requisicao.status_code)
def receber_arquivo(file_url):
    requisicao = requests.get(file_url)

    if requisicao.ok:
            with open('arquivo_baixado.xlsx', 'wb') as file:
                file.write(requisicao.content)
            print("Arquivo baixado com sucesso!")
    else:
        print("Erro ao baixar o arquivo!", requisicao.json())
enviar_arquivo()
receber_arquivo('https://cdn.filestackcontent.com/j1qSBqATxiNSsfq6GvwT')
