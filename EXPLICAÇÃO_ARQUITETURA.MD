*NÃO MEXER*

Aqui vou explicar como funciona a arquitetura atual do projeto, para que todos entendam o fluxo de dados e como cada componente interage.

A arquitetura pode mudar conforme o projeto evoluir, mas qualquer mudança importante deve ser avisada para o grupo antes.


main.py:
Responsável por organizar o fluxo principal do sistema.

Fluxo esperado:

Carrega dados
    ↓
Busca informações no banco
    ↓
Analisa os dados
    ↓
Executa o modelo de Machine Learning
    ↓
Detecta possível anomalia
    ↓
Gera alerta
    ↓
Envia resultado para o painel


--------------------------------------------------


config/:
Contém configurações do projeto.

Exemplo:

database.py

Responsável pelas configurações utilizadas na conexão com o banco.

AVISO:

Senhas, tokens e outras informações sensíveis NÃO devem ir para o GitHub.

Dados como:

HOST
USER
PASSWORD
DATABASE

devem ser armazenados em arquivos como:

.env

O arquivo .env deve estar dentro do .gitignore.

Exemplo:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=senha
DB_NAME=projeto_dat

Nunca colocar senhas diretamente no código.


--------------------------------------------------


database/:
Contém partes relacionadas à geração de dados e comunicação com o banco.

Arquivos atuais:

RegistrationSystem.py:
Responsável pela geração/cadastro de clientes fictícios utilizados para alimentar o sistema.

TransactionGenerator.py:
Responsável pela geração de transações fictícias utilizadas para testes e treinamento do sistema.

seed.py:
Contém dados, funções ou informações utilizadas pelos geradores para criar dados fictícios.

__init__.py:
Define a pasta database como um módulo Python.

Atualmente os geradores estão dentro de database/ porque fazem parte da preparação inicial dos dados do sistema.

Caso essa parte cresça muito no futuro, pode ser separada em outra pasta.


--------------------------------------------------


models/:
Contém a representação dos principais dados utilizados pelo sistema.

cliente.py:
Representa um cliente.

Pode possuir atributos como:

id
nome
email
cidade
dados de comportamento


transacao.py:
Representa uma transação.

Pode possuir atributos como:

id
cliente_id
valor
data_hora
cidade
tipo_transacao


alerta.py:
Representa um alerta gerado pelo sistema.

Pode possuir atributos como:

id
transacao_id
tipo_alerta
score_anomalia
data_hora


__init__.py:
Define a pasta models como um módulo Python.


--------------------------------------------------


ml/:
Contém toda a parte relacionada ao Machine Learning.

Essa é uma das partes principais do projeto.

preprocessamento.py:
Responsável por preparar os dados antes de enviar para o modelo.

Exemplos:

valor da transação
horário
frequência
cidade
distância
quantidade de transações
comportamento do cliente

Também pode realizar:

limpeza de dados
transformação de valores
normalização
seleção de características


treinamento.py:
Responsável pelo treinamento do modelo de Machine Learning.

Inicialmente será utilizado:

Isolation Forest

O objetivo é identificar transações que fogem do comportamento considerado normal.


modelo.pkl:

Pode ser gerado posteriormente pelo treinamento.

Esse arquivo NÃO deve ser criado ou editado manualmente.

Inicialmente não será versionado no GitHub.

O .gitignore deve conter:

*.pkl

Caso no futuro seja necessário versionar o modelo treinado, isso deve ser decidido pelo grupo.


--------------------------------------------------


ui/:
Contém a interface do sistema.

dashboard.py:
Responsável pelo painel utilizado para visualizar os resultados.

Pode mostrar:

clientes
transações
transações suspeitas
alertas
gráficos
estatísticas
resultado do Machine Learning

A tecnologia da interface pode ser definida posteriormente.

Exemplos:

Streamlit
Tkinter
Flask
ou outra solução


--------------------------------------------------


sql/:
Contém os scripts SQL utilizados pelo projeto.

schema.sql:
Responsável pela criação da estrutura do banco.

Exemplos:

CREATE DATABASE
CREATE TABLE
relacionamentos
chaves
tipos de dados


dados_teste.sql:
Pode conter dados SQL utilizados para testes.

Também pode ser utilizado para inserir alguns dados iniciais manualmente.


--------------------------------------------------


data/:
Pasta destinada a dados utilizados durante o desenvolvimento.

Pode futuramente conter:

datasets
arquivos CSV
dados temporários
dados gerados

Atualmente contém apenas:

.gitkeep

O .gitkeep serve para permitir que a pasta continue existindo no Git mesmo estando vazia.

Arquivos grandes ou dados sensíveis não devem ser enviados para o GitHub sem necessidade.


--------------------------------------------------


tests/:
Contém testes do projeto.

test_anomalia.py:
Responsável por testar a parte relacionada à detecção de anomalias e Machine Learning.


test_database.py:
Responsável por testar banco de dados, conexões e operações relacionadas.


Os testes existem para verificar se alterações feitas em uma parte do projeto não quebraram outras partes.


--------------------------------------------------


FLUXO GERAL DO PROJETO


MySQL
  ↓
Clientes e Transações
  ↓
Python
  ↓
Organização / Análise dos dados
  ↓
Pré-processamento
  ↓
Machine Learning
  ↓
Isolation Forest
  ↓
Score de anomalia
  ↓
Possível anomalia detectada
  ↓
Geração de alerta
  ↓
Dashboard


--------------------------------------------------


IMPORTANTE:

A arquitetura atual contém:

config/
data/
database/
ml/
models/
sql/
tests/
ui/

main.py


Atualmente NÃO existem as pastas:

repository/
services/
visualization/

Essas pastas não devem ser criadas apenas porque apareceram em versões antigas da documentação.

Caso o projeto cresça e seja necessário separar melhor as responsabilidades, elas podem ser adicionadas futuramente após decisão do grupo.


--------------------------------------------------


REGRA:

Antes de criar uma pasta nova ou alterar a arquitetura:

1. Verificar se realmente existe necessidade.
2. Avisar o grupo.
3. Atualizar esta documentação.
4. Fazer a alteração em uma branch.
5. Criar Pull Request para a main.


A arquitetura deve acompanhar o projeto real.

Não criar arquivos ou pastas apenas para deixar o projeto "mais bonito".