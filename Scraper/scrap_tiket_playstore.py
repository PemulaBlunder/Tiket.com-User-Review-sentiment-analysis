import asyncio
from playwright.async_api import async_playwright

URL = "https://play.google.com/store/apps/details?id=com.tiket.gits&hl=en"

async def main():
    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=False,
            args=["--disable-blink-features=AutomationControlled"]
        )

        page = await browser.new_page()

        await page.goto(URL, wait_until="networkidle")

        # klik "See all reviews"
        await page.locator('button:has-text("See all reviews")').click()

        await page.wait_for_timeout(3000)

        # fokus ke popup review
        review_dialog = page.locator('[role="dialog"]')
        await review_dialog.hover()

        # scroll mouse
        for _ in range(500):
            await page.mouse.wheel(0, 5000)
            await page.wait_for_timeout(1000)

        html = await page.content()

        with open("playstore_reviews2.html", "w", encoding="utf-8") as f:
            f.write(html)

        await browser.close()

asyncio.run(main())