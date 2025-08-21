#!/usr/bin/env python3
"""
SuperMarketing Framework Setup
Marketing automation and optimization framework for Claude Code
"""

from setuptools import setup, find_packages
import os

# Read the README for long description
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read version
with open(os.path.join(here, 'VERSION'), encoding='utf-8') as f:
    version = f.read().strip()

setup(
    name='supermarketing',
    version=version,
    description='AI-powered marketing automation framework for Claude Code',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='The Owls',
    author_email='contact@theowls.io',
    url='https://github.com/TheOwls-io/SuperMarketing',
    project_urls={
        'Bug Reports': 'https://github.com/TheOwls-io/SuperMarketing/issues',
        'Source': 'https://github.com/TheOwls-io/SuperMarketing',
        'Documentation': 'https://github.com/TheOwls-io/SuperMarketing/blob/main/README.md',
    },
    
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'SuperMarketing': [
            'Core/*.md',
            'Commands/*.md',
            'BrandContext/*.md',
            'BrandContext/*.json',
            'BrandContext/brands/**/*.json',
            'Templates/**/*',
        ],
        'setup': ['**/*.json'],
        'profiles': ['*.json'],
    },
    
    python_requires='>=3.8',
    install_requires=[
        'setuptools>=65.0.0',
    ],
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'black>=22.0.0',
            'flake8>=5.0.0',
        ],
    },
    
    entry_points={
        'console_scripts': [
            'SuperMarketing=SuperMarketing.__main__:main',
            'supermarketing=SuperMarketing.__main__:main',
        ],
    },
    
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Marketing',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Marketing :: Automation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
    ],
    
    keywords='marketing automation claude ai framework campaigns analytics',
)