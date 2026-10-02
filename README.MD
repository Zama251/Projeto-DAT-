*LER TODOS OS .MD ANTES DE COMEÇAR A TRABALHAR NO PROJETO*
*ESSA DOCUMENTAÇÃO E IMPORTANTE ANTES DE COMEÇAR*
*EXPLICAÇÃO ARQUITETURA.MD* - *README.MD* *É EXTREMAMENTE IMPORTANTE*


git basico:

git checkout -b "Nome da pessoa" / cria um branh nova chamada "Nome da pessoa" e muda para ela. e como criar um copia do trabalho separada da main para a versão ficar estavel e não atrapalhar. Dps usar os comandos abaixo para versionamento do projeto. O motivo de usar isso e evitar que as 5 pessoas do grupo façam alterações na main e atrapalhem o trabalho dos outros.
*git checkout -b nome-da-branch | cria uma nova branch com o nome informado e muda para ela.*
*git checkout nome-da-branch | muda para a branch informada.*


git status | ele funciona como um "ls" do linux, mostrando o que foi alterado no projeto e o que ainda não foi commitado.
git add . | adiciona todos os arquivos alterados para o commit. o . e para adicionar todos os arquivos, mas pode ser usado o nome do arquivo para adicionar apenas um arquivo. por exemplo: git add README.md
git commit -m "mensagem" | cria um commit com a mensagem informada.
git push | envia os commits para o repositório remoto.
git pull | puxa as alterações do repositório remoto para o local. antes de fazer o pull, é importante fazer o commit das alterações locais para não perder nada e git status para ver se tem algo que não foi commitado.




Objetivo do trabalho e criar um sistema de Python + SQL + MachineLearning capaz de identificar trasnaçoes que fogem do comportamento normal e geral alertas;

Tecnologias utilizadas: Python, SQL, Machine Learning, Pandas, Scikit-learn, Matplotlib, Github em equipe. 


Funcionamento

MySQL
 ↓
Transações
 ↓
Python + Pandas
 ↓
Análise dos dados
 ↓
Machine Learning
 ↓
Anomalia detectada
 ↓
Alerta no banco

Exemplo

Cliente normalmente faz compras de R$50–200 durante o dia.

Aparece:

R$8.700 às 03:42 em outra cidade

O modelo identifica que o comportamento é diferente e gera:

POSSÍVEL ANOMALIA
Transação: 15234
Valor: R$8.700
Horário: 03:42

Não significa necessariamente fraude; significa que merece investigação.


Passo a passo

1. Criar o banco MySQL.
2. Criar tabelas de clientes, transações e alertas.
3. Criar dados fictícios.
4. Conectar Python ao MySQL.
5. Organizar os dados com Pandas.
6. Fazer análise estatística e gráficos.
7. Treinar um modelo de detecção de anomalias, como Isolation Forest.
8. Identificar transações suspeitas.
9. Salvar os alertas no banco.
10. Criar uma interface/dashboard.

Evolução

Python + SQL → Análise de dados → ML → Detecção de anomalias → Cybersecurity → Dashboard


/------------------------- Problemas ---------------------------/ *Apartir aqui o trabalho começa a relatar problemas que foram encontrados durante o desenvolvimento do projeto.* 
*unico objetivo desse arquivo é relatar problemas encontrados durante o desenvolvimento do projeto/ Ler relatar corrigir se possivel*
*REGRAS* Primeiro ponto do projeto e sempre ler o readme pra ver se teve atualização des da ultima vez que voce entrou no projeto, usar o github para versionamento do projeto, e sempre que for fazer uma alteração no projeto, criar uma branch com seu nome e depois de terminar a alteração, criar um pull request para a branch principal.
Caso necessario usar "--force" de qualquer forma, avisar a equipe antes de fazer o push. 

*Relatar duvidas, ideias etc aqui ou no grupo do whatsapp*



