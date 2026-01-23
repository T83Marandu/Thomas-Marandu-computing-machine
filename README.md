# Maji Ndogo Agriculture Analysis Project

This project provides data analysis tools for understanding agricultural patterns in Maji Ndogo, aimed at supporting automated farming decisions.

## Overview

The Maji Ndogo project analyzes diverse agricultural data including geographic features, weather conditions, soil characteristics, and farm management practices to recommend optimal locations and conditions for different crops.

## Features

- **Data Integration**: Imports and merges data from multiple SQLite database tables
- **Data Cleanup**: Automatically fixes common data issues (column names, spelling errors, negative values)
- **Crop Distribution Analysis**: Analyzes rainfall and elevation patterns for different crops
- **Soil Fertility Mapping**: Identifies the most fertile soil types
- **Climate Analysis**: Examines relationships between geography, climate, and crop yields
- **Performance Optimization**: Identifies top-performing crops and ideal growing conditions

## Installation

1. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
from maji_ndogo_analysis import (
    load_and_clean_data,
    explore_crop_distribution,
    analyse_soil_fertility,
    climate_geography_influence,
    find_ideal_fields,
    find_good_conditions
)

# Load and clean data
df = load_and_clean_data('Maji_Ndogo_farm_survey_small.db')

# Analyze crop distribution
rainfall, elevation = explore_crop_distribution(df, "tea")
print(f"Tea cultivation - Rainfall: {rainfall:.2f}mm, Elevation: {elevation:.2f}m")

# Analyze soil fertility
soil_fertility = analyse_soil_fertility(df)
print(soil_fertility)

# Analyze climate and geography influence
climate_analysis = climate_geography_influence(df, 'Crop_type')
print(climate_analysis)

# Find ideal crop
top_crop = find_ideal_fields(df)
print(f"Top performing crop: {top_crop}")

# Find good conditions for a crop
good_conditions = find_good_conditions(df, "tea")
print(f"Fields with ideal tea conditions: {len(good_conditions)}")
```

## Functions

### `load_and_clean_data(db_path)`
Loads data from SQLite database and performs cleanup operations.

### `explore_crop_distribution(df, crop_filter)`
Returns mean rainfall and elevation for a specific crop type.

**Parameters:**
- `df`: DataFrame with agricultural data
- `crop_filter`: Crop type to filter by (e.g., "tea", "coffee")

**Returns:** Tuple of (mean_rainfall, mean_elevation)

### `analyse_soil_fertility(df)`
Groups data by soil type and returns mean soil fertility.

**Parameters:**
- `df`: DataFrame with agricultural data

**Returns:** Series with mean Soil_Fertility by Soil_Type

### `climate_geography_influence(df, column)`
Analyzes climate and geography metrics grouped by a specified column.

**Parameters:**
- `df`: DataFrame with agricultural data
- `column`: Column name to group by (e.g., 'Crop_type', 'Location')

**Returns:** DataFrame with aggregated Elevation, temperatures, and Rainfall

### `find_ideal_fields(df)`
Identifies the top-performing crop type based on above-average yields.

**Parameters:**
- `df`: DataFrame with agricultural data

**Returns:** String with the name of the top crop type

### `find_good_conditions(df, crop_type)`
Filters fields by crop type and optimal growing conditions.

**Parameters:**
- `df`: DataFrame with agricultural data
- `crop_type`: Crop type to filter by

**Returns:** Filtered DataFrame with fields meeting all criteria

## Data Dictionary

### Geographic Features
- **Field_ID**: Unique identifier for each field
- **Elevation**: Elevation above sea level (meters)
- **Latitude/Longitude**: Geographic coordinates
- **Location**: Province
- **Slope**: Land slope

### Weather Features
- **Rainfall**: Rainfall amount (mm)
- **Min_temperature_C**: Average minimum temperature (°C)
- **Max_temperature_C**: Average maximum temperature (°C)
- **Ave_temps**: Average temperature (°C)

### Soil and Crop Features
- **Soil_fertility**: Soil fertility measure (0-1)
- **Soil_type**: Type of soil
- **pH**: Soil pH level

### Farm Management Features
- **Pollution_level**: Pollution level (0-1)
- **Plot_size**: Plot size (Ha)
- **Crop_type**: Type of crop
- **Annual_yield**: Annual field output
- **Standard_yield**: Normalized yield per crop

## Testing

Run the test suite:
```bash
python test_maji_ndogo.py
```

## Data Quality

The system automatically handles:
- Spelling errors in crop names
- Negative elevation values (converted to positive)
- Column name inconsistencies
- Data type conversions

### Quick Data Cleanup

If you need to manually clean your data, use the standalone **`data_cleanup.py`** file:

```python
# Simply copy and paste the code from data_cleanup.py after loading your data
# Or import and use the load_and_clean_data() function from maji_ndogo_analysis.py
```

## Files in This Repository

- **`maji_ndogo_analysis.py`** - Complete Python module with all functions
- **`maji_ndogo_analysis.ipynb`** - Jupyter notebook with examples
- **`function_implementations.py`** - All 5 exercises ready to copy-paste
- **`data_cleanup.py`** - Standalone data cleanup code
- **`QUICK_START.md`** - Step-by-step guide for students
- **`test_maji_ndogo.py`** - Test suite
- **`requirements.txt`** - Python dependencies

## Average Crop Yields (tons/Ha)

- Coffee: 1.5
- Wheat: 3
- Rice: 4.5
- Maize: 5.5
- Tea: 1.2
- Potato: 20
- Banana: 30
- Cassava: 13

## License

This project is part of the Maji Ndogo agricultural automation initiative.
