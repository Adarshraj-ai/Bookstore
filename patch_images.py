import re
from pathlib import Path

p = Path("home.html")
html = p.read_text(encoding="utf-8")

counter = 1
def replace_img(match):
    global counter
    new_tag = f'<div class="book-image" style="background-image: url(\'https://picsum.photos/seed/book{counter}/300/400\')"></div>'
    counter += 1
    return new_tag

new_html = re.sub(r'<div class="book-image" style="background-image: url\(\'book\d\.jpg\'\)"></div>', replace_img, html)

p.write_text(new_html, encoding="utf-8")
print("home.html book images updated with picsum")
