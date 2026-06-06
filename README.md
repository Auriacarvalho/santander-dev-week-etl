Markdown
# 🛢️ Pipeline ETL Industrial: Santander Dev Week (Data Engineering)

Este repositório contém o desenvolvimento de um pipeline ETL (*Extract, Transform, Load*) robusto e automatizado construído em Python. O objetivo principal do projeto é simular um cenário real de inteligência bancária, onde dados de clientes são extraídos de uma API REST, processados analiticamente para o enriquecimento de informações através de mensagens personalizadas e, por fim, reinseridos no ecossistema de CRM da instituição financeira.

```text
  [EXTRACT]                   [TRANSFORM]                   [LOAD]
+-----------+    API GET    +-------------+   API PUT    +-----------+
| Arquivo   | ------------> | Lógica de   | -----------> | Banco de  |
| CSV (IDs) |               | Negócio /   |              | Dados CRM |
+-----------+               | IA Generat. |              +-----------+
                            +-------------+
🗺️ Arquitetura e Funcionamento do Pipeline
O pipeline foi desenhado seguindo as boas práticas de engenharia de software e desacoplamento de camadas, sendo dividido rigidamente nas três etapas do ciclo de dados:

1. 📥 Extract (Extração de Dados)
Consumo de IDs: O fluxo se inicia com a leitura de um arquivo estruturado (.csv), que atua como o gatilho do lote operacional contendo os identificadores dos clientes.

Consumo de API RESTful: Utilizando requisições HTTP, o script consome os endpoints da API para recuperar o perfil completo de cada usuário em formato JSON, isolando dados de conta, limites e cartões.

2. 🔄 Transform (Transformação & Inteligência de Negócio)
Regras de Engajamento: Nesta camada, o foco é transformar dados brutos em ativos de marketing e retenção. O script analisa o comportamento atual e os saldos do cliente para determinar o melhor direcionamento estratégico.

Enriquecimento com IA Generativa: Integração de modelos de linguagem para gerar de forma automatizada mensagens exclusivas e altamente personalizadas sobre investimentos, saúde financeira ou novos produtos bancários sob medida para cada perfil de correntista.

3. 📤 Load (Carga e Persistência)
Atualização do CRM: Com os dados devidamente transformados e as novas mensagens populadas, o pipeline realiza chamadas de mutação (PUT) de volta para a API.

Garantia de Integridade: O processo assegura que o estado do banco de dados relacional centralizado seja atualizado com sucesso, deixando os novos insights disponíveis imediatamente para os canais de atendimento ou aplicativos finais.

🛠️ Tecnologias e Ferramentas Utilizadas
Python 3: Linguagem principal escolhida pela sua alta performance em automação e manipulação de estruturas de dados.

Pandas: Utilizado para a leitura, filtragem, manipulação de tabelas e gerenciamento inicial dos dados extraídos.

Requests: Biblioteca responsável por estruturar o consumo da API de forma síncrona via protocolo HTTP (GET e PUT).

REST APIs / JSON: Manipulação avançada de dicionários e estruturas semiestruturadas para comunicação entre sistemas independentes.

Jupyter Notebook: Ambiente de desenvolvimento utilizado para a fase de prototipagem, testes de endpoints e documentação narrativa do pipeline passo a passo.

📂 Estrutura do Repositório
/data: Armazena os arquivos de entrada (como SDW2023.csv) contendo a lista de IDs dos clientes que alimentam o início do pipeline.

/notebooks: Jupyter Notebook contendo o código completo documentado, ideal para auditoria e entendimento da separação clara de cada função.

/src: Versão modularizada do script Python (.py) estruturada em funções reutilizáveis, pronta para ser executada em ambientes de produção ou agendadores de tarefas (schedulers).

📦 Instalação e Execução Local
Clone o repositório para sua máquina local:

Bash
   git clone [https://github.com/Auriacarvalho/santander-dev-week-etl.git](https://github.com/Auriacarvalho/santander-dev-week-etl.git)
Instale as dependências de engenharia necessárias para rodar o script:

Bash
   pip install pandas requests jupyter
Certifique-se de que a API de destino esteja ativa e com os endpoints configurados corretamente no script.

Execute o notebook ou o arquivo Python para processar o pipeline:

Bash
   python main.py

