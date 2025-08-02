#!/usr/bin/env python3
"""
Kiwigpt Markdown Client
A simple CLI tool for managing Hugo content with Markdown files.
"""

import os
import sys
import argparse
from datetime import datetime
from pathlib import Path

class KiwigptMarkdownClient:
    def __init__(self, content_dir="content"):
        self.content_dir = Path(content_dir)
        self.posts_dir = self.content_dir / "posts"
        self.pages_dir = self.content_dir / "pages"
        
        # Ensure directories exist
        self.posts_dir.mkdir(parents=True, exist_ok=True)
        self.pages_dir.mkdir(parents=True, exist_ok=True)
    
    def create_post(self, title, description="", tags=None, categories=None, draft=True):
        """Create a new blog post."""
        if tags is None:
            tags = []
        if categories is None:
            categories = ["general"]
        
        # Create filename from title
        filename = title.lower().replace(" ", "-").replace("'", "").replace('"', "")
        filename = "".join(c for c in filename if c.isalnum() or c == "-")
        filepath = self.posts_dir / f"{filename}.md"
        
        # Create front matter
        front_matter = f"""---
title: "{title}"
date: {datetime.now().strftime('%Y-%m-%dT%H:%M:%S+00:00')}
draft: {str(draft).lower()}
description: "{description}"
tags: {tags}
categories: {categories}
author: "Kiwigpt"
showToc: true
TocOpen: false
hidemeta: false
comments: false
canonicalURL: "https://kiwigpt.github.io/posts/{filename}/"
disableHLJS: false
disableShare: false
hideSummary: false
searchHidden: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
ShowRssButtonInSectionTermList: true
UseHugoToc: true
---

# {title}

{description}

## Introduction

Start your post here...

## Main Content

Add your main content here...

## Conclusion

Wrap up your thoughts here...

---

*Published on {datetime.now().strftime('%B %d, %Y')}*
"""
        
        # Write the file
        with open(filepath, 'w') as f:
            f.write(front_matter)
        
        print(f"✅ Created new post: {filepath}")
        print(f"📝 Edit the file to add your content")
        return filepath
    
    def create_page(self, title, description=""):
        """Create a new static page."""
        filename = title.lower().replace(" ", "-").replace("'", "").replace('"', "")
        filename = "".join(c for c in filename if c.isalnum() or c == "-")
        filepath = self.pages_dir / f"{filename}.md"
        
        front_matter = f"""---
title: "{title}"
date: {datetime.now().strftime('%Y-%m-%dT%H:%M:%S+00:00')}
draft: false
description: "{description}"
---

# {title}

{description}

## Content

Add your page content here...

---
"""
        
        with open(filepath, 'w') as f:
            f.write(front_matter)
        
        print(f"✅ Created new page: {filepath}")
        return filepath
    
    def list_posts(self):
        """List all blog posts."""
        posts = list(self.posts_dir.glob("*.md"))
        if not posts:
            print("📝 No posts found")
            return
        
        print("📝 Blog Posts:")
        for post in sorted(posts):
            with open(post, 'r') as f:
                content = f.read()
                # Extract title from front matter
                lines = content.split('\n')
                title = "Untitled"
                for line in lines:
                    if line.startswith('title:'):
                        title = line.split('title:')[1].strip().strip('"')
                        break
            print(f"  - {post.name}: {title}")
    
    def list_pages(self):
        """List all static pages."""
        pages = list(self.pages_dir.glob("*.md"))
        if not pages:
            print("📄 No pages found")
            return
        
        print("📄 Static Pages:")
        for page in sorted(pages):
            with open(page, 'r') as f:
                content = f.read()
                lines = content.split('\n')
                title = "Untitled"
                for line in lines:
                    if line.startswith('title:'):
                        title = line.split('title:')[1].strip().strip('"')
                        break
            print(f"  - {page.name}: {title}")
    
    def build_site(self):
        """Build the Hugo site."""
        print("🔨 Building Hugo site...")
        os.system("hugo --minify")
        print("✅ Site built successfully!")
    
    def serve_site(self):
        """Serve the Hugo site locally."""
        print("🚀 Starting Hugo server...")
        print("📱 Open http://localhost:1313 in your browser")
        os.system("hugo server -D")

def main():
    parser = argparse.ArgumentParser(description="Kiwigpt Markdown Client")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Create post command
    post_parser = subparsers.add_parser("post", help="Create a new blog post")
    post_parser.add_argument("title", help="Post title")
    post_parser.add_argument("--description", "-d", default="", help="Post description")
    post_parser.add_argument("--tags", "-t", nargs="+", default=[], help="Post tags")
    post_parser.add_argument("--categories", "-c", nargs="+", default=["general"], help="Post categories")
    post_parser.add_argument("--publish", "-p", action="store_true", help="Publish immediately (not draft)")
    
    # Create page command
    page_parser = subparsers.add_parser("page", help="Create a new static page")
    page_parser.add_argument("title", help="Page title")
    page_parser.add_argument("--description", "-d", default="", help="Page description")
    
    # List commands
    subparsers.add_parser("list-posts", help="List all blog posts")
    subparsers.add_parser("list-pages", help="List all static pages")
    
    # Build and serve commands
    subparsers.add_parser("build", help="Build the Hugo site")
    subparsers.add_parser("serve", help="Serve the Hugo site locally")
    
    args = parser.parse_args()
    
    client = KiwigptMarkdownClient()
    
    if args.command == "post":
        client.create_post(
            args.title,
            args.description,
            args.tags,
            args.categories,
            not args.publish
        )
    elif args.command == "page":
        client.create_page(args.title, args.description)
    elif args.command == "list-posts":
        client.list_posts()
    elif args.command == "list-pages":
        client.list_pages()
    elif args.command == "build":
        client.build_site()
    elif args.command == "serve":
        client.serve_site()
    else:
        parser.print_help()

if __name__ == "__main__":
    main() 