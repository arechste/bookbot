# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project! A simple Python application that reads text files and analyzes word counts.

## Features

- Reads book files from disk
- Counts total word count in the file
- Analyzes character frequency distribution
- Displays alphabetical characters sorted by frequency (greatest to least)
- Clean, modular code architecture with separated concerns

## Usage

```bash
python3 main.py
```

This will read the Frankenstein text file and output a formatted report with:
- Total word count
- Character frequency analysis (alphabetical characters only)
- Results sorted by character frequency in descending order

## Project Structure

- `main.py` - Application entry point and file handling
- `stats.py` - Text analysis functions
- `books/` - Sample book files

## Development

This project demonstrates:
- File I/O in Python
- Function decomposition and modularity
- Basic text analysis
