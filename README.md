# Caching Fibonacci

File caching_fibonacci.py has a code which demonstrates how to calculate Fibonacci numbers efficiently using recursion and caching in Python.

## Description

The program implements a `caching_fibonacci` function that creates an internal cache for storing previously calculated Fibonacci numbers.

Thanks to caching, repeated calculations are avoided, which significantly improves performance compared to standard recursive solutions.

## Features

- Recursive Fibonacci calculation
- Caching of previously calculated values
- Improved performance
- Clean and readable Python code

# Sum Profit Generator

File sum_profit.py contains a simple Python program that extracts floating-point numbers from a text string and calculates their total sum using a generator.

## Features

- Extracts real numbers from text using regular expressions
- Uses `yield` to create a generator
- Calculates the total profit/income from all detected numbers
- Follows PEP8 style guidelines

## Technologies Used
- Python 3
- Regular Expressions (re)
- Generators (yield)
- Type Hints (typing.Callable)

# Log File Analyzer

This project is a Python script for reading and analyzing log files.

The script parses log records, counts the number of entries for each logging level, and can optionally display only logs of a selected level.

## Features

- Parses log lines into structured dictionaries
- Loads logs from a text file
- Counts logs by level:
  - INFO
  - ERROR
  - DEBUG
  - WARNING
- Filters logs by a selected logging level
- Handles common errors:
  - File not found
  - Permission error
  - Incorrect log file format
- Uses functional programming with `filter()` and `lambda`
- Uses `collections.Counter` for counting log levels

## Log Format

Each log line should have the following format:

text
YYYY-MM-DD HH:MM:SS LEVEL Message

Example: 2024-01-22 08:30:01 INFO User logged in successfully.

## Project Structure
logs/
├── logs.py
└── logs.txt

## How to Run
If you are inside the project folder: python3 logs.py logs.txt

If you are outside the logs folder: python3 logs/logs.py logs/logs.txt
