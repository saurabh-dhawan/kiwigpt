# Deployment Guide for www.kiwigpt.co.nz

## Domain Configuration

### 1. GitHub Repository Setup

1. Create a new repository on GitHub named `kiwigpt`
2. Push this code to the repository:
   ```bash
   git remote add origin https://github.com/yourusername/kiwigpt.git
   git add .
   git commit -m "Initial commit: Kiwigpt AI research blog"
   git push -u origin main
   ```

### 2. GitHub Pages Configuration

1. Go to your repository settings on GitHub
2. Navigate to "Pages" in the sidebar
3. Set source to "GitHub Actions"
4. Add custom domain: `www.kiwigpt.co.nz`
5. Check "Enforce HTTPS"

### 3. DNS Configuration

Configure your domain's DNS settings with your domain provider:

#### A Records:
```
@ -> 185.199.108.153
@ -> 185.199.109.153
@ -> 185.199.110.153
@ -> 185.199.111.153
```

#### CNAME Record:
```
www -> yourusername.github.io
```

### 4. Domain Verification

1. Create a file named `CNAME` in the `static/` directory:
   ```
   www.kiwigpt.co.nz
   ```

2. Add this to your `hugo.toml`:
   ```toml
   [params]
     customDomain = "www.kiwigpt.co.nz"
   ```

## Automated Deployment

The GitHub Actions workflow will automatically:
1. Build the Hugo site
2. Deploy to GitHub Pages
3. Use your custom domain

## Local Development

```bash
# Start development server
hugo server -D

# Build for production
hugo --minify

# Create new post
python scripts/markdown-client.py post "Your Post Title" --description "Description" --tags ai research
```

## Content Management

Use the markdown client for easy content creation:

```bash
# Create a new blog post
python scripts/markdown-client.py post "AI Paper Review" --tags ai research

# Create a new page
python scripts/markdown-client.py page "About" --description "About Kiwigpt"

# List all posts
python scripts/markdown-client.py list-posts

# Build the site
python scripts/markdown-client.py build
```

## SSL Certificate

GitHub Pages will automatically provision an SSL certificate for your custom domain once the DNS is properly configured.

## Troubleshooting

1. **Domain not working**: Check DNS propagation (can take up to 48 hours)
2. **HTTPS not working**: Ensure "Enforce HTTPS" is checked in GitHub Pages settings
3. **Build failures**: Check GitHub Actions logs for Hugo build errors
4. **Content not updating**: Clear browser cache or check if draft is set to false

## Monitoring

- Check deployment status in GitHub Actions tab
- Monitor site performance with Google Analytics
- Set up uptime monitoring for your domain 