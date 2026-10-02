*NÃO MEXER*
Aqui vou explicar como funciona a arquitetura do projeto, para que todos entendam o fluxo de dados e como cada componente interage.

main.py: *Carrega dados --> analisa --> executa modelo --> gera alertas.*

config/: Configurações por exemplo  *AVISO* senhas não devem ir para o github, arquivos sensiveis devem ser adicionados no .gitignore, para que não sejam versionados.

*HOST, USER, PASSWORD, DATABASE*

database/: tudo relacionado ao banco de dados, como scripts de criação de tabelas.
*conexao.py: Abre conexão com o banco de dados MySQL.*,*tabelas.py: cria banco/tabelas/insere dados.*,*seed.py: coloca dados fictícios no banco de dados.*

models/: representação dos dados.
*cliente.py: representa: cliente, com atributos como id, nome, email, etc.*,*transacao.py: representa transação, com atributos como id, cliente_id, valor, data_hora, etc.*,*alerta.py: representa alerta, com atributos como id, transacao_id, tipo_alerta, data_hora, etc.*

repository/: responsável por interagir com o banco de dados, realizando operações como inserir, atualizar, deletar e consultar dados.
*Exemplos: buscar_transacoes_por_cliente(cliente_id), inserir_alerta(alerta), atualizar_transacao(transacao), deletar_cliente(cliente_id), etc.*

services/: contém a lógica de negócios do projeto, como análise de dados, detecção de anomalias e geração de alertas.
*Exemplos: analisar_transacoes(cliente_id), detectar_anomalias(transacoes), gerar_alerta(transacao), etc.*

(*aqui se recomenda duas pessoas*) ml/: contém os modelos de machine learning utilizados para detecção de anomalias.
*preprocessamento.py: realiza o pré-processamento valor, horario, distancia,  frequencia.*,*treinamento.py: contém a implementação do modelo de detecção de anomalias, como Isolation Forest.*
*modelo.pkl: arquivo que contém o modelo treinado salvo, só dps decidir versionar o .pkl.*

visualization/: Matlotlib, *exemplos: graficos_valores(), graficos_anomalias(), graficos_distancias(), etc.*

*ui/: contém a interface do usuário, como dashboards e relatórios. pode ser Streamlit, Tkinter, Flask, etc.*

sql/: contém scripts SQL para criação de tabelas, inserção de dados e consultas complexas.

tests/: contém testes unitários e de integração para garantir que o código funcione corretamente em um ambiente de desenvolvimento e produção.


