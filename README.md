# Hermes Hello World

This project is a "Dynamic Hello" scraper that fetches and displays the top 5 trending repositories on GitHub.

## Features
- Fetches real-time trending data from [GitHub Trending](https://github.com/trending).
- Parses repository names using `BeautifulSoup`.
- Displays the output in a clean, numbered list format.

## Setup

### Prerequisites
- Python 3.11+
- `pip`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/naruebes-dearw/hermes-hello-world.git
   cd hermes-hello-world
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## Usage
Run the scraper script:
```bash
python3 scraper.py
```

## License
MIT
