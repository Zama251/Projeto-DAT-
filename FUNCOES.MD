**Aqui eu queria organizar oque cada um vai fazer**


# *NÃO MEXER*

*`Andrey` — SQL + análise de dados*

Responsável principalmente pela estrutura dos dados no banco e pela análise inicial dos dados.

PRINCIPAL:
├── sql/
│   ├── schema.sql
│   └── dados_teste.sql
│
├── database/tabelas.py
│
└── services/analise_dados.py

FUNÇÕES:
- Criar e organizar as tabelas SQL.
- Definir estrutura de clientes, transações e alertas.
- Criar consultas SQL necessárias para análise.
- Fazer análise estatística inicial dos dados.
- Trabalhar com Pandas para entender distribuição, média, horários, valores etc.
- Auxiliar na preparação dos dados que serão usados pelo Machine Learning.

APOIO:
├── models/cliente.py
├── models/transacao.py
└── visualization/graficos.py


--------------------------------------------------


*`Ian` — Machine Learning / IA + apoio Python*

Responsável principal por toda a parte de Machine Learning e detecção de comportamento anômalo.

PRINCIPAL:
├── ml/
│   ├── preprocessamento.py
│   ├── treinamento.py
│   └── modelo.pkl
│
├── services/detector_anomalia.py
│
└── tests/test_anomalia.py

FUNÇÕES:
- Preparar os dados para Machine Learning.
- Escolher quais características das transações serão utilizadas pelo modelo.
- Fazer normalização/conversão dos dados quando necessário.
- Criar e treinar o modelo de detecção de anomalias.
- Trabalhar inicialmente com Isolation Forest.
- Ajustar parâmetros do modelo.
- Criar score de anomalia.
- Fazer o modelo classificar transações normais/anômalas.
- Testar resultados do modelo.
- Avaliar falsos positivos e falsos negativos.
- Melhorar o modelo conforme os testes.
- Criar funções Python relacionadas ao funcionamento do ML.
- Auxiliar outras partes do projeto quando precisarem consumir o resultado da IA.

APOIO:
├── services/analise_dados.py
├── models/transacao.py
├── main.py
└── visualization/

Ian fica como principal responsável técnico pelo Machine Learning.


--------------------------------------------------


*`Joaquim` — alertas + segurança + lógica Python + integração geral*

Responsável pela lógica principal do sistema depois que os dados saem do banco e/ou passam pelo modelo.

PRINCIPAL:
├── services/alerta_service.py
│
├── repositories/
│   ├── cliente_repository.py
│   ├── transacao_repository.py
│   └── alerta_repository.py
│
├── models/
│   ├── cliente.py
│   ├── transacao.py
│   └── alerta.py
│
├── main.py
│
└── tests/test_database.py

FUNÇÕES:
- Criar funções Python para cadastro de clientes.
- Criar funções Python para cadastro de transações.
- Buscar dados no MySQL.
- Criar consultas utilizadas pelo sistema.
- Receber o resultado produzido pelo modelo de Machine Learning.
- Criar a lógica de geração de alertas.
- Salvar os alertas no banco.
- Trabalhar com validação dos dados.
- Fazer tratamento de erros.
- Implementar cuidados gerais de segurança.
- Evitar consultas inseguras ou entrada de dados sem validação.
- Integrar banco, Machine Learning, alertas e painel.
- Organizar o fluxo principal do programa.
- Fazer testes de integração entre as partes do sistema.

APOIO:
├── database/
├── services/detector_anomalia.py
├── ml/
├── ui/
└── tests/

Também fica responsável pela integração final do sistema junto com Ian e Murilo.


--------------------------------------------------


*`Zati` — integração SQL ↔ Python*

Responsável pela camada básica de comunicação entre Python e MySQL.

PRINCIPAL:
├── config/
│   └── database.py
│
└── database/
    ├── conexao.py
    └── seed.py

FUNÇÕES:
- Configurar conexão entre Python e MySQL.
- Criar abertura e fechamento da conexão.
- Trabalhar com credenciais através do .env.
- Fazer tratamento básico de erros de conexão.
- Criar o sistema inicial para popular o banco.
- Gerar/inserir clientes fictícios.
- Gerar/inserir transações fictícias.
- Garantir que Python consiga enviar e receber dados do MySQL.

APOIO:
├── database/tabelas.py
├── sql/
└── repositories/

OBS:
Zati cuida principalmente da conexão e infraestrutura do banco.
As funções de negócio como buscar cliente, cadastrar transação e gerar alerta ficam principalmente com Joaquim.


--------------------------------------------------


*`Murilo` — painel + visualização + Machine Learning*

Responsável principal pela interface de visualização e trabalha junto com Ian na parte de Machine Learning.

PRINCIPAL:
├── ui/
│   └── dashboard.py
│
├── visualization/
│   └── graficos.py
│
└── tests/

FUNÇÕES:
- Criar o painel/dashboard do sistema.
- Mostrar transações cadastradas.
- Mostrar transações classificadas como anômalas.
- Mostrar alertas.
- Criar filtros de visualização.
- Criar gráficos e estatísticas.
- Mostrar resultados do modelo de Machine Learning.
- Trabalhar junto com Ian nos testes do modelo.
- Analisar resultados das detecções.
- Auxiliar na avaliação da qualidade do modelo.
- Trabalhar em melhorias do Machine Learning.
- Testar integração entre ML e dashboard.

APOIO:
├── ml/
├── services/detector_anomalia.py
├── services/analise_dados.py
├── repositories/
└── models/transacao.py

Murilo trabalha junto com Ian na parte de Machine Learning, mas Ian é o responsável principal pelo núcleo do modelo.


--------------------------------------------------


*RESPONSABILIDADES GERAIS*

Machine Learning:
Ian (principal)
Murilo (apoio)

Integração final:
Joaquim (principal)
Ian + Murilo (apoio)

Testes:
Joaquim
Ian
Murilo

Banco / SQL:
Andrey
Zati
Joaquim (consultas utilizadas pelo sistema)

Dashboard:
Murilo (principal)

Análise de dados:
Andrey (principal)
Ian + Murilo (quando relacionado ao Machine Learning)

Segurança e validações:
Joaquim (principal)

Documentação:
Todos devem documentar a própria parte.

Pull Requests:
Sempre que possível, quem não escreveu a alteração deve revisar antes do merge.