# Brand Context System

The Brand Context System enables SuperMarketing to deliver highly customized, brand-specific marketing outputs by leveraging your brand's unique data, guidelines, and historical performance.

## Overview

Drop your brand information into the BrandContext directory and SuperMarketing automatically customizes all outputs to match your brand's voice, style, and proven strategies.

## Directory Structure

```
BrandContext/
├── active_brand.json          # Current active brand configuration
├── BRAND_CONTEXT.md           # This documentation
└── brands/                    # Individual brand profiles
    └── your_brand_name/
        ├── brand.json         # Core brand identity
        ├── metrics.json       # Performance baselines
        ├── personas.json      # Customer personas
        ├── campaigns/         # Past campaign data
        ├── ab_tests/          # A/B test results
        └── assets/            # Brand guidelines & assets
```

## Quick Start

1. **Create Your Brand Directory**
   ```bash
   mkdir -p BrandContext/brands/your_brand_name
   ```

2. **Add Core Brand Data**
   Copy example templates from `example_tech_startup/` or `example_ecommerce/`

3. **Activate Your Brand**
   ```
   /sm:brand activate your_brand_name
   ```

4. **Use Any Command**
   All commands now use your brand context automatically!

## Data Schemas

### brand.json - Core Identity

```json
{
  "name": "Your Brand Name",
  "domain": "yourbrand.com",
  "industry": "Technology/Retail/Finance/etc",
  "established": "2020",
  "company_size": "50-200",
  
  "positioning": {
    "statement": "The leading solution for...",
    "category": "Premium/Value/Innovation Leader",
    "differentiators": [
      "Unique feature or approach",
      "Key competitive advantage"
    ]
  },
  
  "brand_personality": {
    "archetype": "Hero/Sage/Explorer/etc",
    "traits": ["Innovative", "Trustworthy", "Bold"],
    "values": ["Customer First", "Innovation", "Integrity"]
  },
  
  "voice_and_tone": {
    "voice": "Professional yet approachable",
    "principles": [
      "Clear and concise",
      "Action-oriented",
      "Empathetic"
    ],
    "tone_variations": {
      "social_media": "Casual, engaging, conversational",
      "email": "Personal, helpful, warm",
      "website": "Clear, authoritative, inspiring",
      "ads": "Bold, benefit-focused, urgent"
    },
    "vocabulary": {
      "use": ["innovate", "transform", "empower"],
      "avoid": ["cheap", "try", "maybe"]
    }
  },
  
  "visual_identity": {
    "primary_colors": ["#1E40AF", "#3B82F6"],
    "secondary_colors": ["#6B7280", "#F3F4F6"],
    "fonts": {
      "heading": "Inter Bold",
      "body": "Inter Regular"
    },
    "logo_usage": "Always maintain 20px clearance",
    "imagery_style": "Modern, minimalist, tech-forward"
  },
  
  "target_audience": {
    "primary": {
      "description": "Tech-savvy professionals",
      "demographics": "25-45, urban, college-educated",
      "psychographics": "Early adopters, value efficiency",
      "pain_points": ["Time management", "Scaling challenges"],
      "goals": ["Productivity", "Growth", "Innovation"]
    },
    "secondary": {
      "description": "Small business owners",
      "demographics": "30-55, diverse locations",
      "psychographics": "Pragmatic, cost-conscious",
      "pain_points": ["Limited resources", "Competition"],
      "goals": ["Efficiency", "ROI", "Simplicity"]
    }
  },
  
  "competitors": [
    {
      "name": "Competitor A",
      "strengths": ["Market share", "Brand recognition"],
      "weaknesses": ["Price", "Complexity"],
      "our_advantage": "Better UX at lower cost"
    }
  ],
  
  "messaging": {
    "tagline": "Your Success, Simplified",
    "value_proposition": "The only platform that combines X, Y, and Z",
    "elevator_pitch": "We help businesses... by providing... unlike competitors who...",
    "key_messages": {
      "primary": "Transform your workflow",
      "supporting": [
        "Save 10 hours per week",
        "Trusted by 10,000+ businesses"
      ]
    }
  }
}
```

### metrics.json - Performance Baselines

```json
{
  "email_marketing": {
    "benchmarks": {
      "open_rate": 0.22,
      "click_rate": 0.035,
      "conversion_rate": 0.025,
      "unsubscribe_rate": 0.002
    },
    "best_practices": {
      "subject_line_length": "30-50 chars",
      "preview_text_length": "35-90 chars",
      "optimal_send_times": [
        "Tuesday 10am",
        "Thursday 2pm"
      ],
      "frequency": "2-3 per week"
    },
    "top_performing": {
      "subject_patterns": [
        "[Number] ways to [benefit]",
        "How [customer] achieved [result]"
      ],
      "cta_text": ["Get Started", "Learn More"]
    }
  },
  
  "social_media": {
    "platform_performance": {
      "linkedin": {
        "engagement_rate": 0.045,
        "best_post_times": ["Tuesday 9am", "Wednesday 3pm"],
        "content_mix": {
          "educational": 0.4,
          "promotional": 0.2,
          "thought_leadership": 0.3,
          "company_culture": 0.1
        }
      },
      "twitter": {
        "engagement_rate": 0.025,
        "best_post_times": ["Weekdays 8am", "Lunch hours"],
        "optimal_thread_length": "3-5 tweets"
      }
    }
  },
  
  "paid_advertising": {
    "google_ads": {
      "avg_cpc": 2.50,
      "avg_ctr": 0.035,
      "conversion_rate": 0.03,
      "quality_score": 7.5
    },
    "facebook_ads": {
      "avg_cpm": 12.00,
      "avg_ctr": 0.015,
      "conversion_rate": 0.02
    },
    "top_performing_angles": [
      "Problem/solution",
      "Social proof",
      "Limited time offers"
    ]
  },
  
  "website": {
    "conversion_rates": {
      "homepage_to_signup": 0.05,
      "landing_page_avg": 0.15,
      "blog_to_conversion": 0.02
    },
    "engagement": {
      "avg_session_duration": "2:30",
      "pages_per_session": 3.2,
      "bounce_rate": 0.45
    }
  },
  
  "content_marketing": {
    "blog_performance": {
      "avg_read_time": "4:30",
      "social_shares": 25,
      "conversion_rate": 0.015
    },
    "top_topics": [
      "How-to guides",
      "Industry trends",
      "Case studies"
    ],
    "optimal_length": {
      "blog_post": "1500-2500 words",
      "social_post": "100-250 chars",
      "email": "150-200 words"
    }
  }
}
```

### personas.json - Customer Personas

```json
{
  "personas": [
    {
      "id": "tech_executive",
      "name": "Tech Executive Tom",
      "role": "VP of Engineering",
      "company_size": "100-500 employees",
      
      "demographics": {
        "age": "35-45",
        "income": "$150k-250k",
        "education": "Bachelor's/Master's in CS",
        "location": "Major tech hubs"
      },
      
      "psychographics": {
        "personality": "Analytical, decisive, innovative",
        "values": ["Efficiency", "Innovation", "Team success"],
        "lifestyle": "Busy, tech-savvy, continuous learner"
      },
      
      "pain_points": [
        "Scaling development team",
        "Managing technical debt",
        "Staying current with technology",
        "Budget constraints"
      ],
      
      "goals": [
        "Improve team productivity by 30%",
        "Reduce deployment time",
        "Enhance code quality"
      ],
      
      "objections": [
        "Implementation complexity",
        "Team adoption challenges",
        "ROI uncertainty"
      ],
      
      "preferred_channels": [
        "Email",
        "LinkedIn",
        "Technical blogs",
        "Webinars"
      ],
      
      "content_preferences": {
        "formats": ["White papers", "Case studies", "Technical demos"],
        "topics": ["Best practices", "ROI studies", "Implementation guides"],
        "tone": "Technical but accessible"
      },
      
      "buying_journey": {
        "awareness": "Searches for solutions to specific problems",
        "consideration": "Compares features, reads reviews, requests demos",
        "decision": "Involves team, runs pilot, negotiates terms",
        "trigger_events": ["New funding", "Team growth", "Failed project"]
      },
      
      "messaging_angles": [
        "Reduce complexity",
        "Proven ROI",
        "Industry leaders trust us",
        "Easy team adoption"
      ]
    }
  ]
}
```

### Campaign Data Structure

Store past campaigns in `campaigns/` directory:

```json
{
  "campaign_id": "2024_q1_product_launch",
  "name": "Spring Product Launch",
  "date_range": "2024-01-15 to 2024-02-15",
  "budget": 50000,
  "channels": ["email", "social", "paid_search"],
  
  "objectives": {
    "primary": "Generate 500 qualified leads",
    "secondary": ["Increase brand awareness", "Drive trial signups"]
  },
  
  "results": {
    "leads_generated": 623,
    "cost_per_lead": 80.25,
    "conversion_rate": 0.035,
    "roi": 2.4
  },
  
  "performance_by_channel": {
    "email": {
      "sent": 50000,
      "opens": 11000,
      "clicks": 550,
      "conversions": 125
    },
    "social": {
      "impressions": 500000,
      "engagements": 5000,
      "clicks": 750,
      "conversions": 198
    }
  },
  
  "top_performing_elements": {
    "subject_lines": ["Limited time: 50% off", "Last chance to save"],
    "ad_copy": ["Transform your business today"],
    "visuals": ["product_hero_blue.jpg"],
    "landing_pages": ["sprint-offer-v2"]
  },
  
  "learnings": [
    "Video content performed 3x better than static images",
    "Tuesday sends had 40% higher open rates",
    "Mobile traffic converted at 2x desktop rate"
  ]
}
```

### A/B Test Results

Store test results in `ab_tests/` directory:

```json
{
  "test_id": "email_subject_2024_03",
  "test_type": "email_subject_line",
  "date": "2024-03-15",
  "sample_size": 10000,
  
  "variants": [
    {
      "id": "control",
      "content": "Discover Our New Features",
      "sent": 5000,
      "opens": 1000,
      "open_rate": 0.20,
      "clicks": 150,
      "ctr": 0.03
    },
    {
      "id": "variant_a",
      "content": "🚀 Game-Changing Updates Inside",
      "sent": 5000,
      "opens": 1250,
      "open_rate": 0.25,
      "clicks": 200,
      "ctr": 0.04,
      "winner": true
    }
  ],
  
  "statistical_significance": 0.95,
  "lift": 0.25,
  
  "insights": "Emojis and urgency increased open rates by 25%",
  "implementation": "Applied to all product announcement emails"
}
```

## Integration with Commands

### Automatic Context Loading

When a brand is active, all SuperMarketing commands automatically use brand context:

```
/sm:create email campaign
# Automatically uses:
# - Brand voice and tone
# - Best performing subject patterns
# - Optimal send times
# - Proven CTAs

/sm:analyze performance
# Compares against:
# - Brand benchmarks
# - Historical performance
# - Industry standards

/sm:optimize landing-page
# Applies:
# - Brand visual guidelines
# - Proven conversion elements
# - A/B test winners
```

### Explicit Brand References

Use `@brand` notation in commands:

```
/sm:create ad-copy --tone @brand.voice.social_media
/sm:campaign plan --audience @brand.personas.tech_executive
/sm:measure roi --baseline @brand.metrics.email.conversion_rate
```

## Brand Management Commands

### /sm:brand Command

```bash
# Setup and Management
/sm:brand init                    # Initialize brand directory
/sm:brand import <file>           # Import brand data
/sm:brand activate <brand_name>   # Switch active brand
/sm:brand list                    # List available brands
/sm:brand validate                # Check data completeness

# Analysis and Insights
/sm:brand analyze                 # Analyze brand performance
/sm:brand compare <brand1> <brand2>  # Compare brands
/sm:brand report                  # Generate brand report

# Export and Backup
/sm:brand export                  # Export brand data
/sm:brand backup                  # Create brand backup
```

## Best Practices

### Data Organization

1. **Start Simple**: Begin with core brand.json, add more data over time
2. **Regular Updates**: Update metrics monthly, campaigns after each execution
3. **Document Learnings**: Add insights to campaign and test results
4. **Version Control**: Use git to track brand evolution

### Data Quality

1. **Validate JSON**: Ensure all JSON files are valid
2. **Consistent Naming**: Use lowercase with underscores
3. **Complete Data**: Fill in all required fields
4. **Current Information**: Keep metrics and guidelines up-to-date

### Security

1. **Sensitive Data**: Don't store passwords or API keys
2. **PII Protection**: Anonymize customer data in personas
3. **Access Control**: Limit brand directory access as needed

## Advanced Features

### Multi-Brand Support

Agencies can manage multiple client brands:

```bash
/sm:brand activate client_a
# Work on Client A campaigns

/sm:brand activate client_b  
# Switch to Client B

/sm:brand compare client_a client_b
# Compare performance across clients
```

### Brand Evolution Tracking

Track brand changes over time:

```bash
git diff brands/your_brand/brand.json
# See how brand positioning evolved

git log brands/your_brand/metrics.json
# Track performance improvements
```

### Template Inheritance

Create brand templates that inherit from base:

```json
{
  "extends": "base_brand",
  "overrides": {
    "voice": "More casual variation"
  }
}
```

## Troubleshooting

### Common Issues

**Brand not loading:**
- Check active_brand.json points to correct brand
- Validate JSON syntax in all brand files
- Ensure brand directory exists

**Inconsistent outputs:**
- Run `/sm:brand validate` to check data
- Verify brand.json has all required fields
- Check for conflicting tone settings

**Performance issues:**
- Large campaign histories may slow loading
- Archive old campaigns to `campaigns/archive/`
- Use date ranges in metrics queries

## Examples

See `brands/example_tech_startup/` and `brands/example_ecommerce/` for complete, working brand profiles with all data types.

## Support

For brand context issues:
1. Run `/sm:brand validate` for diagnostics
2. Check this documentation
3. Review example brands
4. Report issues to SuperMarketing GitHub

---

*Brand Context System v1.0 | Part of SuperMarketing Framework*