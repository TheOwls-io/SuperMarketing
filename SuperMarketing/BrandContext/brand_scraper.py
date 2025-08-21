#!/usr/bin/env python3
"""
Brand Scraper Module
Extracts brand information from websites to create brand.json
"""

import json
import re
from urllib.parse import urlparse, urljoin
from pathlib import Path
from typing import Dict, List, Optional, Any
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BrandScraper:
    """Scrapes brand information from websites"""
    
    def __init__(self):
        self.brand_data = self._get_template()
        
    def _get_template(self) -> Dict[str, Any]:
        """Get the brand.json template structure"""
        return {
            "name": "",
            "domain": "",
            "industry": "",
            "established": "",
            "company_size": "",
            
            "positioning": {
                "statement": "",
                "category": "",
                "differentiators": []
            },
            
            "brand_personality": {
                "archetype": "",
                "traits": [],
                "values": []
            },
            
            "voice_and_tone": {
                "voice": "",
                "principles": [],
                "tone_variations": {
                    "social_media": "",
                    "email": "",
                    "website": "",
                    "ads": ""
                },
                "vocabulary": {
                    "use": [],
                    "avoid": []
                }
            },
            
            "visual_identity": {
                "primary_colors": [],
                "secondary_colors": [],
                "fonts": {
                    "heading": "",
                    "body": ""
                },
                "logo_usage": "",
                "imagery_style": ""
            },
            
            "target_audience": {
                "primary": {
                    "description": "",
                    "demographics": "",
                    "psychographics": "",
                    "pain_points": [],
                    "goals": []
                },
                "secondary": {
                    "description": "",
                    "demographics": "",
                    "psychographics": "",
                    "pain_points": [],
                    "goals": []
                }
            },
            
            "competitors": [],
            
            "messaging": {
                "tagline": "",
                "value_proposition": "",
                "elevator_pitch": "",
                "key_messages": {
                    "primary": "",
                    "supporting": []
                }
            }
        }
    
    def scrape_from_url(self, url: str) -> Dict[str, Any]:
        """
        Scrape brand information from a URL
        Note: This is a simplified version that would need beautifulsoup4 and requests
        """
        try:
            # Parse the URL
            parsed = urlparse(url)
            domain = parsed.netloc.replace('www.', '')
            
            # Set basic info
            self.brand_data['domain'] = domain
            self.brand_data['name'] = self._extract_brand_name(domain)
            
            # In a real implementation, we would:
            # 1. Fetch the HTML with requests
            # 2. Parse with BeautifulSoup
            # 3. Extract various elements
            
            # For now, return a template with instructions
            self.brand_data['_extraction_notes'] = {
                "status": "template",
                "message": "To enable full extraction, install: pip install beautifulsoup4 requests cssutils",
                "manual_review_needed": [
                    "Industry classification",
                    "Company size",
                    "Target audience details",
                    "Competitor identification",
                    "Brand personality assessment"
                ],
                "auto_extractable": [
                    "Domain and basic info",
                    "Meta tags (description, keywords)",
                    "Colors from CSS",
                    "Fonts from CSS",
                    "Images and logos",
                    "Social media links",
                    "Contact information"
                ]
            }
            
            return self.brand_data
            
        except Exception as e:
            logger.error(f"Error scraping {url}: {e}")
            return self.brand_data
    
    def _extract_brand_name(self, domain: str) -> str:
        """Extract brand name from domain"""
        # Remove TLD
        name = domain.split('.')[0]
        # Convert to title case
        name = name.replace('-', ' ').replace('_', ' ').title()
        return name
    
    def extract_colors(self, css_content: str) -> List[str]:
        """Extract color values from CSS"""
        colors = []
        
        # Hex colors
        hex_pattern = r'#(?:[0-9a-fA-F]{3}){1,2}\b'
        hex_colors = re.findall(hex_pattern, css_content)
        colors.extend(hex_colors[:10])  # Limit to top 10
        
        # RGB colors
        rgb_pattern = r'rgb\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*\)'
        rgb_colors = re.findall(rgb_pattern, css_content)
        colors.extend(rgb_colors[:5])
        
        return list(set(colors))  # Remove duplicates
    
    def extract_fonts(self, css_content: str) -> Dict[str, str]:
        """Extract font families from CSS"""
        fonts = {
            "heading": "",
            "body": ""
        }
        
        # Font-family declarations
        font_pattern = r'font-family:\s*([^;]+);'
        font_families = re.findall(font_pattern, css_content)
        
        if font_families:
            # Clean up font names
            cleaned_fonts = []
            for font_string in font_families[:10]:  # Check first 10
                # Remove quotes and fallbacks
                font = font_string.split(',')[0].strip().strip('"\'')
                if font and font not in ['inherit', 'initial', 'unset']:
                    cleaned_fonts.append(font)
            
            if cleaned_fonts:
                fonts["heading"] = cleaned_fonts[0]
                fonts["body"] = cleaned_fonts[1] if len(cleaned_fonts) > 1 else cleaned_fonts[0]
        
        return fonts
    
    def extract_meta_info(self, html_content: str) -> Dict[str, str]:
        """Extract meta information from HTML"""
        meta_info = {}
        
        # Title
        title_match = re.search(r'<title>([^<]+)</title>', html_content, re.IGNORECASE)
        if title_match:
            meta_info['title'] = title_match.group(1).strip()
        
        # Meta description
        desc_pattern = r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']'
        desc_match = re.search(desc_pattern, html_content, re.IGNORECASE)
        if desc_match:
            meta_info['description'] = desc_match.group(1).strip()
        
        # Open Graph tags
        og_pattern = r'<meta\s+property=["\']og:(\w+)["\']\s+content=["\'](.*?)["\']'
        og_matches = re.findall(og_pattern, html_content, re.IGNORECASE)
        for prop, content in og_matches:
            meta_info[f'og_{prop}'] = content
        
        return meta_info
    
    def save_brand_config(self, brand_name: str, output_dir: Optional[Path] = None) -> Path:
        """Save the brand configuration to a JSON file"""
        if output_dir is None:
            output_dir = Path(__file__).parent / 'brands' / brand_name.lower().replace(' ', '_')
        
        output_dir.mkdir(parents=True, exist_ok=True)
        output_file = output_dir / 'brand.json'
        
        with open(output_file, 'w') as f:
            json.dump(self.brand_data, f, indent=2)
        
        logger.info(f"Brand configuration saved to {output_file}")
        return output_file


class BrandScraperAdvanced(BrandScraper):
    """
    Advanced brand scraper with full extraction capabilities
    Requires: pip install beautifulsoup4 requests cssutils pillow
    """
    
    def __init__(self):
        super().__init__()
        self.session = None
        self.soup = None
        
    def scrape_from_url_advanced(self, url: str) -> Dict[str, Any]:
        """Full extraction with external libraries"""
        try:
            import requests
            from bs4 import BeautifulSoup
            import cssutils
            
            # Fetch the page
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            # Parse HTML
            self.soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract various elements
            self._extract_basic_info(url)
            self._extract_visual_identity()
            self._extract_messaging()
            self._extract_social_proof()
            
            return self.brand_data
            
        except ImportError:
            logger.warning("Advanced scraping requires: pip install beautifulsoup4 requests cssutils")
            return self.scrape_from_url(url)
        except Exception as e:
            logger.error(f"Error in advanced scraping: {e}")
            return self.scrape_from_url(url)
    
    def _extract_basic_info(self, url: str):
        """Extract basic brand information"""
        # Domain
        parsed = urlparse(url)
        self.brand_data['domain'] = parsed.netloc.replace('www.', '')
        
        # Title/Name
        title_tag = self.soup.find('title')
        if title_tag:
            title = title_tag.text.strip()
            # Often format is "Brand Name | Tagline" or "Brand Name - Description"
            if '|' in title:
                parts = title.split('|')
                self.brand_data['name'] = parts[0].strip()
                self.brand_data['messaging']['tagline'] = parts[1].strip()
            elif '-' in title:
                parts = title.split('-')
                self.brand_data['name'] = parts[0].strip()
            else:
                self.brand_data['name'] = title
        
        # Meta description
        meta_desc = self.soup.find('meta', attrs={'name': 'description'})
        if meta_desc and meta_desc.get('content'):
            self.brand_data['messaging']['value_proposition'] = meta_desc['content']
        
        # Open Graph data
        og_site = self.soup.find('meta', property='og:site_name')
        if og_site and og_site.get('content'):
            self.brand_data['name'] = og_site['content']
    
    def _extract_visual_identity(self):
        """Extract visual elements like colors and fonts"""
        # Get all stylesheets
        styles = []
        
        # Inline styles
        for style in self.soup.find_all('style'):
            styles.append(style.string or '')
        
        # External stylesheets (would need to fetch these)
        for link in self.soup.find_all('link', rel='stylesheet'):
            # In production, fetch and parse external CSS
            pass
        
        all_css = '\n'.join(styles)
        
        # Extract colors
        colors = self.extract_colors(all_css)
        if colors:
            self.brand_data['visual_identity']['primary_colors'] = colors[:3]
            self.brand_data['visual_identity']['secondary_colors'] = colors[3:6]
        
        # Extract fonts
        fonts = self.extract_fonts(all_css)
        if fonts:
            self.brand_data['visual_identity']['fonts'] = fonts
        
        # Logo
        logo_img = (
            self.soup.find('img', class_=re.compile('logo', re.I)) or
            self.soup.find('img', id=re.compile('logo', re.I)) or
            self.soup.find('img', alt=re.compile('logo', re.I))
        )
        if logo_img and logo_img.get('src'):
            self.brand_data['visual_identity']['logo_url'] = urljoin(self.brand_data['domain'], logo_img['src'])
    
    def _extract_messaging(self):
        """Extract messaging and content"""
        # Hero/headline text
        hero_selectors = ['h1', '.hero-title', '.headline', '.hero h1', '.banner h1']
        for selector in hero_selectors:
            hero = self.soup.select_one(selector)
            if hero:
                text = hero.get_text(strip=True)
                if text and len(text) < 200:  # Reasonable length for headline
                    self.brand_data['messaging']['key_messages']['primary'] = text
                    break
        
        # Tagline/subtitle
        subtitle_selectors = ['.tagline', '.subtitle', '.hero-subtitle', 'h2', '.hero p']
        for selector in subtitle_selectors:
            subtitle = self.soup.select_one(selector)
            if subtitle:
                text = subtitle.get_text(strip=True)
                if text and 10 < len(text) < 150:
                    if not self.brand_data['messaging']['tagline']:
                        self.brand_data['messaging']['tagline'] = text
                    break
    
    def _extract_social_proof(self):
        """Extract social links and proof elements"""
        social_platforms = {
            'facebook': ['facebook.com', 'fb.com'],
            'twitter': ['twitter.com', 'x.com'],
            'linkedin': ['linkedin.com'],
            'instagram': ['instagram.com'],
            'youtube': ['youtube.com']
        }
        
        social_links = {}
        for link in self.soup.find_all('a', href=True):
            href = link['href'].lower()
            for platform, domains in social_platforms.items():
                if any(domain in href for domain in domains):
                    social_links[platform] = link['href']
                    break
        
        if social_links:
            self.brand_data['social_presence'] = social_links
        
        # Look for testimonials, reviews, etc.
        testimonial_keywords = ['testimonial', 'review', 'customer', 'client']
        testimonials = []
        for keyword in testimonial_keywords:
            elements = self.soup.find_all(class_=re.compile(keyword, re.I))
            for elem in elements[:3]:  # Limit to first 3
                text = elem.get_text(strip=True)
                if 20 < len(text) < 500:  # Reasonable testimonial length
                    testimonials.append(text)
        
        if testimonials:
            self.brand_data['social_proof'] = testimonials[:3]


def create_brand_from_url(url: str, brand_name: Optional[str] = None) -> Path:
    """
    Main function to create a brand config from a URL
    
    Args:
        url: Website URL to scrape
        brand_name: Optional brand name (extracted from domain if not provided)
    
    Returns:
        Path to the created brand.json file
    """
    scraper = BrandScraperAdvanced()
    
    # Try advanced scraping first, fall back to basic
    brand_data = scraper.scrape_from_url_advanced(url)
    
    # Use provided name or extracted name
    if brand_name:
        brand_data['name'] = brand_name
    elif not brand_data.get('name'):
        parsed = urlparse(url)
        brand_data['name'] = parsed.netloc.replace('www.', '').split('.')[0].title()
    
    # Save the configuration
    safe_name = brand_data['name'].lower().replace(' ', '_').replace('.', '')
    output_path = scraper.save_brand_config(safe_name)
    
    print(f"\n✅ Brand configuration created: {output_path}")
    print(f"   Brand: {brand_data['name']}")
    print(f"   Domain: {brand_data['domain']}")
    
    if brand_data.get('_extraction_notes'):
        print("\n📝 Note: Basic extraction completed.")
        print("   For full extraction, install: pip install beautifulsoup4 requests cssutils")
        print("   Manual review recommended for:")
        for item in brand_data['_extraction_notes'].get('manual_review_needed', []):
            print(f"   - {item}")
    
    return output_path


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python brand_scraper.py <url> [brand_name]")
        print("Example: python brand_scraper.py https://example.com 'Example Brand'")
        sys.exit(1)
    
    url = sys.argv[1]
    brand_name = sys.argv[2] if len(sys.argv) > 2 else None
    
    create_brand_from_url(url, brand_name)