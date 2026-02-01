import pandas as pd
import os
import sys
import glob

# Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "dataset")

def load_knowledge_base():
    print("Loading Nutrition Database...")
    try:
        combined_file = os.path.join(DATA_DIR, "combined_food_data.csv")
        
        if os.path.exists(combined_file):
            knowledge_base = pd.read_csv(combined_file)
            print(f"Database Loaded: {len(knowledge_base)} food items.")
            return knowledge_base
        else:
            print(f"Error: Combined data file not found at {combined_file}")
            return None
            
    except Exception as e:
        print(f"Critical Error loading database: {e}")
        return None

def search_knowledge_base(kb, query):
    if kb is None:
        return None
    
    # Simple substring search
    query = query.lower()
    matches = kb[kb['food'].str.lower().str.contains(query, na=False)]
    return matches

# Standard Unit Mapping
UNITS = {
    'Caloric Value': 'kcal',
    'Protein': 'g',
    'Fat': 'g',
    'Saturated Fats': 'g',
    'Monounsaturated Fats': 'g',
    'Polyunsaturated Fats': 'g',
    'Carbohydrates': 'g',
    'Sugars': 'g',
    'Dietary Fiber': 'g',
    'Water': 'g',
    'Cholesterol': 'mg',
    'Sodium': 'mg',
    'Calcium': 'mg',
    'Magnesium': 'mg',
    'Potassium': 'mg',
    'Phosphorus': 'mg',
    'Iron': 'mg',
    'Zinc': 'mg',
    'Copper': 'mg',
    'Manganese': 'mg',
    'Vitamin C': 'mg',
    'Vitamin B6': 'mg',
    'Vitamin E': 'mg',
    # Others are often small (mcg) or vary, so we might leave them or guess
}

def display_nutrition(food_name, data):
    print(f"\n--- Nutritional Facts for '{food_name}' ---")
    
    majors = ['Caloric Value', 'Protein', 'Fat', 'Carbohydrates', 'Sugars']
    print("\n[Major Nutrients]")
    for m in majors:
        if m in data:
            val = data[m]
            unit = UNITS.get(m, "")
            try:
                f_val = float(val)
                print(f"{m:<20}: {f_val:.2f} {unit}")
            except:
                print(f"{m:<20}: {val} {unit}")
    
    print("\n[Detailed Profile (Top 10 others)]")
    try:
        # Drop major nutrients and artifacts
        others = data.drop(majors, errors='ignore')
        
        # Drop indices and artifact columns
        others = others[~others.index.str.contains('^Unnamed', regex=True)]
        others = others.drop(['index', 'level_0', 'id', 'Nutrition Density'], errors='ignore')
        
        # Check if values are numeric
        others = pd.to_numeric(others, errors='coerce').fillna(0)
        
        # Filter out 0 values for cleaner view
        others = others[others > 0]
        
        # Sort and display with units
        top_others = others.sort_values(ascending=False).head(10)
        for idx, val in top_others.items():
            unit = UNITS.get(idx, "")
            print(f"{idx:<20}: {val:.2f} {unit}")
            
    except Exception as e:
        print(f"(Could not display detailed profile: {e})")

def main():
    kb = load_knowledge_base()
    
    if kb is None:
        print("System cannot function without data. Exiting.")
        return

    print("\n" + "="*50)
    print("   NUTRITION DATABASE SEARCH   ")
    print("="*50)
    print("Type a food name to search.")
    print("Type 'q' or 'exit' to quit.")
    
    while True:
        try:
            user_input = input("\n>> Enter food name: ").strip()
            
            if user_input.lower() in ['q', 'exit', 'quit']:
                print("Goodbye!")
                break
            
            if not user_input:
                continue
            
            matches = search_knowledge_base(kb, user_input)
            
            if matches is not None and not matches.empty:
                print(f"\nFound {len(matches)} matching item(s).")
                
                # Check for exact match first
                exact_match = matches[matches['food'].str.lower() == user_input.lower()]
                
                if not exact_match.empty and len(matches) == 1:
                    print("Exact match found!")
                    display_nutrition(exact_match.iloc[0]['food'], exact_match.iloc[0])
                else:
                    # List top 15 results
                    print(f"\nPlease select an item:")
                    top_matches = matches.head(15).reset_index(drop=True)
                    
                    for idx, row in top_matches.iterrows():
                        print(f"[{idx + 1}] {row['food']}")
                    
                    if len(matches) > 15:
                        print(f"... and {len(matches) - 15} more.")
                    
                    print("[0] Cancel Search")
                    
                    selection = input("\nSelect a number: ").strip()
                    
                    if selection.isdigit():
                        sel_idx = int(selection) - 1
                        if 0 <= sel_idx < len(top_matches):
                            selected_item = top_matches.iloc[sel_idx]
                            display_nutrition(selected_item['food'], selected_item)
                        elif sel_idx == -1:
                            print("Search cancelled.")
                        else:
                            print("Invalid selection.")
                    else:
                        print("Invalid input.")
            else:
                print(f"No results found for '{user_input}'. Try a broader term.")
                
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
