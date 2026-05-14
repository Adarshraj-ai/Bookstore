
    const booksByCategory = {
      Fiction: [
        { title: "The Great Gatsby", author: "F. Scott Fitzgerald", publisher: "Penguin", year: 2004, price: 285, details: "A classic American novel set in the Jazz Age." },
        { title: "The Midnight Library", author: "Matt Haig", publisher: "Penguin", year: 2020, price: 345, details: "Explore alternate life choices in this uplifting fiction." },
        { title: "Pride and Prejudice", author: "Jane Austen", publisher: "Penguin Classics", year: 2003, price: 299, details: "Timeless romance and social commentary from the 19th century." },
        { title: "One Hundred Years of Solitude", author: "Gabriel Garc�a M�rquez", publisher: "HarperCollins", year: 2006, price: 425, details: "A masterpiece of magical realism with unforgettable characters." },
        { title: "The Catcher in the Rye", author: "J.D. Salinger", publisher: "Back Bay Books", year: 2004, price: 315, details: "Coming-of-age story set in New York City." }
      ],
      Mystery: [
        { title: "Sherlock Holmes Collection", author: "Arthur Conan Doyle", publisher: "Dover", year: 2009, price: 599, details: "Complete collection of classic detective mysteries." },
        { title: "The Girl with the Dragon Tattoo", author: "Stieg Larsson", publisher: "Penguin", year: 2008, price: 445, details: "A gripping Nordic noir mystery with unforgettable characters." },
        { title: "Murder on the Orient Express", author: "Agatha Christie", publisher: "Penguin", year: 2001, price: 295, details: "A locked-room mystery with brilliant twists." },
        { title: "The Da Vinci Code", author: "Dan Brown", publisher: "Doubleday", year: 2003, price: 385, details: "Thrilling mystery combining history and suspense." }
      ],
      Romance: [
        { title: "The Notebook", author: "Nicholas Sparks", publisher: "Grand Central Publishing", year: 2004, price: 315, details: "A heartwarming story of love that endures time." },
        { title: "Me Before You", author: "Jojo Moyes", publisher: "Penguin", year: 2012, price: 365, details: "Emotional romance exploring love and difficult choices." },
        { title: "Outlander", author: "Diana Gabaldon", publisher: "Delacorte", year: 1991, price: 495, details: "Epic romance spanning time and continents." },
        { title: "The Hating Game", author: "Sally Thorne", publisher: "HarperCollins", year: 2016, price: 335, details: "Fun, witty enemies-to-lovers contemporary romance." }
      ],
      SelfHelp: [
        { title: "Atomic Habits", author: "James Clear", publisher: "Penguin", year: 2018, price: 449, details: "Build better habits and transform your life through small changes." },
        { title: "The 7 Habits of Highly Effective People", author: "Stephen Covey", publisher: "Free Press", year: 2004, price: 525, details: "Timeless principles for personal and professional success." },
        { title: "Think and Grow Rich", author: "Napoleon Hill", publisher: "Fingerprint", year: 2009, price: 399, details: "Classic guide to achieving wealth and success." },
        { title: "The Power of Now", author: "Eckhart Tolle", publisher: "Hodder", year: 1999, price: 475, details: "Transform your life by living in the present moment." }
      ],
      Children: [
        { title: "Harry Potter and the Sorcerer's Stone", author: "J.K. Rowling", publisher: "Bloomsbury", year: 1997, price: 550, details: "The magical beginning of Harry's wizarding journey." },
        { title: "Percy Jackson & The Olympians", author: "Rick Riordan", publisher: "Puffin", year: 2005, price: 425, details: "Adventure with Greek gods in modern America." },
        { title: "Wings of Fire Series", author: "Tui T. Sutherland", publisher: "Scholastic", year: 2012, price: 380, details: "Epic dragon fantasy for young readers." },
        { title: "The Hobbit", author: "J.R.R. Tolkien", publisher: "HarperCollins", year: 1937, price: 495, details: "Classic fantasy adventure of Bilbo Baggins." }
      ],
      Biography: [
        { title: "Steve Jobs", author: "Walter Isaacson", publisher: "Simon & Schuster", year: 2011, price: 475, details: "Authorized biography of Apple's visionary founder." },
        { title: "The Story of My Life", author: "Helen Keller", publisher: "Dover", year: 1903, price: 225, details: "Inspiring memoir of overcoming profound disabilities." },
        { title: "Elon Musk", author: "Ashlee Vance", publisher: "Ecco", year: 2015, price: 495, details: "Biography of Tesla and SpaceX founder." },
        { title: "Becoming", author: "Michelle Obama", publisher: "Crown", year: 2018, price: 525, details: "Memoir of becoming America's First Lady." }
      ],
      Science: [
        { title: "A Brief History of Time", author: "Stephen Hawking", publisher: "Bantam", year: 1988, price: 395, details: "Accessible exploration of black holes and the universe." },
        { title: "The Selfish Gene", author: "Richard Dawkins", publisher: "Oxford University Press", year: 1976, price: 425, details: "Revolutionary look at evolution and genetics." },
        { title: "Sapiens", author: "Yuval Noah Harari", publisher: "HarperCollins", year: 2014, price: 555, details: "History of humankind from the Stone Age to present." },
        { title: "Cosmos", author: "Carl Sagan", publisher: "Ballantine", year: 1980, price: 475, details: "Journey through space, time, and human understanding." }
      ],
      Education: [
        { title: "Introduction to Algorithms", author: "Cormen, Leiserson & Rivest", publisher: "MIT Press", year: 2009, price: 850, details: "Comprehensive guide to algorithm design and analysis." },
        { title: "Artificial Intelligence: A Modern Approach", author: "Russell & Norvig", publisher: "Pearson", year: 2020, price: 799, details: "Authoritative textbook on AI theory and practice." },
        { title: "The Complete Web Developer", author: "Andrew Mead", publisher: "Udemy", year: 2020, price: 595, details: "Learn full-stack web development from scratch." },
        { title: "Data Science Handbook", author: "Jake VanderPlas", publisher: "O'Reilly", year: 2016, price: 725, details: "Comprehensive guide to data science and machine learning." }
      ]
    };
    
    let currentCategory = 'Fiction';
    let currentBooks = [];
    
    // Initialize localStorage with books if not present
    if (!localStorage.getItem('books')) {
      localStorage.setItem('books', JSON.stringify(booksByCategory));
    }
    
    function addToCart(book) {
      const cart = JSON.parse(localStorage.getItem('cart')) || [];
      cart.push(book);
      localStorage.setItem('cart', JSON.stringify(cart));
      alert(`✅ "${book.title}" added to your cart!`);
    }
    
    function showBookDetails(index) {
      const book = currentBooks[index];
      if (!book) return;
      alert(`📘 ${book.title}\
\
Author: ${book.author}\
Publisher: ${book.publisher}\
Year: ${book.year}\
Price: ₹${book.price}\
\
${book.details}`);
    }
    
    function renderBooks(category, filter = '') {
      currentCategory = category;
      const allBooks = JSON.parse(localStorage.getItem('books')) || {};
      let books = [];
      if (category === 'All') {
        for (const cat in allBooks) {
          books = books.concat(allBooks[cat]);
        }
      } else {
        books = allBooks[category] || [];
      }
      
      if (filter) {
        books = books.filter(book => 
          book.title.toLowerCase().includes(filter.toLowerCase()) || 
          book.author.toLowerCase().includes(filter.toLowerCase())
        );
      }
      
      currentBooks = books;
      
      const categoryEmojis = {
        'All': '🌐', 'All': '🌐',
        'Fiction': '📚',
        'Mystery': '🕵️‍♂️',
        'Romance': '💘',
        'SelfHelp': '🧠',
        'Children': '🧒',
        'Biography': '👤',
        'Science': '🔬',
        'Education': '🎓'
      };
      
      document.getElementById('categoryTitle').textContent = `${categoryEmojis[category]} ${category} ${filter ? `(Search: "${filter}")` : ''}`;
      
      const table = document.getElementById('bookTable');
      table.querySelectorAll('tr:not(:first-child)').forEach(row => row.remove());
      
      if (books.length === 0) {
        const row = document.createElement('tr');
        row.innerHTML = `<td colspan="5" style="text-align: center; color: #999;">No books found</td>`;
        table.appendChild(row);
        return;
      }
      
      books.forEach((book, index) => {
        const row = document.createElement('tr');
        row.innerHTML = `<td>${book.title}</td><td>${book.author}</td><td>${book.publisher}</td><td>₹${book.price}</td><td class="actions"><button class="action details">Details</button><button class="action add">Add to Cart</button></td>`;
        row.querySelector('.details').addEventListener('click', () => showBookDetails(index));
        row.querySelector('.add').addEventListener('click', () => addToCart(book));
        table.appendChild(row);
      });
    }
    
    function filterBooks() {
      const filter = document.getElementById('searchInput').value;
      renderBooks(currentCategory, filter);
    }
    
    function addNewBook() {
      const category = document.getElementById('categorySelect').value;
      const title = document.getElementById('newTitle').value.trim();
      const author = document.getElementById('newAuthor').value.trim();
      const publisher = document.getElementById('newPublisher').value.trim();
      const price = document.getElementById('newPrice').value.trim();
      
      if (!title || !author || !publisher || !price) {
        alert('⚠️ Please fill all fields!');
        return;
      }
      
      const allBooks = JSON.parse(localStorage.getItem('books')) || {};
      allBooks[category] = allBooks[category] || [];
      allBooks[category].push({
        title,
        author,
        publisher,
        year: new Date().getFullYear(),
        price: Number(price),
        details: '✨ New arrival in BooksWorld catalogue!'
      });
      
      localStorage.setItem('books', JSON.stringify(allBooks));
      renderBooks(category);
      alert('✅ Book added successfully!');
      document.getElementById('newTitle').value = '';
      document.getElementById('newAuthor').value = '';
      document.getElementById('newPublisher').value = '';
      document.getElementById('newPrice').value = '';
    }
    
    // Initialize with Fiction category or search query
    const urlParams = new URLSearchParams(window.location.search);
    const searchParam = urlParams.get('search');
    if (searchParam) {
      document.getElementById('searchInput').value = searchParam;
      renderBooks('All', searchParam);
    } else {
      renderBooks('Fiction');
    }
  