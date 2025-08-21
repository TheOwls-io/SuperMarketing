# Brand Import Examples

## Using the Brand Scraper

The SuperMarketing framework includes a powerful brand scraper that can automatically extract brand information from any website.

### Basic Usage

```bash
# Import from a website
python3 -m SuperMarketing brand-import --url https://apple.com

# With custom brand name
python3 -m SuperMarketing brand-import --url https://apple.com --name "Apple Inc"
```

### Standalone Script Usage

```bash
# Direct script usage
python3 SuperMarketing/BrandContext/brand_scraper.py https://nike.com "Nike"
```

### What Gets Extracted

#### With Basic Extraction (No Dependencies)
- Domain name
- Brand name (from domain)
- Basic structure template
- Extraction notes and recommendations

#### With Full Extraction (beautifulsoup4, requests, cssutils installed)
- **Visual Identity**:
  - Primary and secondary colors from CSS
  - Font families (heading and body fonts)
  - Logo URL
  - Imagery style patterns

- **Messaging**:
  - Page title and tagline
  - Meta descriptions
  - Hero headlines
  - Value propositions
  - Key messages

- **Social Presence**:
  - Facebook, Twitter, LinkedIn, Instagram, YouTube links
  - Social proof elements
  - Testimonials (if found)

- **Technical Details**:
  - Open Graph metadata
  - Structured data
  - Schema.org information

### Example Output

After running the import, you'll get a `brand.json` file with this structure:

```json
{
  "name": "Nike",
  "domain": "nike.com",
  "positioning": {
    "statement": "Just Do It",
    "category": "Athletic Apparel & Footwear"
  },
  "visual_identity": {
    "primary_colors": ["#111111", "#FFFFFF"],
    "secondary_colors": ["#F5F5F5", "#757575"],
    "fonts": {
      "heading": "Helvetica Neue",
      "body": "Helvetica"
    }
  },
  "messaging": {
    "tagline": "Just Do It",
    "value_proposition": "Bringing inspiration and innovation to every athlete in the world"
  }
}
```

### Installation for Full Extraction

For best results, install the optional dependencies:

```bash
# Install extraction dependencies
pip install beautifulsoup4 requests cssutils

# For image analysis (future feature)
pip install pillow

# All at once
pip install beautifulsoup4 requests cssutils pillow
```

### Workflow Example

1. **Import from website**:
   ```bash
   python3 -m SuperMarketing brand-import --url https://yourbrand.com
   ```

2. **Review generated file**:
   ```bash
   cat SuperMarketing/BrandContext/brands/yourbrand/brand.json
   ```

3. **Edit and enhance**:
   - Add missing information
   - Refine extracted data
   - Add industry and company size
   - Define target audiences
   - List competitors

4. **Add metrics and personas**:
   - Copy from examples or create new
   - Add historical performance data
   - Define customer personas

5. **Deploy to Claude**:
   ```bash
   cp -r SuperMarketing/BrandContext/brands/yourbrand ~/.claude/SuperMarketing/BrandContext/brands/
   ```

6. **Activate in Claude Code**:
   ```
   /sm:brand activate yourbrand
   ```

### Advanced Usage

#### Batch Import Multiple Brands

Create a script to import multiple brands:

```python
#!/usr/bin/env python3
from SuperMarketing.BrandContext.brand_scraper import create_brand_from_url

brands = [
    ("https://apple.com", "Apple"),
    ("https://google.com", "Google"),
    ("https://amazon.com", "Amazon"),
]

for url, name in brands:
    print(f"Importing {name}...")
    create_brand_from_url(url, name)
```

#### Custom Extraction

Extend the BrandScraperAdvanced class for specific needs:

```python
from SuperMarketing.BrandContext.brand_scraper import BrandScraperAdvanced

class MyBrandScraper(BrandScraperAdvanced):
    def extract_custom_data(self):
        # Add your custom extraction logic
        pass
```

### Tips for Better Extraction

1. **Use the main domain**: Prefer `https://brand.com` over subpages
2. **Check multiple pages**: Home, About, and Brand pages often have different info
3. **Install dependencies**: Full extraction needs beautifulsoup4 and requests
4. **Manual review**: Always review and enhance the generated JSON
5. **Test first**: Try with example.com to see how it works

### Troubleshooting

**No data extracted**:
- Check if the URL is accessible
- Install beautifulsoup4 and requests for full extraction
- Try with --verbose flag for debug info

**Missing colors/fonts**:
- Some sites load CSS dynamically
- Try the main domain instead of subpages
- Manually add from browser inspector

**Wrong brand name**:
- Use --name flag to specify correct name
- Edit the generated JSON file

### Integration with Brand Context

Once imported, the brand data integrates with all SuperMarketing commands:

```bash
# Your brand's voice is now used in:
/sm:create email         # Uses brand voice and tone
/sm:campaign plan        # References brand positioning
/sm:analyze performance  # Compares to brand baselines
```

This makes every marketing output perfectly aligned with your brand!