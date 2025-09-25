#!/usr/bin/env python3
"""
M3A2: Pandas Environmental Analysis - BaseGradingEngine Implementation
GIST 604B - Module 3: Python GIS Containerization

Automated grading system for pandas data analysis assignment.
Extends BaseGradingEngine for standardized grading across all assignments.

Usage:
    python grade_assignment.py
    python grade_assignment.py --verbose
"""

import sys
import os
import logging
from pathlib import Path
from typing import Dict, Any, List
import subprocess
import json

# Add the scripts directory to Python path for BaseGradingEngine import
sys.path.insert(0, str(Path(__file__).parent))

from BaseGradingEngine import BaseGradingEngine

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


class PandasAnalysisGrader(BaseGradingEngine):
    """Pandas Environmental Analysis grading system extending BaseGradingEngine."""

    def __init__(self, assignment_dir: str = ".", verbose: bool = True):
        """Initialize the pandas analysis grader."""
        super().__init__(
            assignment_name="Pandas Environmental Analysis",
            module_name="Module 3 - Python GIS Containerization", 
            total_possible_points=10,
            verbose=verbose
        )
        self.assignment_dir = Path(assignment_dir).resolve()
        self.src_dir = self.assignment_dir / "src"
        self.tests_dir = self.assignment_dir / "tests"
        self.pandas_file = self.src_dir / "pandas_basics.py"

    def get_professional_context(self) -> Dict[str, Any]:
        """Return professional development context for pandas data analysis."""
        return {
            "title": "Pandas for Environmental Data Analysis",
            "skills_assessed": [
                "Data Loading and Exploration (CSV)",
                "Data Filtering and Subset Selection", 
                "Statistical Summarization (groupby)",
                "Data Merging/Joining",
                "Data Export and Persistence",
                "Python Programming Best Practices",
                "Unit Testing with Pytest"
            ],
            "industry_relevance": """
            Pandas is a cornerstone library in environmental data science, GIS, and remote sensing.
            Professionals use it daily for:
            - Cleaning and preparing sensor data (e.g., air quality, water quality).
            - Analyzing climate model outputs and environmental impact assessments.
            - Integrating diverse tabular datasets with spatial information.
            - Generating reports and visualizations for stakeholders.
            Mastery of pandas is crucial for any career involving data-driven environmental analysis.
            """,
            "career_preparation": """
            This assignment directly prepares you for roles such as:
            - Environmental Data Scientist
            - GIS Analyst/Developer
            - Remote Sensing Specialist
            - Hydrologist/Climatologist (data-focused)
            - Urban Planner (demographic/land use analysis)
            The skills developed are highly transferable across various sectors requiring robust data handling.
            """
        }

    def define_component_categories(self) -> Dict[str, Dict[str, Any]]:
        """Define the grading components for pandas assignment."""
        return {
            "load_and_explore": {
                "name": "Load and Explore Data",
                "points": 2,
                "description": "Load CSV data and perform basic exploratory analysis"
            },
            "filter_data": {
                "name": "Filter Environmental Data", 
                "points": 2,
                "description": "Filter data using boolean indexing and conditions"
            },
            "calculate_statistics": {
                "name": "Calculate Station Statistics",
                "points": 2,
                "description": "Calculate summary statistics using groupby operations"
            },
            "join_data": {
                "name": "Join Station Data",
                "points": 2,
                "description": "Join datasets using pandas merge functionality"
            },
            "save_data": {
                "name": "Save Processed Data",
                "points": 1,
                "description": "Save processed data to CSV format"
            },
            "code_quality": {
                "name": "Code Quality",
                "points": 1,
                "description": "Clean, readable code with proper structure"
            }
        }

    def run_tests(self) -> Dict[str, Any]:
        """Run all tests and return results."""
        results = {
            "load_and_explore": self._assess_load_and_explore(),
            "filter_data": self._assess_filter_data(), 
            "calculate_statistics": self._assess_calculate_statistics(),
            "join_data": self._assess_join_data(),
            "save_data": self._assess_save_data(),
            "code_quality": self._assess_code_quality()
        }
        
        return results

    def assess_assignment(self) -> Dict[str, Any]:
        """Assess the pandas assignment implementation."""
        return self.run_tests()

    def _assess_load_and_explore(self) -> Dict[str, Any]:
        """Assess load_and_explore_gis_data function (2 points)."""
        score = 0
        feedback = []
        max_points = 2
        
        try:
            # Check if pandas_basics.py exists
            if not self.pandas_file.exists():
                feedback.append("❌ src/pandas_basics.py file not found")
                return {"score": 0, "max_points": max_points, "feedback": feedback}
            
            # Run specific test for load_and_explore function
            result = self._run_pytest_test("TestLoadAndExploreGISData")
            if result["passed"]:
                score = max_points
                feedback.append("✅ Load and explore function implemented correctly")
            else:
                feedback.append(f"❌ Load and explore test failed: {result['error']}")
                
        except Exception as e:
            feedback.append(f"❌ Error assessing load and explore: {str(e)}")
            
        return {"score": score, "max_points": max_points, "feedback": feedback}

    def _assess_filter_data(self) -> Dict[str, Any]:
        """Assess filter_environmental_data function (2 points)."""
        score = 0
        feedback = []
        max_points = 2
        
        try:
            result = self._run_pytest_test("TestFilterEnvironmentalData")
            if result["passed"]:
                score = max_points
                feedback.append("✅ Filter data function implemented correctly")
            else:
                feedback.append(f"❌ Filter data test failed: {result['error']}")
                
        except Exception as e:
            feedback.append(f"❌ Error assessing filter data: {str(e)}")
            
        return {"score": score, "max_points": max_points, "feedback": feedback}

    def _assess_calculate_statistics(self) -> Dict[str, Any]:
        """Assess calculate_station_statistics function (2 points)."""
        score = 0
        feedback = []
        max_points = 2
        
        try:
            result = self._run_pytest_test("TestCalculateStationStatistics")
            if result["passed"]:
                score = max_points
                feedback.append("✅ Calculate statistics function implemented correctly")
            else:
                feedback.append(f"❌ Calculate statistics test failed: {result['error']}")
                
        except Exception as e:
            feedback.append(f"❌ Error assessing calculate statistics: {str(e)}")
            
        return {"score": score, "max_points": max_points, "feedback": feedback}

    def _assess_join_data(self) -> Dict[str, Any]:
        """Assess join_station_data function (2 points)."""
        score = 0
        feedback = []
        max_points = 2
        
        try:
            result = self._run_pytest_test("TestJoinStationData")
            if result["passed"]:
                score = max_points
                feedback.append("✅ Join data function implemented correctly")
            else:
                feedback.append(f"❌ Join data test failed: {result['error']}")
                
        except Exception as e:
            feedback.append(f"❌ Error assessing join data: {str(e)}")
            
        return {"score": score, "max_points": max_points, "feedback": feedback}

    def _assess_save_data(self) -> Dict[str, Any]:
        """Assess save_processed_data function (1 point)."""
        score = 0
        feedback = []
        max_points = 1
        
        try:
            result = self._run_pytest_test("TestSaveProcessedData")
            if result["passed"]:
                score = max_points
                feedback.append("✅ Save data function implemented correctly")
            else:
                feedback.append(f"❌ Save data test failed: {result['error']}")
                
        except Exception as e:
            feedback.append(f"❌ Error assessing save data: {str(e)}")
            
        return {"score": score, "max_points": max_points, "feedback": feedback}

    def _assess_code_quality(self) -> Dict[str, Any]:
        """Assess overall code quality (1 point)."""
        score = 0
        feedback = []
        max_points = 1
        
        try:
            if not self.pandas_file.exists():
                feedback.append("❌ pandas_basics.py file not found")
                return {"score": 0, "max_points": max_points, "feedback": feedback}
            
            # Check file size (should have meaningful implementation)
            file_size = self.pandas_file.stat().st_size
            if file_size < 500:  # Minimum reasonable implementation size
                feedback.append("❌ Implementation appears incomplete (file too small)")
                return {"score": 0, "max_points": max_points, "feedback": feedback}
            
            # Check for basic code structure
            content = self.pandas_file.read_text(encoding='utf-8', errors='ignore')
            
            # Look for pandas import
            if 'import pandas' in content or 'from pandas' in content:
                score += 0.3
                feedback.append("✅ Pandas import found")
            else:
                feedback.append("❌ Missing pandas import")
            
            # Look for function definitions
            required_functions = [
                'load_and_explore_gis_data',
                'filter_environmental_data', 
                'calculate_station_statistics',
                'join_station_data',
                'save_processed_data'
            ]
            
            functions_found = 0
            for func in required_functions:
                if f'def {func}' in content:
                    functions_found += 1
            
            if functions_found >= 4:
                score += 0.4
                feedback.append(f"✅ Found {functions_found}/5 required functions")
            else:
                feedback.append(f"❌ Only found {functions_found}/5 required functions")
            
            # Look for basic documentation/comments
            if '#' in content or '"""' in content:
                score += 0.3
                feedback.append("✅ Code includes comments/documentation")
            else:
                feedback.append("❌ Code lacks comments/documentation")
                
            score = min(score, max_points)  # Cap at max points
            
        except Exception as e:
            feedback.append(f"❌ Error assessing code quality: {str(e)}")
            
        return {"score": score, "max_points": max_points, "feedback": feedback}

    def _run_pytest_test(self, test_name: str) -> Dict[str, Any]:
        """Run a specific pytest test and return results."""
        try:
            # Set up environment for Docker container
            env = os.environ.copy()
            env['PYTHONPATH'] = str(self.assignment_dir) + ":" + env.get('PYTHONPATH', '')
            
            # Change to assignment directory for proper test execution
            cmd = [
                "python", "-m", "pytest", 
                f"tests/test_pandas_basics.py::{test_name}",
                "-v", "--tb=short", "--no-header"
            ]
            
            result = subprocess.run(
                cmd,
                cwd=self.assignment_dir,
                capture_output=True,
                text=True,
                timeout=60,  # Increased timeout for Docker
                env=env
            )
            
            passed = result.returncode == 0
            error_msg = result.stdout + result.stderr if not passed else ""
            
            return {
                "passed": passed,
                "error": error_msg,
                "stdout": result.stdout,
                "stderr": result.stderr
            }
            
        except subprocess.TimeoutExpired:
            return {
                "passed": False,
                "error": "Test execution timed out",
                "stdout": "",
                "stderr": ""
            }
        except Exception as e:
            return {
                "passed": False,
                "error": f"Test execution error: {str(e)}",
                "stdout": "",
                "stderr": ""
            }


def main():
    """Main grading function."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Grade M3A2 Pandas Environmental Analysis Assignment')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
    parser.add_argument('--assignment-dir', default='.', help='Assignment directory path')
    
    args = parser.parse_args()
    
    try:
        grader = PandasAnalysisGrader(
            assignment_dir=args.assignment_dir,
            verbose=args.verbose
        )
        
        # Calculate grade using BaseGradingEngine
        grade_result = grader.calculate_grade()
        
        # Print results
        print(f"\n📊 Grade: {grade_result['letter_grade']} ({grade_result['percentage']:.1f}%)")
        print(f"🎯 Points: {grade_result['total_points']:.1f}/{grade_result['possible_points']}")
        
        # Set environment variables for CI/CD
        if 'GITHUB_ENV' in os.environ:
            with open(os.environ['GITHUB_ENV'], 'a') as f:
                f.write(f"GRADE_PERCENTAGE={grade_result['percentage']:.1f}\n")
                f.write(f"LETTER_GRADE={grade_result['letter_grade']}\n")
                f.write(f"TOTAL_SCORE={grade_result['total_points']:.2f}\n")
                f.write(f"MAX_POINTS={grade_result['possible_points']}\n")
        
        return 0 if grade_result['percentage'] >= 70 else 1
        
    except Exception as e:
        logger.error(f"Grading failed: {e}")
        return 1


if __name__ == "__main__":
    import os
    sys.exit(main())
