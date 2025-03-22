import os
import boto3
import datetime
from playwright.sync_api import sync_playwright

s3 = boto3.client('s3')

# Set the environment variable within the script
os.environ["PLAYWRIGHT_BROWSERS_PATH"] = "/opt/playwright-browsers"

def run_playwright():
    """
    Launches a headless Chromium browser using Playwright, navigates to a website,
    takes a screenshot, and saves it locally as 'screenshot.png'.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page()
            page.goto("https://www.whatismybrowser.com")
            page.screenshot(path="/tmp/screenshot.png")
        finally:
            browser.close()

def lambda_handler(event, context):
    run_playwright()
    key = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    print(f"Uploading screenshot to S3 with key: {key}")
    s3.upload_file('/tmp/screenshot.png', 'bucket-playwright', key)
    return {
        'statusCode': 200,
        'body': 'Screenshot uploaded to S3!'
    }

if __name__ == '__main__':
	lambda_handler(None, None)