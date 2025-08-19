---
allowed-tools: [Read, Write, Grep, TodoWrite]
description: "Design and execute marketing experiments and A/B tests"
---

# /sm:test - Marketing Testing & Experimentation

## Purpose
Design, execute, and analyze marketing experiments including A/B tests, multivariate tests, and growth experiments.

## Usage
```
/sm:test [test-type] [--hypothesis statement] [--variations count] [--sample-size number] [--duration time]
```

## Arguments
- `test-type` - Type of test (ab|multivariate|split|sequential)
- `--hypothesis` - Test hypothesis and expected outcome
- `--variations` - Number of test variations
- `--sample-size` - Required sample size for significance
- `--duration` - Test duration

## Execution
1. Formulate test hypothesis
2. Calculate required sample size
3. Design test variations
4. Set up test infrastructure
5. Launch and monitor test
6. Ensure statistical significance
7. Analyze results and insights
8. Implement winning variation
9. Document learnings

## Personas
- **Primary**: growth (experimentation), analyst (statistics), copywriter (variations)
- **Supporting**: creative (visual tests)

## Outputs
- Test plan and hypothesis
- Variation designs
- Statistical analysis
- Winner declaration
- Implementation guide
- Test learnings documentation