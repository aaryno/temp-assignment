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

    print("=" * 50)
    print("LOADING AND EXPLORING GIS DATA")
    print("=" * 50)
    
    if not os.path.exists(file_path):
        print(f"❌ ERROR: File not found: {file_path}")
        return None
    
    print(f"📁 Loading file: {file_path}")
    
    try:
        df = pd.read_csv(file_path)
        print("✅ File loaded successfully!")
    except Exception as e:
        print(f"❌ ERROR loading file: {e}")
        return None
    
    print(f"\n📊 Dataset Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    print(f"📋 Column Names: {list(df.columns)}")
    print(f"\n🔍 Data Types:")
    print(df.dtypes)
    
    print(f"\n📋 FIRST 5 ROWS:")
    print(df.head())
    
    print(f"\n📈 SUMMARY STATISTICS:")
    print(df.describe())
    
    missing_values = df.isnull().sum()
    duplicate_rows = df.duplicated().sum()
    
    print(f"\n🔍 DATA QUALITY CHECK:")
    if missing_values.sum() == 0:
        print("  ✅ No missing values found")
    else:
        print(f"Missing values: {missing_values.sum()}")
    
    print(f"Duplicate rows: {duplicate_rows}")
    
    print("\n✅ Data exploration completed successfully!")
    return df


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

    print("=" * 50)
    print("FILTERING ENVIRONMENTAL DATA")
    print("=" * 50)
    
    if df is None or df.empty:
        print("❌ ERROR: Invalid or empty DataFrame")
        return pd.DataFrame()
    
    required_cols = ['temperature_c', 'data_quality']
    if not all(col in df.columns for col in required_cols):
        print(f"❌ ERROR: Missing required columns")
        return pd.DataFrame()
    
    original_count = len(df)
    
    print(f"🎯 Filtering criteria: {min_temp}°C to {max_temp}°C, quality='{quality}'")
    
    temp_filter = (df['temperature_c'] >= min_temp) & (df['temperature_c'] <= max_temp)
    quality_filter = df['data_quality'] == quality
    combined_filter = temp_filter & quality_filter
    
    filtered_df = df[combined_filter].copy()
    
    filtered_count = len(filtered_df)
    removed_count = original_count - filtered_count
    
    print(f"📊 Results: {original_count} → {filtered_count} records ({removed_count} removed)")
    
    print("✅ Filtering completed!")
    return filtered_df


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

    print('=' * 50)
    print('CALCULATING STATION STATISTICS')
    print('=' * 50)
    
    if df is None or df.empty:
        print('❌ ERROR: Invalid DataFrame')
        return pd.DataFrame()
    
    required_cols = ['station_id', 'temperature_c', 'humidity_percent']
    if not all(col in df.columns for col in required_cols):
        print('❌ ERROR: Missing required columns')
        return pd.DataFrame()
    
    grouped = df.groupby('station_id')
    stats_df = pd.DataFrame({
        'station_id': grouped['temperature_c'].mean().index,
        'avg_temperature': grouped['temperature_c'].mean().values,
        'avg_humidity': grouped['humidity_percent'].mean().round(1).values,
        'reading_count': grouped.size().values
    })
    
    print(f'📊 Statistics calculated for {len(stats_df)} stations')
    print('✅ Statistics calculation completed!')
    return stats_df


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

    print('=' * 50)
    print('JOINING STATION DATA WITH READINGS')
    print('=' * 50)
    
    if stations_df is None or stations_df.empty:
        print('❌ ERROR: Invalid stations DataFrame')
        return pd.DataFrame()
        
    if readings_df is None or readings_df.empty:
        print('❌ ERROR: Invalid readings DataFrame')
        return pd.DataFrame()
    
    # Check required columns
    station_required_cols = ['station_id']
    reading_required_cols = ['station_id']
    
    if not all(col in stations_df.columns for col in station_required_cols):
        print('❌ ERROR: Missing required columns in stations DataFrame')
        return pd.DataFrame()
        
    if not all(col in readings_df.columns for col in reading_required_cols):
        print('❌ ERROR: Missing required columns in readings DataFrame')
        return pd.DataFrame()
    
    print(f'📊 Stations dataset: {len(stations_df)} stations')
    print(f'📊 Readings dataset: {len(readings_df)} readings')
    
    # Perform left join to preserve all readings
    joined_df = readings_df.merge(stations_df, on='station_id', how='left')
    
    print(f'✅ After joining: {len(joined_df)} rows (all readings matched to stations)')
    print('✅ Join operation completed!')
    
    return joined_df


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

    print('=' * 50)
    print('CALCULATING STATION STATISTICS')
    print('=' * 50)
    
    if df is None or df.empty:
        print('❌ ERROR: Invalid DataFrame')
        return pd.DataFrame()
    
    required_cols = ['station_id', 'temperature_c', 'humidity_percent']
    if not all(col in df.columns for col in required_cols):
        print('❌ ERROR: Missing required columns')
        return pd.DataFrame()
    
    grouped = df.groupby('station_id')
    stats_df = pd.DataFrame({
        'station_id': grouped['temperature_c'].mean().index,
        'avg_temperature': grouped['temperature_c'].mean().values,
        'avg_humidity': grouped['humidity_percent'].mean().round(1).values,
        'reading_count': grouped.size().values
    })
    
    print(f'📊 Statistics calculated for {len(stats_df)} stations')
    print('✅ Statistics calculation completed!')
    return stats_df


def validate_coordinate_data(df):
    """
    VALIDATE COORDINATE DATA (Comprehensive coordinate validation and quality assessment)
    
    This function performs comprehensive validation of coordinate data including bounds
    checking, format validation, and quality assessment. Essential for ensuring spatial
    data integrity in GIS workflows.
    
    📚 Learning Resource: See `notebooks/06_function_validate_coordinate_data.ipynb`
    🧪 Test Command: `uv run pytest tests/test_pandas_basics.py::test_validate_coordinate_data -v`
    
    Args:
        df (pandas.DataFrame): DataFrame with coordinate columns
        
    Returns:
        pandas.DataFrame: Validated data with invalid coordinates removed
    """
    
    print('=' * 50)
    print('VALIDATING COORDINATE DATA')
    print('=' * 50)
    
    if df is None or df.empty:
        print('❌ ERROR: Invalid or empty DataFrame')
        return pd.DataFrame()
    
    # Check for required coordinate columns
    if 'latitude' not in df.columns or 'longitude' not in df.columns:
        print('❌ ERROR: Missing latitude or longitude columns')
        return df
        
    initial_count = len(df)
    print(f"📊 Starting validation of {initial_count} coordinate records")
    
    # Create copy for validation
    validated_df = df.copy()
    
    # Check for valid latitude range (-90 to 90)
    lat_valid = (validated_df['latitude'] >= -90) & (validated_df['latitude'] <= 90)
    lat_invalid_count = (~lat_valid).sum()
    
    # Check for valid longitude range (-180 to 180)  
    lon_valid = (validated_df['longitude'] >= -180) & (validated_df['longitude'] <= 180)
    lon_invalid_count = (~lon_valid).sum()
    
    # Check for null coordinates
    null_coords = validated_df['latitude'].isnull() | validated_df['longitude'].isnull()
    null_count = null_coords.sum()
    
    # Check for zero coordinates (often invalid)
    zero_coords = (validated_df['latitude'] == 0) & (validated_df['longitude'] == 0)
    zero_count = zero_coords.sum()
    
    print(f"🔍 Validation results:")
    print(f"   Invalid latitude values: {lat_invalid_count}")
    print(f"   Invalid longitude values: {lon_invalid_count}")
    print(f"   Null coordinate values: {null_count}")
    print(f"   Zero coordinates (suspicious): {zero_count}")
    
    # Remove invalid coordinates
    valid_coords = lat_valid & lon_valid & ~null_coords & ~zero_coords
    validated_df = validated_df[valid_coords]
    
    final_count = len(validated_df)
    removed_count = initial_count - final_count
    
    print(f"\n📈 Validation summary:")
    print(f"   Original records: {initial_count}")
    print(f"   Valid records: {final_count}")
    print(f"   Removed records: {removed_count}")
    print(f"   Data quality: {(final_count/initial_count)*100:.1f}%")
    
    print('✅ Coordinate validation completed!')
    return validated_df


def multi_condition_filtering(df, filters_config):
    """
    MULTI-CONDITION FILTERING (Complex filtering with multiple criteria and logical operations)
    
    This function applies multiple filtering conditions dynamically based on configuration,
    supporting complex boolean logic for advanced data selection scenarios.
    
    📚 Learning Resource: See `notebooks/07_function_multi_condition_filtering.ipynb`
    🧪 Test Command: `uv run pytest tests/test_pandas_basics.py::test_multi_condition_filtering -v`
    
    Args:
        df (pandas.DataFrame): Environmental data to filter
        filters_config (dict): Dictionary defining filtering rules
        
    Returns:
        pandas.DataFrame: Filtered data meeting all conditions
    """
    
    print('=' * 50)
    print('APPLYING MULTI-CONDITION FILTERING')
    print('=' * 50)
    
    if df is None or df.empty:
        print('❌ ERROR: Invalid or empty DataFrame')
        return pd.DataFrame()
        
    if not filters_config:
        print('⚠️  No filters specified, returning original data')
        return df
    
    # Start with all data
    filtered_df = df.copy()
    initial_count = len(filtered_df)
    
    print(f"📊 Starting with {initial_count} rows")
    
    # Apply each filter condition
    conditions_applied = []
    
    for column, config in filters_config.items():
        if column == 'logic':
            continue  # Skip logic configuration
            
        if column not in df.columns:
            print(f"⚠️  Warning: Column '{column}' not found in data")
            continue
            
        # Handle different filter types
        if 'min' in config or 'max' in config:
            # Numeric range filtering
            condition = pd.Series([True] * len(filtered_df), index=filtered_df.index)
            
            if 'min' in config:
                condition &= (filtered_df[column] >= config['min'])
                
            if 'max' in config:
                condition &= (filtered_df[column] <= config['max'])
                
            conditions_applied.append(condition)
            print(f"🔢 Applied numeric filter to {column}: {config}")
            
        elif 'include' in config:
            # Include specific values
            condition = filtered_df[column].isin(config['include'])
            conditions_applied.append(condition)
            print(f"✅ Applied include filter to {column}: {config['include']}")
            
        elif 'exclude' in config:
            # Exclude specific values  
            condition = ~filtered_df[column].isin(config['exclude'])
            conditions_applied.append(condition)
            print(f"❌ Applied exclude filter to {column}: {config['exclude']}")
    
    # Combine all conditions
    if conditions_applied:
        logic = filters_config.get('logic', 'AND').upper()
        
        if logic == 'AND':
            # All conditions must be true
            final_condition = conditions_applied[0]
            for condition in conditions_applied[1:]:
                final_condition &= condition
        else:  # OR logic
            # Any condition can be true
            final_condition = conditions_applied[0]
            for condition in conditions_applied[1:]:
                final_condition |= condition
        
        # Apply the combined filter
        filtered_df = filtered_df[final_condition]
        
        print(f"🔗 Combined conditions using {logic} logic")
    
    final_count = len(filtered_df)
    percentage = (final_count / initial_count) * 100 if initial_count > 0 else 0
    
    print(f"📈 Result: {final_count} rows ({percentage:.1f}% of original data)")
    print(f"🚫 Filtered out: {initial_count - final_count} rows")
    print('✅ Multi-condition filtering completed!')
    
    return filtered_df


def analyze_temporal_patterns(df, date_column='date', value_column='temperature', groupby_column='station_id'):
    """
    ANALYZE TEMPORAL PATTERNS (Time series analysis with pandas datetime functionality)
    
    This function analyzes temporal patterns in environmental data including seasonal trends,
    yearly patterns, and statistical summaries over time periods.
    
    📚 Learning Resource: See `notebooks/08_function_analyze_temporal_patterns.ipynb`
    🧪 Test Command: `uv run pytest tests/test_pandas_basics.py::test_analyze_temporal_patterns -v`
    
    Args:
        df (pandas.DataFrame): Environmental data with datetime information
        date_column (str): Name of date/datetime column
        value_column (str): Name of value column to analyze over time
        groupby_column (str): Column to group by for pattern analysis
        
    Returns:
        dict: Temporal analysis results with trends, patterns, and statistics
    """
    
    print('=' * 50)
    print('ANALYZING TEMPORAL PATTERNS')
    print('=' * 50)
    
    # Validate inputs
    if df is None or df.empty:
        print('❌ ERROR: Invalid or empty DataFrame')
        return {}
        
    if date_column not in df.columns:
        print(f"❌ ERROR: Date column '{date_column}' not found")
        return {}
        
    if value_column not in df.columns:
        print(f"❌ ERROR: Value column '{value_column}' not found")
        return {}
    
    # Make a copy and ensure date column is datetime
    analysis_df = df.copy()
    analysis_df[date_column] = pd.to_datetime(analysis_df[date_column])
    
    print(f"📅 Date range: {analysis_df[date_column].min()} to {analysis_df[date_column].max()}")
    print(f"📊 Analyzing {len(analysis_df)} records")
    
    # Extract temporal components
    analysis_df['year'] = analysis_df[date_column].dt.year
    analysis_df['month'] = analysis_df[date_column].dt.month
    analysis_df['day_of_week'] = analysis_df[date_column].dt.dayofweek
    
    results = {}
    
    # 1. Overall statistics
    results['overall_stats'] = {
        'mean': float(analysis_df[value_column].mean()),
        'min': float(analysis_df[value_column].min()),
        'max': float(analysis_df[value_column].max()),
        'std': float(analysis_df[value_column].std()),
        'count': int(len(analysis_df))
    }
    
    print(f"\n📈 Overall {value_column} statistics:")
    print(f"   Mean: {results['overall_stats']['mean']:.2f}")
    print(f"   Range: {results['overall_stats']['min']:.2f} to {results['overall_stats']['max']:.2f}")
    
    # 2. Monthly patterns
    monthly_patterns = analysis_df.groupby('month')[value_column].agg(['mean', 'min', 'max', 'count'])
    results['monthly_patterns'] = monthly_patterns.to_dict('index')
    
    warmest_month = monthly_patterns['mean'].idxmax()
    coolest_month = monthly_patterns['mean'].idxmin()
    
    results['seasonal_summary'] = {
        'warmest_month': int(warmest_month),
        'warmest_temp': float(monthly_patterns.loc[warmest_month, 'mean']),
        'coolest_month': int(coolest_month),
        'coolest_temp': float(monthly_patterns.loc[coolest_month, 'mean']),
        'seasonal_range': float(monthly_patterns['mean'].max() - monthly_patterns['mean'].min())
    }
    
    print(f"\n🌅 Seasonal patterns:")
    print(f"   Warmest month: {warmest_month} ({results['seasonal_summary']['warmest_temp']:.1f}°C)")
    print(f"   Coolest month: {coolest_month} ({results['seasonal_summary']['coolest_temp']:.1f}°C)")
    
    # 3. Station-specific patterns (if available)
    if groupby_column in analysis_df.columns and analysis_df[groupby_column].nunique() > 1:
        station_patterns = analysis_df.groupby(groupby_column)[value_column].agg(['mean', 'min', 'max', 'count'])
        results['station_patterns'] = station_patterns.to_dict('index')
        
        print(f"\n🌡️  Station-specific analysis:")
        print(f"   Analyzed {len(station_patterns)} stations")
    
    print(f"\n✅ Temporal analysis complete!")
    
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
