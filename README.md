


<img width="1920" height="1080" alt="nasahub" src="https://github.com/user-attachments/assets/e8544200-f902-41ee-a2f2-7375cad5043d" />




# Movie database
Here is the updated description, referring to the project as a website.

***

## Project Overview 🎬

This project is a full-stack movie database **website** featuring a dynamic front-end dashboard and a robust backend API built with **FastAPI**. It allows users to manage a personal movie collection through a clean, modern web interface.

The **website** is composed of two main parts: a client-side user interface built with vanilla HTML, CSS, and JavaScript, and the server-side **FastAPI** powering the API.

---

## Front-End Dashboard 🖥️

The front-end is a visually appealing and user-friendly dashboard that provides a complete interface for all movie management tasks.

* **Interactive UI:** Built with pure HTML, CSS, and JavaScript, the dashboard features interactive panels for adding and searching for movies, a responsive grid to display the collection, and modals for editing and rating movies without leaving the page.
* **Asynchronous Communication:** It communicates with the backend **FastAPI** using the `fetch()` method and modern `async/await` syntax. This ensures the UI remains fast and responsive, never freezing while waiting for data from the server.
* **Efficient Loading:** On startup, it cleverly fetches multiple movies in parallel using `Promise.allSettled()`, which provides a much faster initial load than fetching them one by one.
* **User Feedback:** The dashboard provides clear success and error messages for all user actions, creating an intuitive experience.



---

## Backend API with FastAPI 🐍

The backend is a powerful and efficient RESTful API built with **FastAPI**, a modern, high-performance Python web framework. This API handles all the business logic and data storage for the **website**.

* **Data Models:** It uses Pydantic models to define the structure of the movie data, ensuring that all incoming requests are validated and data consistency is maintained.
* **CRUD Operations:** The **FastAPI** provides a complete set of endpoints to handle all core functionalities:
    * **GET**: Retrieve a single movie by its ID or search for one by name.
    * **POST**: Add a new movie to the database.
    * **PUT**: Update an existing movie's details or add a new rating.
    * **DELETE**: Remove a movie from the database.
* **In-Memory Database:** For simplicity, the API uses a Python dictionary as an in-memory database to store the movie data. This means the data persists only as long as the server is running.
* **CORS Enabled:** It includes CORS (Cross-Origin Resource Sharing) middleware, which allows the front-end part of the **website** (running on a different origin) to securely make requests to the API.

---

## How They Work Together 🤝

The front-end and backend work in a classic client-server architecture:

1.  The user interacts with the front-end dashboard in their browser.
2.  An action, like clicking "Add Movie," triggers a JavaScript function.
3.  This function makes an asynchronous HTTP request (e.g., a `POST` request to `http://localhost:8000/add-movie/10`) to the **FastAPI** backend.
4.  The **FastAPI** server receives the request, processes it, updates the in-memory movie dictionary, and sends a JSON response back.
5.  The front-end JavaScript receives the JSON response and updates the UI accordingly, for example, by showing a success message and refreshing the movie list.
## Project by:
Nithin samuel
## Link to product walkthrough
[link to video](Link Here)
## How it Works ?
1. Explaining the working of project
2. Embed video of project demo
## Libraries used
Library Name - Version
## How to configure
Instructions for setting up project
## How to Run
Instructions for running
