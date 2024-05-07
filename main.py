import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Autenticar utilizando o arquivo JSON de credenciais
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('/content/automacao-rh-3d5ee846210a.json', scope)
client = gspread.authorize(creds)

# Abrir a planilha pelo seu ID
planilha = client.open_by_key('15w-tc7V4ZI1t-jBqVOwsbThc-2oHi2y_5EQBHuloOQ0')

# Selecionar uma aba específica
aba = planilha.worksheet('Sheet1')

def adicionar_dados(dados):
    for linha in dados:
        aba.append_row(linha)

# Dados dos usuários fictícios
dados_usuarios = [
    ['12345678', 'Laura Oliveira', 'Engenheira de Software', 'São Paulo', 'Presente'],
    ['23456789', 'Marcos Santos', 'Analista Financeiro', 'Rio de Janeiro', 'Ausente'],
    ['34567890', 'Carolina Lima', 'Designer Gráfico', 'Belo Horizonte', 'Presente'],
    ['45678901', 'Roberto Silva', 'Gerente de Projetos', 'Brasília', 'Ausente'],
    ['56789012', 'Vanessa Costa', 'Psicóloga', 'Salvador', 'Presente'],
    ['67890123', 'Diego Fernandes', 'Consultor de Vendas', 'Recife', 'Presente'],
    ['78901234', 'Julia Pereira', 'Enfermeira', 'Fortaleza', 'Ausente'],
    ['89012345', 'Mateus Oliveira', 'Analista de Sistemas', 'Porto Alegre', 'Presente'],
    ['90123456', 'Fernanda Souza', 'Advogada', 'Curitiba', 'Ausente'],
    ['01234567', 'Lucas Santos', 'Estudante', 'Florianópolis', 'Ausente'],
    ['11223344', 'Ana Silva', 'Arquiteta', 'São Paulo', 'Presente'],
    ['22334455', 'Pedro Almeida', 'Professor', 'Belo Horizonte', 'Presente'],
    ['33445566', 'Mariana Costa', 'Médica', 'Porto Alegre', 'Ausente'],
    ['44556677', 'Rafaela Fernandes', 'Farmacêutica', 'Recife', 'Presente'],
    ['55667788', 'Gustavo Lima', 'Engenheiro Civil', 'Rio de Janeiro', 'Ausente'],
    ['66778899', 'Aline Pereira', 'Analista de Marketing', 'São Paulo', 'Presente'],
    ['77889900', 'Luciano Oliveira', 'Desenvolvedor de Software', 'Brasília', 'Ausente'],
    ['88990011', 'Juliana Santos', 'Contadora', 'Salvador', 'Presente'],
    ['99001122', 'Rodrigo Fernandes', 'Gerente de Vendas', 'Recife', 'Ausente'],
    ['00112233', 'Isabela Costa', 'Médica Veterinária', 'Porto Alegre', 'Presente'],
    ['11223344', 'Mariana Almeida', 'Advogada', 'Curitiba', 'Ausente'],
    ['22334455', 'Rafael Oliveira', 'Engenheiro Eletricista', 'Florianópolis', 'Presente'],
    ['33445566', 'Amanda Santos', 'Estudante', 'São Paulo', 'Ausente'],
    ['44556677', 'Luiz Fernandes', 'Analista de Recursos Humanos', 'Belo Horizonte', 'Presente'],
    ['55667788', 'Camila Lima', 'Farmacêutica', 'Rio de Janeiro', 'Ausente'],
    ['66778899', 'Felipe Costa', 'Professor', 'São Paulo', 'Presente'],
    ['77889900', 'Natália Silva', 'Psicóloga', 'Porto Alegre', 'Ausente'],
    ['88990011', 'Carlos Oliveira', 'Engenheiro Civil', 'Brasília', 'Presente'],
    ['99001122', 'Mariana Fernandes', 'Designer Gráfico', 'Curitiba', 'Ausente'],
    ['00112233', 'Gabriel Costa', 'Advogado', 'Recife', 'Presente'],
    ['11223344', 'Ana Santos', 'Analista de Sistemas', 'São Paulo', 'Presente'],
    ['22334455', 'Thiago Almeida', 'Consultor de Vendas', 'Rio de Janeiro', 'Ausente'],
    ['33445566', 'Larissa Oliveira', 'Gerente de Projetos', 'Salvador', 'Presente'],
    ['44556677', 'Pedro Costa', 'Engenheiro de Software', 'Belo Horizonte', 'Ausente'],
    ['55667788', 'Natália Fernandes', 'Estudante', 'Porto Alegre', 'Presente'],
    ['66778899', 'Lucas Silva', 'Enfermeira', 'Brasília', 'Ausente'],
    ['77889900', 'Fernanda Oliveira', 'Médica', 'São Paulo', 'Presente'],
    ['88990011', 'Daniel Santos', 'Farmacêutico', 'Recife', 'Ausente'],
    ['99001122', 'Isabela Costa', 'Professor', 'Rio de Janeiro', 'Presente'],
    ['00112233', 'Rafael Fernandes', 'Advogada', 'Belo Horizonte', 'Ausente'],
    ['11223344', 'Carolina Almeida', 'Analista de Marketing', 'Florianópolis', 'Presente'],
    ['22334455', 'Gustavo Santos', 'Desenvolvedor de Software', 'Curitiba', 'Ausente'],
    ['33445566', 'Juliana Oliveira', 'Contador', 'São Paulo', 'Presente'],
    ['44556677', 'Mateus Fernandes', 'Analista Financeiro', 'Porto Alegre', 'Ausente'],
    ['55667788', 'Amanda Costa', 'Engenheiro Civil', 'Salvador', 'Presente'],
    ['66778899', 'Lucas Oliveira', 'Psicólogo', 'Recife', 'Ausente'],
    ['77889900', 'Fernanda Santos', 'Consultor de Vendas', 'Belo Horizonte', 'Presente'],
    ['88990011', 'Thiago Costa', 'Gerente de Vendas', 'Brasília', 'Ausente'],
    ['99001122', 'Laura Almeida', 'Designer Gráfico', 'Rio de Janeiro', 'Presente'],
    ['00112233', 'Pedro Fernandes', 'Psiquiatra', 'Porto Alegre', 'Ausente'],
    ['11223344', 'Ana Lima', 'Engenheiro de Software', 'São Paulo', 'Presente'],
    ['22334455', 'Rafaela Oliveira', 'Estudante', 'Curitiba', 'Ausente'],
    ['33445566', 'Gustavo Costa', 'Advogado', 'Recife', 'Presente'],
    ['44556677', 'Juliana Fernandes', 'Analista de Sistemas', 'Rio de Janeiro', 'Ausente'],
    ['55667788', 'Lucas Lima', 'Consultor Financeiro', 'Belo Horizonte', 'Presente'],
    ['66778899', 'Fernanda Silva', 'Gerente de Projetos', 'Florianópolis', 'Ausente'],
    ['77889900', 'Thiago Oliveira', 'Engenheiro Civil', 'Salvador', 'Presente'],
    ['88990011', 'Amanda Santos', 'Desenvolvedor de Software', 'Recife', 'Ausente'],
    ['99001122', 'Rafael Fernandes', 'Contador', 'São Paulo', 'Presente'],
    ['00112233', 'Carolina Lima', 'Analista Financeiro', 'Porto Alegre', 'Ausente'],
    ['11223344', 'Gustavo Almeida', 'Engenheiro de Software', 'Belo Horizonte', 'Presente'],
    ['22334455', 'Juliana Oliveira', 'Estudante', 'Brasília', 'Ausente'],


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

# Exemplo de leitura de célula específica
