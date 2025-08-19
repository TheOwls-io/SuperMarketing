# RULES.md - SuperMarketing Framework Actionable Rules

Simple actionable rules for SuperMarketing framework operation.

## Core Operational Rules

### Campaign Management Rules
- Research → Strategy → Plan → Execute → Measure → Optimize
- Define KPIs before launching any campaign
- Test with small budget before scaling
- Document all learnings for future campaigns
- Always have a control group for measurement

### Content Creation Rules
- Understand audience before creating content
- Follow brand guidelines consistently
- Create multiple variations for testing
- Optimize for channel-specific requirements
- Include clear calls-to-action

### Data & Analytics Rules
- Validate tracking before campaign launch
- Check data accuracy weekly
- Create dashboards before campaigns start
- Set up alerts for anomalies
- Document all metrics definitions

### Channel Management Rules
- Test new channels with <10% of budget
- Optimize top 3 channels first
- Maintain consistent brand voice across channels
- Respect platform-specific best practices
- Monitor competitive activity daily

## Marketing Execution Rules

### Do's ✅
- **Research First**: Always understand market and audience
- **Test Everything**: A/B test continuously
- **Measure Impact**: Track ROI for all activities
- **Document Learnings**: Build knowledge base
- **Iterate Quickly**: Fast feedback loops
- **Personalize**: Segment and customize messaging
- **Mobile First**: Design for mobile experience
- **Follow Compliance**: GDPR, CAN-SPAM, etc.
- **Build Relationships**: Focus on long-term value
- **Stay Agile**: Adapt to market changes

### Don'ts ❌
- **Launch Blind**: Never skip research phase
- **Ignore Data**: Don't rely on gut feelings alone
- **Spam Audiences**: Respect frequency caps
- **Break Trust**: Never mislead customers
- **Work in Silos**: Always collaborate
- **Set and Forget**: Campaigns need optimization
- **Chase Vanity Metrics**: Focus on business impact
- **Copy Competitors**: Differentiate instead
- **Overpromise**: Set realistic expectations
- **Waste Budget**: Kill underperforming campaigns

## Brand Context Loading Rules

### Automatic Brand Loading
- Check for active_brand.json on every command
- Load brand context if brand is active
- Apply brand voice, metrics, and personas automatically
- Fall back to generic if no brand active
- Cache brand data for performance (1 hour default)

### Brand Data Priority
1. **Command-specific overrides** (highest priority)
2. **Active brand context** (standard priority)
3. **Default framework values** (fallback)

### Brand Context Usage
- `/sm:create` → Use @brand.voice and @brand.visual_identity
- `/sm:campaign` → Reference @brand.campaigns and @brand.metrics
- `/sm:analyze` → Compare against @brand.metrics baselines
- `/sm:optimize` → Apply @brand.ab_tests winners
- `/sm:personalize` → Use @brand.personas profiles

## Persona Auto-Activation Rules

### Content Tasks
- Writing copy → copywriter persona + @brand.voice
- Visual design → creative persona + @brand.visual_identity
- Blog/SEO content → content persona + @brand.content_themes
- Social media → social persona + @brand.voice.social_media

### Analytics Tasks
- Performance analysis → analyst persona + @brand.metrics
- Conversion optimization → growth persona + @brand.ab_tests
- ROI calculation → analyst persona + @brand.metrics.roi
- Attribution → analyst persona + @brand.metrics.attribution

### Strategic Tasks
- Campaign planning → strategist persona + @brand.campaigns
- Brand work → brand persona + @brand.positioning
- Market research → strategist + analyst + @brand.competitors
- Positioning → brand + strategist + @brand.messaging

### Channel-Specific Tasks
- Email campaigns → email persona + @brand.metrics.email
- Paid advertising → paid persona + @brand.metrics.paid
- SEO optimization → seo persona + @brand.metrics.seo
- Social media → social persona + @brand.metrics.social

## Quality Standards

### Campaign Quality Gates
1. **Strategy Approval**: Objectives and KPIs defined
2. **Creative Review**: Brand compliance check
3. **Technical Setup**: Tracking implementation
4. **Budget Approval**: Resource allocation confirmed
5. **Launch Checklist**: All elements ready
6. **Performance Check**: Day 1 monitoring
7. **Optimization Review**: Week 1 adjustments
8. **Results Analysis**: Post-campaign review

### Content Quality Checklist
- [ ] Audience-appropriate tone
- [ ] Brand guidelines followed
- [ ] Grammar and spelling checked
- [ ] SEO optimization applied
- [ ] CTAs included and clear
- [ ] Mobile-responsive
- [ ] Accessibility standards met
- [ ] Legal compliance verified

### Data Quality Requirements
- **Accuracy**: >95% data accuracy
- **Completeness**: No critical data gaps
- **Timeliness**: Real-time where needed
- **Consistency**: Standardized definitions
- **Relevance**: Actionable insights only

## Performance Thresholds

### Campaign Performance
- **Email Open Rate**: >20% minimum
- **CTR**: Above industry benchmark
- **Conversion Rate**: >2% for e-commerce
- **ROAS**: Minimum 3:1
- **CAC Payback**: <12 months

### Content Performance
- **Engagement Rate**: >1% social media
- **Time on Page**: >2 minutes for blog
- **Bounce Rate**: <50% for landing pages
- **Share Rate**: >1% for viral content
- **SEO Rankings**: Page 1 for target keywords

### Channel Performance
- **Email Deliverability**: >95%
- **Ad Quality Score**: >7/10
- **Social Reach**: >30% of followers
- **Organic Traffic Growth**: >20% YoY
- **Paid Media Efficiency**: Improving MoM

## Workflow Automation Rules

### Email Automation
- Welcome series for all new subscribers
- Abandoned cart recovery within 1 hour
- Re-engagement after 90 days inactive
- Post-purchase follow-up within 7 days
- Birthday/anniversary campaigns

### Lead Management
- Score leads based on engagement
- Route hot leads to sales immediately
- Nurture warm leads with content
- Re-engage cold leads quarterly
- Clean list of invalid emails monthly

### Reporting Automation
- Daily performance alerts
- Weekly team reports
- Monthly executive dashboards
- Quarterly business reviews
- Annual planning inputs

## Crisis Management Rules

### Issue Response Times
- **Critical**: Respond within 15 minutes
- **High**: Respond within 1 hour
- **Medium**: Respond within 4 hours
- **Low**: Respond within 24 hours

### Escalation Triggers
- Negative sentiment >20%
- Campaign performance -50% from target
- Budget overrun >10%
- Brand safety issue detected
- Legal/compliance concern raised

### Recovery Actions
1. Pause affected campaigns immediately
2. Assess scope and impact
3. Notify stakeholders
4. Implement fix
5. Monitor closely
6. Document lessons learned

## Budget Management Rules

### Allocation Guidelines
- **Proven Channels**: 70% of budget
- **Growth Channels**: 20% of budget
- **Experimental**: 10% of budget
- **Reserve**: 5-10% for opportunities

### Optimization Rules
- Review performance weekly
- Reallocate from underperformers
- Increase investment in winners
- Cut losses quickly (<2 weeks)
- Document ROI by channel

## Testing Protocol

### A/B Testing Rules
- One variable at a time
- Statistical significance required (95%)
- Minimum sample size calculations
- Test duration: full business cycle
- Document and share results

### Multivariate Testing
- Max 3-4 variables
- Larger sample size required
- Longer test duration
- Use for high-traffic pages only
- Implement winners systematically

## Compliance Requirements

### Data Privacy
- Get explicit consent
- Honor opt-out requests immediately
- Secure data transmission and storage
- Regular data audits
- GDPR/CCPA compliance

### Advertising Standards
- Truth in advertising
- Disclosure of partnerships
- Age-appropriate content
- Platform-specific rules
- Industry regulations

### Email Compliance
- CAN-SPAM compliance
- Clear unsubscribe option
- Accurate sender information
- Relevant subject lines
- Physical address included