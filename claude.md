# BookBot Project Context

## Overview
BookBot is a Boot.dev project - a simple Python application that reads book files and analyzes word counts.

## Project Structure
- `main.py` - Main application file with entry point
- `stats.py` - Statistics module for word counting
- `books/frankenstein.txt` - Sample book file for analysis
- `README.md` - Project description

## Architecture
The project follows a modular architecture:
- **main.py**: Handles file I/O and orchestrates the analysis
- **stats.py**: Contains text analysis functions

## Current Functionality
The application:
1. Reads a book file (Frankenstein) from `books/frankenstein.txt`
2. Counts the total number of words in the file
3. Outputs: "Found {num_words} total words"

## Module Functions

### main.py
- `get_book_text(filepath)` - Reads a file and returns its contents as a string
- `main()` - Entry point; orchestrates book text analysis and output

### stats.py
- `get_num_words(text)` - Counts words in text by splitting on whitespace

## How to Run
```bash
python3 main.py
```
Output: `Found 75767 total words` (from Frankenstein)

## Testing
No automated tests currently exist in the project.

## Code Quality
- Functions include docstrings for clarity
- Clean separation of concerns between modules
- Simple, readable implementation
