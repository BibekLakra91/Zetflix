# Zetflix

Zetflix is a Django-based web application that allows users to browse, manage, and keep track of their favorite movies and TV shows. The application supports CRUD operations for user accounts, movies, and TV shows, as well as functionality to manage a personalized watchlist.

## Demo
![Demo](/assets/Zetflix_Demo.gif)
## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- User authentication (registration, login, logout)
- CRUD operations for Movies and TV Shows
- Personalized watchlist management (add, delete, and list items)
- User-specific movie and TV show listings

## Installation

### Clone the Repository

```bash
git clone <Repo_URL>
cd <Repo_Dir>
```

### Create a Virtual Environment

```bash
python -m venv myenv
myenv/Scripts/Activate  # On Windows, use `venv\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python manage.py runserver
```

## Usage

After starting the application, you can access it by navigating to `http://127.0.0.1:8000/` in your web browser.

### Admin Panel

Access the admin panel at `http://127.0.0.1:8000/admin` to manage users, movies, and TV shows.
Login auth and admin in not added as of now. Feel free to create PR

### API Endpoints

Here are some of the main API endpoints:

#### Users

- `POST /user/add/` - Add a user
- `DELETE /user/delete/` - Delete a user

#### Movies

- `GET /movie/get/` - Get a list of all movies
- `POST /movie/add/` - Add a new movie
- `PATCH /movie/update/` - Update a movie by ID 
- `DELETE /movie/delete/` - Delete a movie by ID
- `GET /movie/<id>/` - Get a movie by ID

#### TV Shows

- `GET /api/tvshows/` - Get a list of all TV shows
- `POST /api/tvshow/ass` - Add a new TV show
- `GET /api/tvshow/get` - Get a TV show by ID
- `PUT /api/tvshow/update` - Update a TV show by ID
- `DELETE /api/tvshows/<id>` - Delete a TV show by ID

#### My List

- `GET /mylist/get` - Get the user's watchlist
- `POST /mylist/add` - Add an item to the user's watchlist
- `DELETE /mylist/delete` - Delete an item from the user's watchlist



## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

Please make sure your code follows the project's coding style and includes tests for any new features or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
