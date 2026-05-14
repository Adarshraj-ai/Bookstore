import re
from pathlib import Path
import urllib.parse

p = Path("home.html")
html = p.read_text(encoding="utf-8")

def replace_img(match):
    content = match.group(0)
    # Extract the title from <h4>Title</h4> inside the article
    title_m = re.search(r'<h4>(.*?)</h4>', content)
    title = title_m.group(1) if title_m else "Book"
    
    encoded_title = urllib.parse.quote(title)
    img_url = f"https://image.pollinations.ai/prompt/book%20cover%20for%20{encoded_title}?width=300&height=400&nologo=true"
    
    # Replace the picsum URL
    content = re.sub(r'https://picsum\.photos/seed/book\d+/300/400', img_url, content)
    return content

new_html = re.sub(r'<article class="book-card".*?</article>', replace_img, html, flags=re.DOTALL)

p.write_text(new_html, encoding="utf-8")
print("home.html book images updated with pollinations.ai")
