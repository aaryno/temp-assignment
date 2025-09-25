#!/usr/bin/env python3
"""
Base Grading Engine for GIST 604B Course Assignments

Provides standardized grading interface, JSON output structure, and professional
development context for all course assignments. Ensures consistent student
experience and maintainable grading infrastructure.

Author: GIST 604B Course Infrastructure
Course: GIST 604B - Open Source GIS Programming
"""

import json
import os
import sys
import subprocess
from abc import ABC, abstractmethod
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class BaseGradingEngine(ABC):
    """
    Standardized grading engine interface for all GIST 604B assignments.
    
    Provides consistent JSON output structure, professional development context,
    and standardized feedback mechanisms across all assignment types.
    """
    
    # Required fields in all grade reports
    REQUIRED_REPORT_FIELDS = [
        'assignment', 'module', 'total_points', 'possible_points',
        'percentage', 'letter_grade', 'timestamp', 'performance_summary',
        'professional_context', 'detailed_breakdown'
    ]
    
    # Standard letter grade thresholds
    GRADE_THRESHOLDS = {
        'A': 90.0,
        'B': 80.0, 
        'C': 70.0,
        'D': 60.0,
        'F': 0.0
    }
    
    # Standard environment variables for CI/CD
    STANDARD_ENV_VARS = [
        'ASSIGNMENT_SCORE', 'POSSIBLE_POINTS', 'GRADE_PERCENTAGE',
        'LETTER_GRADE', 'TESTS_PASSED', 'TESTS_TOTAL'
    ]
    
    def __init__(self, assignment_name: str, module_name: str, 
                 total_possible_points: int, assignment_dir: Path = None, 
                 verbose: bool = False):
        """
        Initialize base grading engine.
        
        Args:
            assignment_name: Name of the assignment (e.g., 'pandas-basics')
            module_name: Full module name (e.g., 'Module 5 - Python GIS Programming')
            total_possible_points: Maximum points possible for assignment
            assignment_dir: Directory containing assignment files
            verbose: Enable detailed logging output
        """
        self.assignment_name = assignment_name
        self.module_name = module_name
        self.total_possible_points = total_possible_points
        self.assignment_dir = assignment_dir or Path(__file__).parent.parent
        self.verbose = verbose
        
        # Initialize core data structures
        self.test_results = {}
        self.grade_report = {}
        self.component_categories = {}
        
        # Performance tracking
        self.start_time = datetime.now()
        
        if self.verbose:
            logger.info(f"Initialized {self.assignment_name} grading engine")
    
    @abstractmethod
    def define_component_categories(self) -> Dict[str, Dict[str, Any]]:
        """
        Define the specific components/functions/tasks for this assignment.
        
        Returns:
            Dictionary mapping component IDs to configuration:
            {
                'component_id': {
                    'name': 'Human readable name',
                    'points': 5,
                    'description': 'What this component tests',
                    'concepts': ['list', 'of', 'concepts'],
                    'professional_skill': 'Industry skill demonstrated'
                }
            }
        """
        pass
    
    @abstractmethod
    def run_tests(self) -> Dict[str, Any]:
        """
        Execute assignment-specific tests and return results.
        
        Returns:
            Dictionary mapping component IDs to test results:
            {
                'component_id': {
                    'passed': bool,
                    'score': int,
                    'error': str or None,
                    'implementation_detected': bool,
                    'execution_time': float
                }
            }
        """
        pass
    
    @abstractmethod
    def get_professional_context(self) -> Dict[str, Any]:
        """
        Provide professional development context for this assignment.
        
        Returns:
            Dictionary with professional context:
            {
                'skills_assessed': ['list of technical skills'],
                'industry_relevance': 'Career relevance description',
                'career_preparation': 'Job roles enabled',
                'next_steps': 'Preparation for subsequent learning'
            }
        """
        pass
    
    def calculate_letter_grade(self, percentage: float) -> str:
        """
        Calculate letter grade from percentage using standard thresholds.
        
        Args:
            percentage: Grade percentage (0-100)
            
        Returns:
            Letter grade (A, B, C, D, F)
        """
        for grade, threshold in self.GRADE_THRESHOLDS.items():
            if percentage >= threshold:
                return grade
        return 'F'
    
    def calculate_grade(self) -> Dict[str, Any]:
        """
        Calculate comprehensive grade report with standardized structure.
        
        Returns:
            Complete grade report dictionary
        """
        if self.verbose:
            logger.info("Calculating comprehensive grade report...")
        
        # Ensure tests have been run
        if not self.test_results:
            logger.warning("No test results found, running tests...")
            self.test_results = self.run_tests()
        
        # Ensure component categories are defined
        if not self.component_categories:
            self.component_categories = self.define_component_categories()
        
        # Calculate totals
        total_points = sum(result.get('score', 0) for result in self.test_results.values())
        percentage = (total_points / self.total_possible_points) * 100
        letter_grade = self.calculate_letter_grade(percentage)
        
        # Count performance metrics
        components_passing = sum(1 for result in self.test_results.values() 
                               if result.get('passed', False))
        components_implemented = sum(1 for result in self.test_results.values()
                                   if result.get('implementation_detected', True))
        total_components = len(self.component_categories)
        
        # Create standardized grade report
        self.grade_report = {
            'assignment': self.assignment_name,
            'module': self.module_name,
            'total_points': total_points,
            'possible_points': self.total_possible_points,
            'percentage': round(percentage, 1),
            'letter_grade': letter_grade,
            'timestamp': datetime.now().isoformat(),
            
            'performance_summary': {
                'components_passing': components_passing,
                'total_components': total_components,
                'components_implemented': components_implemented,
                'implementation_rate': round((components_implemented / total_components) * 100, 1),
                'pass_rate': round((components_passing / total_components) * 100, 1)
            },
            
            'professional_context': self.get_professional_context(),
            
            'detailed_breakdown': {},
            
            'improvement_recommendations': [],
            
            'execution_summary': {
                'grading_time': (datetime.now() - self.start_time).total_seconds(),
                'grading_engine_version': '2.0.0',
                'standardized_output': True
            }
        }
        
        # Add detailed breakdown for each component
        self._populate_detailed_breakdown()
        
        # Generate improvement recommendations
        self._generate_improvement_recommendations()
        
        # Validate report structure
        self._validate_report_structure()
        
        if self.verbose:
            logger.info(f"Grade calculation complete: {total_points}/{self.total_possible_points} points ({percentage:.1f}%) - {letter_grade}")
        
        return self.grade_report
    
    def _populate_detailed_breakdown(self):
        """Populate detailed breakdown section of grade report."""
        for component_id, component_config in self.component_categories.items():
            test_result = self.test_results.get(component_id, {})
            
            self.grade_report['detailed_breakdown'][component_id] = {
                'component_name': component_config['name'],
                'points_earned': test_result.get('score', 0),
                'points_possible': component_config['points'],
                'status': self._determine_component_status(test_result),
                'concepts_tested': component_config.get('concepts', []),
                'professional_skill': component_config.get('professional_skill', ''),
                'feedback': self._generate_component_feedback(component_id, test_result, component_config),
                'execution_time': test_result.get('execution_time', 0.0)
            }
    
    def _determine_component_status(self, test_result: Dict[str, Any]) -> str:
        """Determine standardized status for a component."""
        if test_result.get('passed', False):
            return 'passed'
        elif test_result.get('implementation_detected', True):
            return 'implemented_with_errors'
        else:
            return 'not_implemented'
    
    def _generate_component_feedback(self, component_id: str, test_result: Dict[str, Any], 
                                   component_config: Dict[str, Any]) -> str:
        """Generate detailed feedback for a component."""
        if test_result.get('passed', False):
            return f"✅ Excellent implementation of {component_config['name']}"
        
        feedback_parts = []
        
        if not test_result.get('implementation_detected', True):
            feedback_parts.append(f"❌ {component_config['name']} function not found or not properly defined")
            feedback_parts.append(f"💡 Implement: {component_config['description']}")
        else:
            feedback_parts.append(f"⚠️ {component_config['name']} implemented but has issues")
            if test_result.get('error'):
                feedback_parts.append(f"Error: {test_result['error']}")
        
        # Add concept-level guidance
        if component_config.get('concepts'):
            concepts = ', '.join(component_config['concepts'])
            feedback_parts.append(f"🔍 Review concepts: {concepts}")
        
        return ' | '.join(feedback_parts)
    
    def _generate_improvement_recommendations(self):
        """Generate specific improvement recommendations."""
        recommendations = []
        
        for component_id, test_result in self.test_results.items():
            if not test_result.get('passed', False):
                component_config = self.component_categories[component_id]
                
                if not test_result.get('implementation_detected', True):
                    recommendations.append(
                        f"Implement {component_config['name']}: {component_config['description']}"
                    )
                else:
                    concepts = component_config.get('concepts', [])
                    if concepts:
                        recommendations.append(
                            f"Fix {component_config['name']} - focus on: {', '.join(concepts[:3])}"
                        )
        
        # Add general recommendations based on performance
        pass_rate = self.grade_report['performance_summary']['pass_rate']
        if pass_rate < 50:
            recommendations.append("Review assignment instructions and examples carefully")
            recommendations.append("Test functions individually before running full test suite")
        elif pass_rate < 80:
            recommendations.append("Focus on edge cases and error handling in your implementations")
        
        self.grade_report['improvement_recommendations'] = recommendations
    
    def _validate_report_structure(self):
        """Validate that grade report contains all required fields."""
        missing_fields = []
        
        for field in self.REQUIRED_REPORT_FIELDS:
            if field not in self.grade_report:
                missing_fields.append(field)
        
        if missing_fields:
            logger.warning(f"Missing required report fields: {missing_fields}")
        
        # Validate nested structures
        required_nested = {
            'performance_summary': ['components_passing', 'total_components', 'implementation_rate'],
            'professional_context': ['skills_assessed', 'industry_relevance', 'career_preparation']
        }
        
        for parent_field, required_subfields in required_nested.items():
            if parent_field in self.grade_report:
                for subfield in required_subfields:
                    if subfield not in self.grade_report[parent_field]:
                        logger.warning(f"Missing {parent_field}.{subfield}")
    
    def set_environment_variables(self):
        """Set standardized environment variables for CI/CD integration."""
        if not self.grade_report:
            self.calculate_grade()
        
        # Core grading variables
        os.environ['ASSIGNMENT_SCORE'] = str(self.grade_report['total_points'])
        os.environ['POSSIBLE_POINTS'] = str(self.grade_report['possible_points'])
        os.environ['GRADE_PERCENTAGE'] = str(self.grade_report['percentage'])
        os.environ['LETTER_GRADE'] = self.grade_report['letter_grade']
        os.environ['TESTS_PASSED'] = str(self.grade_report['performance_summary']['components_passing'])
        os.environ['TESTS_TOTAL'] = str(self.grade_report['performance_summary']['total_components'])
        
        # Additional performance metrics
        os.environ['IMPLEMENTATION_RATE'] = str(self.grade_report['performance_summary']['implementation_rate'])
        os.environ['PASS_RATE'] = str(self.grade_report['performance_summary']['pass_rate'])
        
        # Assignment identification
        os.environ['ASSIGNMENT_NAME'] = self.assignment_name
        os.environ['MODULE_NAME'] = self.module_name
        
        if self.verbose:
            logger.info("Environment variables set for CI/CD integration")
    
    def save_grade_report(self, output_file: str = 'grade-report.json') -> Path:
        """
        Save grade report to JSON file with standardized formatting.
        
        Args:
            output_file: Output filename
            
        Returns:
            Path to saved report file
        """
        if not self.grade_report:
            self.calculate_grade()
        
        output_path = self.assignment_dir / output_file
        
        with open(output_path, 'w') as f:
            json.dump(self.grade_report, f, indent=2, ensure_ascii=False)
        
        if self.verbose:
            logger.info(f"Grade report saved to {output_path}")
        
        return output_path
    
    def display_grade_summary(self):
        """Display formatted grade summary to console."""
        if not self.grade_report:
            self.calculate_grade()
        
        report = self.grade_report
        
        print("\n" + "="*60)
        print(f"🎓 {report['assignment'].upper()} - GRADE REPORT")
        print("="*60)
        print(f"📚 Module: {report['module']}")
        print(f"📊 Grade: {report['letter_grade']} ({report['percentage']}%)")
        print(f"🎯 Points: {report['total_points']}/{report['possible_points']}")
        print(f"✅ Passing Components: {report['performance_summary']['components_passing']}/{report['performance_summary']['total_components']}")
        
        # Show detailed breakdown
        print("\n📋 Component Breakdown:")
        for component_id, details in report['detailed_breakdown'].items():
            status_icon = "✅" if details['status'] == 'passed' else "⚠️" if details['status'] == 'implemented_with_errors' else "❌"
            print(f"   {status_icon} {details['component_name']}: {details['points_earned']}/{details['points_possible']} points")
        
        # Show recommendations if any
        if report['improvement_recommendations']:
            print(f"\n💡 Recommendations:")
            for i, rec in enumerate(report['improvement_recommendations'], 1):
                print(f"   {i}. {rec}")
        
        # Show professional context
        print(f"\n🚀 Professional Skills: {', '.join(report['professional_context']['skills_assessed'][:3])}...")
        print(f"🎯 Industry Relevance: {report['professional_context']['industry_relevance']}")
        
        print("="*60)
    
    def get_exit_code(self) -> int:
        """
        Get appropriate exit code for CI/CD systems.
        
        Returns:
            0 for passing grades (70%+), 1 for failing grades
        """
        if not self.grade_report:
            self.calculate_grade()
        
        return 0 if self.grade_report['percentage'] >= 70 else 1


class PythonFunctionGradingEngine(BaseGradingEngine):
    """
    Specialized grading engine for Python function-based assignments.
    
    Provides additional functionality for detecting function implementations,
    parsing pytest results, and analyzing Python code quality.
    """
    
    def detect_function_implementation(self, function_name: str, source_file: Path = None) -> bool:
        """
        Detect if a function is implemented in the source code.
        
        Args:
            function_name: Name of function to detect
            source_file: Path to source file (defaults to src/ directory scan)
            
        Returns:
            True if function is detected and appears implemented
        """
        if not source_file:
            # Scan src directory for Python files
            src_dir = self.assignment_dir / 'src'
            python_files = list(src_dir.glob('*.py'))
        else:
            python_files = [source_file]
        
        for py_file in python_files:
            try:
                with open(py_file, 'r') as f:
                    content = f.read()
                    
                # Look for function definition
                if f"def {function_name}(" in content:
                    # Check if it's more than just a pass statement
                    lines = content.split('\n')
                    in_function = False
                    function_lines = []
                    
                    for line in lines:
                        if f"def {function_name}(" in line:
                            in_function = True
                            continue
                        
                        if in_function:
                            if line.strip() and not line.startswith(' ') and not line.startswith('\t'):
                                break
                            function_lines.append(line)
                    
                    # Analyze function content
                    non_empty_lines = [line.strip() for line in function_lines if line.strip() and not line.strip().startswith('#')]
                    
                    # Function is considered implemented if it has more than just docstring and pass
                    if len(non_empty_lines) > 2:  # More than just docstring and pass
                        return True
                    
                    # Check for actual implementation patterns
                    implementation_indicators = ['return', '=', 'if', 'for', 'while', 'try', 'with']
                    for line in non_empty_lines:
                        if any(indicator in line for indicator in implementation_indicators):
                            if 'pass' not in line and 'None' not in line:
                                return True
                    
            except Exception as e:
                logger.warning(f"Error analyzing {py_file}: {e}")
                continue
        
        return False
    
    def parse_pytest_results(self, pytest_output: str = None, results_file: Path = None) -> Dict[str, Any]:
        """
        Parse pytest results into standardized test result format.
        
        Args:
            pytest_output: Raw pytest output text
            results_file: Path to pytest JSON results file
            
        Returns:
            Parsed test results dictionary
        """
        results = {}
        
        if results_file and results_file.exists():
            try:
                with open(results_file, 'r') as f:
                    pytest_data = json.load(f)
                
                # Parse pytest JSON format
                for test in pytest_data.get('tests', []):
                    test_name = test.get('nodeid', '').split('::')[-1]
                    # Map test names to component IDs
                    component_id = self._map_test_to_component(test_name)
                    
                    if component_id:
                        results[component_id] = {
                            'passed': test.get('outcome') == 'passed',
                            'error': test.get('longrepr', '') if test.get('outcome') != 'passed' else None,
                            'execution_time': test.get('duration', 0.0)
                        }
                
            except Exception as e:
                logger.error(f"Error parsing pytest results file: {e}")
        
        return results
    
    def _map_test_to_component(self, test_name: str) -> Optional[str]:
        """Map pytest test name to component ID."""
        # This should be implemented by subclasses based on their test naming conventions
        return None


# Example usage and testing
if __name__ == '__main__':
    print("🧪 GIST 604B Base Grading Engine")
    print("This is a base class - implement specific grading engines by inheriting from BaseGradingEngine")
    print("See module-5 assignments for example implementations")
