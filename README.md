# Project README

<!-- Table of Contents -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#description">Description</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#file-descriptions">File Descriptions</a></li>
    <li><a href="#games">Games</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>


## <a name="description"></a>Description

This repository contains several simple text-based games implemented in Python.  Each game is self-contained within its own directory.


## <a name="installation"></a>Installation

The games require Python 3.  No additional libraries are needed.  To run a game, navigate to its directory and execute the `main.py` file using a Python interpreter.


## <a name="usage"></a>Usage

Each game's usage is described in its respective directory.  Generally, the games are run from the command line by executing the `main.py` script.


## <a name="file-descriptions"></a>File Descriptions

The following table summarizes the files in this repository:

| Directory          | File Name        | Description                                                                                                                               | Type      |
|----------------------|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| Hangman             | `main.py`         | Implements a text-based Hangman game. The `Game` class handles user input, game logic, and output. The `play()` method is the main entry point. | Executable |
| Quiz-Game           | `main.py`         | Implements a text-based quiz game.  Loads questions and answers from `questions.txt` and `answers.txt`. The `Quiz` class handles game logic. | Executable |
| Quiz-Game           | `questions.txt`   | Contains the questions for the quiz game.                                                                                             | Data      |
| Quiz-Game           | `answers.txt`     | Contains the answer key for the quiz game.                                                                                               | Data      |
| Rock-Paper-Scissor | `main.py`         | Implements a text-based Rock-Paper-Scissors game.                                                                                       | Executable |


## <a name="games"></a>Games

* **Hangman:** A classic word-guessing game.
* **Quiz Game:** A quiz game that loads questions and answers from external files.
* **Rock-Paper-Scissors:** The classic hand game.


## <a name="contributing"></a>Contributing

Contributions are welcome! Please open an issue or submit a pull request.


## <a name="license"></a>License

[Specify your license here, e.g., MIT License]