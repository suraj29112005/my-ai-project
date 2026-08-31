import requests
from bs4 import BeautifulSoup

def scrape_headlines(target_url, headline_selector):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(target_url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        headlines = soup.select(headline_selector)

        if not headlines:
            print("No headlines found with the specified selector.")
            return

        print(f"\n--- Fetched {len(headlines)} Headlines ---\n")
        for i, element in enumerate(headlines, start=1):
            text = element.get_text(strip=True)
            if text:
                print(f"{i}. {text}")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example: Scraping Hacker News
    target_url = "https://news.ycombinator.com/"
    headline_selector = ".titleline > a"

    scrape_headlines(target_url, headline_selector)
