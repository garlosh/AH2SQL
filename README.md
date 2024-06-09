# AH2SQL

## Introdução

Bem-vindo ao **AH2SQL**, um projeto desenvolvido para coletar dados da casa de leilões do jogo World of Warcraft (WoW) e armazená-los em um banco de dados SQL. Esta ferramenta é útil para jogadores, analistas e desenvolvedores interessados em monitorar, analisar e extrair insights a partir dos dados do mercado de leilões do WoW.

## Funcionalidades

- **Coleta de Dados**: Extrai informações atualizadas da casa de leilões do WoW.
- **Armazenamento em SQL**: Salva os dados coletados em um banco de dados SQL para fácil acesso e análise.
- **Automatização**: Suporta agendamento de tarefas para coleta periódica de dados.

## Requisitos

- Python 3.12.2
- Servidor de banco de dados SQL MySQL nas versões 5.7 ou 8.0

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/muq33/AH2SQL.git
    cd AH2SQL
    ```

2. Crie um ambiente virtual e instale as dependências:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

## Utilização

### Coleta de Dados

Para coletar dados da casa de leilões, execute o script principal:
```bash
python main.py
```

### Próximos passos
- [X] Extrator dos dados
- [ ] Sumarizador dos dados passados para redução do gasto de memória
- [ ] Classificador dos dados com seus nomes dentro do jogo
- [ ] Criação de uma ferramenta interativa de consulta dos de métricas dos items 
