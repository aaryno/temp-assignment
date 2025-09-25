#!/usr/bin/env python3
"""
Pandas Basics Assignment - Automated Grading Script (Streamlined 2-Hour Approach)

Calculates grades for 4 core pandas functions (4.5 points each = 18 total points)
Ultra-streamlined assessment focused on essential competency within 2-hour constraint.
Generates detailed grade reports and sets environment variables for CI/CD.

Usage:
    python calculate_grade.py
    python calculate_grade.py --output grade-report.json
    python calculate_grade.py --verbose
"""

import json
import os
import sys
import argparse
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional


class PandasGradingEngine:
    """Streamlined grading engine for Pandas Basics assignment (2-hour approach)."""

    # Define the 5 pandas + container function categories (10 points total)
    FUNCTION_CATEGORIES = {
        'load_and_explore': {
            'name': 'load_and_explore_gis_data',
            'points': 2,
            'description': 'Load CSV data and perform basic exploratory analysis',
            'concepts': ['pandas.read_csv', 'DataFrame.info()', 'basic data exploration'],
            'test_method': 'test_load_and_explore_gis_data',
            'professional_skill': 'Essential data loading and basic analysis'
        },
        'filter_environmental': {
            'name': 'filter_environmental_data',
            'points': 2,
            'description': 'Filter data using simple conditions',
            'concepts': ['boolean indexing', 'simple filtering'],
            'test_method': 'test_filter_environmental_data',
            'professional_skill': 'Core data filtering competency'
        },
        'calculate_statistics': {
            'name': 'calculate_station_statistics',
            'points': 2,
            'description': 'Calculate basic summary statistics',
            'concepts': ['DataFrame.groupby()', 'basic aggregate functions'],
            'test_method': 'test_calculate_station_statistics',
            'professional_skill': 'Essential statistical operations'
        },
        'join_station_data': {
            'name': 'join_station_data',
            'points': 5,
            'description': 'Perform basic data joins',
            'concepts': ['DataFrame.merge()', 'simple table joins'],
            'test_method': 'test_join_station_data',
            'professional_skill': 'Foundation data integration skills'
        },
        'save_processed': {
            'name': 'save_processed_data',
            'points': 5,
            'description': 'Save processed data to output files',
            'concepts': ['DataFrame.to_csv()', 'file path management', 'data validation'],
            'test_method': 'test_save_processed_data',
            'professional_skill': 'Essential data output and persistence'
        },
        'containerized_environment': {
            'name': 'setup_containerized_environment',
            'points': 5,
            'description': 'Configure and validate containerized development environment',
            'concepts': ['environment validation', 'package management', 'container benefits'],
            'test_method': 'test_setup_containerized_environment',
            'professional_skill': 'Modern containerized development workflow'
        }
    }

    TOTAL_POSSIBLE_POINTS = 25

    def __init__(self, assignment_dir: Path = None, verbose: bool = False):
        self.assignment_dir = assignment_dir or Path(__file__).parent.parent
        self.verbose = verbose
        self.test_results = {}
        self.grade_report = {}

    def run_tests(self) -> Dict[str, Any]:
        """Run the automated test suite and capture results."""
        if self.verbose:
            print("🧪 Running Pandas assignment test suite...")

        try:
            # Run pytest with comprehensive output
            cmd = [
                'python', '-m', 'pytest',
                str(self.assignment_dir / 'tests' / 'test_pandas_basics.py'),
                '-v', '--tb=short'
            ]

            result = subprocess.run(cmd, capture_output=True, text=True, cwd=self.assignment_dir)

            # Parse test output to determine which tests passed/failed
            self.parse_test_output(result.stdout, result.stderr, result.returncode)

            if self.verbose:
                print(f"✅ Tests completed with return code: {result.returncode}")
                print(f"📊 Passed: {self.count_passed_tests()}/{len(self.FUNCTION_CATEGORIES)}")
                print(f"📝 Functions implemented: {self.count_implemented_functions()}/{len(self.FUNCTION_CATEGORIES)}")

            return self.test_results

        except Exception as e:
            if self.verbose:
                print(f"❌ Error running tests: {e}")
            # Create default failed results
            for category in self.FUNCTION_CATEGORIES:
                self.test_results[category] = {
                    'passed': False,
                    'error': str(e),
                    'score': 0,
                    'function_implemented': False
                }
            return self.test_results

    def parse_test_output(self, stdout: str, stderr: str, return_code: int):
        """Parse pytest output to determine test results."""
        # Initialize all tests as failed
        for category in self.FUNCTION_CATEGORIES:
            self.test_results[category] = {
                'passed': False,
                'error': None,
                'score': 0,
                'function_implemented': False
            }

        # Parse stdout for test results
        lines = stdout.split('\n')
        for line in lines:
            line = line.strip()

            # Look for test results
            for category, config in self.FUNCTION_CATEGORIES.items():
                test_method = config['test_method']
                if test_method in line:
                    function_implemented = self.is_function_implemented(config['name'])

                    if 'PASSED' in line or '✓' in line:
                        self.test_results[category] = {
                            'passed': True,
                            'error': None,
                            'score': config['points'],
                            'function_implemented': function_implemented,
                            'concepts_mastered': config['concepts']
                        }
                        if self.verbose:
                            print(f"✅ {config['name']}: PASSED ({config['points']} points)")

                    elif 'FAILED' in line or '✗' in line:
                        error_msg = 'Test failed - check function logic and implementation'
                        if not function_implemented:
                            error_msg = 'Function not implemented - replace pass statement with code'

                        # Partial credit for implementation attempt (proportional to new point scale)
                        partial_score = 1.0 if function_implemented else 0

                        self.test_results[category] = {
                            'passed': False,
                            'error': error_msg,
                            'score': partial_score,
                            'function_implemented': function_implemented,
                            'partial_credit_reason': 'Implementation attempt' if function_implemented else None
                        }

                        if self.verbose:
                            status = "IMPLEMENTED BUT INCORRECT" if function_implemented else "NOT IMPLEMENTED"
                            print(f"❌ {config['name']}: {status} ({partial_score} points)")

                    elif 'SKIPPED' in line:
                        self.test_results[category] = {
                            'passed': False,
                            'error': 'Test skipped - check for import or syntax errors',
                            'score': 0,
                            'function_implemented': function_implemented
                        }

    def is_function_implemented(self, function_name: str) -> bool:
        """Check if a function has been implemented (not just 'pass')."""
        try:
            src_file = self.assignment_dir / 'src' / 'pandas_basics.py'
            if not src_file.exists():
                return False

            content = src_file.read_text()

            # Look for function definition
            function_start = f"def {function_name}("
            if function_start not in content:
                return False

            # Extract function body
            lines = content.split('\n')
            in_function = False
            function_body_lines = []

            for line in lines:
                if function_start in line:
                    in_function = True
                    continue
                elif in_function:
                    if line.strip().startswith('def ') or (line.strip() and not line.startswith(' ') and not line.startswith('\t')):
                        break
                    if line.strip():
                        function_body_lines.append(line.strip())

            # Check if function body is more than just 'pass' or docstring
            non_trivial_lines = [line for line in function_body_lines
                               if line != 'pass' and not line.startswith('"""') and not line.startswith("'''")]

            return len(non_trivial_lines) > 0

        except Exception:
            return False

    def count_passed_tests(self) -> int:
        """Count how many tests passed."""
        return sum(1 for result in self.test_results.values() if result.get('passed', False))

    def count_implemented_functions(self) -> int:
        """Count how many functions have been implemented."""
        return sum(1 for result in self.test_results.values() if result.get('function_implemented', False))

    def calculate_grade(self) -> Dict[str, Any]:
        """Calculate comprehensive grade report."""
        total_score = sum(result.get('score', 0) for result in self.test_results.values())
        percentage = (total_score / self.TOTAL_POSSIBLE_POINTS) * 100

        # Determine letter grade
        if percentage >= 90:
            letter_grade = 'A'
        elif percentage >= 80:
            letter_grade = 'B'
        elif percentage >= 70:
            letter_grade = 'C'
        elif percentage >= 60:
            letter_grade = 'D'
        else:
            letter_grade = 'F'

        # Create detailed grade report (streamlined 2-hour approach)
        self.grade_report = {
            'assignment': 'pandas-basics-streamlined',
            'module': 'Module 5 - Python GIS Programming (2-Hour Ultra-Efficient)',
            'total_points': round(total_score, 2),
            'possible_points': self.TOTAL_POSSIBLE_POINTS,
            'percentage': round(percentage, 1),
            'letter_grade': letter_grade,
            'timestamp': datetime.now().isoformat(),

            'performance_summary': {
                'functions_implemented': self.count_implemented_functions(),
                'tests_passed': self.count_passed_tests(),
                'total_functions': len(self.FUNCTION_CATEGORIES),
                'implementation_rate': round((self.count_implemented_functions() / len(self.FUNCTION_CATEGORIES)) * 100, 1),
                'time_efficiency_focus': '2-hour maximum constraint with essential skills only'
            },

            'detailed_breakdown': {},

            'skills_assessment': {
                'core_data_loading': 'competent' if self.test_results.get('load_and_explore', {}).get('passed') else 'developing',
                'basic_filtering': 'competent' if self.test_results.get('filter_environmental', {}).get('passed') else 'developing',
                'essential_statistics': 'competent' if self.test_results.get('calculate_statistics', {}).get('passed') else 'developing',
                'foundation_integration': 'competent' if self.test_results.get('join_station_data', {}).get('passed') else 'developing'
            },

            'professional_context': {
                'skills_assessed': [
                    'Core pandas DataFrame operations for data manipulation',
                    'Essential data filtering and basic analysis techniques',
                    'Foundation statistical operations and data grouping',
                    'Basic data integration and joining capabilities'
                ],
                'industry_relevance': 'Essential foundation skills for data-driven roles in GIS, environmental analysis, and business intelligence',
                'career_preparation': 'Foundation competency enabling success in subsequent advanced modules and entry-level data analyst positions',
                'next_steps': 'Ready for spatial analysis with GeoPandas and advanced programming assignments',
                'efficiency_focus': 'Maximum learning impact achieved within 2-hour time investment'
            },

            'improvement_recommendations': []
        }

        # Add detailed breakdown for each function
        for category, config in self.FUNCTION_CATEGORIES.items():
            result = self.test_results.get(category, {})
            self.grade_report['detailed_breakdown'][category] = {
                'function_name': config['name'],
                'points_earned': round(result.get('score', 0), 2),
                'points_possible': config['points'],
                'status': 'passed' if result.get('passed') else ('implemented' if result.get('function_implemented') else 'not_implemented'),
                'concepts_tested': config['concepts'],
                'professional_skill': config['professional_skill'],
                'error_message': result.get('error'),
                'streamlined_focus': 'Essential competency within 2-hour constraint'
            }

        # Add improvement recommendations
        for category, result in self.test_results.items():
            if not result.get('passed', False):
                config = self.FUNCTION_CATEGORIES[category]
                if not result.get('function_implemented', False):
                    self.grade_report['improvement_recommendations'].append(
                        f"Implement {config['name']} function: {config['description']}"
                    )
                else:
                    self.grade_report['improvement_recommendations'].append(
                        f"Fix logic in {config['name']} function - check {', '.join(config['concepts'])}"
                    )

        return self.grade_report

    def set_environment_variables(self):
        """Set environment variables for GitHub Actions integration."""
        grade_report = self.grade_report or self.calculate_grade()

        # Set key environment variables
        os.environ['ASSIGNMENT_SCORE'] = str(grade_report['total_points'])
        os.environ['POSSIBLE_POINTS'] = str(grade_report['possible_points'])
        os.environ['GRADE_PERCENTAGE'] = str(grade_report['percentage'])
        os.environ['LETTER_GRADE'] = grade_report['letter_grade']
        os.environ['TESTS_PASSED'] = str(grade_report['performance_summary']['tests_passed'])
        os.environ['TESTS_TOTAL'] = str(grade_report['performance_summary']['total_functions'])
        os.environ['FUNCTIONS_IMPLEMENTED'] = str(grade_report['performance_summary']['functions_implemented'])
        os.environ['IMPLEMENTATION_RATE'] = str(grade_report['performance_summary']['implementation_rate'])

        # Professional development metrics
        os.environ['DATA_LOADING_SKILL'] = grade_report['skills_assessment']['data_loading_proficiency']
        os.environ['DATA_FILTERING_SKILL'] = grade_report['skills_assessment']['data_filtering_proficiency']
        os.environ['STATISTICAL_ANALYSIS_SKILL'] = grade_report['skills_assessment']['statistical_analysis_proficiency']
        os.environ['DATA_INTEGRATION_SKILL'] = grade_report['skills_assessment']['data_integration_proficiency']

        if self.verbose:
            print(f"🌐 Environment variables set:")
            print(f"   ASSIGNMENT_SCORE={os.environ['ASSIGNMENT_SCORE']}")
            print(f"   GRADE_PERCENTAGE={os.environ['GRADE_PERCENTAGE']}")
            print(f"   LETTER_GRADE={os.environ['LETTER_GRADE']}")

    def save_grade_report(self, output_file: str = 'grade-report.json'):
        """Save detailed grade report to JSON file."""
        grade_report = self.grade_report or self.calculate_grade()

        output_path = self.assignment_dir / output_file
        with open(output_path, 'w') as f:
            json.dump(grade_report, f, indent=2)

        if self.verbose:
            print(f"📊 Grade report saved to {output_path}")

        return output_path


def main():
    """Main grading execution function."""
    parser = argparse.ArgumentParser(description='Grade Pandas Basics Assignment')
    parser.add_argument('--output', '-o', default='grade-report.json',
                       help='Output file for grade report (default: grade-report.json)')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose output')
    parser.add_argument('--directory', '-d', type=Path,
                       help='Assignment directory (default: parent of script directory)')

    args = parser.parse_args()

    # Initialize grading engine
    grading_engine = PandasGradingEngine(
        assignment_dir=args.directory,
        verbose=args.verbose
    )

    if args.verbose:
        print("🎯 PANDAS BASICS ASSIGNMENT GRADING")
        print("=" * 50)
        print(f"📁 Assignment directory: {grading_engine.assignment_dir}")
        print(f"📊 Total possible points: {grading_engine.TOTAL_POSSIBLE_POINTS}")
        print(f"🧪 Functions to test: {len(grading_engine.FUNCTION_CATEGORIES)}")
        print()

    # Run tests and calculate grade
    grading_engine.run_tests()
    grade_report = grading_engine.calculate_grade()

    # Set environment variables for CI/CD
    grading_engine.set_environment_variables()

    # Save grade report
    grading_engine.save_grade_report(args.output)

    # Display summary
    print(f"🎓 ASSIGNMENT GRADE: {grade_report['total_points']}/{grade_report['possible_points']} points ({grade_report['percentage']}%) - {grade_report['letter_grade']}")
    print(f"🧪 TESTS PASSED: {grade_report['performance_summary']['tests_passed']}/{grade_report['performance_summary']['total_functions']}")
    print(f"💻 FUNCTIONS IMPLEMENTED: {grade_report['performance_summary']['functions_implemented']}/{grade_report['performance_summary']['total_functions']}")

    # Return appropriate exit code for CI/CD
    return 0 if grade_report['percentage'] >= 70 else 1


if __name__ == '__main__':
    sys.exit(main())
