import time
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from rich import print


# the category for which we seek reviews
CATEGORY = "맛집"
# the location
LOCATION = "명동"
# google's main URL
URL = "https://www.google.com"


if __name__ == '__main__':
    with sync_playwright() as pw:
        # creates an instance of the Chromium browser and launches it
        browser = pw.chromium.launch(headless=False)
        # creates a new browser page (tab) within the browser instance
        page = browser.new_page()
        # go to url with Playwright page element
        page.goto(URL)
        # deal with cookies page
        page.click('textarea#APjFqb.gLFyf')
        # write what you're looking for
        page.fill("textarea", f"{LOCATION} {CATEGORY}")
        # press enter
        page.keyboard.press('Enter')
        # change to english
        # page.locator("text='Change to English'").click()
        time.sleep(2)
        # click in the "Maps" HTML element
        # page.click('a.LatpMc.nPDzT.T3FoJb >> nth=2')
        page.click('a.LatpMc.nPDzT.T3FoJb')
        # page.click('div.GKS7s')
        # page.click('span.FMKtTb.UqcIvb')
        # page.click('CAsQAQ')
        time.sleep(4)
        # scrolling
        for i in range(30):
            # tackle the body element
            html = page.inner_html('body')
            # create beautiful soup element
            soup = BeautifulSoup(html, 'html.parser')
            # select items
            categories = soup.select('.hfpxzc')
            last_category_in_page = categories[-1].get('aria-label')
            last_last_page = categories[-1].get('aria-label')
            # scroll to the last item
            last_category_location = page.locator(
                f"text={last_category_in_page}").first
            last_category_location.scroll_into_view_if_needed()
            # wait to load contents
            time.sleep(2)


        # get links of all categories after scroll
        links = [item.get('href') for item in soup.select('.hfpxzc')]
        print(links)
        print(len(links))
        f = open("links.txt", 'w')
        for link in links:
            f.write(link)
            f.write('\n')
        f.close()

        for link in links:
            # go to subject link
            page.goto(link)
            time.sleep(4)
            # load all reviews
            page.locator("text='리뷰'").first.click()
            time.sleep(4)
            # create new soup
            html = page.inner_html('body')
            # create beautiful soup element
            soup = BeautifulSoup(html, 'html.parser')
            # scrape reviews
            reviews = soup.select('.MyEned')
            reviews = [review.find('span').text for review in reviews]
            # print reviews
            for review in reviews:
                print(review)
                print('\n')