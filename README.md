# Kiwigpt - AI Research Blog

A modern, fast, and beautiful website built with Hugo and the PaperMod theme. This site showcases AI research insights, tutorials, and thought leadership content at www.kiwigpt.co.nz.

## 🚀 Features

- **Fast & Modern**: Built with Hugo static site generator
- **Beautiful Design**: PaperMod theme for clean, professional look
- **SEO Optimized**: Built-in SEO features and meta tags
- **Mobile Responsive**: Works perfectly on all devices
- **Automated Deployment**: GitHub Actions + GitHub Pages
- **Markdown Support**: Easy content creation with Markdown
- **Search Functionality**: Built-in search capabilities
- **Social Sharing**: Easy sharing on social platforms

## 🛠️ Tech Stack

- **Hugo**: Static site generator
- **PaperMod**: Clean and modern theme
- **GitHub Pages**: Free hosting
- **GitHub Actions**: Automated deployment
- **Markdown**: Content authoring

## 📁 Project Structure

```
kiwigpt/
├── content/           # Your content (posts, pages)
│   ├── posts/        # Blog posts
│   └── pages/        # Static pages
├── themes/           # Hugo themes
│   └── PaperMod/     # PaperMod theme
├── assets/           # Static assets (images, CSS, JS)
├── .github/          # GitHub Actions workflows
├── hugo.toml         # Hugo configuration
└── README.md         # This file
```

## 🚀 Quick Start

### Prerequisites

- Hugo (v0.148.2 or later)
- Git
- GitHub account

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/kiwigpt.git
   cd kiwigpt
   ```

2. **Install Hugo** (if not already installed)
   ```bash
   # macOS
   brew install hugo
   
   # Windows
   choco install hugo-extended
   
   # Linux
   sudo apt-get install hugo
   ```

3. **Start the development server**
   ```bash
   hugo server -D
   ```

4. **Open your browser**
   Navigate to `http://localhost:1313`

### Creating Content

1. **Create a new post**
   ```bash
   hugo new posts/my-new-post.md
   ```

2. **Create a new page**
   ```bash
   hugo new pages/about.md
   ```

3. **Edit the front matter**
   ```markdown
   ---
   title: "My New Post"
   date: 2024-01-15T10:00:00+00:00
   draft: false
   description: "Description of your post"
   tags: ["tag1", "tag2"]
   categories: ["category"]
   ---
   ```

## 🚀 Deployment

This site is automatically deployed using GitHub Actions. Every push to the `main` branch triggers a new deployment.

### Manual Deployment

1. **Build the site**
   ```bash
   hugo --minify
   ```

2. **Deploy to GitHub Pages**
   - Push to the `main` branch
   - GitHub Actions will automatically build and deploy

## 📝 Content Guidelines

### Post Structure

- Use descriptive titles
- Include relevant tags and categories
- Write compelling descriptions
- Use proper Markdown formatting

### Images

- Store images in `assets/images/`
- Use descriptive filenames
- Optimize for web (compress if needed)

### SEO

- Include meta descriptions
- Use proper heading hierarchy
- Add alt text to images
- Include relevant keywords

## 🎨 Customization

### Theme Configuration

Edit `hugo.toml` to customize:
- Site title and description
- Social media links
- Menu items
- Theme parameters

### Styling

- Custom CSS: `assets/css/custom.css`
- Custom JS: `assets/js/custom.js`

## 🔧 Configuration

### Hugo Configuration (`hugo.toml`)

Key settings:
- `baseURL`: Your site URL
- `theme`: PaperMod
- `title`: Site title
- `params`: Theme parameters

### GitHub Pages

- Repository name: `kiwigpt`
- Branch: `main`
- Source: GitHub Actions
- Custom domain: `www.kiwigpt.co.nz`

## 📊 Analytics

Add Google Analytics or other tracking by editing the theme configuration.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- [Hugo](https://gohugo.io/) - Static site generator
- [PaperMod](https://github.com/adityatelange/hugo-PaperMod) - Beautiful theme
- [GitHub Pages](https://pages.github.com/) - Free hosting
- [GitHub Actions](https://github.com/features/actions) - CI/CD

---

Built with ❤️ using Hugo and PaperMod 