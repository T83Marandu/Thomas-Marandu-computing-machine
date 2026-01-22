# Quick Start Guide - Maji Ndogo Analysis Functions

## For Students: Copy-Paste Code to Complete Your Test

This guide provides the essential code you need to complete the Maji Ndogo agriculture analysis challenges.

---

## Option 1: Use the Complete Functions File

Copy all functions from **`function_implementations.py`** into your notebook.

---

## Option 2: Copy Functions One by One

### Exercise 1: Explore Crop Distribution

```python
### START FUNCTION
def explore_crop_distribution(df, crop_filter):
    crop_filter_lower = crop_filter.lower()
    filtered_df = df[df['Crop_type'] == crop_filter_lower]
    mean_rainfall = filtered_df['Rainfall'].mean()
    mean_elevation = filtered_df['Elevation'].mean()
    return (mean_rainfall, mean_elevation)
### END FUNCTION
```

**Test:**
```python
explore_crop_distribution(MD_agric_df, "tea")
# Expected: (1534.5079956188388, 775.208667535597)
```

---

### Exercise 2: Analyse Soil Fertility

```python
### START FUNCTION
def analyse_soil_fertility(df):
    result = df.groupby('Soil_Type')['Soil_Fertility'].mean()
    return result
### END FUNCTION
```

**Test:**
```python
analyse_soil_fertility(MD_agric_df)
# Expected: Series with mean fertility by soil type
```

---

### Exercise 3: Climate and Geography Influence

```python
### START FUNCTION
def climate_geography_influence(df, column):
    result = df.groupby(column)[['Elevation', 'Min_temperature_C', 'Max_temperature_C', 'Rainfall']].mean()
    return result
### END FUNCTION
```

**Test:**
```python
climate_geography_influence(MD_agric_df, 'Crop_type')
# Expected: DataFrame with 4 columns (Elevation, Min_temperature_C, Max_temperature_C, Rainfall)
```

---

### Exercise 4: Find Ideal Fields

```python
### START FUNCTION
def find_ideal_fields(df):
    avg_yield = df['Standard_yield'].mean()
    above_avg_df = df[df['Standard_yield'] > avg_yield]
    crop_counts = above_avg_df.groupby('Crop_type').size()
    crop_counts_sorted = crop_counts.sort_values(ascending=False)
    top_crop = crop_counts_sorted.index[0]
    return top_crop
### END FUNCTION
```

**Test:**
```python
type(find_ideal_fields(MD_agric_df))
# Expected: str
```

---

### Exercise 5: Find Good Conditions

```python
### START FUNCTION
def find_good_conditions(df, crop_type):
    crop_type_lower = crop_type.lower()
    avg_yield = df['Standard_yield'].mean()
    filtered_df = df[
        (df['Crop_type'] == crop_type_lower) &
        (df['Standard_yield'] > avg_yield) &
        (df['Ave_temps'] >= 12) &
        (df['Ave_temps'] <= 15) &
        (df['Pollution_level'] < 0.0001)
    ]
    return filtered_df
### END FUNCTION
```

**Test:**
```python
find_good_conditions(MD_agric_df, "tea").shape
# Expected: (14, 17)
```

---

## Data Cleanup Code

Before running the challenges, make sure your data is cleaned:

```python
# Drop Field_ID columns
MD_agric_df.drop(columns='Field_ID', inplace=True)

# Fix column names
if 'Chosen_crop' in MD_agric_df.columns:
    MD_agric_df.rename(columns={'Chosen_crop': 'Crop_type'}, inplace=True)
if 'Soil_type' in MD_agric_df.columns:
    MD_agric_df.rename(columns={'Soil_type': 'Soil_Type'}, inplace=True)
if 'Soil_fertility' in MD_agric_df.columns:
    MD_agric_df.rename(columns={'Soil_fertility': 'Soil_Fertility'}, inplace=True)

# Fix crop name spelling
if 'Crop_type' in MD_agric_df.columns:
    MD_agric_df['Crop_type'] = MD_agric_df['Crop_type'].str.lower().str.strip()
    crop_corrections = {
        'coffe': 'coffee', 'cofee': 'coffee',
        'tee': 'tea', 'te': 'tea',
        'maiz': 'maize', 'mazie': 'maize',
        'weat': 'wheat', 'whea': 'wheat',
        'rize': 'rice', 'bananna': 'banana',
        'casava': 'cassava', 'potatos': 'potato', 'potatoes': 'potato'
    }
    MD_agric_df['Crop_type'] = MD_agric_df['Crop_type'].replace(crop_corrections)

# Fix negative elevations
if 'Elevation' in MD_agric_df.columns:
    MD_agric_df['Elevation'] = MD_agric_df['Elevation'].abs()
```

---

## SQL Query for Data Loading

```python
import pandas as pd
from sqlalchemy import create_engine, text

# Create engine
engine = create_engine('sqlite:///Maji_Ndogo_farm_survey_small.db')

# SQL query to join all tables
sql_query = """
SELECT *
FROM geographic_features
LEFT JOIN weather_features USING (Field_ID)
LEFT JOIN soil_and_crop_features USING (Field_ID)
LEFT JOIN farm_management_features USING (Field_ID)
"""

# Load data
with engine.connect() as connection:
    MD_agric_df = pd.read_sql_query(text(sql_query), connection)
```

---

## Complete Workflow

1. Import libraries: `pandas`, `sqlalchemy`
2. Load data using SQL query above
3. Clean data using cleanup code above
4. Copy and paste all 5 exercise function implementations (Exercise 1-5)
5. Test each function with the test cases provided
6. Submit your notebook

---

## Files in This Repository

- **`function_implementations.py`** - All 5 functions ready to copy
- **`maji_ndogo_analysis.py`** - Complete module with all functions
- **`maji_ndogo_analysis.ipynb`** - Jupyter notebook with examples
- **`QUICK_START.md`** - This guide

---

## Need Help?

All functions are marked with `### START FUNCTION` and `### END FUNCTION` comments as required for grading. Just copy the entire block including these markers.

Good luck with your test! 🌾
