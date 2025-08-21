"""
SuperMarketing Brand Context System
Personalized brand data for customized marketing outputs
"""

import json
import os
from pathlib import Path

class BrandContext:
    """Manages brand context loading and activation"""
    
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.brands_dir = self.base_dir / 'brands'
        self.active_brand_file = self.base_dir / 'active_brand.json'
        self.active_brand = None
        self._load_active_brand()
    
    def _load_active_brand(self):
        """Load the currently active brand from config"""
        if self.active_brand_file.exists():
            with open(self.active_brand_file, 'r') as f:
                config = json.load(f)
                self.active_brand = config.get('active')
    
    def get_available_brands(self):
        """List all available brand profiles"""
        if not self.brands_dir.exists():
            return []
        return [d.name for d in self.brands_dir.iterdir() if d.is_dir()]
    
    def activate_brand(self, brand_name):
        """Activate a specific brand"""
        brand_path = self.brands_dir / brand_name
        if not brand_path.exists():
            raise ValueError(f"Brand '{brand_name}' not found")
        
        # Update active brand config
        config = {}
        if self.active_brand_file.exists():
            with open(self.active_brand_file, 'r') as f:
                config = json.load(f)
        
        config['active'] = brand_name
        config['available_brands'] = self.get_available_brands()
        
        with open(self.active_brand_file, 'w') as f:
            json.dump(config, f, indent=2)
        
        self.active_brand = brand_name
        return True
    
    def get_brand_data(self, brand_name=None):
        """Load all data for a brand"""
        if brand_name is None:
            brand_name = self.active_brand
        
        if brand_name is None:
            return None
        
        brand_path = self.brands_dir / brand_name
        if not brand_path.exists():
            return None
        
        data = {}
        
        # Load core brand files
        for file_name in ['brand.json', 'metrics.json', 'personas.json']:
            file_path = brand_path / file_name
            if file_path.exists():
                with open(file_path, 'r') as f:
                    data[file_name.replace('.json', '')] = json.load(f)
        
        return data

# Example brands included
EXAMPLE_BRANDS = [
    'example_tech_startup',
    'example_ecommerce'
]