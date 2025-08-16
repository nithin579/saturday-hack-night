


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
[[link to video](https://drive.google.com/file/d/1cSlUcpa6lAweMuBRi3570nrgROR5ud4P/view?usp=sharing)](Link Here)
## How it Works ?
This full-stack website operates on a classic client-server architecture. The front-end and backend are decoupled, communicating with each other through a RESTful API.

Front-End (Client): A user interacts with the dashboard in their web browser. This interface is built with vanilla HTML, CSS, and JavaScript. When the user performs an action like adding a movie, the JavaScript code creates an asynchronous fetch request to the backend API.

Backend (Server): The FastAPI server, built with Python, is always listening for requests. It receives the fetch request from the front-end, validates the incoming data using Pydantic models, and performs the required logic (e.g., adding the new movie to the in-memory dictionary).

Response: After processing the request, the FastAPI server sends a JSON response back to the front-end. This response indicates whether the operation was successful and includes any relevant data.

UI Update: The front-end's JavaScript receives this JSON response. It then updates the HTML DOM to reflect the changes, such as displaying a success message and adding the new movie card to the grid, all without needing to reload the page.
## Libraries used
Here's a breakdown of your project based on your request.

## How it Works?
This full-stack website operates on a classic client-server architecture. The front-end and backend are decoupled, communicating with each other through a RESTful API.

Front-End (Client): A user interacts with the dashboard in their web browser. This interface is built with vanilla HTML, CSS, and JavaScript. When the user performs an action like adding a movie, the JavaScript code creates an asynchronous fetch request to the backend API.

Backend (Server): The FastAPI server, built with Python, is always listening for requests. It receives the fetch request from the front-end, validates the incoming data using Pydantic models, and performs the required logic (e.g., adding the new movie to the in-memory dictionary).

Response: After processing the request, the FastAPI server sends a JSON response back to the front-end. This response indicates whether the operation was successful and includes any relevant data.

UI Update: The front-end's JavaScript receives this JSON response. It then updates the HTML DOM to reflect the changes, such as displaying a success message and adding the new movie card to the grid, all without needing to reload the page.

Project Demo
(Note: I cannot embed videos directly. You would typically embed a video in a GitHub README file using this Markdown format after uploading the video to a platform like YouTube.)

Markdown

[![Movie DB Demo Video](https://img.youtube.com/vi/VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=VIDEO_ID_HERE)
## Libraries Used
The project uses a minimal set of powerful libraries for the backend and no external libraries for the front-end.

Backend (Python)
These would be listed in a requirements.txt file.

fastapi - 0.111.0

uvicorn - 0.29.0 (Used as the ASGI server to run the API)

pydantic - 2.7.1 (Used by FastAPI for data validation)

Front-End (JavaScript)
No external libraries are used. The front-end is built with pure, "vanilla" JavaScript, HTML, and CSS, demonstrating core web development skills.

## How to Run
You need to run the backend server first, and then open the front-end file.
