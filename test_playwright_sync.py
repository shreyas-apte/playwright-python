from playwright.sync_api import sync_playwright

def take_screenshot(url, output_path="screenshot.png"):
    """
    Opens a website and takes a screenshot.

    Args:
        url: The URL of the website to open.
        output_path: The path to save the screenshot.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # or p.firefox.launch() or p.webkit.launch()
        page = browser.new_page()
        page.goto(url)
        page.screenshot(path=output_path)
        browser.close()

if __name__ == "__main__":
    website_url = "https://www.whatismybrowser.com" # Replace with your desired URL
    screenshot_path = "./screenshot.png"
    take_screenshot(website_url, screenshot_path)
    print(f"Screenshot saved to: {screenshot_path}")