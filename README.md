# SuperMarketing Framework 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/SuperMarketing/SuperMarketing_Framework)

AI-powered marketing automation and optimization framework for Claude Code, featuring specialized marketing personas and campaign management tools.

## What is SuperMarketing? 🎯

SuperMarketing transforms Claude Code into a comprehensive marketing assistant by adding:

- 🎭 **11 Marketing Personas**: Strategist, Copywriter, Creative, Analyst, Growth Hacker, and more
- 📊 **17 Marketing Commands**: Campaign management, content creation, analytics, optimization
- 📈 **Channel Optimization**: Multi-channel campaign orchestration and performance tracking
- 🔄 **Marketing Workflows**: Automated campaign execution and optimization
- 💡 **Data-Driven Insights**: Analytics, attribution, and predictive modeling

## Marketing Personas 🎭

### Creative & Content Specialists
- **strategist**: Marketing strategy, campaign planning, positioning
- **copywriter**: Persuasive copy, headlines, messaging frameworks  
- **creative**: Visual concepts, brand identity, creative campaigns
- **content**: Content marketing, SEO optimization, editorial calendars

### Analytics & Performance Experts
- **analyst**: Data analysis, ROI measurement, attribution modeling
- **growth**: Growth hacking, conversion optimization, A/B testing
- **seo**: Search optimization, keyword research, technical SEO

### Channel & Engagement Specialists
- **social**: Social media strategy, community management, viral campaigns
- **email**: Email marketing, automation, segmentation strategies
- **paid**: PPC, paid social, media buying, ad optimization
- **brand**: Brand positioning, voice & tone, brand guidelines

## Marketing Commands 🛠️

### Campaign & Strategy
- `/sm:campaign` - Plan and execute integrated marketing campaigns
- `/sm:strategy` - Develop comprehensive marketing strategies
- `/sm:research` - Market research and competitive analysis

### Content & Creative
- `/sm:create` - Generate marketing content and creative assets
- `/sm:optimize` - Optimize campaigns for performance
- `/sm:personalize` - Create personalized experiences

### Analytics & Performance
- `/sm:analyze` - Analyze marketing performance and insights
- `/sm:measure` - Track KPIs and attribution
- `/sm:report` - Generate marketing reports and dashboards
- `/sm:forecast` - Predictive analytics and forecasting

### Testing & Workflow
- `/sm:test` - A/B testing and experimentation
- `/sm:workflow` - Marketing automation workflows
- `/sm:calendar` - Content calendar management
- `/sm:brief` - Creative briefs and documentation
- `/sm:collaborate` - Team collaboration tools
- `/sm:launch` - Campaign launch checklists
- `/sm:audit` - Marketing audits and compliance

### Brand Management (NEW!)
- `/sm:brand` - Manage brand context for personalized outputs

## Installation 📦

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Access to ~/.claude directory

### Step 1: Install the Package

Choose your preferred installation method:

#### Method 1: pip (Recommended)
```bash
# From PyPI
pip install SuperMarketing

# Or from source
git clone https://github.com/SuperMarketing/SuperMarketing_Framework.git
cd SuperMarketing_Framework
pip install -e .
```

#### Method 2: pip with requirements.txt
```bash
# Clone the repo
git clone https://github.com/SuperMarketing/SuperMarketing_Framework.git
cd SuperMarketing_Framework

# Install dependencies
pip install -r requirements.txt

# Install package
pip install -e .
```

### Step 2: Run the Installer

```bash
# Standard installation
SuperMarketing install

# Interactive mode (choose components)
SuperMarketing install --interactive

# Marketing team profile
SuperMarketing install --profile marketing-team

# See all options
SuperMarketing install --help
```

## Brand Context System 🎯 (NEW!)

SuperMarketing now includes a powerful Brand Context System that personalizes all marketing outputs based on your brand's unique data:

### What It Does
- **Automatic Customization**: All commands use your brand's voice, style, and proven strategies
- **Historical Learning**: Leverages past campaign performance and A/B test results
- **Persona Integration**: Uses your actual customer personas for targeting
- **Performance Baselines**: Compares results against your brand's benchmarks

### Quick Setup
1. **Drop Your Brand Data**
   ```bash
   # Navigate to BrandContext directory
   cd SuperMarketing/BrandContext/brands/
   
   # Create your brand folder
   mkdir your_brand
   
   # Add your brand files (see examples provided)
   - brand.json      # Your brand identity
   - metrics.json    # Performance baselines
   - personas.json   # Customer profiles
   ```

2. **Activate Your Brand**
   ```
   /sm:brand activate your_brand
   ```

3. **All Commands Now Use Your Brand!**
   ```
   /sm:create email campaign
   # Automatically uses your brand voice, best subject lines, optimal send times
   
   /sm:analyze performance
   # Compares against your historical benchmarks
   
   /sm:optimize landing-page
   # Applies your proven A/B test winners
   ```

### Example Brand Profiles Included
- **Tech Startup** (B2B SaaS): Complete profile with campaigns and tests
- **E-commerce** (Fashion): Full brand setup with seasonal data

See `BrandContext/BRAND_CONTEXT.md` for complete documentation.

## Quick Start 🚀

### Campaign Planning
```
/sm:campaign product-launch --channels social,email,paid --budget 50000 --timeline 8-weeks
```

### Content Creation
```
/sm:create email-campaign --audience b2b-decision-makers --tone professional --format newsletter
```

### Performance Analysis
```
/sm:analyze campaign-performance --period last-quarter --focus roi --depth deep
```

### A/B Testing
```
/sm:test landing-page --hypothesis "Video increases conversion" --variations 2 --duration 2-weeks
```

## Marketing Workflows 📊

### Product Launch Campaign
1. `/sm:strategy` - Develop go-to-market strategy
2. `/sm:campaign` - Plan multi-channel campaign
3. `/sm:create` - Generate creative assets
4. `/sm:test` - A/B test messaging
5. `/sm:launch` - Execute campaign
6. `/sm:measure` - Track performance
7. `/sm:optimize` - Continuous improvement

### Lead Generation Funnel
1. `/sm:research` - Audience research
2. `/sm:create` - Content and lead magnets
3. `/sm:workflow` - Email nurture automation
4. `/sm:personalize` - Dynamic content
5. `/sm:analyze` - Funnel optimization

### Brand Awareness Campaign
1. `/sm:strategy` - Brand positioning
2. `/sm:create` - Brand assets
3. `/sm:campaign` - Awareness campaign
4. `/sm:measure` - Brand lift tracking
5. `/sm:report` - Executive reporting

## Channel Integration 📱

### Supported Channels
- **Social Media**: Facebook, Instagram, LinkedIn, Twitter/X, TikTok, YouTube
- **Email Marketing**: Newsletters, automation, transactional
- **Paid Media**: Google Ads, Facebook Ads, LinkedIn Ads
- **Content Marketing**: Blog, SEO, video, podcasts
- **Website**: Landing pages, conversion optimization

### Performance Metrics
- **Awareness**: Reach, impressions, brand lift
- **Engagement**: CTR, likes, shares, comments
- **Conversion**: CVR, CPA, ROAS, revenue
- **Retention**: LTV, churn rate, NPS

## Key Features ✨

### Intelligent Persona Selection
- Automatic activation based on task context
- Cross-persona collaboration for complex campaigns
- Domain expertise for specialized tasks

### Multi-Channel Orchestration
- Integrated campaign management
- Channel-specific optimization
- Cross-channel attribution

### Data-Driven Optimization
- Real-time performance tracking
- Predictive analytics
- Automated recommendations

### Marketing Automation
- Workflow automation
- Dynamic personalization
- Trigger-based campaigns

## Configuration ⚙️

After installation, customize SuperMarketing:
- `~/.claude/settings.json` - Main configuration
- `~/.claude/marketing/` - Marketing-specific settings
- `~/.claude/templates/` - Campaign templates

## Use Cases 💼

### B2B Marketing
- Lead generation campaigns
- Account-based marketing
- Thought leadership content
- LinkedIn advertising

### B2C Marketing  
- E-commerce campaigns
- Social media marketing
- Email automation
- Influencer partnerships

### Content Marketing
- SEO optimization
- Blog content strategy
- Video marketing
- Podcast promotion

### Performance Marketing
- PPC campaigns
- Conversion optimization
- Retargeting strategies
- Attribution modeling

## Comparison with SuperClaude

| Feature | SuperClaude | SuperMarketing |
|---------|-------------|----------------|
| **Focus** | Software Development | Marketing & Growth |
| **Personas** | Developer roles | Marketing specialists |
| **Commands** | Code & deployment | Campaigns & analytics |
| **Outputs** | Code & documentation | Content & insights |
| **Metrics** | Code quality | Marketing KPIs |

## Contributing 🤝

We welcome contributions from marketing professionals and developers:
- Share campaign templates
- Add industry-specific features
- Improve analytics capabilities
- Enhance channel integrations

## License 📄

MIT License - See LICENSE file for details

## Support 💬

- Documentation: [supermarketing.ai/docs](https://supermarketing.ai/docs)
- Issues: [GitHub Issues](https://github.com/SuperMarketing/SuperMarketing_Framework/issues)
- Community: [Discord](https://discord.gg/supermarketing)

---

*Built for marketers who want AI-powered campaign excellence* 🎯