"""
Unit Tests for Pandas Basics Assignment
=======================================

This file contains professional unit tests using pytest to verify that your
pandas functions work correctly.

Learning Objectives:
- Understand how unit tests work in professional development
- Learn pytest framework and assertions
- Practice test-driven development (TDD) principles
- See how to test data analysis functions

Run these tests with:
    pytest tests/test_pandas_basics.py -v

Individual test:
    pytest tests/test_pandas_basics.py::test_load_and_explore_gis_data -v

Debug failing tests:
    pytest tests/test_pandas_basics.py::test_function_name --pdb
"""

import pytest
import pandas as pd
import numpy as np
import os
import tempfile
import shutil
from pathlib import Path

# Import the functions we want to test
import sys
sys.path.insert(0, 'src')

try:
    from pandas_basics import (
        load_and_explore_gis_data,
        filter_environmental_data,
        calculate_station_statistics,
        join_station_data,
        save_processed_data,
        validate_coordinate_data,
        multi_condition_filtering,
        analyze_temporal_patterns
    )
except ImportError as e:
    pytest.fail(f"Cannot import functions from src.pandas_basics: {e}")


# ==============================================================================
# PYTEST FIXTURES - Reusable test data
# ==============================================================================

@pytest.fixture
def sample_stations_csv(tmp_path):
    """
    Create a temporary CSV file with sample station data.

    This is a pytest 'fixture' - a way to create reusable test data.
    The tmp_path fixture automatically creates a temporary directory.
    """
    csv_data = """station_id,station_name,latitude,longitude,elevation_m,station_type
STN_001,Central Park,40.7829,-73.9654,35,meteorological
STN_002,Times Square,40.7580,-73.9855,10,air_quality
STN_003,Brooklyn Bridge,40.7061,-73.9969,25,meteorological
STN_004,Queens Plaza,40.7505,-73.9370,15,air_quality
STN_005,Staten Island,40.5795,-74.1502,45,meteorological"""

    csv_file = tmp_path / "test_stations.csv"
    csv_file.write_text(csv_data)
    return str(csv_file)


@pytest.fixture
def sample_stations_df():
    """Create a sample stations DataFrame for testing."""
    return pd.DataFrame({
        'station_id': ['STN_001', 'STN_002', 'STN_003', 'STN_004', 'STN_005'],
        'station_name': ['Central Park', 'Times Square', 'Brooklyn Bridge', 'Queens Plaza', 'Staten Island'],
        'latitude': [40.7829, 40.7580, 40.7061, 40.7505, 40.5795],
        'longitude': [-73.9654, -73.9855, -73.9969, -73.9370, -74.1502],
        'elevation_m': [35, 10, 25, 15, 45],
        'station_type': ['meteorological', 'air_quality', 'meteorological', 'air_quality', 'meteorological']
    })


@pytest.fixture
def sample_readings_df():
    """Create a sample temperature readings DataFrame for testing."""
    np.random.seed(42)  # For reproducible test data
    return pd.DataFrame({
        'station_id': ['STN_001'] * 4 + ['STN_002'] * 4 + ['STN_003'] * 2,
        'date': ['2023-01-15', '2023-01-16', '2023-01-17', '2023-01-18'] * 2 + ['2023-01-15', '2023-01-16'],
        'temperature_c': [20.0, 35.0, 25.0, 5.0, 22.0, 18.0, 24.0, 27.0, 19.0, 21.0],
        'humidity_percent': [60.0, 45.0, 65.0, 50.0, 62.0, 55.0, 70.0, 75.0, 58.0, 63.0],
        'data_quality': ['good', 'poor', 'good', 'good', 'good', 'good', 'good', 'fair', 'good', 'good']
    })


# ==============================================================================
# UNIT TESTS FOR EACH FUNCTION
# ==============================================================================

class TestLoadAndExploreGISData:
    """
    Test class for load_and_explore_gis_data function.

    Grouping related tests in classes is a pytest best practice.
    """

    def test_loads_csv_successfully(self, sample_stations_csv):
        """Test that function can load a CSV file and return a DataFrame."""
        result = load_and_explore_gis_data(sample_stations_csv)

        # Assert that we get a pandas DataFrame
        assert isinstance(result, pd.DataFrame), "Function should return a pandas DataFrame"

        # Assert correct dimensions
        assert len(result) == 5, "Should load 5 rows of data"
        assert len(result.columns) == 6, "Should have 6 columns"

    def test_has_correct_columns(self, sample_stations_csv):
        """Test that loaded DataFrame has the expected columns."""
        result = load_and_explore_gis_data(sample_stations_csv)

        expected_columns = ['station_id', 'station_name', 'latitude', 'longitude', 'elevation_m', 'station_type']
        assert list(result.columns) == expected_columns, f"Columns should be {expected_columns}"

    def test_handles_missing_file_gracefully(self):
        """Test that function handles missing files appropriately."""
        result = load_and_explore_gis_data('nonexistent_file.csv')

        # Function should return None or empty DataFrame for missing files
        assert result is None or (isinstance(result, pd.DataFrame) and result.empty), \
            "Should handle missing files gracefully"

    def test_data_types_are_correct(self, sample_stations_csv):
        """Test that numeric columns are loaded as numeric types."""
        result = load_and_explore_gis_data(sample_stations_csv)

        # Check that numeric columns are actually numeric
        assert pd.api.types.is_numeric_dtype(result['latitude']), "Latitude should be numeric"
        assert pd.api.types.is_numeric_dtype(result['longitude']), "Longitude should be numeric"
        assert pd.api.types.is_numeric_dtype(result['elevation_m']), "Elevation should be numeric"


class TestFilterEnvironmentalData:
    """Test class for filter_environmental_data function."""

    def test_filters_by_temperature_range(self, sample_readings_df):
        """Test that function correctly filters by temperature range."""
        result = filter_environmental_data(sample_readings_df, min_temp=15, max_temp=30, quality='good')

        assert isinstance(result, pd.DataFrame), "Should return a DataFrame"

        # All temperatures should be within range
        if not result.empty:
            assert all(result['temperature_c'] >= 15), "All temperatures should be >= 15"
            assert all(result['temperature_c'] <= 30), "All temperatures should be <= 30"

    def test_filters_by_quality(self, sample_readings_df):
        """Test that function correctly filters by data quality."""
        result = filter_environmental_data(sample_readings_df, min_temp=0, max_temp=50, quality='good')

        if not result.empty:
            assert all(result['data_quality'] == 'good'), "All records should have 'good' quality"

    def test_returns_correct_count(self, sample_readings_df):
        """Test that filtering returns expected number of rows."""
        # With our test data: temp 15-30 AND quality='good' should keep specific rows
        result = filter_environmental_data(sample_readings_df, min_temp=15, max_temp=30, quality='good')

        # Count manually: temp 20,25,22,18,24,27,19,21 AND quality 'good'
        # Expected: 20,25,22,18,24,19,21 (7 rows)
        expected_count = 7
        assert len(result) == expected_count, f"Should return {expected_count} rows after filtering"

    def test_handles_empty_dataframe(self):
        """Test function with empty DataFrame."""
        empty_df = pd.DataFrame()
        result = filter_environmental_data(empty_df, min_temp=15, max_temp=30, quality='good')

        assert isinstance(result, pd.DataFrame), "Should return DataFrame even for empty input"
        assert result.empty, "Result should be empty for empty input"

    def test_handles_missing_columns(self):
        """Test function handles DataFrames missing required columns."""
        bad_df = pd.DataFrame({'wrong_column': [1, 2, 3]})
        result = filter_environmental_data(bad_df, min_temp=15, max_temp=30, quality='good')

        # Function should handle this gracefully (return empty DataFrame or raise informative error)
        assert isinstance(result, pd.DataFrame), "Should return DataFrame"


class TestCalculateStationStatistics:
    """Test class for calculate_station_statistics function."""

    def test_groups_by_station(self, sample_readings_df):
        """Test that function correctly groups data by station."""
        result = calculate_station_statistics(sample_readings_df)

        assert isinstance(result, pd.DataFrame), "Should return a DataFrame"

        # Should have one row per unique station
        unique_stations = sample_readings_df['station_id'].nunique()
        assert len(result) == unique_stations, f"Should have {unique_stations} rows (one per station)"

    def test_has_required_columns(self, sample_readings_df):
        """Test that result has all required statistical columns."""
        result = calculate_station_statistics(sample_readings_df)

        required_columns = ['station_id', 'reading_count', 'avg_temperature']
        for col in required_columns:
            assert col in result.columns, f"Result should contain column '{col}'"

    def test_calculations_are_correct(self, sample_readings_df):
        """Test that statistical calculations are mathematically correct."""
        result = calculate_station_statistics(sample_readings_df)

        # Test STN_001 specifically
        stn_001_data = sample_readings_df[sample_readings_df['station_id'] == 'STN_001']
        stn_001_result = result[result['station_id'] == 'STN_001']

        if not stn_001_result.empty:
            expected_avg_temp = stn_001_data['temperature_c'].mean()
            actual_avg_temp = stn_001_result['avg_temperature'].iloc[0]

            assert abs(actual_avg_temp - expected_avg_temp) < 0.01, \
                f"Average temperature calculation incorrect. Expected {expected_avg_temp}, got {actual_avg_temp}"

    def test_reading_count_correct(self, sample_readings_df):
        """Test that reading count is calculated correctly."""
        result = calculate_station_statistics(sample_readings_df)

        # STN_001 should have 4 readings in our test data
        stn_001_result = result[result['station_id'] == 'STN_001']
        if not stn_001_result.empty:
            expected_count = 4
            actual_count = stn_001_result['reading_count'].iloc[0]
            assert actual_count == expected_count, f"Reading count should be {expected_count}, got {actual_count}"


class TestJoinStationData:
    """Test class for join_station_data function."""

    def test_joins_dataframes_successfully(self, sample_stations_df, sample_readings_df):
        """Test that function successfully joins two DataFrames."""
        result = join_station_data(sample_stations_df, sample_readings_df)

        assert isinstance(result, pd.DataFrame), "Should return a DataFrame"

        # Should have same number of rows as readings (left join behavior)
        assert len(result) == len(sample_readings_df), \
            f"Result should have {len(sample_readings_df)} rows (same as readings)"

    def test_adds_station_columns(self, sample_stations_df, sample_readings_df):
        """Test that join adds columns from stations DataFrame."""
        result = join_station_data(sample_stations_df, sample_readings_df)

        # Should have columns from both DataFrames
        original_columns = set(sample_readings_df.columns)
        new_columns = set(result.columns) - original_columns

        assert len(new_columns) > 0, "Should add new columns from stations data"
        assert 'station_name' in result.columns, "Should add station_name column"
        assert 'latitude' in result.columns, "Should add latitude column"

    def test_preserves_all_readings(self, sample_stations_df, sample_readings_df):
        """Test that all readings are preserved in the join."""
        result = join_station_data(sample_stations_df, sample_readings_df)

        # All original station_ids should still be present
        original_station_ids = set(sample_readings_df['station_id'])
        result_station_ids = set(result['station_id'])

        assert original_station_ids == result_station_ids, \
            "All original station IDs should be preserved"

    def test_handles_empty_dataframes(self):
        """Test function behavior with empty DataFrames."""
        empty_df = pd.DataFrame()
        stations_df = pd.DataFrame({'station_id': ['STN_001'], 'name': ['Test']})

        result = join_station_data(stations_df, empty_df)
        assert isinstance(result, pd.DataFrame), "Should handle empty DataFrames gracefully"


class TestSaveProcessedData:
    """Test class for save_processed_data function."""

    def test_saves_file_successfully(self, sample_stations_df, tmp_path):
        """Test that function successfully saves DataFrame to CSV."""
        output_file = tmp_path / "test_output.csv"

        result = save_processed_data(sample_stations_df, str(output_file))

        # Function should return True on success
        assert result is True, "Function should return True on successful save"

        # File should exist
        assert output_file.exists(), "Output file should be created"

    def test_saved_file_is_readable(self, sample_stations_df, tmp_path):
        """Test that saved file can be read back correctly."""
        output_file = tmp_path / "test_readable.csv"

        save_processed_data(sample_stations_df, str(output_file))

        # Read the file back
        loaded_df = pd.read_csv(output_file)

        # Should have same dimensions
        assert len(loaded_df) == len(sample_stations_df), "Loaded data should have same number of rows"
        assert len(loaded_df.columns) == len(sample_stations_df.columns), \
            "Loaded data should have same number of columns"

    def test_handles_invalid_path(self, sample_stations_df):
        """Test function behavior with invalid file paths."""
        invalid_path = "/invalid/path/that/does/not/exist/file.csv"

        result = save_processed_data(sample_stations_df, invalid_path)

        # Should return False or handle gracefully
        assert result is False, "Should return False for invalid paths"

    def test_creates_directories_if_needed(self, sample_stations_df, tmp_path):
        """Test that function creates directories if they don't exist."""
        nested_path = tmp_path / "nested" / "directory" / "output.csv"

        result = save_processed_data(sample_stations_df, str(nested_path))

        if result is True:  # If function supports directory creation
            assert nested_path.exists(), "Should create nested directories"


# ==============================================================================
# INTEGRATION TESTS - Test functions working together
# ==============================================================================

class TestIntegration:
    """Integration tests that verify functions work together correctly."""

    def test_full_workflow(self, sample_stations_csv, tmp_path):
        """Test complete workflow from loading to saving data."""
        # Step 1: Load data
        stations_df = load_and_explore_gis_data(sample_stations_csv)
        assert stations_df is not None, "Should load stations data"

        # Step 2: Create some readings data for testing
        readings_df = pd.DataFrame({
            'station_id': ['STN_001', 'STN_002', 'STN_003'],
            'temperature_c': [22.0, 25.0, 18.0],
            'humidity_percent': [65.0, 70.0, 60.0],
            'data_quality': ['good', 'good', 'good']
        })

        # Step 3: Filter the data
        filtered_df = filter_environmental_data(readings_df, min_temp=15, max_temp=30, quality='good')
        assert not filtered_df.empty, "Should have filtered data"

        # Step 4: Join with stations
        joined_df = join_station_data(stations_df, filtered_df)
        assert len(joined_df) > 0, "Should have joined data"
        assert 'station_name' in joined_df.columns, "Should have station names after join"

        # Step 5: Calculate statistics
        stats_df = calculate_station_statistics(filtered_df)
        assert len(stats_df) > 0, "Should calculate statistics"

        # Step 6: Save results
        output_file = tmp_path / "integration_test_output.csv"
        result = save_processed_data(joined_df, str(output_file))
        assert result is True, "Should save final results"
        assert output_file.exists(), "Output file should exist"


class TestValidateCoordinateData:
    """Tests for coordinate data validation and quality assessment."""
    
    def test_validate_coordinate_data_basic_functionality(self):
        """Test basic coordinate validation functionality."""
        # Create test data with good coordinates
        data = {
            'station_id': ['A1', 'B2', 'C3'],
            'latitude': [40.7128, 34.0522, 41.8781],
            'longitude': [-74.0060, -118.2437, -87.6298]
        }
        df = pd.DataFrame(data)
        
        result = validate_coordinate_data(df)
        
        # Should return DataFrame
        assert isinstance(result, pd.DataFrame), "Should return DataFrame"
        
        # Should keep all good coordinates
        assert len(result) == 3, "Should keep all valid coordinates"
        
    def test_validate_coordinate_data_invalid_coordinates(self):
        """Test handling of invalid coordinate values."""
        # Create test data with invalid coordinates
        data = {
            'station_id': ['A1', 'B2', 'C3', 'D4', 'E5'],
            'latitude': [40.7128, 91.0, -95.0, 0.0, None],  # Invalid: >90, <-90, zero, null
            'longitude': [-74.0060, -118.2437, 200.0, 0.0, -74.0060]  # Invalid: >180, zero, valid
        }
        df = pd.DataFrame(data)
        
        result = validate_coordinate_data(df)
        
        # Should filter out invalid coordinates
        assert len(result) == 1, "Should only keep one valid coordinate"
        assert result.iloc[0]['station_id'] == 'A1', "Should keep the valid coordinate"
        
    def test_validate_coordinate_data_missing_columns(self):
        """Test handling when coordinate columns are missing."""
        # Test data without latitude/longitude columns
        data = {
            'station_id': ['A1', 'B2'],
            'temperature': [20.5, 18.3]
        }
        df = pd.DataFrame(data)
        
        result = validate_coordinate_data(df)
        
        # Should return original data when coordinate columns missing
        assert len(result) == len(df), "Should return original data when columns missing"
        
    def test_validate_coordinate_data_empty_input(self):
        """Test handling of empty or None input."""
        # Test with None
        result = validate_coordinate_data(None)
        assert isinstance(result, pd.DataFrame), "Should return DataFrame even with None input"
        assert len(result) == 0, "Should return empty DataFrame with None input"
        
        # Test with empty DataFrame
        empty_df = pd.DataFrame()
        result = validate_coordinate_data(empty_df)
        assert isinstance(result, pd.DataFrame), "Should return DataFrame with empty input"
        assert len(result) == 0, "Should return empty DataFrame with empty input"


class TestMultiConditionFiltering:
    """Tests for multi-condition filtering functionality."""
    
    def test_multi_condition_filtering_numeric_ranges(self):
        """Test filtering with numeric range conditions."""
        # Create test data
        data = {
            'temperature': [15, 20, 25, 30, 35],
            'humidity': [40, 50, 60, 70, 80],
            'station_id': ['A', 'B', 'C', 'D', 'E']
        }
        df = pd.DataFrame(data)
        
        # Filter config for temperature range
        filters_config = {
            'temperature': {'min': 20, 'max': 30},
            'logic': 'AND'
        }
        
        result = multi_condition_filtering(df, filters_config)
        
        # Should filter to temperature 20-30
        assert len(result) == 3, "Should return 3 rows matching temperature range"
        assert all(result['temperature'] >= 20), "All temperatures should be >= 20"
        assert all(result['temperature'] <= 30), "All temperatures should be <= 30"
        
    def test_multi_condition_filtering_include_values(self):
        """Test filtering with include conditions."""
        data = {
            'quality': ['good', 'fair', 'poor', 'good', 'fair'],
            'station_id': ['A', 'B', 'C', 'D', 'E']
        }
        df = pd.DataFrame(data)
        
        filters_config = {
            'quality': {'include': ['good', 'fair']},
            'logic': 'AND'
        }
        
        result = multi_condition_filtering(df, filters_config)
        
        # Should keep only 'good' and 'fair' quality
        assert len(result) == 4, "Should return 4 rows with good/fair quality"
        assert all(result['quality'].isin(['good', 'fair'])), "Should only have good/fair quality"
        
    def test_multi_condition_filtering_empty_config(self):
        """Test behavior with empty filter configuration."""
        data = {'temperature': [20, 25, 30], 'station_id': ['A', 'B', 'C']}
        df = pd.DataFrame(data)
        
        result = multi_condition_filtering(df, {})
        
        # Should return original data with empty config
        assert len(result) == len(df), "Should return all data with empty config"
        
    def test_multi_condition_filtering_invalid_input(self):
        """Test handling of invalid input."""
        # Test with None input
        result = multi_condition_filtering(None, {})
        assert isinstance(result, pd.DataFrame), "Should return DataFrame with None input"
        assert len(result) == 0, "Should return empty DataFrame with None input"


class TestAnalyzeTemporalPatterns:
    """Tests for temporal pattern analysis functionality."""
    
    def test_analyze_temporal_patterns_basic_functionality(self):
        """Test basic temporal analysis functionality."""
        # Create test data with dates
        dates = pd.date_range('2023-01-01', '2023-12-31', freq='D')
        data = {
            'date': dates,
            'temperature': np.random.normal(20, 5, len(dates)),
            'station_id': ['A'] * len(dates)
        }
        df = pd.DataFrame(data)
        
        result = analyze_temporal_patterns(df)
        
        # Should return dictionary with expected keys
        assert isinstance(result, dict), "Should return dictionary"
        assert 'overall_stats' in result, "Should contain overall statistics"
        assert 'monthly_patterns' in result, "Should contain monthly patterns"
        assert 'seasonal_summary' in result, "Should contain seasonal summary"
        
        # Overall stats should have expected keys
        stats = result['overall_stats']
        expected_stats = ['mean', 'min', 'max', 'std', 'count']
        for stat in expected_stats:
            assert stat in stats, f"Overall stats should contain {stat}"
            
    def test_analyze_temporal_patterns_monthly_analysis(self):
        """Test monthly pattern detection."""
        # Create data with clear seasonal pattern
        dates = pd.date_range('2023-01-01', '2023-12-31', freq='D')
        # Create seasonal temperature pattern (warmer in summer months)
        temperatures = [20 + 10 * np.sin(2 * np.pi * (i / 365.25)) for i in range(len(dates))]
        
        data = {
            'date': dates,
            'temperature': temperatures,
            'station_id': ['A'] * len(dates)
        }
        df = pd.DataFrame(data)
        
        result = analyze_temporal_patterns(df)
        
        # Should identify seasonal patterns
        seasonal = result['seasonal_summary']
        assert 'warmest_month' in seasonal, "Should identify warmest month"
        assert 'coolest_month' in seasonal, "Should identify coolest month"
        assert 'seasonal_range' in seasonal, "Should calculate seasonal range"
        
        # Seasonal range should be positive
        assert seasonal['seasonal_range'] > 0, "Seasonal range should be positive"
        
    def test_analyze_temporal_patterns_invalid_columns(self):
        """Test handling when required columns are missing."""
        data = {'station_id': ['A', 'B'], 'value': [1, 2]}
        df = pd.DataFrame(data)
        
        # Test with missing date column
        result = analyze_temporal_patterns(df, date_column='nonexistent')
        assert result == {}, "Should return empty dict when date column missing"
        
        # Test with missing value column  
        result = analyze_temporal_patterns(df, value_column='nonexistent')
        assert result == {}, "Should return empty dict when value column missing"
        
    def test_analyze_temporal_patterns_empty_input(self):
        """Test handling of empty input."""
        result = analyze_temporal_patterns(None)
        assert result == {}, "Should return empty dict with None input"
        
        result = analyze_temporal_patterns(pd.DataFrame())
        assert result == {}, "Should return empty dict with empty DataFrame"


# ==============================================================================
# PYTEST CONFIGURATION AND HELPERS
# ==============================================================================

def test_imports_work():
    """Basic test to ensure all required imports are working."""
    import pandas as pd
    import numpy as np
    assert pd.__version__ is not None, "Pandas should be installed and working"
    assert np.__version__ is not None, "NumPy should be installed and working"


# Custom pytest markers for different types of tests
pytestmark = pytest.mark.filterwarnings("ignore::RuntimeWarning")


# ==============================================================================
# LEARNING NOTES FOR STUDENTS
# ==============================================================================

"""
🎓 LEARNING NOTES: Understanding These Tests

1. **Pytest Fixtures**:
   - Functions decorated with @pytest.fixture create reusable test data
   - tmp_path fixture automatically creates temporary directories for testing

2. **Test Organization**:
   - Tests grouped in classes by function they test
   - Each test function starts with "test_"
   - Descriptive test names explain what is being tested

3. **Assert Statements**:
   - assert condition, "error message if condition fails"
   - These are the actual tests - they pass or fail based on conditions

4. **Test Types**:
   - Unit tests: Test individual functions in isolation
   - Integration tests: Test functions working together
   - Edge case tests: Test with unusual inputs (empty data, missing files)

5. **Running Tests**:
   - pytest tests/ : Run all tests
   - pytest tests/test_pandas_basics.py::TestLoadAndExploreGISData : Run specific class
   - pytest tests/ -v : Verbose output
   - pytest tests/ -s : Show print statements
   - pytest tests/ --pdb : Drop into debugger on failure

6. **Professional Benefits**:
   - Catch bugs early in development
   - Ensure code works as expected
   - Make refactoring safer
   - Document expected behavior
   - Industry standard practice

Keep these tests passing as you implement your functions!
"""
