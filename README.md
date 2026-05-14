# Bookstore

Bookstore is a professional, premium, and functional online e-commerce bookstore. It features a modern shop interface, smart search capabilities, dynamic AI-generated book covers, and a seamless checkout experience. 

This project focuses on providing a clean, responsive aesthetic for the best possible user experience, demonstrating strong frontend design principles and functional cart/checkout flows.

## 🌟 Features
- **Modern Shop Interface**: A clean and premium catalogue page for browsing books.
- **Smart Search**: Quickly find books with an intelligent search implementation.
- **Dynamic AI-Generated Book Covers**: Unique and relevant book covers generated via Python scripts.
- **Seamless Checkout**: Functional cart and checkout experience with individual and global buy options.
- **Responsive UI**: Optimized for desktop, tablet, and mobile screens.
- **User Management Pages**: Includes interfaces for Login, Register, Profile, and Order tracking.

## 🛠️ Tech Stack
- **Frontend**: HTML5, Vanilla JavaScript
- **Styling**: Vanilla CSS
- **Build/Tooling**: Python (Scripts for compiling the shop, patching images, and updating navigation)

## 💻 Running the Project Locally

These instructions will help you set up a copy of the project on your local machine.

### Prerequisites
- A modern web browser (Chrome, Firefox, Edge, Safari)
- **Python 3.x** (Required if you want to run the python utility scripts like `build_shop.py`)

### Installing & Usage

1. **Clone the repository** to your local machine:
   ```bash
   git clone https://github.com/your-username/bookstore.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd bookstore
   ```

3. **Run the Project**:
   Since the frontend is built with vanilla HTML/CSS/JS, you can easily run it by starting a local web server. If you have Python installed, you can use its built-in server:
   ```bash
   python -m http.server 8000
   ```
   Then open your browser and navigate to `http://localhost:8000/home.html`.
   *(Alternatively, you can just open `home.html` directly in your web browser).*

4. **Running Utility Scripts (Optional)**:
   The project includes several Python scripts to build the shop structure and update components. You can run them manually when needed:
   ```bash
   python build_shop.py
   python update_nav.py
   ```

## 🤝 Contributions

Contributions are welcome! Whether it's improving the UI, adding new features to the shop, or optimizing the Python build scripts, feel free to dive in.

If you have any questions about the setup or the Python tooling structure, feel free to reach out.

Happy coding!
