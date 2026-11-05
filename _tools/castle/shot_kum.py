from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':390,'height':800})
    pg.goto('http://localhost:8765/guides/kumamoto-castle/',wait_until='load')
    pg.evaluate("document.querySelectorAll('img').forEach(i=>i.loading='eager')"); pg.wait_for_timeout(1500)
    print(pg.evaluate("document.documentElement.scrollWidth"), pg.evaluate("[...document.images].filter(i=>!i.naturalWidth).map(i=>i.src)"))
    b.close()
