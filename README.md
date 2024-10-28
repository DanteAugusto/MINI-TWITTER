# Mini-Twitter

Mini-Twitter is a simplified social network developed with Django, where users can create accounts, share thoughts, and interact with the posts of other users. Inspired by Twitter, this project allows for the creation and management of posts, as well as functionalities for liking and following users.

## Features

- **User Registration**: Users can easily create an account.
- **Create Posts**: Users can write new posts that can be viewed on the homepage.
- **Edit and Delete Posts**: Users have the option to edit or delete their own posts.
- **Like Posts**: Users can like posts from other users.
- **Follow and Unfollow Users**: Users can follow other users to see their posts on the homepage.

## Homepage

On the homepage, users will be able to see a list of all their posts and the posts from users they are following, facilitating interaction and sharing of thoughts.

## Technologies Used

- **Django**: The web framework used to build the application.
- **SQLite**: For data persistence.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/mini-twitter.git
   cd mini-twitter
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
3. Install the dependencies:
   ```bash
   pip install django
4. Run the database migrations:
   ```bash
   python manage.py migrate
5. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
6. Start the development server:
   ```bash
   python manage.py runserver
7. Access the application in your browser at ```http://127.0.0.1:8000/```.
Feel free to create your user account, customize it with a profile picture, and post as much as you like. For the posts, edit and delete your own as you wish, and of course, like the coolest ones.
