import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'shop.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Replace Catalogue.html with shop.html everywhere
    content = content.replace('Catalogue.html', 'shop.html')
    
    # 2. Update the navbar
    # Look for the nav block. Usually it's:
    # <nav>
    #   <a href="cart.html">🛒 Cart</a>
    #   <a href="orders.html">📦 Orders</a>
    #   <a href="profile.html">👤 Profile</a>
    # </nav>
    
    # We want to add <a href="shop.html">🛍️ Shop</a> before Cart if it's not there.
    if '🛍️ Shop' not in content and '<nav>' in content:
        content = content.replace('<nav>', '<nav>\n        <a href="shop.html">🛍️ Shop</a>')
    
    # Also for top.html which has target="_top"
    if f == 'top.html' and '🛍️ Shop' not in content:
        content = content.replace('<nav>', '<nav>\n        <a href="shop.html" target="_top">🛍️ Shop</a>')
    
    # In home.html, we should also add a "Shop All Books" button
    # Let's find the search-hero block
    if f == 'home.html' and 'Shop All Books' not in content:
        hero_replacement = """    <div class="search-hero">
      <input type="text" id="homeSearch" placeholder="Search for books, authors, or genres..." onkeypress="handleSearch(event)">
      <button onclick="performSearch()">🔍 Search</button>
      <button onclick="window.location.href='shop.html'" style="background: linear-gradient(135deg, #10b981, #059669);">🛍️ Shop All Books</button>
    </div>"""
        content = re.sub(r'<div class="search-hero">.*?</div>', hero_replacement, content, flags=re.DOTALL)
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Updated navigation and references to shop.html")
