# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project! A simple Python application that reads text files and analyzes word counts.

## Features

- Reads book files from disk
- Counts total word count in the file
- Analyzes character frequency distribution
- Displays alphabetical characters sorted by frequency (greatest to least)
- Clean, modular code architecture with separated concerns

## Getting Books

Books need to be stored as text files in the `books/` directory. You can download text files from various sources using `wget`:

```bash
# Obtain Frankenstein
wget -O books/frankenstein.txt https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/frankenstein.txt

# Obtain Moby Dick
wget -O books/mobydick.txt https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/mobydick.txt

# Obtain Pride and Prejudice
wget -O books/prideandprejudice.txt https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/prideandprejudice.txt
```

You can also use other text file sources or add your own books to the `books/` directory.

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
