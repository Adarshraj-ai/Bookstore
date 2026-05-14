import pathlib
import re

p = pathlib.Path('Catalogue.html')
try:
    t = p.read_text(encoding='utf-8')
except Exception:
    t = p.read_text(encoding='latin-1')

# The file contains literal '\n' characters as a string!
old_render = r"function renderBooks(category, filter = '') {\n      currentCategory = category;\n      const allBooks = JSON.parse(localStorage.getItem('books')) || {};\n      let books = allBooks[category] || [];"

new_render = r"function renderBooks(category, filter = '') {\n      currentCategory = category;\n      const allBooks = JSON.parse(localStorage.getItem('books')) || {};\n      let books = [];\n      if (category === 'All') {\n        for (const cat in allBooks) {\n          books = books.concat(allBooks[cat]);\n        }\n      } else {\n        books = allBooks[category] || [];\n      }"

t = t.replace(old_render, new_render)
t = t.replace(r"'Fiction': '📚',", r"'All': '🌐',\n        'Fiction': '📚',")

old_init = r"// Initialize with Fiction category\n    renderBooks('Fiction');"

new_init = r"// Initialize with Fiction category or search query\n    const urlParams = new URLSearchParams(window.location.search);\n    const searchParam = urlParams.get('search');\n    if (searchParam) {\n      document.getElementById('searchInput').value = searchParam;\n      renderBooks('All', searchParam);\n    } else {\n      renderBooks('Fiction');\n    }"

t = t.replace(old_init, new_init)

p.write_text(t, encoding='utf-8')
print('patched successfully')
