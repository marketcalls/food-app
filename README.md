
# Food App

A simple food-based web application built with Flask and styled using Tailwind CSS. This app allows users to discover delicious recipes and share their own.

## Features

- Home page with featured recipes
- About page with information about the app
- Recipe detail pages
- Contact form

## Project Structure

```
food_app/
│
├── app.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── recipe.html
│   ├── contact.html
└── static/
    ├── images/
    │   ├── Beef Tacos.jpg
    │   ├── Chicken Alfredo.jpg
    │   ├── Spaghetti Carbonara.jpg
    │   └── Vegetable Stir Fry.jpg
    └── styles.css
```

## Getting Started

### Prerequisites

- Python 3.x
- Virtual environment

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/marketcalls/food-app.git
    cd food-app
    ```

2. **Create a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    pip install Flask
    ```

4. **Run the application**:

    ```bash
    python app.py
    ```

5. **Access the application**:

    Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Usage

### Home Page

- Displays a welcome message and a list of featured recipes.
- Each recipe includes an image, name, and a link to view the recipe details.

### About Page

- Provides information about the app and its mission.

### Recipe Detail Page

- Displays details about a specific recipe.

### Contact Page

- Contains a contact form for users to send messages.

## Technologies Used

- **Flask**: A micro web framework for Python.
- **Tailwind CSS**: A utility-first CSS framework for rapid UI development.

## Screenshots

### Home Page
![Home Page](static/images/home_page_screenshot.png)

### About Page
![About Page](static/images/about_page_screenshot.png)

### Recipe Detail Page
![Recipe Detail Page](static/images/recipe_detail_page_screenshot.png)

### Contact Page
![Contact Page](static/images/contact_page_screenshot.png)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The Flask framework for providing the foundation of the application.
- Tailwind CSS for the beautiful and responsive design components.
