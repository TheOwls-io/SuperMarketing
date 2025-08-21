#!/usr/bin/env python3
"""
SuperMarketing CLI Entry Point
Currently provides manual installation instructions until automated installer is ready
"""

import sys
import os
import argparse
from pathlib import Path


def main():
    """Main entry point for SuperMarketing CLI"""
    parser = argparse.ArgumentParser(
        description='SuperMarketing Framework - Marketing automation for Claude Code',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  SuperMarketing install        # Install framework (coming soon)
  SuperMarketing help           # Show installation instructions
  SuperMarketing version        # Show version information
  SuperMarketing brand-import   # Import brand from URL
        """
    )
    
    parser.add_argument(
        'command',
        nargs='?',
        default='help',
        choices=['install', 'update', 'uninstall', 'help', 'version', 'brand-import'],
        help='Command to execute'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output'
    )
    
    # Brand import arguments
    parser.add_argument(
        '--url',
        type=str,
        help='URL to import brand from'
    )
    
    parser.add_argument(
        '--name',
        type=str,
        help='Brand name (optional, extracted from domain if not provided)'
    )
    
    args = parser.parse_args()
    
    if args.command == 'version':
        print_version()
    elif args.command == 'help':
        print_help()
    elif args.command == 'install':
        print_install_instructions()
    elif args.command == 'update':
        print("Update functionality coming soon. For now, use manual installation.")
        print_install_instructions()
    elif args.command == 'uninstall':
        print_uninstall_instructions()
    elif args.command == 'brand-import':
        import_brand_from_url(args)
    else:
        parser.print_help()


def print_version():
    """Print version information"""
    version_file = Path(__file__).parent.parent / 'VERSION'
    if version_file.exists():
        version = version_file.read_text().strip()
    else:
        version = '1.0.0'
    
    print(f"SuperMarketing Framework v{version}")
    print("Marketing automation and optimization for Claude Code")
    print("https://github.com/TheOwls-io/SuperMarketing")


def print_help():
    """Print help information"""
    print("""
SuperMarketing Framework - Marketing Automation for Claude Code
==============================================================

SuperMarketing transforms Claude Code into a comprehensive marketing assistant
with specialized personas, campaign management tools, and brand context.

COMMANDS:
  install       Install the framework (manual process for now)
  update        Update the framework (coming soon)
  uninstall     Remove the framework
  brand-import  Import brand from website URL
  help          Show this help message
  version       Show version information

INSTALLATION:
  The automated installer is in development. For now, use manual installation:
  
  1. Clone the repository:
     git clone https://github.com/TheOwls-io/SuperMarketing.git
  
  2. Copy framework files to Claude directory:
     cp -r SuperMarketing/SuperMarketing_Framework/SuperMarketing ~/.claude/
  
  3. Use marketing commands in Claude Code:
     /sm:campaign, /sm:create, /sm:analyze, /sm:brand, etc.

BRAND IMPORT:
  Import brand configuration from a website:
  
  python3 -m SuperMarketing brand-import --url https://example.com
  python3 -m SuperMarketing brand-import --url https://example.com --name "Brand Name"

FEATURES:
  • 17 Marketing Commands (/sm:*)
  • 11 Marketing Personas
  • Brand Context System
  • Automatic Brand Import from URL
  • Campaign Management
  • Content Creation
  • Analytics & Reporting

DOCUMENTATION:
  https://github.com/TheOwls-io/SuperMarketing

SUPPORT:
  Report issues at: https://github.com/TheOwls-io/SuperMarketing/issues
    """)


def print_install_instructions():
    """Print installation instructions"""
    print("""
SuperMarketing Installation Instructions
========================================

The automated installer is currently in development. 
Please use the manual installation process:

1. CLONE THE REPOSITORY:
   git clone https://github.com/TheOwls-io/SuperMarketing.git
   cd SuperMarketing/SuperMarketing_Framework

2. INSTALL DEPENDENCIES:
   pip install -r requirements.txt

3. COPY FRAMEWORK FILES:
   mkdir -p ~/.claude/SuperMarketing
   cp -r SuperMarketing ~/.claude/

4. VERIFY INSTALLATION:
   ls -la ~/.claude/SuperMarketing/

5. USE IN CLAUDE CODE:
   The framework will be automatically loaded by Claude Code.
   Use commands like:
   - /sm:campaign plan
   - /sm:create email
   - /sm:analyze performance
   - /sm:brand activate

BRAND CONTEXT SETUP (Optional):
   1. Navigate to ~/.claude/SuperMarketing/BrandContext/brands/
   2. Create a folder for your brand
   3. Add brand.json, metrics.json, and personas.json
   4. Activate with: /sm:brand activate your_brand

For more information, visit:
https://github.com/TheOwls-io/SuperMarketing
    """)


def print_uninstall_instructions():
    """Print uninstall instructions"""
    print("""
SuperMarketing Uninstall Instructions
=====================================

To remove SuperMarketing from your system:

1. REMOVE FRAMEWORK FILES:
   rm -rf ~/.claude/SuperMarketing

2. REMOVE PYTHON PACKAGE (if installed):
   pip uninstall supermarketing

3. VERIFY REMOVAL:
   ls -la ~/.claude/

The framework has been removed. You can reinstall at any time
by following the installation instructions.
    """)


def import_brand_from_url(args):
    """Import brand configuration from a URL"""
    if not args.url:
        print("\n❌ Error: URL is required for brand import")
        print("\nUsage:")
        print("  python3 -m SuperMarketing brand-import --url https://example.com")
        print("  python3 -m SuperMarketing brand-import --url https://example.com --name 'Brand Name'")
        return
    
    try:
        from SuperMarketing.BrandContext.brand_scraper import create_brand_from_url
        
        print(f"\n🔍 Analyzing website: {args.url}")
        print("=" * 50)
        
        # Import the brand
        output_path = create_brand_from_url(args.url, args.name)
        
        print("\n📋 Next Steps:")
        print("1. Review and edit the generated brand.json file")
        print(f"   Location: {output_path}")
        print("2. Add metrics.json and personas.json for complete profile")
        print("3. Copy to ~/.claude/SuperMarketing/BrandContext/brands/")
        print("4. Activate in Claude Code with: /sm:brand activate <brand_name>")
        
        print("\n💡 Tip: For better extraction, install:")
        print("   pip install beautifulsoup4 requests cssutils")
        
    except ImportError as e:
        print(f"\n❌ Import error: {e}")
        print("\nThe brand scraper module requires the SuperMarketing package to be properly installed.")
        print("Make sure you're in the SuperMarketing_Framework directory.")
    except Exception as e:
        print(f"\n❌ Error importing brand: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()


if __name__ == '__main__':
    main()