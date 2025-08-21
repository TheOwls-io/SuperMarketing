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
        """
    )
    
    parser.add_argument(
        'command',
        nargs='?',
        default='help',
        choices=['install', 'update', 'uninstall', 'help', 'version'],
        help='Command to execute'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output'
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
  install     Install the framework (manual process for now)
  update      Update the framework (coming soon)
  uninstall   Remove the framework
  help        Show this help message
  version     Show version information

INSTALLATION:
  The automated installer is in development. For now, use manual installation:
  
  1. Clone the repository:
     git clone https://github.com/TheOwls-io/SuperMarketing.git
  
  2. Copy framework files to Claude directory:
     cp -r SuperMarketing/SuperMarketing_Framework/SuperMarketing ~/.claude/
  
  3. Use marketing commands in Claude Code:
     /sm:campaign, /sm:create, /sm:analyze, /sm:brand, etc.

FEATURES:
  • 17 Marketing Commands (/sm:*)
  • 11 Marketing Personas
  • Brand Context System
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


if __name__ == '__main__':
    main()