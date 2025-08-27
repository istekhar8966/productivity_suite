# Python CLI Productivity Suite

A comprehensive, terminal-based productivity suite built with Python and the `rich` library for a beautiful and interactive user interface.

## Features

-   **To-Do List Manager**: Add, remove, update, and list your tasks. Your tasks are saved and will be there when you return.
-   **Notes Manager**: A simple and effective way to jot down and view short notes.
-   **Pomodoro Timer**: A beautiful, full-screen, customizable Pomodoro timer to help you focus. It uses large, custom-drawn ASCII art for the display.
-   **Quick Calculator**: A simple, interactive calculator for basic arithmetic.

## Screenshots

*(Coming soon!)*

## Requirements

-   Python 3.6+
-   `rich`

## Installation

1.  **Clone the repository (or download the files):**

    ```bash
    git clone [<your-repo-url>](https://github.com/istekhar8966/productivity_suite.git)
    cd productivity-suite
    ```

2.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the application, run the `main.py` script from the root of the project directory:

```bash
python main.py
```

This will launch the main menu, from which you can navigate to all the different tools in the suite.

## Code Structure

-   `main.py`: The main entry point of the application. Handles the main menu and navigation.
-   `database.py`: Manages the SQLite database connection and table creation.
-   `todo.py`: Contains all functions related to the to-do list feature.
-   `notes.py`: Contains all functions for the notes manager.
-   `pomodoro.py`: Implements the full-screen Pomodoro timer.
-   `digital_clock.py`: A helper module that generates the large ASCII art for the timer.
-   `calculator.py`: A simple, non-interactive expression evaluator.
-   `requirements.txt`: A list of all Python dependencies.
-   `.gitignore`: Specifies which files and directories to ignore for version control.
