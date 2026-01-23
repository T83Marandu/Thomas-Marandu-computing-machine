# ============================================================================
# DATA CLEANUP CODE - Insert this where it says "# Insert your code here"
# ============================================================================
# This code should be inserted AFTER you've dropped the Field_ID column

# Fix swapped/incorrect column names
if 'Chosen_crop' in MD_agric_df.columns:
    MD_agric_df.rename(columns={'Chosen_crop': 'Crop_type'}, inplace=True)

if 'Soil_type' in MD_agric_df.columns:
    MD_agric_df.rename(columns={'Soil_type': 'Soil_Type'}, inplace=True)
    
if 'Soil_fertility' in MD_agric_df.columns:
    MD_agric_df.rename(columns={'Soil_fertility': 'Soil_Fertility'}, inplace=True)

# Fix spelling errors in crop types
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

# Fix negative elevation values (convert to positive)
if 'Elevation' in MD_agric_df.columns:
    MD_agric_df['Elevation'] = MD_agric_df['Elevation'].abs()
