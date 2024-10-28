# Mini-Twitter

Mini-Twitter é uma rede social simplificada desenvolvida com Django, onde os usuários podem criar contas, compartilhar pensamentos e interagir com as publicações de outros usuários. Inspirado no Twitter, este projeto permite a criação e gerenciamento de posts, além de funcionalidades de curtir e seguir usuários.

## Funcionalidades

- **Cadastro de Usuário**: Os usuários podem criar uma conta facilmente.
- **Criar Posts**: Os usuários podem escrever novos posts, que podem ser visualizados na página inicial.
- **Editar e Deletar Posts**: Os usuários têm a opção de editar ou excluir seus próprios posts.
- **Curtir Posts**: Os usuários podem curtir posts de outros usuários.
- **Seguir e Deixar de Seguir Usuários**: Os usuários podem seguir outros usuários para ver seus posts na página inicial.

## Página Inicial

Na página inicial, os usuários poderão ver uma lista de todos os seus posts e dos posts dos usuários que estão seguindo, facilitando a interação e o compartilhamento de pensamentos.

## Tecnologias Utilizadas

- **Django**: Framework web utilizado para construir a aplicação.
- **SQLite**: Para persistência de dados.

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/mini-twitter.git
   cd mini-twitter

2. Crie um ambiente virtual e ative-o:
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows

3. Instale as dependências:
    pip install django

4. Execute as migrações do banco de dados:
    python manage.py migrate

5. Crie um superusuário (opcional):
    python manage.py createsuperuser

6. Inicie o servidor de desenvolvimento:
    python manage.py runserver

7. Acesse a aplicação no navegador em http://127.0.0.1:8000/.

Sinta-se livre para criar sua conta de usuário, personalizar ela com uma foto de perfil e muitos posts.
Quanto aos posts, edite-os e delete-os à vontade (os que forem seus) e, claro, curta os mais legais.
