"""
Pytest configuration and fixtures for HVAC AI Adoption testing.
"""
import pytest


@pytest.fixture
def sample_proposal():
    """
    Sample proposal text for testing.
    
    Returns a realistic HVAC AI adoption proposal with key elements:
    - Clear pilot scope (Dispatch Optimization)
    - Quantified ROI metrics
    - Data sources specified
    - Security approach defined
    - KPIs and baselines
    - Realistic timeline
    """
    return """
    Pilot: Dispatch Optimization with CRM integration
    ROI: 6-month payback, 30-40% efficiency improvement
    Data: CRM exports, work orders, GPS API
    Security: Private AI, on-premises deployment
    KPI: Baseline established, 90-day monitoring
    Feasibility: Prototype in 4 weeks, 90-day deployment
    """


@pytest.fixture
def minimal_proposal():
    """Minimal proposal for edge case testing."""
    return "Pilot: Basic AI test"


@pytest.fixture
def comprehensive_proposal():
    """Comprehensive proposal with all sections."""
    return """
    Project: HVAC Service Route Optimization with Predictive Maintenance
    
    Pilot Scope:
    Start with dispatch optimization for our 50-truck service fleet.
    Integration with existing CRM and GPS tracking systems.
    Focus on reducing drive time and improving first-call resolution.
    
    ROI Analysis:
    - 6-month payback period projected
    - 30-40% improvement in route efficiency
    - 15-20% reduction in fuel costs
    -  annual savings expected
    
    Data Sources:
    - CRM exports (service history, customer data)
    - Work order database (5 years historical data)
    - GPS API for real-time tracking
    - Weather API for seasonal planning
    
    Security & Privacy:
    - Private AI deployment on-premises
    - No customer data leaves our network
    - HIPAA-compliant data handling
    - Regular security audits
    
    KPIs & Baselines:
    - Current baseline: 8.2 calls/day per technician
    - Target: 10+ calls/day (20% improvement)
    - First-call resolution: 75% → 85%
    - Customer satisfaction: 4.2 → 4.5+ stars
    
    Timeline & Feasibility:
    - Week 1-4: Prototype development
    - Week 5-8: Pilot with 10 trucks
    - Week 9-12: Evaluation and refinement
    - 90-day full deployment to all trucks
    
    Team & Resources:
    - Project Manager (dedicated)
    - 2 developers (part-time)
    - Operations lead (advisor)
    - Budget:  for pilot phase
    """
