<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<br />
<div align="center">
  <a href="https://github.com/hillswor/namaka-server">
    <img src="public/namaka-logo.svg" alt="Logo" width="100" height="100">
  </a>

<h3 align="center">Namaka</h3>

  <p align="center">
    The server side of a full-stack application that creates an API for the Next.js front end to interact and pull data from.  The API is connected to a PostgreSQL database hosted by Render.  The app enables reef tank enthusiasts to monitor crucial water parameters and interact with one another through a message board.
    <br />
    <a href="https://namaka-server.onrender.com">View API</a>
    ·
    <a href="https://github.com/hillswor/namaka-server/issues">Report Bug</a>
    ·
    <a href="https://github.com/hillswor/namaka-server/issues">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

With Namaka, users can track and manage aspects of their saltwater aquariums. The user-friendly platform enables users to monitor various parameters crucial to maintaining a healthy aquatic environment. Each aquarium gets its dedicated dashboard, where you can log information, analyze trends, and optimize care routines.

Moreover, Namaka aims to be home to a thriving community with an interactive message board that allows users to ask questions, share experiences, offer advice, or simply engage in conversation.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

 [![Python][Python]][Python-url]
 [![Flask][Flask]][Flask-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Getting Started

First, install dependencies and enter your virtual environment:

```bash
$ pipenv install && pipenv shell
```

You will need to connect your application to your own PostgreSQL database to test the code.  To do so, add a .env file to the root directory and save the link to your database under the variable "DATABASE_URI".  

```
# .env file
DATABASE_URI="Your Link"
```
Sessions are used in this API, so you will also need to generate a secret key and save it in the .env file under a variable named SECRET_KEY.

```bash
$ python
>>> import secrets
# Generate a random secret key with 32 bytes (256 bits) of entropy
>>> secret_key = secrets.token_hex(16)
>>> print(secret_key)
bea9a8fc2d70cfc4098759c2cc682975
```
```
# .env file
SECRET_KEY="bea9a8fc2d70cfc4098759c2cc682975"
```
Next, apply the database migrations:
```
$ flask db upgrade
```
Then start your development server using Gunicorn:

```bash
$ gunicorn app:app
```
You have the option of seeding the database:
```bash
$ python seed.py
```
Open [http://localhost:8000](http://localhost:8000) with your browser to see the result.

Database models are in the models.py file.  The routes use Flask RESTful and are in app.py.  Be sure to update the seed file and run migrations accordingly if there are any changes made to the database models.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

The app is currently comprised of the following routes found in app.py:

```
GET "/"
```
Displays a welcome message.
```
POST "/users"
```
Adds new user to app.
```
POST "/login"
```
Validates login information and logs the user in.
```
Post "/logout"
```
Logs the user out of current session.
```
GET "/check-session"
```
Checks if there is a user signed in to the session.
```
POST "/aquariums"
```
Adds a new aquarium under the logged in user.
```
GET "/aquariums/<int:id>"
PATCH "/aquariums/<int:id>"
DELETE "/aquariums/<int:id>"
```
Allows the user to view, edit or delete an existing aquarium by providing its unique identifier in the URL.
```
POST "/water-parameters"
```
Logs water parameters for an existing aquarium.
```
GET "/posts"
```
Displays all posts.
```
POST "/comments"
```
Adds a comment to a user's post.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Roadmap

- [ ] Adjust models to allow aquarium owners to share their aquariums
- [ ] Add CRUD functionality to the Post, Comment and WaterParameter models

See the [open issues](https://github.com/hillswor/namaka-client/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

Distributed under the MIT License. See `LICENSE.md` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Bruce Hillsworth - [@bhillsworth](https://twitter.com/bhillsworth) - bruce.hillsworth@gmail.com

Project Link: [https://github.com/hillswor/squatch-spotter-server](https://github.com/hillswor/squatch-spotter-server)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/hillswor/squatch-spotter-server.svg?style=for-the-badge
[contributors-url]: https://github.com/hillswor/squatch-spotter-server/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/hillswor/squatch-spotter-server.svg?style=for-the-badge
[forks-url]: https://github.com/hillswor/squatch-spotter-server/network/members
[stars-shield]: https://img.shields.io/github/stars/hillswor/squatch-spotter-server.svg?style=for-the-badge
[stars-url]: https://github.com/hillswor/squatch-spotter-server/stargazers
[issues-shield]: https://img.shields.io/github/issues/hillswor/squatch-spotter-server.svg?style=for-the-badge
[issues-url]: https://github.com/hillswor/squatch-spotter-server/issues
[license-shield]: https://img.shields.io/github/license/hillswor/squatch-spotter-server.svg?style=for-the-badge
[license-url]: https://github.com/hillswor/squatch-spotter-server/blob/master/LICENSE.md
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/bruce-hillsworth
[product-screenshot]: images/screenshot.png
[Python]: https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=python&logoColor=#3776AB
[Python-url]: https://docs.python.org/3/
[Flask]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=ffffff
[Flask-url]: https://flask.palletsprojects.com/en/2.3.x/

