# 📚 Booksworld — Online Bookstore

> A responsive online bookstore with dynamic search, category filtering, and a persistent shopping cart — built with zero frameworks using vanilla JavaScript.

<div align="center">

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=flat-square)
![Deployment](https://img.shields.io/badge/Deployed%20on-GitHub%20Pages-181717?style=flat-square&logo=github)

**[🌐 View Live Demo](https://adarshraj-ai.github.io/booksworld-website)**

</div>

---

## 📌 Overview

Booksworld is a fully client-side bookstore application. Users can browse categorized books, search by title or author, filter by genre, add items to a cart, and return later to find their cart exactly as they left it — thanks to Local Storage persistence.

---

## ✨ Features

- 📖 **Book Catalog** — Categorized listings with cover image, title, author & price
- 🔍 **Dynamic Search** — Real-time search filtering as you type (no page reload)
- 🏷️ **Genre Filter** — Filter books by category instantly
- 🛒 **Shopping Cart** — Add, remove, and update quantities with live price total
- 💾 **Cart Persistence** — Cart saved to `localStorage` — survives page refresh
- 📱 **Responsive Design** — CSS Grid + Flexbox layout adapts to all screen sizes
- ⚡ **Performance** — Lazy loading for images, minified assets, fast first paint

---

## 🛠️ Tech Stack

| Technology | Usage |
|-----------|-------|
| HTML5 | Semantic page structure |
| CSS3 | Grid, Flexbox, responsive design |
| Vanilla JavaScript | DOM manipulation, search, cart logic, localStorage |
| GitHub Pages | Free deployment |

---

## 📁 Project Structure

```
booksworld-website/
├── index.html
├── cart.html
├── css/
│   └── style.css
├── js/
│   ├── books.js       # Book data array
│   ├── filter.js      # Search & filter logic
│   └── cart.js        # Cart operations & localStorage
├── assets/
│   └── images/
└── README.md
```

---

## 🧠 JavaScript Features Breakdown

**Search & Filter (`filter.js`)**
```javascript
// Real-time filtering — no libraries needed
input.addEventListener('input', () => {
  const query = input.value.toLowerCase();
  books.filter(book =>
    book.title.toLowerCase().includes(query) ||
    book.author.toLowerCase().includes(query)
  );
});
```

**Cart Persistence (`cart.js`)**
```javascript
// Save cart to localStorage on every update
function saveCart(cart) {
  localStorage.setItem('booksworld_cart', JSON.stringify(cart));
}

// Restore cart on page load
function loadCart() {
  return JSON.parse(localStorage.getItem('booksworld_cart')) || [];
}
```

---

## 🚀 Run Locally

```bash
# Clone the repo
git clone https://github.com/Adarshraj-ai/booksworld-website.git

# Open directly in browser — no build needed
cd booksworld-website
open index.html
```

---

## 👨‍💻 Author

**Adarsh Singh**
📧 adarshmass111b@gmail.com
🔗 [github.com/Adarshraj-ai](https://github.com/Adarshraj-ai)

---

> ⭐ If this helped you learn vanilla JS, leave a star!
