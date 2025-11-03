# Contributing to HVAC AI Adoption Framework

First off, thank you for considering contributing to the HVAC AI Adoption Framework! It's people like you who help make this framework better for the entire HVAC industry.

## 🌟 Ways to Contribute

### 1. **Share Your Pilot Results** (Commons Protocol)
The most valuable contribution is sharing your implementation experience:

- Document your pilot implementation
- Share lessons learned
- Report what worked and what didn't
- Contribute anonymized metrics

### 2. **Improve Documentation**
- Fix typos or clarify instructions
- Add examples or use cases
- Translate content to other languages
- Create video tutorials

### 3. **Enhance the Scoring Engine**
- Improve semantic analysis algorithms
- Add new scoring criteria
- Optimize performance
- Fix bugs

### 4. **Add Case Studies**
- Share real-world implementations
- Document challenges and solutions
- Provide anonymized data
- Create before/after comparisons

### 5. **Build Tools and Integrations**
- Create plugins or extensions
- Integrate with HVAC software
- Build visualization tools
- Develop mobile applications

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git installed on your machine
- GitHub account
- Basic understanding of HVAC operations (helpful)
- Familiarity with AI concepts (helpful)

### Development Setup

```bash
# 1. Fork the repository on GitHub

# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/hvac-ai-adoption.git
cd hvac-ai-adoption

# 3. Add upstream remote
git remote add upstream https://github.com/ORIGINAL_OWNER/hvac-ai-adoption.git

# 4. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 5. Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# 6. Install pre-commit hooks
pre-commit install

# 7. Create a feature branch
git checkout -b feature/your-feature-name
```

---

## 📝 Contribution Process

### For Documentation Changes

1. **Find or create an issue** describing the documentation improvement
2. **Make your changes** following our style guide
3. **Test locally** to ensure formatting is correct
4. **Submit a pull request** with a clear description

### For Code Changes

1. **Check existing issues** or create a new one
2. **Discuss your approach** before writing code
3. **Write tests** for new functionality
4. **Follow coding standards** (see below)
5. **Update documentation** as needed
6. **Submit a pull request** with tests passing

### For Commons Protocol Contributions

1. **Use the template** in `templates/commons-contribution.md`
2. **Anonymize sensitive data** (company names, specific metrics)
3. **Include context** (industry segment, company size, etc.)
4. **Document outcomes** (metrics, lessons learned)
5. **Submit via pull request** to `case-studies/`

---

## 🎯 Pull Request Guidelines

### Before Submitting

- [ ] Code follows our style guidelines
- [ ] Tests pass locally (`pytest tests/`)
- [ ] Documentation is updated
- [ ] Commit messages are clear and descriptive
- [ ] PR description explains what and why

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

## Related Issue
Closes #[issue number]

## Testing
How did you test this?

## Checklist
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] Code follows style guidelines
- [ ] All tests pass
```

---

## 💻 Coding Standards

### Python Style Guide

We follow PEP 8 with some modifications:

```python
# Good examples:

def score_proposal(proposal_text: str, rubric: Dict) -> Dict:
    """
    Score an HVAC AI adoption proposal.
    
    Args:
        proposal_text: The proposal content to score
        rubric: Scoring criteria and weights
        
    Returns:
        Dictionary with scores and recommendations
    """
    # Clear variable names
    total_score = 0
    category_scores = {}
    
    # Use type hints
    for category, weight in rubric.items():
        score: float = analyze_category(proposal_text, category)
        category_scores[category] = score
        total_score += score * weight
    
    return {
        'total_score': total_score,
        'category_scores': category_scores,
        'grade': calculate_grade(total_score)
    }
```

### Documentation Style

```python
def analyze_category(text: str, category: str) -> float:
    """
    Analyze proposal text for a specific category.
    
    This function uses semantic analysis to evaluate how well
    the proposal addresses requirements for a given category.
    
    Args:
        text (str): Proposal text to analyze
        category (str): Category name from rubric
        
    Returns:
        float: Score from 0.0 to 1.0
        
    Raises:
        ValueError: If category is not in rubric
        
    Example:
        >>> analyze_category(proposal, "Technical Readiness")
        0.85
    """
    pass
```

### Commit Message Format

```
type(scope): subject

body

footer
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `style`: Formatting, missing semicolons, etc
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance

**Examples:**
```
feat(scoring): add contradiction detection to semantic analyzer

Implements NLP-based contradiction detection to identify 
conflicting statements in proposals.

Closes #42
```

---

## 🧪 Testing Guidelines

### Writing Tests

```python
import pytest
from scripts.score_proposal import score_proposal

def test_score_proposal_basic():
    """Test basic proposal scoring functionality."""
    proposal = """
    Business Case: We will reduce HVAC service costs by 30%
    Technical Readiness: Our team has data science expertise
    """
    
    result = score_proposal(proposal)
    
    assert result['total_score'] >= 0
    assert result['total_score'] <= 100
    assert 'grade' in result
    assert 'category_scores' in result

def test_score_proposal_empty():
    """Test scoring with empty proposal."""
    with pytest.raises(ValueError):
        score_proposal("")

def test_score_proposal_contradiction():
    """Test contradiction detection."""
    proposal = """
    We will implement AI immediately.
    We need 12 months of preparation.
    """
    
    result = score_proposal(proposal)
    
    assert 'contradictions' in result
    assert len(result['contradictions']) > 0
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=scripts tests/

# Run specific test file
pytest tests/test_scoring.py

# Run specific test
pytest tests/test_scoring.py::test_score_proposal_basic
```

---

## 📚 Commons Protocol Contribution Template

When sharing your implementation experience:

```markdown
# Pilot Implementation: [Anonymous Company ID]

## Context
- **Industry Segment**: Residential/Commercial/Industrial
- **Company Size**: <50 / 50-200 / 200-1000 / 1000+ employees
- **Region**: [General region, no specifics]
- **AI Maturity**: None / Basic / Intermediate / Advanced

## Use Case Selected
[Which AI use case from the framework]

## Implementation Timeline
- Planning: [weeks]
- Execution: [weeks]
- Measurement: [weeks]

## Results

### Quantitative
- Metric 1: [baseline] → [post-implementation] ([%change])
- Metric 2: [baseline] → [post-implementation] ([%change])
- ROI: [calculation]

### Qualitative
- What worked well
- What didn't work
- Unexpected challenges
- Key success factors

## Lessons Learned

### Do This
1. [Lesson]
2. [Lesson]

### Avoid This
1. [Anti-pattern]
2. [Anti-pattern]

## Recommendations
[What would you change for next time?]

## Data Points (optional)
- Initial Proposal Score: [X/100]
- Final Implementation Score: [Y/100]
- Time to Value: [weeks]
- Adoption Rate: [%]
```

---

## 🔍 Code Review Process

### As a Reviewer

- Be respectful and constructive
- Explain reasoning behind suggestions
- Approve when changes look good
- Ask questions when unclear

### As an Author

- Respond to all comments
- Make requested changes or explain why not
- Be open to feedback
- Thank reviewers for their time

### Review Checklist

- [ ] Code is readable and maintainable
- [ ] Tests cover new functionality
- [ ] Documentation is clear and complete
- [ ] No security vulnerabilities introduced
- [ ] Performance is acceptable
- [ ] Follows project conventions

---

## 🌐 Community Guidelines

### Code of Conduct

We are committed to providing a welcoming and inspiring community for all. Please be:

- **Respectful** - Disagreement is fine, rudeness is not
- **Collaborative** - We're all here to make things better
- **Professional** - Keep conversations focused on the work
- **Inclusive** - Welcome people of all backgrounds
- **Patient** - Remember everyone was a beginner once

### Communication Channels

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and ideas
- **Pull Requests**: Code and documentation changes
- **Email**: Private or sensitive matters

### Response Times

- Issues: We aim to respond within 3 business days
- Pull Requests: Initial review within 5 business days
- Discussions: Community-driven, no SLA

---

## 🎓 Learning Resources

### For HVAC Professionals New to AI

- [AI Fundamentals for HVAC](course-modules/01-foundations/)
- [Private AI Explained](references/private-ai-guide.md)
- [Common AI Myths](docs/AI-MYTHS.md)

### For Developers New to HVAC

- [HVAC Operations Overview](docs/HVAC-101.md)
- [Industry Terminology](docs/GLOSSARY.md)
- [Common HVAC Workflows](references/workflows.md)

### For Everyone

- [Semantic Analysis Basics](docs/SEMANTIC-ANALYSIS.md)
- [Scoring Rubric Deep Dive](references/rubric-guide.md)
- [Implementation Playbook](references/implementation-guide.md)

---

## 🏆 Recognition

### Contributors Hall of Fame

We recognize contributions in several ways:

- **Contributors File**: Listed in CONTRIBUTORS.md
- **Release Notes**: Called out in CHANGELOG.md
- **README Badges**: Displayed on the main page
- **Commons Protocol**: Implementations featured as case studies

### Levels of Contribution

- 🌱 **Seedling**: First contribution
- 🌿 **Growing**: 5+ contributions
- 🌳 **Established**: 20+ contributions
- 🏆 **Champion**: Significant impact on project

---

## ❓ Questions?

- Check the [FAQ](docs/FAQ.md)
- Search [existing issues](https://github.com/emcdo411/hvac-ai-adoption/issues)
- Start a [discussion](https://github.com/emcdo411/hvac-ai-adoption/discussions)
- Email: your.email@example.com

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

<div align="center">

**Thank you for making the HVAC AI Adoption Framework better! 🙏**

[Back to README](README.md) • [View Issues](https://github.com/emcdo411/hvac-ai-adoption/issues) • [Start Discussion](https://github.com/emcdo411/hvac-ai-adoption/discussions)

</div>
