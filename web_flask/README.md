# Web Framework

This repository contains a Flask web application with various routes. Each route is implemented in a separate script, and the instructions for running and testing each script are provided below.

## Prerequisites
- Python 3.x
- Flask

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/AirBnB_clone_v2.git
   cd AirBnB_clone_v2/web_flask
   ```

2. Install Flask (if not already installed):
   ```bash
   pip install Flask
   ```

## Scripts

### 0-hello_route.py
- Start a Flask web application.
- Web application listens on `0.0.0.0`, port `5000`.
- Route `/`: Displays "Hello HBNB!"
- Use the option `strict_slashes=False` in the route definition.

   ```bash
   python3 -m web_flask.0-hello_route
   ```

### 1-hbnb_route.py
- Start a Flask web application.
- Web application listens on `0.0.0.0`, port `5000`.
- Routes:
  - `/`: Displays "Hello HBNB!"
  - `/hbnb`: Displays "HBNB"
- Use the option `strict_slashes=False` in the route definition.

   ```bash
   python3 -m web_flask.1-hbnb_route
   ```

### 2-c_route.py
- Start a Flask web application.
- Web application listens on `0.0.0.0`, port `5000`.
- Routes:
  - `/`: Displays "Hello HBNB!"
  - `/hbnb`: Displays "HBNB"
  - `/c/<text>`: Displays "C " followed by the value of the text variable (replace underscores with spaces).
- Use the option `strict_slashes=False` in the route definition.

   ```bash
   python3 -m web_flask.2-c_route
   ```

### 3-python_route.py
- Start a Flask web application.
- Web application listens on `0.0.0.0`, port `5000`.
- Routes:
  - `/`: Displays "Hello HBNB!"
  - `/hbnb`: Displays "HBNB"
  - `/c/<text>`: Displays "C " followed by the value of the text variable (replace underscores with spaces).
  - `/python/<text>`: Displays "Python " followed by the value of the text variable (replace underscores with spaces).
  - Default value of text is "is cool".
- Use the option `strict_slashes=False` in the route definition.

   ```bash
   python3 -m web_flask.3-python_route
   ```

### 4-number_route.py
- Start a Flask web application.
- Web application listens on `0.0.0.0`, port `5000`.
- Routes:
  - `/`: Displays "Hello HBNB!"
  - `/hbnb`: Displays "HBNB"
  - `/c/<text>`: Displays "C " followed by the value of the text variable (replace underscores with spaces).
  - `/python/<text>`: Displays "Python " followed by the value of the text variable (replace underscores with spaces).
  - `/number/<n>`: Displays "n is a number" only if n is an integer.
- Use the option `strict_slashes=False` in the route definition.

   ```bash
   python3 -m web_flask.4-number_route
   ```

### 5-number_template.py
- Start a Flask web application.
- Web application listens on `0.0.0.0`, port `5000`.
- Routes:
  - `/`: Displays "Hello HBNB!"
  - `/hbnb`: Displays "HBNB"
  - `/c/<text>`: Displays "C " followed by the value of the text variable (replace underscores with spaces).
  - `/python/<text>`: Displays "Python " followed by the value of the text variable (replace underscores with spaces).
  - `/number/<n>`: Displays "n is a number" only if n is an integer.
  - `/number_template/<n>`: Displays an HTML page only if n is an integer:
    - H1 tag: "Number: n" inside the tag BODY.
- Use the option `strict_slashes=False` in the route definition.

   ```bash
   python3 -m web_flask.5-number_template
   ```

### 6-number_odd_or_even.py
- Start a Flask web application.
- Web application listens on `0.0.0.0`, port `5000`.
- Routes:
  - `/`: Displays "Hello HBNB!"
  - `/hbnb`: Displays "HBNB"
  - `/c/<text>`: Displays "C " followed by the value of the text variable (replace underscores with spaces).
  - `/python/<text>`: Displays "Python " followed by the value of the text variable (replace underscores with spaces).
  - `/number/<n>`: Displays "n is a number" only if n is an integer.
  - `/number_template/<n>`: Displays an HTML page only if n is an integer:
    - H1 tag: "Number: n" inside the tag BODY.
  - `/number_odd_or_even/<n>`: Displays an HTML page only if n is an integer:
    - H1 tag: "Number: n is even|odd" inside the tag BODY.
- Use the option `strict_slashes=False` in the route definition.

   ```bash
   python3 -m web_flask.6-number_odd_or_even
   ```

Feel free to explore and test each route using the provided commands and instructions.
