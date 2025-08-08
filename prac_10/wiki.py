"""
CP1404 - William Hunter
Wikipedia API & Python library
Estimate: 30 mins
Actual: 30 mins
"""

import wikipedia

def main():
    """Main search function for Wikipedia using both page title."""
    while True:
        page_title = input("Enter page title: ").strip()
        if page_title == "":
            print("Thank you.")
            break

        try:
            page = wikipedia.page(page_title, auto_suggest=False)
            print(f"\nPage title: {page.title}")
            print(f"Summary:\n{page.summary}\n")
            print(f"URL: {page.url}")

        except wikipedia.exceptions.DisambiguationError as e:
            print(f"Disambiguation error. Options include: {e.options}")
        except wikipedia.exceptions.PageError:
            print("Page not found. Please try a different title.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()


