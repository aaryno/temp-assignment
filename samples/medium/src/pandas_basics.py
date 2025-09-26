"""
Pandas Basics for GIS Data Analysis - Student Implementation
===========================================================

Welcome! This module teaches you essential pandas skills for working with GIS data.

Pandas is Python's most popular library for working with tabular data (like CSV files).
Think of it as Excel, but with the power of Python programming!

Don't worry if you're new to pandas - we've provided Jupyter notebooks in the `notebooks/`
directory to guide you through building each function step by step.

What you'll learn:
- How to load CSV files into pandas DataFrames
- How to explore and understand your data
- How to filter data based on conditions
- How to calculate statistics and group data
- How to join datasets together
- How to save your results

ASSIGNMENT INSTRUCTIONS:
========================
1. Complete each function below by replacing the TODO comments with your code
2. Use the Jupyter notebooks in `notebooks/` to learn how to build each function
3. Test your functions as you go: `uv run pytest tests/test_pandas_basics.py::test_function_name -v`
4. Make sure all tests pass before submitting: `uv run pytest tests/ -v`

IMPORTANT: The notebooks show you HOW to build each function, but you must implement
the actual code here in this file to pass the unit tests!
"""

import pandas as pd
import numpy as np
import os
from pathlib import Path


def load_and_explore_gis_data(file_path):
    """
    LOAD AND EXPLORE GIS DATA (Like opening a spreadsheet and getting familiar with it)

    This function loads a CSV file and shows you important information about the data,
    like how many rows and columns it has, what the columns are called, and what the
    first few rows look like.

    Think of this as your first step whenever you get a new dataset - you need to
    understand what you're working with before you can analyze it!

    📚 Learning Resource: See `notebooks/01_function_load_and_explore_gis_data.ipynb`
    🧪 Test Command: `uv run pytest tests/test_pandas_basics.py::test_load_and_explore_gis_data -v`

    Args:
        file_path (str): Path to the CSV file (like 'data/weather_stations.csv')

    Returns:
        pandas.DataFrame: The loaded data as a DataFrame (like a spreadsheet in Python)

    Example:
        >>> df = load_and_explore_gis_data('data/weather_stations.csv')
        Dataset loaded successfully!
        Shape: (15, 5) - 15 rows and 5 columns
        ...
    """

    print('Loading data...')
    if not os.path.exists(file_path):
        print('File not found')
        return None
    
    try:
        df = pd.read_csv(file_path)
        print(f'Loaded {len(df)} rows')
        print(df.head())
        return df
    except Exception as e:
        print(f'Error: {e}')
        return None


def filter_environmental_data(df, min_temp=15, max_temp=30, quality="good"):
    """
    FILTER ENVIRONMENTAL DATA (Like applying filters in Excel to show only certain data)

    This function filters temperature readings to show only data that meets your criteria:
    - Temperature within a specified range (default: 15-30°C)
    - Only data with a specific quality level (default: "good")

    This is essential for data cleaning - removing outliers and poor quality measurements!

    📚 Learning Resource: See `notebooks/02_function_filter_environmental_data.ipynb`
    🧪 Test Command: `uv run pytest tests/test_pandas_basics.py::test_filter_environmental_data -v`

    Args:
        df (pandas.DataFrame): The environmental data to filter (must have 'temperature_c' and 'data_quality' columns)
        min_temp (float): Minimum temperature threshold in Celsius (default: 15)
        max_temp (float): Maximum temperature threshold in Celsius (default: 30)
        quality (str): Required data quality level (default: "good")

    Returns:
        pandas.DataFrame: Filtered data meeting all specified conditions

    Example:
        >>> filtered = filter_environmental_data(df, min_temp=10, max_temp=35, quality="good")
        Filtering data...
        Original dataset: 500 rows
        After filtering: 247 rows kept, 253 rows removed
        ...
    """

    if df is None or df.empty:
        return pd.DataFrame()
    
    # Basic filtering with minimal validation
    required_cols = ['temperature_c', 'data_quality']
    if not all(col in df.columns for col in required_cols):
        print('Missing required columns')
        return pd.DataFrame()
    
    filtered = df[(df['temperature_c'] >= min_temp) & 
                  (df['temperature_c'] <= max_temp) & 
                  (df['data_quality'] == quality)]
    
    print(f'Filtered to {len(filtered)} records')
    return filtered


def calculate_station_statistics(df):
    """
    CALCULATE STATION STATISTICS (Like creating a summary report for each weather station)

    This function groups temperature readings by station and calculates summary statistics
    for each station. This is essential for understanding patterns across different
    monitoring locations!

    📚 Learning Resource: See `notebooks/03_function_calculate_station_statistics.ipynb`
    🧪 Test Command: `uv run pytest tests/test_pandas_basics.py::test_calculate_station_statistics -v`

    Args:
        df (pandas.DataFrame): Environmental data with 'station_id', 'temperature_c', and 'humidity_percent' columns

    Returns:
        pandas.DataFrame: Statistics summary with columns:
            - station_id: Station identifier
            - avg_temperature: Mean temperature in Celsius (rounded to 1 decimal)
            - avg_humidity: Mean humidity percentage (rounded to 1 decimal)
            - reading_count: Number of readings for this station

    Example:
        >>> stats = calculate_station_statistics(df)
        Station Statistics Summary:
        station_id  avg_temperature  avg_humidity  reading_count
        STN_001            22.5           65.2            45
        STN_002            21.8           67.1            52
        ...
    """

    if df is None or df.empty:
        print('Empty dataset')
        return pd.DataFrame()
    
    required_cols = ['station_id', 'temperature_c', 'humidity_percent']
    if not all(col in df.columns for col in required_cols):
        print('Missing required columns')
        return pd.DataFrame()
    
    # Basic grouping and aggregation
    grouped = df.groupby('station_id')
    stats = pd.DataFrame({
        'station_id': grouped.groups.keys(),
        'avg_temperature': grouped['temperature_c'].mean().round(1),
        'avg_humidity': grouped['humidity_percent'].mean().round(1),
        'reading_count': grouped.size()
    })
    
    print(f'Calculated stats for {len(stats)} stations')
    return stats.reset_index(drop=True)


def join_station_data(stations_df, readings_df):
    """
    JOIN STATION DATA WITH READINGS (Like connecting two Excel sheets with a common column)

    This function combines weather station location information with temperature readings.
    After joining, each temperature reading will have the station's name, coordinates,
    and elevation - enabling geographic analysis!

    📚 Learning Resource: See `notebooks/04_function_join_station_data.ipynb`
    🧪 Test Command: `uv run pytest tests/test_pandas_basics.py::test_join_station_data -v`

    Args:
        stations_df (pandas.DataFrame): Weather station information with columns:
            - station_id: Unique station identifier
            - station_name: Human-readable station name
            - latitude, longitude: Station coordinates
            - elevation_m: Station elevation in meters

        readings_df (pandas.DataFrame): Environmental measurements with columns:
            - station_id: Links to stations_df station_id
            - date: Measurement date
            - temperature_c: Temperature measurement in Celsius
            - humidity_percent: Humidity measurement percentage
            - data_quality: Quality assessment flag

    Returns:
        pandas.DataFrame: Combined dataset with both station information and environmental readings

    Example:
        >>> combined = join_station_data(stations_df, readings_df)
        Joining station locations with temperature readings...
        Stations dataset: 15 stations
        Readings dataset: 500 readings
        After joining: 500 rows (all readings matched to stations)
        ...
    """

    if stations_df is None or stations_df.empty or readings_df is None or readings_df.empty:
        print('Invalid input data')
        return pd.DataFrame()
    
    if 'station_id' not in stations_df.columns or 'station_id' not in readings_df.columns:
        print('Missing station_id column')
        return pd.DataFrame()
    
    # Basic left join to preserve all readings
    joined = pd.merge(readings_df, stations_df, on='station_id', how='left')
    
    print(f'Joined {len(readings_df)} readings with {len(stations_df)} stations')
    return joined


def save_processed_data(df, output_file):
    """
    SAVE PROCESSED DATA (Like saving your Excel work so you can use it later)

    This function saves your processed DataFrame to a CSV file that you can open in
    QGIS, Excel, or other programs. It includes validation to make sure the file
    was saved correctly!

    📚 Learning Resource: See `notebooks/05_function_save_processed_data.ipynb`
    🧪 Test Command: `uv run pytest tests/test_pandas_basics.py::test_save_processed_data -v`

    Args:
        df (pandas.DataFrame): The processed data to save
        output_file (str): Path where to save the CSV file (e.g., 'output/processed_data.csv')

    Returns:
        bool: True if saving was successful, False otherwise

    Example:
        >>> success = save_processed_data(processed_df, 'output/final_results.csv')
        Saving processed data...
        File saved: output/final_results.csv
        File size: 15.2 KB
        Data rows saved: 247
        Ready for use in QGIS!
    """

    # TODO: Print a header to show what function is running
    # TODO: Use print("=" * 50) and print("SAVING PROCESSED DATA")

    # TODO: Input validation
    # TODO: Check if df is None, return False if invalid
    # TODO: Check if df is empty (warn but continue - empty files can be valid)
    # TODO: Check if output_file is valid string, return False if invalid

    # TODO: Convert output_file to Path object for easier manipulation
    # TODO: Use: output_path = Path(output_file)

    # TODO: Print information about the data being saved
    # TODO: - DataFrame shape
    # TODO: - Number of columns
    # TODO: - Memory usage (optional)

    # TODO: Print information about output location
    # TODO: - Full file path
    # TODO: - Directory where file will be saved
    # TODO: - Filename

    # TODO: Create output directory if it doesn't exist
    # TODO: Use output_path.parent.mkdir(parents=True, exist_ok=True)
    # TODO: Wrap in try/except to handle permission errors
    # TODO: Return False if directory creation fails

    # TODO: Save the data using df.to_csv()
    # TODO: Use these parameters for good formatting:
    # TODO: - index=False (don't save row numbers)
    # TODO: - float_format='%.3f' (round floats to 3 decimals)
    # TODO: - na_rep='' (empty string for missing values)
    # TODO: Wrap in try/except to handle save errors (permissions, disk space, etc.)
    # TODO: Return False if saving fails

    # TODO: Validate the saved file
    # TODO: Check that file exists using output_path.exists()
    # TODO: Get file size using output_path.stat().st_size
    # TODO: Try reading the file back to verify it's valid
    # TODO: Compare original and reloaded shapes to ensure data integrity

    if df is None:
        print('Invalid DataFrame')
        return False
    
    if not output_file:
        print('Invalid output file')
        return False
    
    try:
        # Create directory if needed
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Save data
        df.to_csv(output_file, index=False)
        print(f'Saved {len(df)} rows to {output_file}')
        return True
        
    except Exception as e:
        print(f'Error saving file: {e}')
        return False


def validate_coordinate_data(df):
    """
    VALIDATE COORDINATE DATA (Basic coordinate validation)
    
    Medium-quality implementation with basic validation.
    """
    
    print('VALIDATING COORDINATE DATA')
    
    if df is None or df.empty:
        return pd.DataFrame()
    
    # Basic coordinate validation (less comprehensive than good sample)
    if 'latitude' not in df.columns or 'longitude' not in df.columns:
        return df
        
    # Simple range checking
    valid_lat = (df['latitude'] >= -90) & (df['latitude'] <= 90)
    valid_lon = (df['longitude'] >= -180) & (df['longitude'] <= 180)
    
    # Remove invalid coordinates
    validated_df = df[valid_lat & valid_lon]
    
    print(f'Validated {len(validated_df)} out of {len(df)} coordinates')
    return validated_df


def multi_condition_filtering(df, filters_config):
    """
    MULTI-CONDITION FILTERING (Basic implementation)
    
    Medium-quality implementation with simple filtering logic.
    """
    
    print('APPLYING MULTI-CONDITION FILTERING')
    
    if df is None or df.empty or not filters_config:
        return df
    
    # Simple implementation - only handles numeric ranges
    filtered_df = df.copy()
    
    for column, config in filters_config.items():
        if column == 'logic':
            continue
            
        if column not in df.columns:
            continue
            
        # Only handle min/max filtering
        if 'min' in config:
            filtered_df = filtered_df[filtered_df[column] >= config['min']]
        if 'max' in config:
            filtered_df = filtered_df[filtered_df[column] <= config['max']]
    
    print(f'Filtered to {len(filtered_df)} rows')
    return filtered_df


def analyze_temporal_patterns(df, date_column='date', value_column='temperature', groupby_column='station_id'):
    """
    ANALYZE TEMPORAL PATTERNS (Basic implementation)
    
    Medium-quality implementation with simple temporal analysis.
    """
    
    print('ANALYZING TEMPORAL PATTERNS')
    
    if df is None or df.empty:
        return {}
        
    if date_column not in df.columns or value_column not in df.columns:
        return {}
    
    # Basic implementation - just overall stats
    analysis_df = df.copy()
    analysis_df[date_column] = pd.to_datetime(analysis_df[date_column])
    
    results = {
        'overall_stats': {
            'mean': float(analysis_df[value_column].mean()),
            'min': float(analysis_df[value_column].min()),
            'max': float(analysis_df[value_column].max()),
            'count': int(len(analysis_df))
        }
    }
    
    # Simple monthly analysis
    analysis_df['month'] = analysis_df[date_column].dt.month
    monthly_stats = analysis_df.groupby('month')[value_column].mean()
    
    results['monthly_patterns'] = monthly_stats.to_dict()
    results['seasonal_summary'] = {
        'warmest_month': int(monthly_stats.idxmax()),
        'warmest_temp': float(monthly_stats.max()),
        'coolest_month': int(monthly_stats.idxmin()),
        'coolest_temp': float(monthly_stats.min()),
        'seasonal_range': float(monthly_stats.max() - monthly_stats.min())
    }
    
    print('Temporal analysis complete')
    return results


# Helper functions (you don't need to modify these)
def _check_required_columns(df, required_columns, data_name="DataFrame"):
    """
    Helper function to check if DataFrame has required columns.

    Args:
        df: DataFrame to check
        required_columns: List of required column names
        data_name: Name for error messages

    Returns:
        List of missing column names (empty if all present)
    """
    if df is None or df.empty:
        return required_columns

    missing_columns = [col for col in required_columns if col not in df.columns]
    return missing_columns


def _format_number(value, decimals=1):
    """
    Helper function to safely format numbers with specified decimal places.

    Args:
        value: Number to format
        decimals: Number of decimal places

    Returns:
        Formatted number or original value if not numeric
    """
    try:
        return round(float(value), decimals)
    except (ValueError, TypeError):
        return value
