import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Autenticar utilizando o arquivo JSON de credenciais
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('seu caminho json', scope)
client = gspread.authorize(creds)

# Abrir a planilha pelo seu ID
planilha = client.open_by_key('id da planilha')

# Selecionar uma aba específica
aba = planilha.worksheet('aba da planilha')

# Função para adicionar uma nova linha com os dados especificados
def adicionar_dados(telefone, nome, cargo, regiao, status):
    nova_linha = [telefone, nome, cargo, regiao, status]
    aba.append_row(nova_linha)

# Função para deletar uma linha com base no nome do usuário
def deletar_por_nome(nome):
    dados = aba.get_all_values()
    for i, linha in enumerate(dados):
        if linha[1] == nome:  # Verifica se o nome está na segunda coluna (índice 1)
            aba.delete_rows(i + 1)  # Deleta a linha (índice começa em 1)

# Exemplo de deletar uma linha pelo nome do usuário
deletar_por_nome("")

# Exemplo de adicionar dados
adicionar_dados('123456789', 'Lucas Silva', 'Analista', 'São Paulo', 'Ativo')