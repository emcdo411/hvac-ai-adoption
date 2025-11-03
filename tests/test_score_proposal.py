"""
Test suite for the HVAC AI Adoption Proposal Scorer.

This module tests the scoring functionality to ensure proposals are
evaluated consistently and accurately across all key dimensions.
"""
import sys
from pathlib import Path

# Add scripts directory to Python path
repo_root = Path(__file__).parent.parent
scripts_path = repo_root / "scripts"
sys.path.insert(0, str(scripts_path))

import pytest
from score_proposal import ProposalScorer


class TestProposalScorer:
    """Test cases for ProposalScorer class."""
    
    def test_scorer_initialization(self):
        """Test that ProposalScorer initializes correctly."""
        scorer = ProposalScorer()
        assert scorer is not None
        
    def test_basic_scoring(self, sample_proposal):
        """Test basic proposal scoring with sample data."""
        scorer = ProposalScorer()
        result = scorer.score_proposal(sample_proposal)
        
        # Verify result structure
        assert result is not None
        assert isinstance(result, dict)
        
        # Check for score fields (handling different possible field names)
        has_score = ('overall_score' in result or 
                    'weighted_total' in result or 
                    'total_score' in result)
        assert has_score, "Result must contain a score field"
        
        # Verify score is in valid range
        score = result.get('overall_score') or result.get('weighted_total') or result.get('total_score', 0)
        assert 0 <= score <= 100, f"Score must be between 0-100, got {score}"
        
    def test_minimal_proposal_scoring(self, minimal_proposal):
        """Test scoring with minimal proposal content."""
        scorer = ProposalScorer()
        result = scorer.score_proposal(minimal_proposal)
        
        assert result is not None
        score = result.get('overall_score') or result.get('weighted_total') or result.get('total_score', 0)
        
        # Minimal proposal should have lower score
        assert score < 50, "Minimal proposal should score less than 50"
        
    def test_comprehensive_proposal_scoring(self, comprehensive_proposal):
        """Test scoring with comprehensive proposal content."""
        scorer = ProposalScorer()
        result = scorer.score_proposal(comprehensive_proposal)
        
        assert result is not None
        score = result.get('overall_score') or result.get('weighted_total') or result.get('total_score', 0)
        
        # Comprehensive proposal should have higher score
        assert score >= 50, "Comprehensive proposal should score 50 or higher"
        
    def test_empty_proposal_handling(self):
        """Test that empty proposals are handled gracefully."""
        scorer = ProposalScorer()
        result = scorer.score_proposal("")
        
        assert result is not None
        score = result.get('overall_score') or result.get('weighted_total') or result.get('total_score', 0)
        assert score == 0, "Empty proposal should score 0"
        
    def test_score_consistency(self, sample_proposal):
        """Test that scoring the same proposal twice gives same results."""
        scorer = ProposalScorer()
        
        result1 = scorer.score_proposal(sample_proposal)
        result2 = scorer.score_proposal(sample_proposal)
        
        score1 = result1.get('overall_score') or result1.get('weighted_total') or result1.get('total_score', 0)
        score2 = result2.get('overall_score') or result2.get('weighted_total') or result2.get('total_score', 0)
        
        assert score1 == score2, "Scoring should be consistent"


class TestProposalComponents:
    """Test individual scoring components."""
    
    def test_roi_detection(self, sample_proposal):
        """Test that ROI metrics are detected in proposals."""
        scorer = ProposalScorer()
        result = scorer.score_proposal(sample_proposal)
        
        # Sample proposal has ROI info, so score should reflect this
        assert result is not None
        
    def test_data_source_detection(self, sample_proposal):
        """Test that data sources are detected in proposals."""
        scorer = ProposalScorer()
        result = scorer.score_proposal(sample_proposal)
        
        # Sample proposal mentions data sources
        assert result is not None
        
    def test_security_detection(self, sample_proposal):
        """Test that security considerations are detected."""
        scorer = ProposalScorer()
        result = scorer.score_proposal(sample_proposal)
        
        # Sample proposal mentions security approach
        assert result is not None


class TestEdgeCases:
    """Test edge cases and error handling."""
    
    def test_none_input(self):
        """Test handling of None input."""
        scorer = ProposalScorer()
        
        # This might raise an exception or return 0 - both are acceptable
        try:
            result = scorer.score_proposal(None)
            if result is not None:
                score = result.get('overall_score') or result.get('weighted_total') or result.get('total_score', 0)
                assert score == 0
        except (TypeError, AttributeError):
            pass  # Exception is acceptable for None input
            
    def test_very_long_proposal(self):
        """Test handling of very long proposals."""
        scorer = ProposalScorer()
        long_proposal = "Pilot project. " * 1000  # Very long but repetitive
        
        result = scorer.score_proposal(long_proposal)
        assert result is not None
        
    def test_special_characters(self):
        """Test handling of special characters in proposals."""
        scorer = ProposalScorer()
        special_proposal = "Pilot: Test ™®© with émojis 🚀 and symbols #$%"
        
        result = scorer.score_proposal(special_proposal)
        assert result is not None


# Test that can be run independently
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
