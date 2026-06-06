# 🛢️ Pipeline ETL: Santander Dev Week

Este repositório contém o projeto de Engenharia de Dados desenvolvido durante a **Santander Dev Week**, em parceria com a Digital Innovation One (DIO). O objetivo principal do projeto é construir um pipeline ETL (*Extract, Transform, Load*) robusto utilizando Python para automatizar a extração, manipulação e o enriquecimento de dados de clientes a partir de uma API REST baseada em regras de negócio simuladas.

## 🗺️ Visão Geral do Projeto

O projeto simula um cenário real onde dados transacionais e de cadastro precisam ser extraídos de um banco de dados (via API), passar por um processamento analítico para a geração de mensagens personalizadas e marketing direcionado, e por fim, ser carregados de volta para atualizar o sistema de CRM da instituição financeira.

### 🚀 As Etapas do Pipeline (ETL)

1. **📥 Extract (Extração):** Leitura de uma lista de IDs de usuários a partir de um arquivo estruturado (`.csv`) e consumo de uma API RESTful para recuperar as informações completas de cada cliente em formato JSON.
2. **🔄 Transform (Transformação):** Aplicação de lógica de negócios e inteligência analítica. O script processa os dados de cada usuário para gerar de forma automatizada mensagens personalizadas sobre investimentos, saúde financeira ou novos produtos bancários.
3. **📤 Load (Carga):** Envio dos dados enriquecidos e das novas mensagens de volta para a API utilizando o método `PUT`, atualizando o registro de cada cliente no banco de dados centralizado de forma segura.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

* **Python 3:** Linguagem principal para a automação de todo o fluxo de engenharia.
* **Pandas:** Utilizado para a leitura, manipulação de tabelas e gerenciamento inicial dos dados extraídos.
* **Requests:** Biblioteca responsável por realizar as requisições HTTP (`GET` e `PUT`) e integrar o pipeline de forma síncrona com os endpoints da API.
* **REST APIs / JSON:** Manipulação de estruturas de dados semiestruturadas recebidas e enviadas para o servidor.
* **Jupyter Notebook:** Ambiente de desenvolvimento utilizado para a prototipagem, testes de endpoints e documentação do pipeline passo a passo.

---

## 📂 Estrutura do Repositório

* **`/data`**: Contém os arquivos de entrada (como `SDW2023.csv`) contendo a lista de IDs dos clientes que alimentam o início do pipeline.
* **`/notebooks`**: Jupyter Notebook contendo o código completo documentado, com a separação clara de cada uma das funções de Extração, Transformação e Carga.
* **`/src`**: Versão modularizada do script Python (`.py`) pronta para ser executada em ambientes de produção ou agendadores de tarefas (*schedulers*).

---

## 📦 Como Executar o Projeto

1. Clone o repositório para sua máquina local:
```bash
   git clone [https://github.com/Auriacarvalho/santander-dev-week-etl.git](https://github.com/Auriacarvalho/santander-dev-week-etl.git)
Instale as dependências necessárias para rodar o script:

Bash
   pip install pandas requests jupyter
Certifique-se de que a API de destino esteja ativa e com os endpoints configurados corretamente no script.

Execute o notebook ou o arquivo Python para processar o pipeline:

Bash
   python main.py
