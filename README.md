# Login page Automation with Playwright

This repository contains a test automation script for verifying the login functionality of a web application using Playwright and pytest. The automation covers the following key features:

1. **Email and password field validation**.
2. **Login button functionality**.
3. **Error handling and success message validation** after attempting to login.

## Project Setup

### Prerequisites

To get started, you need to have the following tools installed:

- **Python 3.x**: Ensure you have Python installed on your machine. If not, you can download and install it from [python.org](https://www.python.org/downloads/).
- **Node.js**: Playwright relies on Node.js for its installation. Download and install Node.js from [nodejs.org](https://nodejs.org/).
- **Playwright**: A fast and reliable automation library for browser testing.
- **pytest**: A framework that makes building simple and scalable test cases easy.

### Install Dependencies

1. Clone this repository or download the project files.
2. Install the required Python dependencies by running the following command in your terminal or command prompt:
    ```bash
    pip install -r requirements.txt
    ```

    Where `requirements.txt` contains:
    ```text
    playwright
    pytest
    ```

    Alternatively, you can install Playwright and pytest directly via pip:
    ```bash
    pip install playwright pytest
    playwright install
    ```

### Project Structure

- **`login_main_page.py`**: Contains the `Login_page_main` class with methods to interact with login page elements (email, password, submit button).
- **`test_login.py`**: Contains the test case for performing the login action and verifying the result (success or error).
- **`logger.py`**: Contains the logging configuration for the test execution, including a custom logger with detailed timestamps and log levels.

### Running the Test

To run the test, execute the following command in your terminal:

```bash
pytest test_login.py
