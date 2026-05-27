# Python Practice Projects

This repository contains a collection of small Python practice projects.
Each project demonstrates different core Python concepts such as recursion, generators, file handling, decorators, and error handling.

---

## Caching Fibonacci

The file `caching_fibonacci.py` contains code that demonstrates how to calculate Fibonacci numbers efficiently using recursion and caching in Python.

### Description

The program implements a `caching_fibonacci` function that creates an internal cache for storing previously calculated Fibonacci numbers.

Thanks to caching, repeated calculations are avoided, which significantly improves performance compared to a standard recursive solution.

### Features

- Recursive Fibonacci calculation
- Caching of previously calculated values
- Improved performance
- Clean and readable Python code

### How to Run

```bash
python3 caching_fibonacci.py
```

---

## Sum Profit Generator

The file `sum_profit.py` contains a simple Python program that extracts floating-point numbers from a text string and calculates their total sum using a generator.

### Description

The program uses a generator function to find real numbers in a text and calculate the total profit or income.

### Features

- Extracts real numbers from text using regular expressions
- Uses `yield` to create a generator
- Calculates the total profit or income from all detected numbers
- Follows PEP 8 style guidelines

### Technologies Used

- Python 3
- Regular Expressions (`re`)
- Generators (`yield`)
- Type Hints (`typing.Callable`)

### How to Run

```bash
python3 sum_profit.py
```

---

## Log File Analyzer

The file `logs.py` contains a Python script for reading and analyzing log files.

### Description

The script parses log records, counts the number of entries for each logging level, and can optionally display only logs of a selected level.

### Features

- Parses log lines into structured dictionaries
- Loads logs from a text file
- Counts logs by level:
  - `INFO`
  - `ERROR`
  - `DEBUG`
  - `WARNING`
- Filters logs by a selected logging level
- Handles common errors:
  - File not found
  - Permission error
  - Incorrect log file format
- Uses functional programming with `filter()` and `lambda`
- Uses `collections.Counter` for counting log levels

### Log Format

Each log line should have the following format:

```text
YYYY-MM-DD HH:MM:SS LEVEL Message
```

Example:

```text
2024-01-22 08:30:01 INFO User logged in successfully.
```

### Project Structure

```text
logs/
├── logs.py
└── logs.txt
```

### How to Run

If you are inside the project folder:

```bash
python3 logs.py logs.txt
```

If you are outside the `logs` folder:

```bash
python3 logs/logs.py logs/logs.txt
```

To filter logs by level, pass the log level as the second argument:

```bash
python3 logs.py logs.txt ERROR
```

---

## Assistant Bot

The file `bot.py` contains a simple Python console assistant bot for managing contacts.

### Description

This project contains a command-line bot that allows users to save, update, view, and list phone contacts.

The bot supports basic commands and handles user input errors using the `input_error` decorator.

### Features

- Add a new contact
- Change an existing contact's phone number
- Show a phone number by contact name
- Show all saved contacts
- Handle incorrect user input without stopping the program
- Exit the bot safely

### Available Commands

| Command | Description | Example |
|---|---|---|
| `hello` | Shows a greeting message | `hello` |
| `add [name] [phone]` | Adds a new contact | `add Bob 0501234567` |
| `change [name] [new_phone]` | Changes an existing contact's phone number | `change Bob 0677654321` |
| `phone [name]` | Shows the phone number of a contact | `phone Bob` |
| `all` | Shows all saved contacts | `all` |
| `close` | Exits the bot | `close` |
| `exit` | Exits the bot | `exit` |

### Example Usage

```text
Welcome to the assistant bot!
Enter a command: hello
How can I help you?

Enter a command: add Bob 0501234567
Contact added.

Enter a command: phone Bob
0501234567

Enter a command: change Bob 0677654321
Contact updated.

Enter a command: all
Bob: 0677654321

Enter a command: exit
Good bye!
```

### Error Handling

The bot uses the `input_error` decorator to handle common input mistakes.

Examples:

```text
Enter a command: add
Give me name and phone please.

Enter a command: phone
Enter the argument for the command

Enter a command: phone Alice
Contact was not found.
```

The following errors are handled:

- `ValueError`
- `KeyError`
- `IndexError`

### How to Run

```bash
python3 bot.py
```

---

## Requirements

- Python 3.x

No external libraries are required for most scripts.
If a script uses additional modules, make sure they are installed before running it.

---

## Author

Created as a Python learning project.
