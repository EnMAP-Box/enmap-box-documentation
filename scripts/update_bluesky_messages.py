import time
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

PROFILE_URL = 'https://bsky.app/profile/humboldteolab.bsky.social'
NEWS_RST_PATH = 'source/news.rst'


def get_embed_html(post_url):
    """Fetch the embed HTML for a given Bluesky post URL using oEmbed."""
    oembed_url = f'https://bsky.social/oembed?url={post_url}'
    response = requests.get(oembed_url)
    if response.status_code == 200:
        return response.json().get('html', '')
    else:
        print(f"❌ Failed to fetch oEmbed for {post_url}")
        return ''


def scrape_bluesky_posts():
    """Scrape the latest three posts containing 'EnMAP' or '#EnMAP'."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(PROFILE_URL)
        time.sleep(5)

        # Scroll down to load posts
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        post_links = []

        # Find post URLs containing "enmap"
        for link in soup.find_all('a', href=True):
            href = link['href']
            if re.match(r'^/profile/[^/]+/post/[^/]+$', href):
                post_url = f'https://bsky.app{href}'
                text = link.get_text()
                if 'enmap' in text.lower() and post_url not in post_links:
                    post_links.append(post_url)
            if len(post_links) >= 3:
                break

        # Get oEmbed HTML for each post URL
        return [get_embed_html(url) for url in post_links]

    finally:
        driver.quit()


def update_news_rst(embeds):
    """Update the news.rst file with the latest Bluesky embeds."""
    with open(NEWS_RST_PATH, 'r', encoding='utf-8') as file:
        content = file.read()

    new_html = f"""
.. raw:: html

    <div style="display: flex; justify-content: space-between; gap: 40px; align-items: flex-start;">

        <div style="flex: 1; min-width: 45%;">

            <h2>Upcoming Events</h2>

            <table border="1" class="docutils">
                <thead>
                    <tr>
                        <th>Title</th>
                        <th>Date</th>
                        <th>Location</th>
                        <th>Comments</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><a href="https://enmap.geographie-muenchen.de/">2nd EnMAP User Workshop</a></td>
                        <td>2-4 April 2025</td>
                        <td>Munich, Germany</td>
                        <td>Tutorial</td>
                    </tr>
                    <tr>
                        <td><a href="https://www.fossgis-konferenz.de/2025/">FOSSGIS 2025</a></td>
                        <td>26-29 March</td>
                        <td>Münster, Germany</td>
                        <td>Oral Presentation</td>
                    </tr>
                    <tr>
                        <td><a href="https://lps25.esa.int/">Living Planet Symposium 2025</a></td>
                        <td>23-27 June 2025</td>
                        <td>Vienna, Austria</td>
                        <td></td>
                    </tr>
                </tbody>
            </table>

        </div>

        <div style="flex: 1; min-width: 45%;">

            <h2>Bluesky Feed</h2>

            <!-- Latest Bluesky embeds -->
            <div>
                {embeds[0] if len(embeds) > 0 else ''}
            </div>
            <div style="margin-top: 20px;">
                {embeds[1] if len(embeds) > 1 else ''}
            </div>
            <div style="margin-top: 20px;">
                {embeds[2] if len(embeds) > 2 else ''}
            </div>

        </div>
    </div>
"""

    # Replace the existing Bluesky feed block (from .. raw:: html to end of divs)
    pattern = re.compile(
        r'(?s)(\.\. raw:: html\s*\n\s*<div style="display: flex;.*?</div>\s*</div>\s*</div>)',
        re.MULTILINE,
    )

    updated_content, count = re.subn(pattern, new_html.strip(), content)
    if count == 0:
        print("⚠️ Warning: Could not find Bluesky feed section in news.rst to replace. Adding at the end.")
        updated_content = content.strip() + "\n\n" + new_html.strip()

    with open(NEWS_RST_PATH, 'w', encoding='utf-8') as file:
        file.write(updated_content)

    print("✅ news.rst has been updated with the latest Bluesky posts.")


if __name__ == "__main__":
    latest_embeds = scrape_bluesky_posts()
    update_news_rst(latest_embeds)
