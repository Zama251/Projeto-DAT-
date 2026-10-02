# Projeto DAT

**LER TODOS OS ARQUIVOS `.MD` ANTES DE COMEÇAR A TRABALHAR NO PROJETO.**

Essa documentação é importante antes de começar.

Arquivos principais:

- `README.MD`
- `EXPLICAÇÃO_ARQUITETURA.MD`

*O `README.MD` deve ser lido sempre que alguém voltar a trabalhar no projeto, pois pode conter alterações, problemas encontrados ou novas regras da equipe.*

---

# Ferramentas / Bibliotecas

Instalar todas as dependências do projeto com:

    bash
pip install -r requirements.txt


Caso seja necessário adicionar uma nova biblioteca ao projeto, adicioná-la também ao `requirements.txt` para que todos da equipe consigam instalar as mesmas dependências. **(Ian pode ajudar com isso). apaga essa mensagem depois de ler**

---

# Git básico

Para baixar o projeto pela primeira vez:

```bash
git clone URL_DO_REPOSITORIO
```

Depois entre na pasta do projeto.

Antes de começar uma nova tarefa, sempre atualizar a `main`:

```bash
git switch main
git pull origin main
```

Depois criar uma branch para trabalhar:

```bash
git switch -c nome-da-branch
```

Exemplo:

```bash
git switch -c joaquim-banco
```

A ideia é não trabalhar diretamente na `main`.

Fluxo básico:

```text
git clone
    ↓
git switch main
    ↓
git pull origin main
    ↓
git switch -c nome-da-branch
    ↓
trabalha
    ↓
git status
    ↓
git add .
    ↓
git commit -m "descrição da alteração"
    ↓
git push
    ↓
Pull Request
    ↓
main
```

Na primeira vez que uma branch for enviada para o GitHub, pode ser necessário usar:

```bash
git push -u origin nome-da-branch
```

Depois disso normalmente basta:

```bash
git push
```

---

# Branches

Uma branch funciona como uma cópia separada do projeto principal.

Uma forma simples de imaginar isso é como uma árvore:

```
              main
             / | \
            /  |  \
      joaquim murilo ian
```

A `main` é o tronco principal.

Cada branch é um galho onde uma pessoa pode trabalhar sem alterar diretamente a versão principal.

Quando o trabalho daquela branch estiver pronto, é criado um Pull Request para integrar as alterações novamente na `main`.

Isso evita que as cinco pessoas da equipe façam alterações diretamente na `main` e acabem atrapalhando o trabalho umas das outras.

Comando recomendado para criar uma branch:

```bash
git switch -c nome-da-branch
```

Também é possível usar:

```bash
git checkout -b nome-da-branch
```

Os dois comandos criam uma nova branch e mudam para ela.

Para mudar para uma branch que já existe:

```bash
git switch nome-da-branch
```

ou:

```bash
git checkout nome-da-branch
```

Prefira `git switch`, pois o comando deixa mais claro que estamos trabalhando com branches.

---

**Comandos importantes**

### Ver o estado do projeto

```bash
git status
```

Mostra o estado atual do repositório, incluindo arquivos novos, arquivos modificados, alterações preparadas para commit e alterações ainda não adicionadas.

O `git status` mostra o estado desses arquivos em relação ao Git.

---

### Adicionar alterações

Adicionar todos os arquivos alterados:

```bash
git add .
```

Adicionar somente um arquivo:

```bash
git add README.MD
```

O `git add` prepara as alterações para o próximo commit.

---

### Criar um commit

```bash
git commit -m "mensagem"
```

Exemplo:

```bash
git commit -m "Adiciona conexão inicial com MySQL"
```

A mensagem deve explicar resumidamente o que foi alterado.

---

### Enviar alterações para o GitHub

```bash
git push
```

Envia os commits da branch atual para o repositório remoto.

---

### Buscar alterações do GitHub

```bash
git pull
```

Atualiza a branch local utilizando as alterações existentes no repositório remoto.

Antes de utilizar `git pull`, execute:

```bash
git status
```

Se existirem alterações locais importantes ainda não commitadas, faça o commit ou salve essas alterações antes de atualizar a branch.

---

# Pull Request

Depois de terminar uma alteração:

1. Faça o commit.
2. Faça o push da branch.
3. Abra o GitHub.
4. Crie um Pull Request da sua branch para a `main`.
5. Revise as alterações antes de fazer o merge.

Exemplo:

```text
joaquim-banco
      ↓
Pull Request
      ↓
main
```

Evitar fazer merge sem verificar os arquivos alterados.

---

# Regras do Git para a equipe

Nunca desenvolver diretamente na `main`.

Sempre atualizar a `main` antes de criar uma nova branch:

```bash
git switch main
git pull origin main
```

Depois criar a branch da tarefa:

```bash
git switch -c nome-da-branch
```

Sempre fazer commits com mensagens que expliquem o que foi alterado.

Evitar commits como:

```text
"teste"
"coisa"
"att"
"mudança"
```

Preferir:

```text
"Adiciona tabela de transações"
"Implementa preprocessamento dos dados"
"Corrige conexão com MySQL"
```

Não utilizar:

```bash
git push --force (PERIGOSO POR FAVOR TOMEM CUIDADO)
```

sem avisar a equipe.

**O `--force` pode sobrescrever histórico remoto e apagar alterações de outras pessoas.**

Caso seja realmente necessário utilizar algum comando destrutivo ou alterar uma parte importante da estrutura do projeto, avisar a equipe antes.

---

# Objetivo do projeto

O objetivo do trabalho é criar um sistema utilizando Python, SQL e Machine Learning capaz de identificar transações que fogem do comportamento considerado normal e gerar alertas para possível investigação.

Uma transação marcada como anômala não significa necessariamente que seja fraude.

O sistema apenas identifica comportamentos diferentes do padrão esperado.

---

# Tecnologias utilizadas

- Python
- MySQL / SQL
- Pandas
- Scikit-learn
- Matplotlib
- Machine Learning
- Git
- GitHub

---

# Funcionamento

```text
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
Alerta salvo no banco
  ↓
Dashboard / investigação
```

---

# Exemplo

Um cliente normalmente realiza compras entre:

```text
R$50 e R$200
```

durante o dia.

Então aparece uma transação:

```text
Valor: R$8.700
Horário: 03:42
Cidade diferente do comportamento normal
```

O modelo identifica que esse comportamento foge do padrão e gera:

```text
POSSÍVEL ANOMALIA

Transação: 15234
Valor: R$8.700
Horário: 03:42
```

Isso não significa necessariamente fraude.

Significa apenas que essa transação possui características diferentes do comportamento considerado normal e merece investigação.

---

# Passo a passo do desenvolvimento

1. Criar o banco MySQL.
2. Criar as tabelas de clientes, transações e alertas.
3. Criar dados fictícios para testes.
4. Conectar Python ao MySQL.
5. Buscar e organizar os dados utilizando Pandas.
6. Fazer análise estatística e criar gráficos.
7. Preparar os dados para o Machine Learning.
8. Treinar um modelo de detecção de anomalias, inicialmente utilizando Isolation Forest.
9. Identificar transações consideradas suspeitas pelo modelo.
10. Salvar os alertas no banco de dados.
11. Criar uma interface/dashboard para visualizar transações e alertas.
12. Testar o funcionamento completo do sistema.

---

# Evolução do projeto

```text
Python + SQL
      ↓
Análise de dados
      ↓
Machine Learning
      ↓
Detecção de anomalias
      ↓
Cybersecurity
      ↓
Dashboard
```

---

# Problemas encontrados

A partir desta seção devem ser relatados problemas encontrados durante o desenvolvimento do projeto.

O objetivo é permitir que qualquer integrante da equipe consiga:


Ler
 ↓
Entender
 ↓
Investigar
 ↓
Corrigir, se possível
```

Ao encontrar um problema, registrar:

```text
Problema:

Arquivo / área:

O que estava sendo feito:

Erro apresentado:

Solução encontrada:

Status:
[ ] Não resolvido
[ ] Em investigação
[ ] Resolvido
```

Exemplo:

```text
Problema:
Python não conecta ao MySQL.

Arquivo / área:
database/conexao.py

O que estava sendo feito:
Tentativa de conectar ao banco local.

Erro apresentado:
Access denied for user.

Solução encontrada:
Ainda não encontrada.

Status:
[X] Em investigação
```

---

# Dúvidas e ideias

Dúvidas, ideias de funcionalidades, alterações de arquitetura ou possíveis melhorias podem ser relatadas nesta documentação ou no grupo da equipe.

Caso uma decisão importante seja tomada pelo WhatsApp, registrar posteriormente no projeto se ela afetar código, arquitetura ou funcionamento do sistema.


# Regra principal

Antes de trabalhar:

```text
LER README.MD
        ↓
LER EXPLICAÇÃO_ARQUITETURA.MD
        ↓
git switch main
        ↓
git pull origin main
        ↓
criar uma branch
        ↓
trabalhar
        ↓
commit
        ↓
push
        ↓
Pull Request
```

A `main` deve permanecer o mais estável possível.