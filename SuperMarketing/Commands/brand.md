# /sm:brand

Manage brand context for personalized marketing outputs.

## Usage
```
/sm:brand [action] [options]
```

## Actions

### Setup & Management
- `init` - Initialize brand directory structure
- `import <file>` - Import brand data from file
- `activate <brand>` - Switch to specified brand
- `deactivate` - Deactivate current brand
- `list` - Show all available brands
- `current` - Display currently active brand

### Validation & Analysis  
- `validate [brand]` - Check data completeness
- `analyze [brand]` - Analyze brand performance
- `compare <brand1> <brand2>` - Compare two brands
- `report [brand]` - Generate comprehensive brand report

### Data Operations
- `export [brand]` - Export brand data
- `backup [brand]` - Create brand backup
- `restore <backup>` - Restore from backup
- `update [field]` - Update specific brand data

## Options
- `--format` - Output format (json/markdown/table)
- `--include` - Specific data to include
- `--exclude` - Data to exclude
- `--output` - Output file path

## Examples

### Basic Setup
```
/sm:brand init
/sm:brand import company_brand.json
/sm:brand activate my_brand
```

### Brand Analysis
```
/sm:brand validate
/sm:brand analyze --include metrics,campaigns
/sm:brand report --format markdown
```

### Multi-Brand Management
```
/sm:brand list
/sm:brand compare brand_a brand_b
/sm:brand switch client_brand
```

## Brand Context Integration

When a brand is active, all marketing commands automatically use:
- Brand voice and tone
- Visual guidelines
- Performance baselines
- Customer personas
- Historical campaign data
- A/B test winners

## Data Structure

Brand data is stored in:
```
BrandContext/
└── brands/
    └── [brand_name]/
        ├── brand.json       # Core identity
        ├── metrics.json     # Performance data
        ├── personas.json    # Customer profiles
        ├── campaigns/       # Campaign history
        └── ab_tests/        # Test results
```

## Automatic Context Loading

Active brand data is available via:
- `@brand.voice` - Voice and tone
- `@brand.metrics` - Performance baselines
- `@brand.personas` - Customer personas
- `@brand.campaigns` - Past campaigns
- `@brand.tests` - A/B test results

## Best Practices

1. **Keep Data Current** - Update metrics monthly
2. **Document Learnings** - Add insights to campaigns
3. **Version Control** - Use git for brand evolution
4. **Validate Regularly** - Check data completeness

## Error Handling

Common issues:
- Invalid JSON: Run `validate` to check syntax
- Missing data: Use `report` to identify gaps
- Performance issues: Archive old campaigns

## Related Commands
- `/sm:campaign` - Uses brand campaign history
- `/sm:create` - Applies brand voice and visuals
- `/sm:analyze` - Compares to brand baselines
- `/sm:personalize` - Leverages brand personas