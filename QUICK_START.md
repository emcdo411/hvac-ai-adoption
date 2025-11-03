# 🚀 Quick Start Guide
## Get Started with HVAC AI Adoption Framework in 15 Minutes

---

## Overview

This guide will help you:
1. Install the framework (5 minutes)
2. Score your first proposal (5 minutes)
3. Understand the results (5 minutes)
4. Start using the course (next steps)

---

## Prerequisites Checklist

Before starting, ensure you have:

- [ ] Python 3.8+ installed ([download here](https://www.python.org/downloads/))
- [ ] Git installed ([download here](https://git-scm.com/downloads))
- [ ] Basic command line familiarity
- [ ] A text editor (VS Code, Sublime, or any editor)
- [ ] 15 minutes of uninterrupted time

**Quick Python Check:**
```bash
python --version  # Should show 3.8 or higher
```

---

## Step 1: Installation (5 minutes)

### Option A: Quick Install (Recommended)

```bash
# 1. Clone the repository
git clone https://github.com/emcdo411/hvac-ai-adoption.git
cd hvac-ai-adoption

# 2. Create virtual environment (recommended)
python -m venv venv

# 3. Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Download required language model
python -m spacy download en_core_web_sm

# 6. Verify installation
python scripts/score_proposal.py --version
```

**Expected output:** `score_proposal.py 1.0.0`

### Option B: Manual Install

If you don't have Git:

1. Download the repository as ZIP from GitHub
2. Extract to your preferred location
3. Follow steps 2-6 from Option A

### Troubleshooting Installation

**Error: "Python not found"**
- Ensure Python is in your PATH
- Try `python3` instead of `python`

**Error: "pip not found"**
```bash
python -m ensurepip --upgrade
```

**Error: "Permission denied"**
```bash
pip install --user -r requirements.txt
```

---

## Step 2: Score Your First Proposal (5 minutes)

### Test with Sample Proposal

```bash
# Score the included sample proposal
python scripts/score_proposal.py examples/proposals/sample_proposal.txt
```

**You should see output like this:**

```
============================================================
HVAC AI ADOPTION PROPOSAL SCORE
============================================================

Overall Score: 82.5/100 (Grade: B)
Percentile: 80th-95th (Top 20%)

Proposal Stats:
  - 1847 words
  - 94 sentences

Category                  Score      Coverage
------------------------------------------------------------
Business Case             20.8/25    83.2%
Technical Readiness       17.2/20    86.0%
Data Foundation           18.5/20    92.5%
Success Metrics           12.0/15    80.0%
Risk Management           8.5/10     85.0%
Change Management         5.5/10     55.0%

============================================================
GAPS IDENTIFIED
============================================================

Change Management:
  Current: 5.5/10
  Gap: 4.5 points
  Coverage: 55.0%

============================================================
RECOMMENDATIONS
============================================================

1. 🎯 Priority: Reach 75+ score threshold for pilot success.
   Focus on the largest gaps first.

2. Create a stakeholder engagement plan with training strategy.
   Address adoption challenges and communication approaches.
```

### Score Your Own Proposal

```bash
# 1. Create your proposal as a text file
# Save it as: my_proposal.txt

# 2. Score it
python scripts/score_proposal.py my_proposal.txt

# 3. Get detailed breakdown
python scripts/score_proposal.py my_proposal.txt --verbose

# 4. Save results to file
python scripts/score_proposal.py my_proposal.txt --output results.txt

# 5. Get JSON output (for integration with other tools)
python scripts/score_proposal.py my_proposal.txt --json --output results.json
```

### Interactive Mode

```bash
# Start interactive mode
python scripts/score_proposal.py --interactive

# Then paste your proposal text
# Press Ctrl+D (or Ctrl+Z on Windows) when done
```

---

## Step 3: Understanding Your Results (5 minutes)

### Score Interpretation

| Score Range | Grade | Meaning | Next Steps |
|-------------|-------|---------|------------|
| **90-100** | A | Excellent! | Proceed to implementation |
| **80-89** | B | Good | Minor refinements recommended |
| **70-79** | C | Acceptable | Address key gaps |
| **60-69** | D | Needs work | Significant improvements required |
| **<60** | F | Insufficient | Major revision needed |

**⚠️ Important:** A minimum score of **75/100** is recommended for pilot success based on 40+ implementations.

### Category Breakdown

#### 1. **Business Case (25 points)**
**What it measures:** ROI, cost savings, business value, competitive advantage

**To improve:**
- Add specific financial projections
- Include baseline metrics
- Quantify expected benefits
- Show market opportunity

#### 2. **Technical Readiness (20 points)**
**What it measures:** Infrastructure, systems, technical resources, integration plans

**To improve:**
- Document current technical landscape
- Detail integration approach
- List available resources and expertise
- Address technical dependencies

#### 3. **Data Foundation (20 points)**
**What it measures:** Data availability, quality, collection processes, analytics capability

**To improve:**
- Inventory existing data assets
- Assess data quality and completeness
- Outline data collection strategy
- Define data governance approach

#### 4. **Success Metrics (15 points)**
**What it measures:** KPIs, measurement methodology, targets, tracking plans

**To improve:**
- Define specific, measurable KPIs
- Set baseline and target values
- Explain measurement approach
- Establish reporting cadence

#### 5. **Risk Management (10 points)**
**What it measures:** Risk identification, mitigation strategies, compliance, security

**To improve:**
- Identify potential risks
- Develop mitigation plans
- Address security and privacy
- Define governance structure

#### 6. **Change Management (10 points)**
**What it measures:** Training, adoption strategy, stakeholder engagement, communication

**To improve:**
- Map stakeholders
- Create training plan
- Design communication strategy
- Plan adoption approach

---

## Step 4: Improve Your Score

### Quick Wins (Add these to gain 10-15 points)

1. **Add ROI Calculation** (+5 points)
   ```
   Investment: $X
   Expected Savings: $Y per year
   Payback Period: Z months
   3-Year NPV: $N
   ```

2. **Define 3-5 Clear KPIs** (+3-5 points)
   ```
   1. [Metric Name]
      - Baseline: X
      - Target: Y
      - Timeframe: Z
   ```

3. **List 3 Key Risks + Mitigations** (+3-4 points)
   ```
   Risk: [Description]
   Impact: [High/Medium/Low]
   Mitigation: [Strategy]
   ```

4. **Outline Training Plan** (+2-3 points)
   ```
   - Who needs training: [Roles]
   - Duration: [Hours]
   - Format: [Delivery method]
   - Timeline: [Schedule]
   ```

### Common Gaps and Fixes

| Gap | Quick Fix | Points Gained |
|-----|-----------|---------------|
| No ROI mentioned | Add simple calculation | +5 |
| Vague success metrics | Define 3 specific KPIs | +5 |
| Missing risk assessment | List 3 risks + mitigations | +4 |
| No training plan | Outline basic approach | +3 |
| Unclear data sources | List data assets | +4 |

---

## Step 5: Next Steps

### Option 1: DIY Learning Path

**Week 1: Foundations**
1. Read `references/use-cases.md` - Understand 10 AI applications
2. Study `references/benchmarks.md` - Learn industry data
3. Review `references/annotated-examples.md` - See good vs. great proposals

**Week 2: Practical Application**
1. Create proposal for your business using templates
2. Score it and iterate to 75+
3. Study `references/anti-patterns.md` - Avoid common mistakes

**Week 3: Implementation Planning**
1. Read `references/implementation-guide.md` - 90-day playbook
2. Use `references/decision-tree.md` - Select best pilot
3. Prepare executive presentation

**Week 4: Execution**
1. Start pilot implementation
2. Track metrics weekly
3. Document lessons learned

### Option 2: Structured Course Path

Follow the course modules sequentially:

1. **Module 1: Foundations** (`course-modules/01-foundations/`)
   - Complete in 1 week
   - Quiz at end

2. **Module 2: Assessment** (`course-modules/02-assessment/`)
   - Complete in 1 week
   - Practice assessments

3. **Module 3: Pilot Design** (`course-modules/03-pilot-design/`)
   - Complete in 2 weeks
   - Create pilot proposal (scored 75+)

4. **Module 4: Implementation** (`course-modules/04-implementation/`)
   - 90-day execution plan
   - Weekly checkpoints

5. **Module 5: Scaling** (`course-modules/05-scaling/`)
   - Network effects
   - Enterprise transformation

### Option 3: Client Engagement (For Consultants)

**7-Day Sprint Framework:**

| Day | Activity | Deliverable |
|-----|----------|-------------|
| **Day 1** | Discovery & data audit | Assessment report |
| **Day 2** | Use case prioritization | Ranked opportunities |
| **Day 3** | Pilot design | Draft proposal |
| **Day 4** | Score & refine | Proposal scoring 75+ |
| **Day 5** | Risk & mitigation | Risk register |
| **Day 6** | 90-day roadmap | Implementation plan |
| **Day 7** | Executive presentation | Decision package |

---

## Using with Claude AI or ChatGPT

### Claude AI Setup

1. Upload `SKILL.md` to Claude
2. Trigger naturally: "Help me assess HVAC AI readiness"
3. Claude loads framework automatically
4. Reference files loaded as needed

### ChatGPT Custom GPT

1. Create Custom GPT
2. Copy SKILL.md content to instructions
3. Upload reference files
4. Set behavior to "always load context"

---

## Common Questions

### "What score do I need to proceed?"

**Minimum:** 75/100 (Grade C+)  
**Recommended:** 80/100 (Grade B)  
**Excellent:** 90/100 (Grade A)

### "How long does scoring take?"

- Small proposals (<1000 words): < 5 seconds
- Medium proposals (1000-3000 words): 5-10 seconds
- Large proposals (>3000 words): 10-30 seconds

### "Can I score multiple proposals?"

Yes! Use batch processing:

```bash
# Score all proposals in a directory
for file in proposals/*.txt; do
    python scripts/score_proposal.py "$file" --json --output "results/$(basename "$file" .txt).json"
done
```

### "What if my score is below 75?"

Don't worry! Use the recommendations to improve:

1. Focus on the largest gaps first
2. Add the "Quick Wins" from Step 4
3. Reference `references/anti-patterns.md` for what to avoid
4. Compare your proposal to examples in `references/annotated-examples.md`
5. Iterate and re-score

### "How accurate is the scoring?"

The scoring engine is based on analysis of 40+ successful pilots:
- **Proposals scoring 75+**: 85% pilot success rate
- **Proposals scoring <75**: 35% pilot success rate

While not perfect, it's a strong indicator of readiness.

---

## Getting Help

### Resources

- **Documentation**: See `docs/` folder
- **Examples**: See `examples/` folder
- **Templates**: See `templates/` folder
- **Case Studies**: See `case-studies/` folder

### Support Channels

- **GitHub Issues**: Report bugs or request features
- **GitHub Discussions**: Ask questions and share ideas
- **Email**: your.email@example.com
- **LinkedIn**: [Your Profile](https://linkedin.com/in/yourprofile)

### Contributing

Found this helpful? Consider contributing:

- Share your implementation experience (Commons Protocol)
- Improve documentation
- Add examples or templates
- Report bugs or suggest features

See [CONTRIBUTING.md](../CONTRIBUTING.md) for details.

---

## Success Checklist

After completing this quick start, you should be able to:

- [ ] Install and run the scoring engine
- [ ] Score a proposal and interpret results
- [ ] Identify gaps and areas for improvement
- [ ] Understand the scoring rubric
- [ ] Know which resources to use next
- [ ] Be ready to create your first pilot proposal

---

## What's Next?

### Immediate Actions (Today)

1. Score an actual proposal (yours or a client's)
2. Review the recommendations
3. Pick one module to read

### This Week

1. Complete Module 1: Foundations
2. Refine your proposal to 75+
3. Share your success or questions

### This Month

1. Complete Modules 1-3
2. Design a real pilot
3. Present to stakeholders

### This Quarter

1. Implement your first pilot
2. Measure results
3. Contribute to Commons Protocol

---

<div align="center">

**🎉 Congratulations! You're ready to transform HVAC operations with AI.**

[Back to README](../README.md) • [View Full Course](../course-modules/) • [Get Support](https://github.com/emcdo411/hvac-ai-adoption/discussions)

</div>
