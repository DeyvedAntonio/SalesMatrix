# SalesMatrix
Para demonstrar as minhas habilidades a recrutadores e clientes, o projeto ideal é uma Plataforma Inteligente de Gestão e Predição de Vendas. Este projeto integra o ciclo completo: coleta de dados (Django), armazenamento robusto (SQL/PostgreSQL), análise preditiva (Python/ML) e visualização executiva (Power BI e Streamlit).

Parte 1: O Núcleo do Sistema (Django & Python OOP)
• Objetivo: Demonstrar domínio em desenvolvimento backend, persistência de dados e arquitetura de software.
• Requisitos:
    ◦ Criar um ambiente virtual (venv) e um projeto Django estruturado com apps separados.
    ◦ Desenvolver Models para Produto, Vendedor, Cliente e Venda, utilizando ForeignKey para relacionamentos.
    ◦ Implementar Class Based Views (CBVs) para o CRUD de vendas e autenticação de usuários.
    ◦ Garantir resiliência com tratamento de exceções (try/except) em buscas e entradas de dados.
Parte 2: Engenharia e SQL Analytics (PostgreSQL)
• Objetivo: Provar conhecimento em bancos de dados relacionais e extração de informações complexas.
• Requisitos:
    ◦ Configurar o Django para utilizar PostgreSQL em vez do SQLite padrão.
    ◦ Criar um script analise.sql que responda perguntas de negócio (ex: ticket médio por vendedor e produtos mais rentáveis) usando JOIN e GROUP BY.
    ◦ Realizar migrações de banco de dados para garantir a integridade da estrutura.
Parte 3: Inteligência de Dados (Pandas & Machine Learning)
• Objetivo: Transformar dados brutos em previsões acionáveis.
• Requisitos:
    ◦ Utilizar Pandas e NumPy para limpeza e tratamento de valores ausentes ou outliers na base de vendas.
    ◦ Desenvolver um modelo de Regressão com Scikit-Learn para prever vendas futuras ou um modelo de Classificação para prever o Churn (perda) de clientes.
    ◦ Avaliar o modelo com métricas técnicas de performance antes do deploy.
Parte 4: Visualização e IA (Power BI, Streamlit & LangChain)
• Objetivo: Entregar o valor final ao usuário com dashboards e IA generativa.
• Requisitos:
    ◦ Criar um dashboard no Power BI com cálculos em DAX (ex: crescimento mês a mês) e filtros cruzados.
    ◦ Desenvolver um Data App com Streamlit que permita ao usuário interagir com o modelo de Machine Learning.
    ◦ Diferencial de Portfólio: Integrar um assistente de IA usando LangChain e o padrão RAG para que o usuário possa "perguntar" ao sistema sobre os dados de vendas.
Parte 5: Infraestrutura (Docker & Deploy)
• Objetivo: Mostrar que você entende como colocar uma aplicação no mundo real.
• Requisitos:
    ◦ Containerizar a aplicação Django e o banco de dados usando Docker.
    ◦ Realizar o deploy na AWS utilizando Nginx e uWSGI.
O que você acha de começarmos detalhando a modelagem do banco de dados (Parte 1) para o sistema de vendas?
