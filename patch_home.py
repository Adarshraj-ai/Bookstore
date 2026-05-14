import re
from pathlib import Path

p = Path("home.html")
html = p.read_text(encoding="utf-8")

# Images to cycle through
imgs = ["book1.jpg", "book2.jpg", "book3.jpg", "book4.jpg"]

def replace_book_card(match):
    global idx
    content = match.group(0)
    
    # Extract title, author, price from the card content
    title_m = re.search(r'<h4>(.*?)</h4>', content)
    author_m = re.search(r'<p>(.*?) · (.*?)</p>', content)
    price_m = re.search(r'<p class="price">₹(.*?)</p>', content)
    
    title = title_m.group(1) if title_m else "Unknown Title"
    author = author_m.group(1).replace("'", "\\'") if author_m else "Unknown Author"
    publisher = author_m.group(2).replace("'", "\\'") if author_m else "Unknown Publisher"
    price = price_m.group(1) if price_m else "0"
    details = f"A wonderful book titled {title}."
    
    img = imgs[idx % 4]
    idx += 1
    
    # Replace the background gradient with image
    content = re.sub(
        r'style="background: linear-gradient[^"]*"',
        f'style="background-image: url(\'{img}\')"',
        content
    )
    
    # Add cursor pointer and onclick to the article
    if '<article class="book-card"' in content:
        content = content.replace('<article class="book-card"', f'<article class="book-card" style="cursor: pointer;" onclick="openModal(\'{title.replace(chr(39), chr(92)+chr(39))}\', \'{author}\', \'{publisher}\', {price}, \'{details}\')"')
        
    return content

idx = 0
new_html = re.sub(r'<article class="book-card">.*?</article>', replace_book_card, html, flags=re.DOTALL)

# Add Modal HTML before script
modal_html = """
  <div id="bookModal" class="modal">
    <div class="modal-content">
      <span class="close" onclick="closeModal()">&times;</span>
      <h2 id="modalTitle">Book Title</h2>
      <p><strong>Author:</strong> <span id="modalAuthor"></span></p>
      <p><strong>Publisher:</strong> <span id="modalPublisher"></span></p>
      <p><strong>Price:</strong> ₹<span id="modalPrice"></span></p>
      <p><strong>Details:</strong> <span id="modalDetails"></span></p>
      <div class="modal-actions">
        <button class="btn-cart" onclick="addModalToCart()">Add to Cart</button>
        <button class="btn-buy" onclick="buyNowModal()">Buy Now</button>
      </div>
    </div>
  </div>
"""
if '<div id="bookModal"' not in new_html:
    new_html = new_html.replace('  <script>', modal_html + '\n  <script>')

# Add Modal CSS
modal_css = """
    .modal { display: none; position: fixed; z-index: 2000; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.7); backdrop-filter: blur(5px); }
    .modal-content { background: linear-gradient(135deg, #1e293b, #0f172a); margin: 10% auto; padding: 30px; border: 1px solid #334155; border-radius: 20px; width: 90%; max-width: 500px; color: white; position: relative; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5); }
    .close { position: absolute; right: 20px; top: 15px; color: #94a3b8; font-size: 28px; font-weight: bold; cursor: pointer; }
    .close:hover { color: white; }
    .modal-content h2 { margin-bottom: 15px; color: #38bdf8; }
    .modal-content p { margin-bottom: 10px; font-size: 1.05rem; }
    .modal-actions { display: flex; gap: 15px; margin-top: 25px; }
    .btn-cart, .btn-buy { flex: 1; padding: 12px; border: none; border-radius: 10px; font-size: 1.1rem; font-weight: bold; cursor: pointer; transition: transform 0.2s; }
    .btn-cart { background: #334155; color: white; }
    .btn-cart:hover { background: #475569; transform: translateY(-2px); }
    .btn-buy { background: #0ea5e9; color: white; }
    .btn-buy:hover { background: #0284c7; transform: translateY(-2px); }
"""
if '.modal {' not in new_html:
    new_html = new_html.replace('</style>', modal_css + '</style>')

# Add Modal JS
modal_js = """
    let currentModalBook = null;
    function openModal(title, author, publisher, price, details) {
      currentModalBook = { title, author, publisher, price, details };
      document.getElementById('modalTitle').innerText = title;
      document.getElementById('modalAuthor').innerText = author;
      document.getElementById('modalPublisher').innerText = publisher;
      document.getElementById('modalPrice').innerText = price;
      document.getElementById('modalDetails').innerText = details;
      document.getElementById('bookModal').style.display = 'block';
    }
    function closeModal() {
      document.getElementById('bookModal').style.display = 'none';
    }
    function addModalToCart() {
      if (currentModalBook) {
        const cart = JSON.parse(localStorage.getItem('cart') || '[]');
        cart.push(currentModalBook);
        localStorage.setItem('cart', JSON.stringify(cart));
        alert(`✅ "${currentModalBook.title}" added to your cart!`);
        closeModal();
      }
    }
    function buyNowModal() {
      if (currentModalBook) {
        const cart = JSON.parse(localStorage.getItem('cart') || '[]');
        cart.push(currentModalBook);
        localStorage.setItem('cart', JSON.stringify(cart));
        window.location.href = 'checkout.html';
      }
    }
    window.onclick = function(event) {
      if (event.target == document.getElementById('bookModal')) {
        closeModal();
      }
    }
"""
if 'function openModal' not in new_html:
    new_html = new_html.replace('</script>', modal_js + '\n  </script>')

p.write_text(new_html, encoding="utf-8")
print("home.html patched")
