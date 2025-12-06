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
3. Counts the frequency of each character (normalized to lowercase)
4. Generates a formatted report with word count and character frequency (alphabetical characters only)
5. Displays results sorted by character frequency (greatest to least)

## Module Functions

### main.py
- `get_book_text(filepath)` - Reads a file and returns its contents as a string
- `main()` - Entry point; orchestrates book text analysis and calls report printing
- `print_report(book_path, num_words, chars_sorted_list)` - Formats and prints analysis results

### stats.py
- `get_num_words(text)` - Counts words in text by splitting on whitespace
- `get_chars_dict(text)` - Counts character occurrences (normalized to lowercase)
- `chars_dict_to_sorted_list(num_chars_dict)` - Converts character dict to sorted list of dicts
- `sort_on(d)` - Helper function that returns the "num" value for sorting

## How to Run
```bash
python3 main.py
```
Produces formatted report with word count and character frequency analysis

## Testing
No automated tests currently exist in the project.

## Code Quality
- Functions include docstrings for clarity
- Clean separation of concerns between modules
- Simple, readable implementation
