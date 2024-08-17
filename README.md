# Learning Log

**Learning Log** é uma aplicação web que permite aos usuários registrar os assuntos de interesse e criar entradas de diário à medida que aprendem algo novo sobre cada assunto. O objetivo é ajudar os usuários a acompanhar seu progresso e refletir sobre seus aprendizados ao longo do tempo.

## Funcionalidades Principais

- **Registro de Usuários:** Os usuários podem se cadastrar e criar suas contas.
- **Login de Usuários:** Os usuários podem fazer login para acessar seus dados personalizados.
- **Criação de Assuntos:** Após o login, os usuários podem criar novos assuntos que desejam estudar ou acompanhar.
- **Entradas de Diário:** Para cada assunto, os usuários podem adicionar novas entradas que descrevem o que aprenderam.
- **Leitura e Edição:** Os usuários podem visualizar todas as suas entradas anteriores, além de editar ou atualizar o conteúdo das entradas existentes.

## Fluxo da Aplicação

1. **Página Inicial:** Descreve brevemente o propósito do site e convida os usuários a se cadastrar ou fazer login.
2. **Registro e Login:** O usuário pode se registrar ou logar para acessar o sistema.
3. **Área de Assuntos:** Após logar, o usuário pode criar, visualizar e gerenciar os assuntos de interesse.
4. **Diário de Aprendizado:** Dentro de cada assunto, o usuário pode adicionar novas entradas, além de visualizar e editar entradas existentes.

## Tecnologias Utilizadas

- **Django:** Framework web utilizado para construir a aplicação.
- **HTML/CSS:** Para o front-end e layout das páginas.
- **SQLite:** Banco de dados padrão utilizado no desenvolvimento.
- **Bootstrap:** Framework CSS para estilização e design responsivo.

## Como Rodar o Projeto Localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/learning-log.git
# Clone o repositório
git clone https://github.com/seu-usuario/learning-log.git

# Entre no diretório do projeto
cd learning-log

# Crie e ative um ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate  # Para Windows

# Instale as dependências
pip install -r requirements.txt

# Aplique as migrações do banco de dados
python manage.py migrate

# Inicie o servidor
python manage.py runserver

# Acesse a aplicação no navegador
http://localhost:8000
Contribuição

## Sinta-se à vontade para contribuir com o projeto. Para isso:

Fork o repositório.
Crie um branch para sua feature (git checkout -b feature/nova-feature).
Faça commit das suas alterações (git commit -am 'Adiciona nova feature').
Envie para o branch (git push origin feature/nova-feature).
Abra um Pull Request.



Esse README fornece uma visão clara sobre o propósito e funcionamento da aplicação, além de instruções para instalar e contribuir com o projeto.
