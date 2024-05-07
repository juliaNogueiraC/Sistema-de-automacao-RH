import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Autenticar utilizando o arquivo JSON de credenciais
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('caminho da pasta json', scope)
client = gspread.authorize(creds)

# Abrir a planilha pelo seu ID
planilha = client.open_by_key('id_da_planilha')

# Selecionar uma aba específica
aba = planilha.worksheet('aba da planilha')

def adicionar_dados(dados):
    for linha in dados:
        aba.append_row(linha)

# Dados dos usuários fictícios
dados_usuarios = [
    ['98765432', 'Maria Souza', 'Analista de Marketing', 'Rio de Janeiro', 'Presente'],
    ['87654321', 'João Santos', 'Engenheiro Civil', 'São Paulo', 'Presente'],
    ['76543210', 'Ana Oliveira', 'Contadora', 'Brasília', 'Ausente'],
    ['65432109', 'Luiz Pereira', 'Desenvolvedor de Software', 'Belo Horizonte', 'Presente'],
    ['54321098', 'Carla Ferreira', 'Gerente de Vendas', 'Recife', 'Ausente'],
    ['43210987', 'Rafael Costa', 'Médico', 'Porto Alegre', 'Presente'],
    ['32109876', 'Juliana Lima', 'Advogada', 'Curitiba', 'Presente'],
    ['21098765', 'Lucas Vieira', 'Estudante', 'Florianópolis', 'Ausente'],
    ['10987654', 'Fernanda Almeida', 'Arquiteta', 'Salvador', 'Ausente'],
    ['09876543', 'Ricardo Santos', 'Chef de Cozinha', 'Fortaleza', 'Presente'],
    ['98765433', 'Amanda Silva', 'Jornalista', 'Rio de Janeiro', 'Presente'],
    ['87654322', 'André Costa', 'Fotógrafo', 'São Paulo', 'Ausente'],
    ['76543211', 'Mariana Oliveira', 'Analista de Recursos Humanos', 'Brasília', 'Presente'],
    ['65432100', 'Gabriel Pereira', 'Professor', 'Belo Horizonte', 'Presente'],
    ['54321090', 'Camila Ferreira', 'Farmacêutica', 'Recife', 'Ausente']
]

# Adicionando os dados dos usuários fictícios
adicionar_dados(dados_usuarios)

# Função para deletar uma linha com base no nome do usuário
def deletar_por_nome(nome):
    dados = aba.get_all_values()
    for i, linha in enumerate(dados):
        if linha[1] == nome:  # Verifica se o nome está na segunda coluna (índice 1)
            aba.delete_rows(i + 1)  # Deleta a linha (índice começa em 1)

# Exemplo de deletar uma linha pelo nome do usuário
deletar_por_nome("nome")

# Exemplo de adicionar dados
#adicionar_dados('1234', 'pimba', 'vigia', 'piaui', 'ausente')

