# BookBot Project Context

## Overview
BookBot is a Boot.dev project - a simple Python application that reads book files and analyzes word counts.

## Project Structure
- `main.py` - Main application file
- `books/frankenstein.txt` - Sample book file for analysis
- `README.md` - Project description

## Current Functionality
The application:
1. Reads a book file (Frankenstein) from `books/frankenstein.txt`
2. Counts the total number of words in the file
3. Outputs: "Found {num_words} total words"

## Main Functions
- `get_book_text(filepath)` - Opens and reads a file, returns contents as string
- `get_num_words(text)` - Splits text into words and returns word count
- `main()` - Orchestrates the book analysis

## How to Run
```bash
python3 main.py
```
Current output: `Found 75767 total words` from Frankenstein

## Testing
No automated tests currently exist in the project.

## Git Status
- Branch: main
- Recent changes to main.py have been made (function structure improvements)
