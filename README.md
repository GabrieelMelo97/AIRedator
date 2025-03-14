# Avaliador de Redação com IA

Um sistema inteligente para avaliação de redações utilizando agentes de IA e fluxos de trabalho automatizados.

![Sistema](https://drive.google.com/uc?id=1j2J_NFFtNn8EVW92bDxvU4FxZIjqLisc)

## 📋 Sobre o Projeto

Este projeto implementa um sistema de avaliação de redações que utiliza agentes de IA especializados para analisar diferentes aspectos do texto, incluindo relevância, gramática, estrutura e profundidade da argumentação.

### 🎯 Funcionalidades

- Avaliação automática de redações
- Análise detalhada por critérios específicos
- Interface web interativa
- Histórico de avaliações
- Feedback em tempo real
- Sistema modular e extensível

## 🚀 Estrutura do Projeto

```
avaliador_de_redacao/
├── src/                    # Código fonte principal
│   ├── agents.py          # Implementação dos agentes de IA
│   ├── workflows.py       # Fluxos de trabalho e lógica principal
│   ├── utils.py           # Utilitários e funções auxiliares
│   └── config.py          # Configurações do sistema
├── frontend/              # Interface web
│   ├── app.py            # Aplicação Streamlit
│   └── requirements.txt   # Dependências do frontend
├── tests/                 # Testes unitários
│   ├── test_agents.py
│   └── test_workflows.py
├── requirements.txt       # Dependências principais
└── main.py               # Script principal
```

## 🛠️ Requisitos

- Python 3.9 ou superior
- Poetry (gerenciador de dependências)
- Deepseek API Key

## 📦 Instalação

1. Clone o repositório:
```bash
git https://github.com/GabrieelMelo97/AIRedator
cd avaliador_de_redacao
```

2. Instale o Poetry (caso ainda não tenha):
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. Instale as dependências do projeto:
```bash
poetry install
```

## 🎮 Como Usar

### Interface Web (Recomendado)

1. Ative o ambiente virtual do Poetry:
```bash
poetry shell
```

2. Execute a aplicação Streamlit:
```bash
poetry run streamlit run frontend/app.py
```

3. Acesse a interface em `http://localhost:8501`


## 🧪 Testes

Para executar os testes, você pode usar qualquer um dos seguintes comandos:

```bash
# Executar todos os testes com cobertura
poetry run pytest

# Executar testes com relatório detalhado de cobertura
poetry run pytest -v --cov=src --cov-report=term-missing

# Executar testes de um arquivo específico
poetry run pytest tests/test_specific_file.py
```

Os testes são configurados para:
- Executar todos os arquivos que começam com `test_` na pasta `tests/`
- Gerar relatório de cobertura do código na pasta `src/`
- Mostrar linhas que não foram testadas (missing coverage)

## 📊 Critérios de Avaliação

O sistema avalia as redações considerando os seguintes critérios:

- **Relevância**: Adequação ao tema proposto
- **Gramática**: Correção gramatical e ortográfica
- **Estrutura**: Organização e coesão do texto
- **Profundidade**: Qualidade e profundidade da argumentação

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Faça commit das mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Faça push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👥 Autores

- Gabriel Melo - [@GabrieelMelo97](https://github.com/GabrieelMelo97/AIRedator)

