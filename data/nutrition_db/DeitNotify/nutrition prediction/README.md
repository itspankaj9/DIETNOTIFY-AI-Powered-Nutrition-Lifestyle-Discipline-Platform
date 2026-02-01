# 🥗 Nutrition Database Search System

A robust, interactive Python command-line tool for retrieving accurate nutritional information from a curated food dataset.

Unlike AI-based estimators that might "guess" values, this system searches a verified database of over 2,000 food items to provide **exact, recorded nutritional facts**.

## ✨ Features

*   **🔍 Exact Search**: Finds verified food data; no hallucinations or estimates.
*   **🔢 Precision Units**: Displays values in standard units (`kcal`, `g`, `mg`).
*   **🧠 Smart Disambiguation**: Interactive menu handling for vague terms (e.g., searching "Burger" lets you choose between "Cheeseburger", "Veggie Burger", etc.).
*   **⚡ Optimized Performance**: Uses a single, merged CSV dataset for instant retrieval.
*   **📁 Zero Dependencies**: (Almost) - only requires `pandas`.

## 📂 Project Structure

```text
.
├── dataset/                  
│   └── combined_food_data.csv  # The core dataset (merged & optimized)
├── nutrition_search.py         # The main interactive search application
└── README.md                   # Project documentation
```

## �️ Installation & Setup

### 1. Prerequisites
Ensure you have Python installed. The only external requirement is `pandas`.

```bash
pip install pandas
```

### 2. Clone/Download
Download this repository to your local machine.

## 🚀 How to Run

1.  Open your terminal or command prompt.
2.  Navigate to the project directory.
3.  Run the script:

```bash
python nutrition_search.py
```

## � Usage Example

**1. Start the System:**
```text
==================================================
   NUTRITION DATABASE SEARCH
==================================================
Type a food name to search.
Type 'q' or 'exit' to quit.
```

**2. Search for a Food (e.g., "Apple"):**
```text
>> Enter food name: apple

Found 30 matching item(s).
Please select an item:
[1] apple pie
[2] apple butter
[3] apple juice
...
```

**3. Select & View Data:**
```text
Select a number: 1

--- Nutritional Facts for 'apple pie' ---

[Major Nutrients]
Caloric Value       : 265.00 kcal
Protein             : 2.40 g
Fat                 : 12.50 g
Carbohydrates       : 37.10 g
Sugars              : 18.00 g

[Detailed Profile]
Sodium              : 205.00 mg
Cholesterol         : 0.00 mg
...
```

## 📊 Dataset Info
The system relies on `dataset/combined_food_data.csv`. This file contains standard nutritional columns including:
*   **Macronutrients**: Calories, Protein, Fat, Saturated Fats, Carbohydrates, Sugars, Fiber.
*   **Micronutrients**: Sodium, Cholesterol, Calcium, Magnesium, Potassium, Iron, Zinc, Vitamin C, etc.

## 🤝 Contributing
Feel free to add more food items to `combined_food_data.csv` following the existing schema to expand the knowledge base!
