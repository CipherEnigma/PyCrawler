# PyCrawler
An AI webscraper platform using Python, selenium, ollama
This project is an intelligent web scraping tool that utilizes Python, Selenium, and Ollama to extract, analyze, and present data from the web efficiently. Designed for flexibility and ease of use, the scraper is powered by AI to handle dynamic websites, automate complex workflows, and provide meaningful insights beyond raw data extraction.
# Features
Dynamic Web Scraping: Leverages Selenium to interact with JavaScript-driven websites, handle page navigation, form submissions, and other interactive elements.
AI-Powered Analysis: Integrates with Ollama to process scraped content, summarize key insights, and extract structured information such as sentiment or keywords.
Customizable Workflow: Easily adaptable for scraping e-commerce, social media, news sites, and more.
Error Handling & Retrying: Ensures reliability through intelligent error handling, retries on failures, and detection of captchas.
Output Flexibility: Export data in multiple formats, including CSV, JSON, or database storage.
# Requirements
Python 3.8 or higher
Selenium WebDriver (ChromeDriver, GeckoDriver, etc.)
Ollama API key
Other dependencies listed in requirements.txt
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/ai-web-scraper.git
   cd ai-web-scraper
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up Selenium WebDriver:
   - Download the appropriate WebDriver for your browser.
   - Ensure it's added to your system's PATH.

4. Configure Ollama API:
   - Sign up for an Ollama API key [here](https://ollama.com/).
   - Add the key to your environment variables:
     ```bash
     export OLLAMA_API_KEY=your_api_key
     ```

## Usage

1. Define the target website(s) and scraping parameters in `config.py`.
2. Run the scraper:
   ```bash
   python scraper.py
   ```
3. Processed data will be stored in the output directory or sent to the defined database/storage location.

## Example Workflow

1. **Scraping:** Use Selenium to navigate and scrape e-commerce product pages.
2. **AI Analysis:** Send product descriptions to Ollama to classify by categories or extract customer sentiment.
3. **Export Results:** Save data as a CSV for further analysis.

## Project Structure

```
ai-web-scraper/
│
├── scraper.py       # Main script for running the scraper
├── config.py        # Configuration file for URLs, parameters, etc.
├── requirements.txt # List of dependencies
├── utils/           # Helper functions for data cleaning, saving, etc.
├── logs/            # Log files for debugging
└── output/          # Directory for storing extracted data
```

## Contributions

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See `LICENSE` for more details.

--- 

This README provides a professional and comprehensive overview, making it easy for developers to understand the project and get started.
