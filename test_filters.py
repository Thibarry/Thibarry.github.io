import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # Listen to console logs
        page.on("console", lambda msg: print(f"Console: {msg.text}"))
        
        await page.goto("file:///c:/Users/thibarry/Documents/Personnel/Agentic/Antigravity/ai-architect-portfolio/projects.html")
        
        # Wait for page to load
        await page.wait_for_timeout(1000)
        
        # Click a filter
        print("Clicking Theme: RAG")
        await page.select_option("#filter-theme", "RAG")
        
        await page.wait_for_timeout(500)
        
        # Check how many cards are visible
        cards = await page.query_selector_all(".project-card")
        visible_count = 0
        for card in cards:
            is_visible = await card.is_visible()
            if is_visible:
                visible_count += 1
                title = await card.get_attribute("data-title")
                print(f"Visible card: {title}")
                
        print(f"Total visible cards: {visible_count}")
        
        await browser.close()

asyncio.run(run())
