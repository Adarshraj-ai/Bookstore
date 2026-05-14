import re
from pathlib import Path
import urllib.parse

# 1. Update shop.html
shop_p = Path('shop.html')
shop_html = shop_p.read_text(encoding='utf-8')

# shop.html has: const imgUrl = `book${(b.title.length % 4) + 1}.jpg`;
new_js = r"const imgUrl = `https://image.pollinations.ai/prompt/book%20cover%20for%20${encodeURIComponent(b.title)}?width=300&height=400&nologo=true`;"
shop_html = re.sub(r'const imgUrl = `book.*?`;', new_js, shop_html)

shop_p.write_text(shop_html, encoding='utf-8')

# 2. Update home.html
home_p = Path('home.html')
home_html = home_p.read_text(encoding='utf-8')

def replace_img(match):
    content = match.group(0)
    title_m = re.search(r'<h4>(.*?)</h4>', content)
    title = title_m.group(1) if title_m else "Book"
    encoded_title = urllib.parse.quote(title)
    img_url = f"https://image.pollinations.ai/prompt/book%20cover%20for%20{encoded_title}?width=300&height=400&nologo=true"
    content = re.sub(r"background-image: url\('book\d\.jpg'\)", f"background-image: url('{img_url}')", content)
    return content

new_home = re.sub(r'<article class="book-card".*?</article>', replace_img, home_html, flags=re.DOTALL)
home_p.write_text(new_home, encoding='utf-8')

print("Images updated to Pollinations AI successfully.")
