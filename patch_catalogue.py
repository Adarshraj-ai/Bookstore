from pathlib import Path
p = Path("Catalogue.html")
t = p.read_text(encoding="utf-8")
old = r'row.innerHTML = `<td>${book.title}</td><td>${book.author}</td><td>${book.publisher}</td><td>${book.price}</td><td class="actions"><button class="action details">Details</button><button class="action add">Add to Cart</button></td>`;'
new = r'row.innerHTML = `<td>${book.title}</td><td>${book.author}</td><td>${book.publisher}</td><td>${book.price}</td><td class="actions"><button class="action details">Details</button><button class="action add">Add to Cart</button></td>`;'
if old not in t:
    raise SystemExit("not found")
p.write_text(t.replace(old, new), encoding="utf-8")
print("ok")
