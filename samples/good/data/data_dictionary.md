# Module 05-02: Pandas Basics - Streamlined Weather Data Dictionary

## Dataset Overview

Streamlined real-world meteorological data optimized for essential pandas competency development within 2-hour time constraint.

**Total Size:** ~4KB  
**Geographic Focus:** Core Arizona weather stations  
**Educational Philosophy:** Maximum learning efficiency through focused essential skills  
**Professional Context:** Foundation environmental data workflows

## Dataset Specifications

### Arizona Weather Stations (Streamlined)
**File:** `arizona_weather_stations.csv`  
**Source:** NOAA Climate Data Online  
**License:** Public Domain  
**Records:** 8 core stations (reduced for efficiency)  
**Size:** ~1KB

#### Attributes:
| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `station_id` | String | NOAA identifier | "USW00023183" |
| `station_name` | String | Official name | "Phoenix Sky Harbor" |
| `latitude` | Float | Decimal degrees | 33.4484 |
| `longitude` | Float | Decimal degrees | -112.0740 |
| `elevation_m` | Float | Meters above sea level | 337.1 |
| `station_type` | String | Network type | "ASOS", "COOP" |

### Daily Temperature Readings (Streamlined)
**File:** `arizona_daily_temperatures.csv`  
**Source:** NOAA Climate Data Online  
**License:** Public Domain  
**Records:** 56 observations (7 days × 8 stations) - optimized for 2-hour learning  
**Size:** ~3KB

#### Attributes:
| Field | Type | Description | Range | Example |
|-------|------|-------------|-------|---------|
| `station_id` | String | Station identifier | Links to stations | "USW00023183" |
| `date` | Date | Observation date | 2024-01-XX | "2024-01-15" |
| `temperature_c` | Float | Daily mean temp | -10 to 45°C | 18.3 |
| `humidity_percent` | Float | Relative humidity | 0-100% | 45.2 |
| `data_quality` | String | Quality flag | verified/provisional | "verified" |

## Core Stations (Essential Learning Focus)

| Station | Location | Elevation | Climate Zone | Learning Purpose |
|---------|----------|-----------|--------------|------------------|
| Phoenix Sky Harbor | Urban Phoenix | 337m | Hot Desert | Urban baseline reference |
| Flagstaff Pulliam | Northern Arizona | 2,135m | Continental | Elevation contrast |
| Tucson WFO | Southern Arizona | 777m | Hot Desert | Regional comparison |
| Yuma MCAS | Southwest Border | 65m | Hot Desert | Statistical analysis |

## Data Quality Standards (Optimized for Learning)

- **NOAA Quality Control:** Essential quality flags ("verified", "provisional")
- **Completeness:** 100% data availability for core learning dataset
- **Accuracy:** Professional-grade instruments, simplified for educational focus
- **Temporal Coverage:** January 2024 - sufficient for fundamental pandas operations

## Professional Applications (Foundation Skills)

- **Environmental Consulting:** Essential data manipulation competency
- **Government Agencies:** Foundation for weather data workflows
- **Data Analysis Roles:** Core pandas skills for any data-driven career
- **GIS Programming:** Essential preparation for geospatial data analysis

## Usage Instructions

### Loading Data
```python
import pandas as pd

stations = pd.read_csv('arizona_weather_stations.csv')
temperatures = pd.read_csv('arizona_daily_temperatures.csv', 
                          parse_dates=['date'])
```

### Basic Analysis
```python
# Merge datasets
data = temperatures.merge(stations, on='station_id')

# Elevation-temperature relationship
elevation_temp = data.groupby('station_name').agg({
    'elevation_m': 'first',
    'temperature_c': 'mean'
})
```

## Career Preparation (Essential Foundation)

Students develop core pandas competency using authentic meteorological data sources, providing foundation skills for:
- Data analyst positions requiring pandas proficiency
- GIS roles involving environmental data processing
- Environmental consulting basic data workflows
- Government positions requiring data manipulation skills

This provides essential pandas foundation enabling success in subsequent advanced modules and professional data analysis roles.