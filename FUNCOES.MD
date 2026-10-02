**Aqui eu queria organizar oque cada um vai fazer**


# *NÃO MEXER*

# DIVISÃO DE FUNÇÕES

Essa divisão serve para definir os principais responsáveis por cada parte do projeto.

Responsável principal NÃO significa que somente aquela pessoa pode alterar o arquivo.
Caso seja necessário alterar uma parte de outra pessoa, avisar antes para evitar conflito.

--------------------------------------------------

*`Andrey` — SQL + análise de dados*

Responsável principalmente pela estrutura do banco e análise inicial dos dados.

PRINCIPAL:

├── sql/
│   ├── schema.sql
│   └── dados_teste.sql
│
└── models/
    ├── cliente.py
    └── transacao.py

FUNÇÕES:

- Criar a estrutura das tabelas SQL.
- Criar tabelas de clientes.
- Criar tabelas de transações.
- Criar tabela de alertas.
- Definir tipos de dados e relacionamentos.
- Criar consultas SQL necessárias para análise.
- Auxiliar na organização dos dados utilizados pelo Pandas.
- Fazer análise inicial dos dados.
- Analisar valores, horários, quantidade de transações e comportamento geral.
- Auxiliar Ian e Murilo na escolha de dados relevantes para Machine Learning.

APOIO:

├── database/
└── ml/preprocessamento.py


--------------------------------------------------

*`Ian` — Machine Learning / IA + Python*

Responsável principal pela parte de Machine Learning do projeto.

PRINCIPAL:

├── ml/
│   ├── preprocessamento.py
│   └── treinamento.py
│
└── tests/
    └── test_anomalia.py

FUNÇÕES:

- Preparar os dados utilizados pelo Machine Learning.
- Escolher as características importantes das transações.
- Transformar e organizar os dados.
- Trabalhar com Pandas e Scikit-learn.
- Criar e treinar o modelo de detecção de anomalias.
- Trabalhar inicialmente com Isolation Forest.
- Criar score de anomalia.
- Identificar transações normais e suspeitas.
- Testar o modelo.
- Avaliar resultados.
- Reduzir falsos positivos.
- Ajustar parâmetros do modelo.
- Criar funções Python auxiliares relacionadas ao ML.
- Trabalhar junto com Murilo na apresentação dos resultados.
- Trabalhar junto com Joaquim na integração entre modelo e sistema.

APOIO:

├── database/TransactionGenerator.py
├── models/transacao.py
├── ui/dashboard.py
└── main.py

Ian é o principal responsável técnico pelo núcleo de Machine Learning.


--------------------------------------------------

*`Joaquim` — alertas + segurança + lógica Python + integração*

Responsável principalmente pela lógica do sistema, geração de alertas, segurança e integração geral.

PRINCIPAL:

├── models/
│   ├── alerta.py
│   ├── cliente.py
│   └── transacao.py
│
├── main.py
│
└── tests/
    └── test_database.py

FUNÇÕES:

- Criar a lógica principal do sistema.
- Integrar as diferentes partes do projeto.
- Criar funções Python para busca de clientes.
- Criar funções Python para busca de transações.
- Criar funções para cadastro quando necessário.
- Receber resultados do Machine Learning.
- Criar a lógica para geração de alertas.
- Trabalhar com validação de dados.
- Fazer tratamento de erros.
- Trabalhar com segurança geral do sistema.
- Evitar entrada de dados inválidos.
- Evitar consultas SQL inseguras.
- Integrar banco, Machine Learning e dashboard.
- Organizar o funcionamento do main.py.
- Criar testes de integração.
- Auxiliar Ian e Murilo quando houver necessidade de integração entre módulos.

APOIO:

├── database/
├── ml/
├── ui/
└── tests/

Joaquim fica como principal responsável pela integração final do sistema.


--------------------------------------------------

*`Zati` — integração SQL ↔ Python*

Responsável principalmente pela comunicação entre Python e MySQL.

PRINCIPAL:

├── config/
│   └── database.py
│
└── database/
    ├── seed.py
    ├── RegistrationSystem.py
    └── TransactionGenerator.py

FUNÇÕES:

- Criar a configuração da conexão com MySQL.
- Utilizar variáveis do arquivo .env.
- Criar conexão entre Python e banco.
- Fazer tratamento básico de erros de conexão.
- Trabalhar com inserção de dados no MySQL.
- Trabalhar com leitura de dados do MySQL.
- Auxiliar no gerador de cadastros.
- Auxiliar no gerador de transações.
- Garantir que os dados gerados consigam chegar corretamente ao banco.
- Trabalhar junto com Andrey na compatibilidade entre Python e as tabelas SQL.

OBS:

RegistrationSystem.py e TransactionGenerator.py já possuem código inicial e devem ser utilizados como base.

APOIO:

├── sql/
├── models/
└── main.py


--------------------------------------------------

*`Murilo` — painel + visualização + apoio em Machine Learning*

Responsável principalmente pela interface e visualização dos resultados do sistema.

PRINCIPAL:

├── ui/
│   └── dashboard.py
│
└── tests/

FUNÇÕES:

- Criar o dashboard do sistema.
- Mostrar clientes.
- Mostrar transações.
- Mostrar transações consideradas anômalas.
- Mostrar alertas.
- Criar filtros.
- Criar gráficos.
- Mostrar estatísticas.
- Mostrar resultados do modelo de Machine Learning.
- Trabalhar junto com Ian na análise das detecções.
- Auxiliar nos testes do modelo.
- Auxiliar na avaliação dos resultados.
- Trabalhar com Matplotlib.
- Trabalhar na integração entre ML e painel.

APOIO:

├── ml/
├── models/
└── main.py

Murilo trabalha junto com Ian na parte de Machine Learning, mas Ian é o responsável principal pelo modelo.


--------------------------------------------------

# RESPONSABILIDADES GERAIS

Machine Learning:
Ian - principal
Murilo - apoio

Integração geral:
Joaquim - principal
Ian e Murilo - apoio

SQL:
Andrey - principal

Integração Python / MySQL:
Zati - principal

Dashboard:
Murilo - principal

Alertas:
Joaquim - principal

Segurança e validações:
Joaquim - principal

Análise de dados:
Andrey - principal
Ian e Murilo - apoio

Testes:
Ian
Joaquim
Murilo

Documentação:
Todos devem documentar alterações importantes da própria parte.

Pull Requests:
Sempre que possível, quem não escreveu a alteração deve revisar antes do merge.

--------------------------------------------------

# OBSERVAÇÃO

Não criar novas pastas ou arquivos principais sem necessidade.

Caso seja necessário alterar a arquitetura do projeto, avisar o grupo antes.

A divisão de funções serve para organização e não impede colaboração entre os integrantes.