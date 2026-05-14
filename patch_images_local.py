import re
from pathlib import Path

# 1. Update shop.html
shop_p = Path('shop.html')
shop_html = shop_p.read_text(encoding='utf-8')

# We want to change the imgUrl logic in renderBooks
old_js = r"const imgUrl = `https://image.pollinations.ai/prompt/book%20cover%20for%20\$\{encodeURIComponent\(b.title\)\}\?width=300&height=400&nologo=true`;"
new_js = r"const imgUrl = `book${(b.title.length % 4) + 1}.jpg`;"
if old_js in shop_html:
    shop_html = shop_html.replace(old_js, new_js)
else:
    # try regex
    shop_html = re.sub(r'const imgUrl = `https://image\.pollinations\.ai/.*?`;', new_js, shop_html)

shop_p.write_text(shop_html, encoding='utf-8')

# 2. Update home.html
home_p = Path('home.html')
home_html = home_p.read_text(encoding='utf-8')

counter = 1
def replace_img(match):
    global counter
    new_url = f"book{((counter - 1) % 4) + 1}.jpg"
    counter += 1
    return f"background-image: url('{new_url}')"

new_home = re.sub(r"background-image: url\('https://image\.pollinations\.ai/.*?'\)", replace_img, home_html)
home_p.write_text(new_home, encoding='utf-8')

print("Images updated to local book1-4.jpg files successfully.")
