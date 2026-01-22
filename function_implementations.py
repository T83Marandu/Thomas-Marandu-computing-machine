"""
Maji Ndogo Agriculture Analysis - Function Implementations
Copy and paste these functions into your notebook to complete the challenges.
"""

# ============================================================================
# EXERCISE 1: Explore Crop Distribution
# ============================================================================

### START FUNCTION
def explore_crop_distribution(df, crop_filter):
    """
    Filter data by crop type and return mean Rainfall and Elevation.
    
    Args:
        df: DataFrame with agricultural data
        crop_filter: String value for the crop type to filter by
        
    Returns:
        tuple: (mean_rainfall, mean_elevation)
    """
    # Filter by crop type (case-insensitive)
    crop_filter_lower = crop_filter.lower()
    filtered_df = df[df['Crop_type'] == crop_filter_lower]
    
    # Calculate means
    mean_rainfall = filtered_df['Rainfall'].mean()
    mean_elevation = filtered_df['Elevation'].mean()
    
    return (mean_rainfall, mean_elevation)
### END FUNCTION


# ============================================================================
# EXERCISE 2: Analyse Soil Fertility
# ============================================================================

### START FUNCTION
def analyse_soil_fertility(df):
    """
    Group data by Soil_Type and return mean Soil_Fertility.
    
    Args:
        df: DataFrame with agricultural data
        
    Returns:
        pd.Series: Mean Soil_Fertility grouped by Soil_Type
    """
    # Group by Soil_Type and calculate mean Soil_Fertility
    result = df.groupby('Soil_Type')['Soil_Fertility'].mean()
    
    return result
### END FUNCTION


# ============================================================================
# EXERCISE 3: Climate and Geography Influence
# ============================================================================

### START FUNCTION
def climate_geography_influence(df, column):
    """
    Group data by specified column and aggregate climate/geography metrics.
    
    Args:
        df: DataFrame with agricultural data
        column: Column name to group by
        
    Returns:
        pd.DataFrame: Aggregated data with Elevation, Min_temperature_C, 
                      Max_temperature_C, and Rainfall means
    """
    # Group by specified column and aggregate
    result = df.groupby(column).agg({
        'Elevation': 'mean',
        'Min_temperature_C': 'mean',
        'Max_temperature_C': 'mean',
        'Rainfall': 'mean'
    })
    
    return result
### END FUNCTION


# ============================================================================
# EXERCISE 4: Find Ideal Fields
# ============================================================================

### START FUNCTION
def find_ideal_fields(df):
    """
    Find the top performing crop type based on above-average Standard_yield.
    
    Args:
        df: DataFrame with agricultural data
        
    Returns:
        str: Name of the top performing crop type
    """
    # Calculate average Standard_yield
    avg_yield = df['Standard_yield'].mean()
    
    # Filter fields with above-average Standard_yield
    above_avg_df = df[df['Standard_yield'] > avg_yield]
    
    # Group by Crop_type and count
    crop_counts = above_avg_df.groupby('Crop_type').size()
    
    # Sort in descending order
    crop_counts_sorted = crop_counts.sort_values(ascending=False)
    
    # Get the top crop type
    top_crop = crop_counts_sorted.index[0]
    
    return top_crop
### END FUNCTION


# ============================================================================
# EXERCISE 5: Find Good Conditions
# ============================================================================

### START FUNCTION
def find_good_conditions(df, crop_type):
    """
    Filter DataFrame by crop type and specific conditions.
    
    Args:
        df: DataFrame with agricultural data
        crop_type: Type of crop to filter by
        
    Returns:
        pd.DataFrame: Filtered DataFrame
    """
    # Convert crop_type to lowercase for consistency
    crop_type_lower = crop_type.lower()
    
    # Calculate average Standard_yield
    avg_yield = df['Standard_yield'].mean()
    
    # Apply all filters
    filtered_df = df[
        (df['Crop_type'] == crop_type_lower) &
        (df['Standard_yield'] > avg_yield) &
        (df['Ave_temps'] >= 12) &
        (df['Ave_temps'] <= 15) &
        (df['Pollution_level'] < 0.0001)
    ]
    
    return filtered_df
### END FUNCTION


# Data Cleanup Code (if needed)
"""
To clean your data after loading from the database, use this code:

# Drop Field_ID columns
MD_agric_df.drop(columns='Field_ID', inplace=True)

# Fix column names
if 'Chosen_crop' in MD_agric_df.columns:
    MD_agric_df.rename(columns={'Chosen_crop': 'Crop_type'}, inplace=True)

if 'Soil_type' in MD_agric_df.columns:
    MD_agric_df.rename(columns={'Soil_type': 'Soil_Type'}, inplace=True)
    
if 'Soil_fertility' in MD_agric_df.columns:
    MD_agric_df.rename(columns={'Soil_fertility': 'Soil_Fertility'}, inplace=True)

# Fix spelling errors in crop types
if 'Crop_type' in MD_agric_df.columns:
    MD_agric_df['Crop_type'] = MD_agric_df['Crop_type'].str.lower().str.strip()
    crop_corrections = {
        'coffe': 'coffee',
        'cofee': 'coffee',
        'tee': 'tea',
        'te': 'tea',
        'maiz': 'maize',
        'mazie': 'maize',
        'weat': 'wheat',
        'whea': 'wheat',
        'rize': 'rice',
        'bananna': 'banana',
        'casava': 'cassava',
        'potatos': 'potato',
        'potatoes': 'potato'
    }
    MD_agric_df['Crop_type'] = MD_agric_df['Crop_type'].replace(crop_corrections)

# Fix negative elevation values
if 'Elevation' in MD_agric_df.columns:
    MD_agric_df['Elevation'] = MD_agric_df['Elevation'].abs()
"""
