from playwright.sync_api import sync_playwright
import os

def verify_heritage_section():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get absolute path to index.html
        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"

        print(f"Navigating to: {file_path}")
        page.goto(file_path)

        # Locate the heritage section
        heritage_section = page.locator("#about")

        # Take a screenshot of the heritage section
        heritage_section.screenshot(path="verification/heritage_section.png")

        # Also take a mobile screenshot
        page.set_viewport_size({"width": 375, "height": 812})
        heritage_section.screenshot(path="verification/heritage_section_mobile.png")

        browser.close()

if __name__ == "__main__":
    verify_heritage_section()
