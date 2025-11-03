#!/usr/bin/env python3
"""
HVAC AI Adoption Proposal Scoring Engine

This script analyzes HVAC AI adoption proposals and provides quantitative
scoring based on the proven rubric from 40+ pilot implementations.

Usage:
    python score_proposal.py proposal.txt
    python score_proposal.py proposal.txt --verbose
    python score_proposal.py --interactive

Author: Maurice - AI Arbitrage Coach
License: MIT
Version: 1.0.0
"""

import argparse
import json
import sys
from typing import Dict, List, Tuple
from pathlib import Path

try:
    import nltk
    import numpy as np
    from nltk.tokenize import sent_tokenize, word_tokenize
    from nltk.corpus import stopwords
except ImportError:
    print("Error: Required packages not installed.")
    print("Run: pip install nltk numpy")
    sys.exit(1)

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)
    
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)


class ProposalScorer:
    """
    Scores HVAC AI adoption proposals based on comprehensive rubric.
    """
    
    # Scoring categories and weights
    RUBRIC = {
        'business_case': {
            'weight': 25,
            'keywords': [
                'roi', 'return on investment', 'cost savings', 'revenue',
                'efficiency', 'productivity', 'competitive advantage',
                'market opportunity', 'business value', 'impact'
            ]
        },
        'technical_readiness': {
            'weight': 20,
            'keywords': [
                'infrastructure', 'systems', 'technology', 'platform',
                'integration', 'api', 'database', 'architecture',
                'technical capability', 'expertise', 'resources'
            ]
        },
        'data_foundation': {
            'weight': 20,
            'keywords': [
                'data', 'dataset', 'historical records', 'analytics',
                'data quality', 'data collection', 'measurements',
                'metrics', 'reporting', 'information systems'
            ]
        },
        'success_metrics': {
            'weight': 15,
            'keywords': [
                'kpi', 'metric', 'measurement', 'baseline', 'target',
                'goal', 'objective', 'performance indicator', 'tracking',
                'evaluation', 'success criteria', 'benchmark'
            ]
        },
        'risk_management': {
            'weight': 10,
            'keywords': [
                'risk', 'mitigation', 'contingency', 'challenge',
                'governance', 'compliance', 'security', 'privacy',
                'backup plan', 'failsafe', 'risk assessment'
            ]
        },
        'change_management': {
            'weight': 10,
            'keywords': [
                'training', 'adoption', 'communication', 'stakeholder',
                'buy-in', 'change management', 'user acceptance',
                'engagement', 'support', 'transition', 'culture'
            ]
        }
    }
    
    def __init__(self, verbose: bool = False):
        """Initialize the scorer."""
        self.verbose = verbose
        self.stop_words = set(stopwords.words('english'))
        
    def score_proposal(self, proposal_text: str) -> Dict:
        """
        Score a proposal and return detailed results.
        
        Args:
            proposal_text: The proposal content to analyze
            
        Returns:
            Dictionary with scores, grade, and recommendations
        """
        if not proposal_text or len(proposal_text.strip()) < 100:
            raise ValueError("Proposal text is too short (minimum 100 characters)")
        
        # Preprocess text
        sentences = sent_tokenize(proposal_text.lower())
        words = word_tokenize(proposal_text.lower())
        words = [w for w in words if w.isalnum() and w not in self.stop_words]
        
        # Score each category
        category_scores = {}
        category_details = {}
        
        for category, config in self.RUBRIC.items():
            score, details = self._score_category(
                proposal_text, sentences, words, category, config
            )
            category_scores[category] = score
            category_details[category] = details
        
        # Calculate total score
        total_score = sum(category_scores.values())
        
        # Determine grade
        grade = self._calculate_grade(total_score)
        
        # Identify gaps
        gaps = self._identify_gaps(category_scores, category_details)
        
        # Generate recommendations
        recommendations = self._generate_recommendations(gaps, category_scores)
        
        # Detect contradictions
        contradictions = self._detect_contradictions(sentences)
        
        return {
            'total_score': round(total_score, 1),
            'grade': grade,
            'percentile': self._score_to_percentile(total_score),
            'category_scores': category_scores,
            'category_details': category_details,
            'gaps': gaps,
            'recommendations': recommendations,
            'contradictions': contradictions,
            'word_count': len(words),
            'sentence_count': len(sentences)
        }
    
    def _score_category(
        self, 
        text: str, 
        sentences: List[str], 
        words: List[str],
        category: str, 
        config: Dict
    ) -> Tuple[float, Dict]:
        """Score a single category."""
        max_score = config['weight']
        keywords = config['keywords']
        
        # Count keyword matches
        matches = sum(1 for keyword in keywords if keyword in text.lower())
        keyword_coverage = min(matches / len(keywords), 1.0)
        
        # Calculate sentence coverage
        relevant_sentences = [
            s for s in sentences 
            if any(kw in s for kw in keywords)
        ]
        sentence_coverage = len(relevant_sentences) / len(sentences)
        
        # Calculate depth score (how much is discussed)
        depth_score = min(len(relevant_sentences) / 3, 1.0)  # 3+ sentences = full depth
        
        # Combine factors
        coverage_score = (keyword_coverage * 0.4 + 
                         sentence_coverage * 0.3 + 
                         depth_score * 0.3)
        
        score = coverage_score * max_score
        
        details = {
            'max_score': max_score,
            'keywords_matched': matches,
            'total_keywords': len(keywords),
            'relevant_sentences': len(relevant_sentences),
            'coverage': round(coverage_score * 100, 1)
        }
        
        if self.verbose:
            print(f"\n{category.replace('_', ' ').title()}:")
            print(f"  Score: {score:.1f}/{max_score}")
            print(f"  Coverage: {details['coverage']}%")
            print(f"  Keywords matched: {matches}/{len(keywords)}")
        
        return score, details
    
    def _calculate_grade(self, score: float) -> str:
        """Convert numeric score to letter grade."""
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'
    
    def _score_to_percentile(self, score: float) -> str:
        """Convert score to percentile range."""
        if score >= 90:
            return '95th+ (Top 10%)'
        elif score >= 80:
            return '80th-95th (Top 20%)'
        elif score >= 70:
            return '60th-80th (Top 40%)'
        elif score >= 60:
            return '40th-60th (Middle)'
        else:
            return 'Below 40th'
    
    def _identify_gaps(
        self, 
        category_scores: Dict[str, float],
        category_details: Dict[str, Dict]
    ) -> List[Dict]:
        """Identify missing or weak elements."""
        gaps = []
        
        for category, score in category_scores.items():
            max_score = self.RUBRIC[category]['weight']
            if score < max_score * 0.7:  # Less than 70% of max
                coverage = category_details[category]['coverage']
                gaps.append({
                    'category': category.replace('_', ' ').title(),
                    'current_score': round(score, 1),
                    'max_score': max_score,
                    'gap': round(max_score - score, 1),
                    'coverage': coverage
                })
        
        return sorted(gaps, key=lambda x: x['gap'], reverse=True)
    
    def _generate_recommendations(
        self, 
        gaps: List[Dict],
        category_scores: Dict[str, float]
    ) -> List[str]:
        """Generate actionable recommendations."""
        recommendations = []
        
        for gap in gaps[:3]:  # Top 3 gaps
            category = gap['category'].lower().replace(' ', '_')
            
            if category == 'business_case':
                recommendations.append(
                    "Add quantifiable business outcomes with specific ROI projections. "
                    "Include baseline metrics and target improvements."
                )
            elif category == 'technical_readiness':
                recommendations.append(
                    "Detail your existing technical infrastructure and integration plans. "
                    "Address system compatibility and technical resource availability."
                )
            elif category == 'data_foundation':
                recommendations.append(
                    "Document your current data landscape including quality, volume, and accessibility. "
                    "Outline data collection and preparation strategies."
                )
            elif category == 'success_metrics':
                recommendations.append(
                    "Define specific, measurable KPIs with baseline and target values. "
                    "Include measurement methodology and reporting frequency."
                )
            elif category == 'risk_management':
                recommendations.append(
                    "Identify potential risks and develop mitigation strategies. "
                    "Address data privacy, security, and compliance requirements."
                )
            elif category == 'change_management':
                recommendations.append(
                    "Create a stakeholder engagement plan with training strategy. "
                    "Address adoption challenges and communication approaches."
                )
        
        # Add general recommendations based on overall score
        total = sum(category_scores.values())
        if total < 75:
            recommendations.insert(0,
                "🎯 Priority: Reach 75+ score threshold for pilot success. "
                "Focus on the largest gaps first."
            )
        
        return recommendations
    
    def _detect_contradictions(self, sentences: List[str]) -> List[Dict]:
        """Detect potential contradictions in the proposal."""
        contradictions = []
        
        # Simple contradiction patterns
        positive_patterns = ['will', 'can', 'have', 'ready', 'available']
        negative_patterns = ['cannot', 'lack', 'missing', 'need', 'require']
        
        for i, sent in enumerate(sentences):
            has_positive = any(p in sent for p in positive_patterns)
            has_negative = any(p in sent for p in negative_patterns)
            
            if has_positive and has_negative:
                contradictions.append({
                    'sentence_num': i + 1,
                    'text': sent[:100] + '...' if len(sent) > 100 else sent,
                    'type': 'mixed_signals'
                })
        
        return contradictions[:5]  # Return top 5
    
    def format_report(self, results: Dict) -> str:
        """Format results as a readable report."""
        report = []
        report.append("=" * 60)
        report.append("HVAC AI ADOPTION PROPOSAL SCORE")
        report.append("=" * 60)
        report.append(f"\nOverall Score: {results['total_score']}/100 (Grade: {results['grade']})")
        report.append(f"Percentile: {results['percentile']}")
        report.append(f"\nProposal Stats:")
        report.append(f"  - {results['word_count']} words")
        report.append(f"  - {results['sentence_count']} sentences")
        
        report.append(f"\n{'Category':<25} {'Score':<10} {'Coverage'}")
        report.append("-" * 60)
        for category, score in results['category_scores'].items():
            details = results['category_details'][category]
            category_name = category.replace('_', ' ').title()
            max_score = details['max_score']
            coverage = details['coverage']
            report.append(f"{category_name:<25} {score:.1f}/{max_score:<5} {coverage}%")
        
        if results['gaps']:
            report.append("\n" + "=" * 60)
            report.append("GAPS IDENTIFIED")
            report.append("=" * 60)
            for gap in results['gaps']:
                report.append(f"\n{gap['category']}:")
                report.append(f"  Current: {gap['current_score']}/{gap['max_score']}")
                report.append(f"  Gap: {gap['gap']} points")
                report.append(f"  Coverage: {gap['coverage']}%")
        
        if results['recommendations']:
            report.append("\n" + "=" * 60)
            report.append("RECOMMENDATIONS")
            report.append("=" * 60)
            for i, rec in enumerate(results['recommendations'], 1):
                report.append(f"\n{i}. {rec}")
        
        if results['contradictions']:
            report.append("\n" + "=" * 60)
            report.append("POTENTIAL CONTRADICTIONS")
            report.append("=" * 60)
            for contradiction in results['contradictions']:
                report.append(f"\nSentence {contradiction['sentence_num']}:")
                report.append(f"  {contradiction['text']}")
        
        report.append("\n" + "=" * 60)
        report.append("SCORING INTERPRETATION")
        report.append("=" * 60)
        report.append(f"\nGrade {results['grade']} - ", end='')
        if results['grade'] == 'A':
            report.append("Excellent! Ready for implementation.")
        elif results['grade'] == 'B':
            report.append("Good. Minor improvements recommended.")
        elif results['grade'] == 'C':
            report.append("Acceptable. Address key gaps before proceeding.")
        elif results['grade'] == 'D':
            report.append("Needs work. Significant improvements required.")
        else:
            report.append("Insufficient. Major revision needed.")
        
        report.append(f"\n\n⚠️  Minimum 75/100 recommended for pilot success")
        report.append("=" * 60)
        
        return '\n'.join(report)


def main():
    """Main entry point for the scoring tool."""
    parser = argparse.ArgumentParser(
        description='Score HVAC AI adoption proposals',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s proposal.txt
  %(prog)s proposal.txt --verbose
  %(prog)s proposal.txt --json --output results.json
  %(prog)s --interactive
        """
    )
    
    parser.add_argument(
        'proposal_file',
        nargs='?',
        help='Path to proposal text file'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Show detailed scoring breakdown'
    )
    parser.add_argument(
        '-j', '--json',
        action='store_true',
        help='Output results as JSON'
    )
    parser.add_argument(
        '-o', '--output',
        help='Save results to file'
    )
    parser.add_argument(
        '-i', '--interactive',
        action='store_true',
        help='Interactive mode'
    )
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 1.0.0'
    )
    
    args = parser.parse_args()
    
    scorer = ProposalScorer(verbose=args.verbose)
    
    # Interactive mode
    if args.interactive:
        print("=" * 60)
        print("HVAC AI PROPOSAL SCORING - INTERACTIVE MODE")
        print("=" * 60)
        print("\nPaste your proposal text (press Ctrl+D when done):\n")
        
        try:
            proposal_text = sys.stdin.read()
        except KeyboardInterrupt:
            print("\n\nCancelled.")
            sys.exit(0)
    
    # File mode
    elif args.proposal_file:
        proposal_path = Path(args.proposal_file)
        if not proposal_path.exists():
            print(f"Error: File not found: {args.proposal_file}")
            sys.exit(1)
        
        with open(proposal_path, 'r', encoding='utf-8') as f:
            proposal_text = f.read()
    
    else:
        parser.print_help()
        sys.exit(1)
    
    # Score the proposal
    try:
        results = scorer.score_proposal(proposal_text)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    # Output results
    if args.json:
        output = json.dumps(results, indent=2)
        if args.output:
            with open(args.output, 'w') as f:
                f.write(output)
            print(f"Results saved to: {args.output}")
        else:
            print(output)
    else:
        report = scorer.format_report(results)
        if args.output:
            with open(args.output, 'w') as f:
                f.write(report)
            print(f"Report saved to: {args.output}")
        else:
            print(report)


if __name__ == '__main__':
    main()
