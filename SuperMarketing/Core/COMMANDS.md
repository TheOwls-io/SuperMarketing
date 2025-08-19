# COMMANDS.md - SuperMarketing Command Execution Framework

Command execution framework for Claude Code SuperMarketing integration.

## Command System Architecture

### Core Command Structure
```yaml
---
command: "/{command-name}"
category: "Primary classification"
purpose: "Marketing objective"
personas: "Auto-activated personas"
performance-profile: "optimization|standard|complex"
---
```

### Command Processing Pipeline
1. **Input Parsing**: Campaign briefs, market data, creative assets
2. **Context Resolution**: Auto-persona activation based on marketing domain
3. **Channel Selection**: Platform-specific optimization
4. **Execution Strategy**: Tool orchestration and resource allocation
5. **Performance Tracking**: KPI monitoring and optimization

### Integration Layers
- **Claude Code**: Native slash command compatibility
- **Persona System**: Marketing specialist auto-activation
- **Channel Platforms**: Social, email, paid, SEO integration
- **Analytics Tools**: Performance tracking and attribution

## Marketing Command Categories

### Campaign & Strategy Commands

**`/sm:campaign $ARGUMENTS`**
```yaml
---
command: "/sm:campaign"
category: "Campaign Management"
purpose: "Plan and execute integrated marketing campaigns"
personas: "strategist, creative, analyst"
performance-profile: "complex"
---
```
- **Auto-Persona**: Strategist (planning), Creative (assets), Analyst (measurement)
- **Tool Orchestration**: [Campaign planning, asset creation, channel distribution, performance tracking]
- **Arguments**: `[campaign-type]`, `--channels`, `--budget`, `--timeline`, `--goals`
- **Outputs**: Campaign brief, creative assets, media plan, measurement framework

**`/sm:strategy $ARGUMENTS`**
```yaml
---
command: "/sm:strategy"
category: "Strategic Planning"
purpose: "Develop comprehensive marketing strategies"
personas: "strategist, brand, analyst"
performance-profile: "complex"
---
```
- **Auto-Persona**: Strategist (lead), Brand (positioning), Analyst (market intelligence)
- **Tool Orchestration**: [Market analysis, competitive research, strategy documentation]
- **Arguments**: `[strategy-type]`, `--market`, `--competition`, `--objectives`, `--timeline`
- **Outputs**: Strategy document, go-to-market plan, KPI framework

**`/sm:research $ARGUMENTS`**
```yaml
---
command: "/sm:research"
category: "Market Intelligence"
purpose: "Conduct market research and competitive analysis"
personas: "analyst, strategist, seo"
performance-profile: "standard"
---
```
- **Auto-Persona**: Analyst (data), Strategist (insights), SEO (search trends)
- **Tool Orchestration**: [Data collection, trend analysis, competitor research, insight generation]
- **Arguments**: `[research-type]`, `--market`, `--competitors`, `--keywords`, `--depth`
- **Outputs**: Research report, competitive matrix, trend analysis, recommendations

### Content & Creative Commands

**`/sm:create $ARGUMENTS`**
```yaml
---
command: "/sm:create"
category: "Content Creation"
purpose: "Generate marketing content and creative assets"
personas: "copywriter, creative, content"
performance-profile: "standard"
---
```
- **Auto-Persona**: Copywriter (messaging), Creative (visuals), Content (long-form)
- **Tool Orchestration**: [Content generation, design creation, copy optimization]
- **Arguments**: `[content-type]`, `--channel`, `--audience`, `--tone`, `--format`
- **Outputs**: Copy variations, creative concepts, content pieces, asset specifications

**`/sm:optimize $ARGUMENTS`**
```yaml
---
command: "/sm:optimize"
category: "Performance Optimization"
purpose: "Optimize content and campaigns for better performance"
personas: "growth, seo, paid"
performance-profile: "optimization"
---
```
- **Auto-Persona**: Growth (CRO), SEO (organic), Paid (ad optimization)
- **Tool Orchestration**: [A/B testing, SEO optimization, conversion optimization]
- **Arguments**: `[optimization-target]`, `--metrics`, `--goals`, `--constraints`
- **Outputs**: Optimization recommendations, test plans, implementation guide

**`/sm:personalize $ARGUMENTS`**
```yaml
---
command: "/sm:personalize"
category: "Personalization"
purpose: "Create personalized experiences and messaging"
personas: "email, copywriter, analyst"
performance-profile: "standard"
---
```
- **Auto-Persona**: Email (segmentation), Copywriter (dynamic copy), Analyst (data)
- **Tool Orchestration**: [Segmentation, dynamic content, personalization rules]
- **Arguments**: `[personalization-type]`, `--segments`, `--variables`, `--rules`
- **Outputs**: Personalization strategy, dynamic content, segment definitions

### Analytics & Performance Commands

**`/sm:analyze $ARGUMENTS`**
```yaml
---
command: "/sm:analyze"
category: "Analytics & Insights"
purpose: "Analyze marketing performance and generate insights"
personas: "analyst, growth, strategist"
performance-profile: "complex"
---
```
- **Auto-Persona**: Analyst (data), Growth (optimization), Strategist (insights)
- **Tool Orchestration**: [Data analysis, attribution modeling, insight generation]
- **Arguments**: `[analysis-type]`, `--metrics`, `--period`, `--segments`, `--attribution`
- **Outputs**: Performance report, insights, recommendations, action items

**`/sm:measure $ARGUMENTS`**
```yaml
---
command: "/sm:measure"
category: "Measurement & Attribution"
purpose: "Track KPIs and attribute conversions"
personas: "analyst, paid, growth"
performance-profile: "standard"
---
```
- **Auto-Persona**: Analyst (measurement), Paid (ROAS), Growth (funnel metrics)
- **Tool Orchestration**: [KPI tracking, attribution analysis, ROI calculation]
- **Arguments**: `[measurement-type]`, `--kpis`, `--attribution-model`, `--timeframe`
- **Outputs**: KPI dashboard, attribution report, ROI analysis

**`/sm:report $ARGUMENTS`**
```yaml
---
command: "/sm:report"
category: "Reporting & Dashboards"
purpose: "Generate marketing reports and dashboards"
personas: "analyst, strategist"
performance-profile: "standard"
---
```
- **Auto-Persona**: Analyst (data visualization), Strategist (executive summary)
- **Tool Orchestration**: [Data aggregation, visualization, narrative generation]
- **Arguments**: `[report-type]`, `--audience`, `--metrics`, `--format`, `--frequency`
- **Outputs**: Executive dashboard, performance report, trend analysis

**`/sm:forecast $ARGUMENTS`**
```yaml
---
command: "/sm:forecast"
category: "Predictive Analytics"
purpose: "Forecast trends and predict outcomes"
personas: "analyst, strategist, paid"
performance-profile: "complex"
---
```
- **Auto-Persona**: Analyst (modeling), Strategist (planning), Paid (budget allocation)
- **Tool Orchestration**: [Predictive modeling, trend analysis, scenario planning]
- **Arguments**: `[forecast-type]`, `--model`, `--variables`, `--horizon`, `--confidence`
- **Outputs**: Forecast model, predictions, confidence intervals, recommendations

### Testing & Experimentation Commands

**`/sm:test $ARGUMENTS`**
```yaml
---
command: "/sm:test"
category: "Testing & Experimentation"
purpose: "Design and execute marketing experiments"
personas: "growth, analyst, copywriter"
performance-profile: "optimization"
---
```
- **Auto-Persona**: Growth (test design), Analyst (statistics), Copywriter (variations)
- **Tool Orchestration**: [Test design, execution, analysis, recommendations]
- **Arguments**: `[test-type]`, `--hypothesis`, `--variations`, `--sample-size`, `--duration`
- **Outputs**: Test plan, variations, results analysis, winner declaration

### Workflow & Collaboration Commands

**`/sm:workflow $ARGUMENTS`**
```yaml
---
command: "/sm:workflow"
category: "Marketing Automation"
purpose: "Create automated marketing workflows"
personas: "email, growth, strategist"
performance-profile: "standard"
---
```
- **Auto-Persona**: Email (automation), Growth (optimization), Strategist (journey design)
- **Tool Orchestration**: [Workflow design, trigger setup, action configuration]
- **Arguments**: `[workflow-type]`, `--triggers`, `--actions`, `--conditions`, `--goals`
- **Outputs**: Workflow diagram, automation rules, performance metrics

**`/sm:calendar $ARGUMENTS`**
```yaml
---
command: "/sm:calendar"
category: "Content Planning"
purpose: "Manage content and campaign calendars"
personas: "content, social, strategist"
performance-profile: "standard"
---
```
- **Auto-Persona**: Content (editorial), Social (posting), Strategist (campaign timing)
- **Tool Orchestration**: [Calendar planning, content scheduling, deadline management]
- **Arguments**: `[calendar-type]`, `--channels`, `--frequency`, `--themes`, `--deadlines`
- **Outputs**: Content calendar, posting schedule, campaign timeline

**`/sm:brief $ARGUMENTS`**
```yaml
---
command: "/sm:brief"
category: "Project Documentation"
purpose: "Create marketing briefs and documentation"
personas: "strategist, creative, copywriter"
performance-profile: "standard"
---
```
- **Auto-Persona**: Strategist (objectives), Creative (requirements), Copywriter (messaging)
- **Tool Orchestration**: [Brief creation, requirement gathering, approval workflow]
- **Arguments**: `[brief-type]`, `--project`, `--stakeholders`, `--requirements`, `--deliverables`
- **Outputs**: Creative brief, project brief, requirements document

**`/sm:collaborate $ARGUMENTS`**
```yaml
---
command: "/sm:collaborate"
category: "Team Collaboration"
purpose: "Facilitate marketing team collaboration"
personas: "strategist, brand"
performance-profile: "standard"
---
```
- **Auto-Persona**: Strategist (coordination), Brand (approval)
- **Tool Orchestration**: [Task assignment, review cycles, approval workflows]
- **Arguments**: `[collaboration-type]`, `--team`, `--tasks`, `--deadlines`, `--approvals`
- **Outputs**: Task assignments, review feedback, approval status

### Launch & Execution Commands

**`/sm:launch $ARGUMENTS`**
```yaml
---
command: "/sm:launch"
category: "Campaign Launch"
purpose: "Execute campaign launch checklists"
personas: "strategist, paid, social"
performance-profile: "complex"
---
```
- **Auto-Persona**: Strategist (coordination), Paid (ad launch), Social (organic launch)
- **Tool Orchestration**: [Pre-launch checks, asset deployment, monitoring setup]
- **Arguments**: `[launch-type]`, `--channels`, `--assets`, `--schedule`, `--monitoring`
- **Outputs**: Launch checklist, deployment confirmation, monitoring dashboard

**`/sm:audit $ARGUMENTS`**
```yaml
---
command: "/sm:audit"
category: "Marketing Audit"
purpose: "Conduct marketing audits and compliance checks"
personas: "analyst, seo, brand"
performance-profile: "complex"
---
```
- **Auto-Persona**: Analyst (performance), SEO (technical), Brand (consistency)
- **Tool Orchestration**: [Audit execution, issue identification, recommendation generation]
- **Arguments**: `[audit-type]`, `--scope`, `--criteria`, `--compliance`, `--benchmarks`
- **Outputs**: Audit report, issue log, improvement roadmap, compliance status

## Command Execution Matrix

### Performance Profiles
```yaml
optimization: "High-performance testing and iteration"
standard: "Balanced execution with moderate complexity"
complex: "Resource-intensive with comprehensive analysis"
```

### Command Categories
- **Strategy**: campaign, strategy, research
- **Creative**: create, optimize, personalize
- **Analytics**: analyze, measure, report, forecast
- **Testing**: test
- **Workflow**: workflow, calendar, brief, collaborate
- **Execution**: launch, audit

### Channel-Specific Flags
- `--channel [social|email|paid|seo|content]`
- `--platform [facebook|instagram|linkedin|google|tiktok]`
- `--audience [b2b|b2c|enterprise|smb]`
- `--funnel [awareness|consideration|conversion|retention]`

### Marketing KPI Tracking
- **Awareness**: Reach, impressions, brand lift
- **Engagement**: CTR, likes, shares, comments
- **Conversion**: CVR, CPA, ROAS, revenue
- **Retention**: LTV, churn rate, repeat purchase rate