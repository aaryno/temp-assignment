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
            assignment_name="Pandas Environmental Analysis with AI Integration",
            module_name="Module 3 - Python GIS Containerization", 
            total_possible_points=15,
            verbose=verbose
        )
        self.assignment_dir = Path(assignment_dir).resolve()
        self.src_dir = self.assignment_dir / "src"
        self.tests_dir = self.assignment_dir / "tests"
        self.pandas_file = self.src_dir / "pandas_basics.py"

    def get_professional_context(self) -> str:
        """Return professional development context for pandas data analysis."""
        return """
        **Professional Development Context - Pandas Data Analysis:**
        
        **Industry Applications:**
        - Environmental consultants use pandas for processing sensor data and generating reports
        - Urban planners analyze demographic and land use data for city planning decisions  
        - Research institutions process large environmental datasets for climate studies
        - GIS companies integrate pandas with spatial libraries for comprehensive analysis
        - Government agencies use pandas for transparent, reproducible data analysis workflows
        
        **Career Skills Developed:**
        - Data loading and exploration (essential for any data-driven GIS role)
        - Data filtering and quality assessment (critical for reliable analysis)
        - Statistical analysis and aggregation (foundation for spatial statistics)
        - Data joining and integration (combining multiple data sources)
        - Professional code organization and testing practices
        
        **Technical Competencies:**
        - Python pandas library proficiency (industry standard for data analysis)
        - Unit testing with pytest (professional development practice)
        - CSV data processing (common GIS data format)
        - Data validation and quality control
        - Reproducible analysis workflows
        """

    def assess_assignment(self) -> Dict[str, Any]:
        """Assess the pandas assignment implementation."""
        results = {
            # Core Functions (10 points)
            "load_and_explore": self._assess_load_and_explore(),           # 2 points
            "filter_data": self._assess_filter_data(),                     # 2 points
            "calculate_statistics": self._assess_calculate_statistics(),   # 2 points
            "join_data": self._assess_join_data(),                        # 2 points
            "save_data": self._assess_save_data(),                        # 2 points
            
            # Advanced Functions (3 points)  
            "validate_coordinates": self._assess_validate_coordinates(),   # 1 point
            "multi_condition_filtering": self._assess_multi_condition_filtering(), # 1 point
            "temporal_analysis": self._assess_temporal_analysis(),        # 1 point
            
            # AI Learning Reflection (2 points)
            "ai_reflection": self._assess_ai_reflection(),               # 2 points
            
            # Code Quality
            "code_quality": self._assess_code_quality()                  # Bonus
        }
        
        return results

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
            result = self._run_pytest_test("test_load_and_explore_gis_data")
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
            result = self._run_pytest_test("test_filter_environmental_data")
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
            result = self._run_pytest_test("test_calculate_station_statistics")
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
            result = self._run_pytest_test("test_join_station_data")
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
            result = self._run_pytest_test("test_save_processed_data")
            if result["passed"]:
                score = max_points
                feedback.append("✅ Save data function implemented correctly")
            else:
                feedback.append(f"❌ Save data test failed: {result['error']}")
                
        except Exception as e:
            feedback.append(f"❌ Error assessing save data: {str(e)}")
            
        return {"score": score, "max_points": max_points, "feedback": feedback}

    def _assess_validate_coordinates(self) -> Dict[str, Any]:
        """Assess validate_coordinate_data function (1 point).""" 
        score = 0
        feedback = []
        max_points = 1
        
        try:
            result = self._run_pytest_test("test_validate_coordinate_data")
            if result["passed"]:
                score = max_points
                feedback.append("✅ Coordinate validation function implemented correctly")
            else:
                feedback.append(f"❌ Coordinate validation test failed: {result['error']}")
                
        except Exception as e:
            feedback.append(f"❌ Error assessing coordinate validation: {str(e)}")
            
        return {"score": score, "max_points": max_points, "feedback": feedback}

    def _assess_multi_condition_filtering(self) -> Dict[str, Any]:
        """Assess multi_condition_filtering function (1 point)."""
        score = 0
        feedback = []
        max_points = 1
        
        try:
            result = self._run_pytest_test("test_multi_condition_filtering")
            if result["passed"]:
                score = max_points
                feedback.append("✅ Multi-condition filtering function implemented correctly")
            else:
                feedback.append(f"❌ Multi-condition filtering test failed: {result['error']}")
                
        except Exception as e:
            feedback.append(f"❌ Error assessing multi-condition filtering: {str(e)}")
            
        return {"score": score, "max_points": max_points, "feedback": feedback}

    def _assess_temporal_analysis(self) -> Dict[str, Any]:
        """Assess analyze_temporal_patterns function (1 point)."""
        score = 0
        feedback = []
        max_points = 1
        
        try:
            result = self._run_pytest_test("test_analyze_temporal_patterns")
            if result["passed"]:
                score = max_points
                feedback.append("✅ Temporal analysis function implemented correctly")
            else:
                feedback.append(f"❌ Temporal analysis test failed: {result['error']}")
                
        except Exception as e:
            feedback.append(f"❌ Error assessing temporal analysis: {str(e)}")
            
        return {"score": score, "max_points": max_points, "feedback": feedback}

    def _assess_ai_reflection(self) -> Dict[str, Any]:
        """Assess AI learning reflection document (2 points)."""
        score = 0
        feedback = []
        max_points = 2
        
        try:
            reflection_file = self.assignment_dir / "AI_LEARNING_REFLECTION.md"
            
            if not reflection_file.exists():
                feedback.append("❌ AI_LEARNING_REFLECTION.md file not found")
                return {"score": 0, "max_points": max_points, "feedback": feedback}
            
            # Read reflection content
            content = reflection_file.read_text(encoding='utf-8')
            word_count = len(content.split())
            
            if word_count < 500:
                feedback.append(f"❌ Reflection too short ({word_count} words, minimum 500)")
                score = max_points * 0.5  # Half credit for effort
            else:
                score = max_points
                feedback.append(f"✅ AI learning reflection completed ({word_count} words)")
                
                # Check for key topics (bonus feedback)
                topics_covered = 0
                if "ask mode" in content.lower() or "copilot chat" in content.lower():
                    topics_covered += 1
                if "agent mode" in content.lower() or "inline suggest" in content.lower():
                    topics_covered += 1
                if "edit mode" in content.lower():
                    topics_covered += 1
                if "pandas" in content.lower():
                    topics_covered += 1
                if "learning" in content.lower():
                    topics_covered += 1
                    
                if topics_covered >= 4:
                    feedback.append("✨ Excellent coverage of AI learning topics")
                elif topics_covered >= 2:
                    feedback.append("✓ Good reflection on AI learning experience")
                    
        except Exception as e:
            feedback.append(f"❌ Error assessing AI reflection: {str(e)}")
            
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
                'validate_coordinate_data',
                'multi_condition_filtering', 
                'analyze_temporal_patterns',
                'filter_environmental_data',
                'calculate_station_statistics',
                'join_station_data',
                'save_processed_data'
            ]
            
            functions_found = 0
            for func in required_functions:
                if f'def {func}' in content:
                    functions_found += 1
            
            if functions_found >= 6:
                score += 0.4
                feedback.append(f"✅ Found {functions_found}/8 required functions")
            elif functions_found >= 4:
                score += 0.2
                feedback.append(f"⚠️ Found {functions_found}/8 required functions (partial credit)")
            else:
                feedback.append(f"❌ Only found {functions_found}/8 required functions")
            
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
            # Change to assignment directory for proper test execution
            cmd = [
                "python", "-m", "pytest", 
                f"tests/test_pandas_basics.py::{test_name}",
                "-v", "--tb=short"
            ]
            
            result = subprocess.run(
                cmd,
                cwd=self.assignment_dir,
                capture_output=True,
                text=True,
                timeout=30
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
        print(f"🎯 Points: {grade_result['total_score']:.1f}/{grade_result['max_points']}")
        
        # Set environment variables for CI/CD
        if 'GITHUB_ENV' in os.environ:
            with open(os.environ['GITHUB_ENV'], 'a') as f:
                f.write(f"GRADE_PERCENTAGE={grade_result['percentage']:.1f}\n")
                f.write(f"LETTER_GRADE={grade_result['letter_grade']}\n")
                f.write(f"TOTAL_SCORE={grade_result['total_score']:.2f}\n")
                f.write(f"MAX_POINTS={grade_result['max_points']}\n")
        
        return 0 if grade_result['percentage'] >= 70 else 1
        
    except Exception as e:
        logger.error(f"Grading failed: {e}")
        return 1


if __name__ == "__main__":
    import os
    sys.exit(main())
