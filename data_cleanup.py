"""
Data Cleanup Code for Maji Ndogo Agriculture Analysis
Copy and paste this code into your notebook after loading the data
"""

# ============================================================================
# DATA CLEANUP - Insert this code after loading your DataFrame
# ============================================================================

# Step 1: Drop Field_ID columns
MD_agric_df.drop(columns='Field_ID', inplace=True)

# Step 2: Fix column names (rename columns with incorrect names)
if 'Chosen_crop' in MD_agric_df.columns:
    MD_agric_df.rename(columns={'Chosen_crop': 'Crop_type'}, inplace=True)

if 'Soil_type' in MD_agric_df.columns:
    MD_agric_df.rename(columns={'Soil_type': 'Soil_Type'}, inplace=True)
    
if 'Soil_fertility' in MD_agric_df.columns:
    MD_agric_df.rename(columns={'Soil_fertility': 'Soil_Fertility'}, inplace=True)

# Step 3: Fix spelling errors in crop types
if 'Crop_type' in MD_agric_df.columns:
    # Convert to lowercase and strip whitespace
    MD_agric_df['Crop_type'] = MD_agric_df['Crop_type'].str.lower().str.strip()
    
    # Fix common spelling errors
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

# Step 4: Fix negative elevation values
if 'Elevation' in MD_agric_df.columns:
    MD_agric_df['Elevation'] = MD_agric_df['Elevation'].abs()

# ============================================================================
# VERIFICATION - Run these to check your data is clean
# ============================================================================

print("Data cleanup complete!")
print(f"Number of unique crop types: {len(MD_agric_df['Crop_type'].unique())}")
print(f"Minimum elevation: {MD_agric_df['Elevation'].min()}")
print(f"Columns: {list(MD_agric_df.columns)}")
