from patchright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        # Launches using Patchright's CDP-patched browser driver
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Navigate to target site
        page.goto("https://bot.sannysoft.com/")
        
        # Take screenshot to verify detection checks pass
        page.screenshot(path="patchright_test.png", full_page=True)
        

if __name__ == "__main__":
    main()