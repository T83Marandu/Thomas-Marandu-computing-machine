"""
Test script for Maji Ndogo Analysis functions
"""

import pandas as pd
import sqlite3
import numpy as np
from maji_ndogo_analysis import (
    load_and_clean_data,
    explore_crop_distribution,
    analyse_soil_fertility,
    climate_geography_influence,
    find_ideal_fields,
    find_good_conditions
)


def create_sample_database():
    """Create a sample SQLite database for testing"""
    
    # Create sample data
    np.random.seed(42)
    n_records = 500
    
    field_ids = list(range(1, n_records + 1))
    
    # Geographic features
    geographic_data = {
        'Field_ID': field_ids,
        'Elevation': np.random.uniform(50, 1000, n_records),
        'Latitude': np.random.uniform(-10, 10, n_records),
        'Longitude': np.random.uniform(20, 40, n_records),
        'Location': np.random.choice(['Province_A', 'Province_B', 'Province_C'], n_records),
        'Slope': np.random.uniform(0, 45, n_records)
    }
    
    # Add some negative elevations to test cleanup
    negative_indices = np.random.choice(n_records, 10, replace=False)
    geographic_data['Elevation'][negative_indices] *= -1
    
    # Weather features
    weather_data = {
        'Field_ID': field_ids,
        'Rainfall': np.random.uniform(400, 2000, n_records),
        'Min_temperature_C': np.random.uniform(-8, 5, n_records),
        'Max_temperature_C': np.random.uniform(25, 35, n_records),
        'Ave_temps': np.random.uniform(10, 20, n_records)
    }
    
    # Soil and crop features
    crop_types = ['tea', 'coffee', 'wheat', 'rice', 'maize', 'potato', 'banana', 'cassava']
    # Add some misspellings
    crop_types_with_errors = crop_types + ['tee', 'coffe', 'weat']
    
    soil_and_crop_data = {
        'Field_ID': field_ids,
        'Soil_fertility': np.random.uniform(0.3, 0.9, n_records),
        'Soil_type': np.random.choice(['Loamy', 'Sandy', 'Silt', 'Rocky', 'Peaty', 'Volcanic'], n_records),
        'pH': np.random.uniform(4.5, 8.5, n_records)
    }
    
    # Farm management features
    farm_management_data = {
        'Field_ID': field_ids,
        'Pollution_level': np.random.uniform(0, 0.001, n_records),
        'Plot_size': np.random.uniform(0.5, 10, n_records),
        'Chosen_crop': np.random.choice(crop_types_with_errors, n_records),
        'Annual_yield': np.random.uniform(5, 100, n_records),
        'Standard_yield': np.random.uniform(0.2, 0.9, n_records)
    }
    
    # Create database
    conn = sqlite3.connect('Maji_Ndogo_farm_survey_small.db')
    
    # Create tables
    pd.DataFrame(geographic_data).to_sql('geographic_features', conn, if_exists='replace', index=False)
    pd.DataFrame(weather_data).to_sql('weather_features', conn, if_exists='replace', index=False)
    pd.DataFrame(soil_and_crop_data).to_sql('soil_and_crop_features', conn, if_exists='replace', index=False)
    pd.DataFrame(farm_management_data).to_sql('farm_management_features', conn, if_exists='replace', index=False)
    
    conn.close()
    print("Sample database created: Maji_Ndogo_farm_survey_small.db")


def test_load_and_clean():
    """Test data loading and cleaning"""
    print("\n=== Testing load_and_clean_data ===")
    
    df = load_and_clean_data()
    
    print(f"DataFrame shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print(f"\nUnique crop types: {df['Crop_type'].unique()}")
    print(f"Number of unique crop types: {len(df['Crop_type'].unique())}")
    print(f"Min elevation: {df['Elevation'].min()}")
    print(f"Annual_yield dtype: {df['Annual_yield'].dtype}")
    
    # Verify no negative elevations
    assert df['Elevation'].min() >= 0, "Negative elevations found!"
    print("✓ No negative elevations")
    
    # Verify Field_ID is dropped
    assert 'Field_ID' not in df.columns, "Field_ID column still present!"
    print("✓ Field_ID column dropped")
    
    return df


def test_explore_crop_distribution(df):
    """Test explore_crop_distribution function"""
    print("\n=== Testing explore_crop_distribution ===")
    
    result_tea = explore_crop_distribution(df, "tea")
    print(f"Tea - Rainfall: {result_tea[0]:.2f}, Elevation: {result_tea[1]:.2f}")
    
    result_wheat = explore_crop_distribution(df, "wheat")
    print(f"Wheat - Rainfall: {result_wheat[0]:.2f}, Elevation: {result_wheat[1]:.2f}")
    
    # Verify it returns a tuple
    assert isinstance(result_tea, tuple), "Should return a tuple"
    assert len(result_tea) == 2, "Tuple should have 2 elements"
    print("✓ Returns tuple with 2 elements")
    
    return result_tea, result_wheat


def test_analyse_soil_fertility(df):
    """Test analyse_soil_fertility function"""
    print("\n=== Testing analyse_soil_fertility ===")
    
    result = analyse_soil_fertility(df)
    print(result)
    
    # Verify it returns a Series
    assert isinstance(result, pd.Series), "Should return a Series"
    print("✓ Returns a Series")
    
    return result


def test_climate_geography_influence(df):
    """Test climate_geography_influence function"""
    print("\n=== Testing climate_geography_influence ===")
    
    result = climate_geography_influence(df, 'Crop_type')
    print(result)
    
    # Verify it returns a DataFrame with correct columns
    assert isinstance(result, pd.DataFrame), "Should return a DataFrame"
    expected_columns = ['Elevation', 'Min_temperature_C', 'Max_temperature_C', 'Rainfall']
    assert list(result.columns) == expected_columns, f"Columns should be {expected_columns}"
    print("✓ Returns DataFrame with correct columns")
    
    return result


def test_find_ideal_fields(df):
    """Test find_ideal_fields function"""
    print("\n=== Testing find_ideal_fields ===")
    
    result = find_ideal_fields(df)
    print(f"Top performing crop: {result}")
    
    # Verify it returns a string
    assert isinstance(result, str), "Should return a string"
    print("✓ Returns a string")
    
    return result


def test_find_good_conditions(df):
    """Test find_good_conditions function"""
    print("\n=== Testing find_good_conditions ===")
    
    top_crop = find_ideal_fields(df)
    result = find_good_conditions(df, top_crop)
    print(f"Filtered data shape: {result.shape}")
    print(f"Columns: {len(result.columns)}")
    
    # Verify it returns a DataFrame
    assert isinstance(result, pd.DataFrame), "Should return a DataFrame"
    print("✓ Returns a DataFrame")
    
    # Test with tea specifically
    result_tea = find_good_conditions(df, "tea")
    print(f"Tea filtered data shape: {result_tea.shape}")
    
    return result


def run_all_tests():
    """Run all tests"""
    print("=" * 60)
    print("MAJI NDOGO ANALYSIS - TEST SUITE")
    print("=" * 60)
    
    # Create sample database
    create_sample_database()
    
    # Load and clean data
    df = test_load_and_clean()
    
    # Test all functions
    test_explore_crop_distribution(df)
    test_analyse_soil_fertility(df)
    test_climate_geography_influence(df)
    test_find_ideal_fields(df)
    test_find_good_conditions(df)
    
    print("\n" + "=" * 60)
    print("ALL TESTS COMPLETED SUCCESSFULLY!")
    print("=" * 60)


if __name__ == "__main__":
    run_all_tests()
