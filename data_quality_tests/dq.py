import pandas as pd
import numpy as np
import json
import datetime
from typing import Dict
import inspect
import gc
import os


class DataQuality:
    """
    Initiate a data quality assessment class with (as of now) 4 test cases to check data quality
    """

    def __init__(self, df):
        self.df = df

    def generate_schema(self) -> Dict:
        """
        Generate a schema definition from the DataFrame
        without statistical information
            
        Returns:
        --------
        dict
            A schema definition including column names, types, and basic properties
        """
        schema = {
            "version": 1,
            "creation_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "row_count": self.get_row_count(),
            "column_count": len(self.df.columns),
            "columns": {},
            "schema_fingerprint": ""
        }
        
        for column in self.df.columns:
            col_data = self.df[column]
            dtype_name = str(col_data.dtype)
            
            # Determine nullability and unique counts
            null_count = col_data.isna().sum()
            unique_count = col_data.nunique()
            
            # Basic column properties only
            schema["columns"][column] = {
                "dtype": dtype_name,
                "nullable": bool(null_count > 0),
                "null_count": int(null_count),
                "unique_count": int(unique_count)
            }
        
        # Create a schema fingerprint for quick comparison (without hashlib)
        column_fingerprints = []
        for col_name in sorted(schema["columns"].keys()):
            col_info = schema["columns"][col_name]
            column_fingerprints.append(
                f"{col_name}:{col_info['dtype']}:{col_info['nullable']}"
            )
        
        # Join all column fingerprints to create schema fingerprint
        schema["schema_fingerprint"] = "|".join(column_fingerprints)
        
        return schema
    
    def print_schema(self) -> None:
        """
        Generate and print a human-readable schema of the DataFrame
        without statistical information
        """
        schema = self.generate_schema()
        
        print("\n===== DATAFRAME SCHEMA =====")
        print(f"Created: {schema['creation_date']}")
        print(f"Rows: {schema['row_count']}")
        print(f"Columns: {schema['column_count']}")
        print(f"Schema Fingerprint: {schema['schema_fingerprint'][:50]}...")  # Show truncated fingerprint
        print("\n=== COLUMNS ===")
        
        # Column type counts for summary
        type_counts = {}
        for col_info in schema["columns"].values():
            dtype = col_info["dtype"]
            if dtype not in type_counts:
                type_counts[dtype] = 0
            type_counts[dtype] += 1
            
        # Print type summary
        print("Type Distribution:")
        for dtype, count in type_counts.items():
            print(f"  - {dtype}: {count} columns")
        
        print("\nDetailed Column Information:")
        for col_name, col_info in schema["columns"].items():
            print(f"  • {col_name}")
            print(f"    Type: {col_info['dtype']}")
            print(f"    Nullable: {'Yes' if col_info['nullable'] else 'No'}")
            print(f"    Null Count: {col_info['null_count']}")
            print(f"    Unique Values: {col_info['unique_count']}")

    
    def save_schema_to_file(self) -> None:
        """
        Generate schema and automatically save it to a JSON file in the current directory
        using the DataFrame name. Checks for existing schema files and offers
        version update if the same schema name is found.
        """
        schema = self.generate_schema()

        # Try to determine DataFrame name
        df_name = "dataframe"  # Default name

        # Look for variable names in parent frames - safer approach

        # Check all variables in caller's frame
        frame = inspect.currentframe().f_back
        if frame:
            for var_name, var_val in frame.f_locals.items():
                if isinstance(var_val, pd.DataFrame) and var_val is self.df:
                    df_name = var_name
                    break
                
        # Create filename
        file_name = f"{df_name}_schema.json"

        # Check if file already exists
        
        if os.path.exists(file_name):
            try:
                with open(file_name, 'r') as file:
                    existing_schema = json.load(file)

                # If schema exists, ask user if they want to update
                user_response = input(f"Schema file '{file_name}' already exists. Update with version {existing_schema.get('version', 1) + 1}? (y/n): ")

                if user_response.lower() == 'y':
                    # Update version and save
                    schema['version'] = existing_schema.get('version', 1) + 1
                    with open(file_name, 'w') as file:
                        json.dump(schema, file, indent=2)
                    print(f"Schema updated and saved to {file_name} (version {schema['version']})")
                else:
                    print("Schema update cancelled.")
            except Exception as e:
                print(f"Error reading existing schema: {e}")
                print("Saving as new schema...")
                with open(file_name, 'w') as file:
                    json.dump(schema, file, indent=2)
                print(f"Schema saved to {file_name}")
        else:
            # No existing file, save directly
            try:
                with open(file_name, 'w') as file:
                    json.dump(schema, file, indent=2)
                print(f"Schema saved to {file_name}")
            except Exception as e:
                print(f"Error saving schema: {e}")

    def compare_with_schema(self, other_schema: Dict) -> Dict:
        """
        Compare current DataFrame schema with another schema
        
        Parameters:
        -----------
        other_schema : dict
            Another schema to compare against
            
        Returns:
        --------
        dict
            Differences between the schemas
        """
        current_schema = self.generate_schema()
        
        if current_schema["schema_fingerprint"] == other_schema.get("schema_fingerprint", ""):
            return {"status": "Schemas are identical"}
            
        differences = {
            "new_columns": [],
            "missing_columns": [],
            "type_changes": [],
            "nullable_changes": []
        }
            
        # Check for new and missing columns
        current_cols = set(current_schema["columns"].keys())
        other_cols = set(other_schema.get("columns", {}).keys())
            
        differences["new_columns"] = list(current_cols - other_cols)
        differences["missing_columns"] = list(other_cols - current_cols)
            
        # Check common columns for changes
        common_columns = current_cols.intersection(other_cols)
        for column in common_columns:
            current_col = current_schema["columns"][column]
            other_col = other_schema["columns"][column]
                
            # Check for type changes
            if current_col["dtype"] != other_col["dtype"]:
                differences["type_changes"].append({
                    "column": column,
                    "current_type": current_col["dtype"],
                    "other_type": other_col["dtype"]
                })
                    
            # Check for nullable changes
            if current_col["nullable"] != other_col["nullable"]:
                differences["nullable_changes"].append({
                    "column": column,
                    "current_nullable": current_col["nullable"],
                    "other_nullable": other_col["nullable"]
                })
                
        return differences

    def get_row_count(self) -> int:
        """
        Returns the count of rows for the user to use
        """
        return len(self.df)
    
    def data_quality_check(self):
        
        """
        
        Data Quality check 
        Input - dataset
        Output - data quality as test cases

        The out put will be in the form of the test cases below followed by Passed or Failed

        the test case checks are of conditional checks and logic that goes on in normal EDA.
        
        Checks include:
        
        1. Test for null values
        2. Test for duplicates
        3. Test for dtype matching
        4. Test for outliers - depricated
        5. Test for column header whitespaces               
    
        """      
        
        # TEST FOR NULL VALUES
        # if null values exist -> condition = true then test failed, else false
        
        
        #print("TEST FOR NULL VALUES:")
        print("Note:")
        print("Fail - Failed for test case due to existing condition.")
        print("Pass - Clear of condition.")
        print("")
        print("Number of rows: ", self.get_row_count())
        print("")
        if self.df.isnull().values.any() == True:
            print("Test Case Null Values: Fail")
        else:
            print('Test Case Null Values: Pass')
            
        
        #print("Total number of null values: ",null_sum)
        print("")

        
        
        # TEST FOR DUPLICATES
        
        if self.df.duplicated().any() == True:
            print("Test Case Duplicated Values: Fail")
        else:
            print("Test Case Duplicated Values: Pass")
        #duplicate_sum = df.duplicated().sum()
        #print("Total number of duplicates: ", duplicate_sum)
        print("")
        


        # TEST For dtype matching
        
        # num_list is checking whether the columns are numeric or not-
        # a list of true and false where false is not number and true is number
        num_col_list_bool = self.df.apply(lambda s: pd.to_numeric(s, errors='coerce').notnull().all()).to_list()
        # col_list is a list of columns
        col_list = self.df.columns
        # index_cols is a list of tuples of the format - (bool,column_name) example - (False, 'booking_id')
        index_cols = list(zip(num_col_list_bool, col_list))
        dtype_truth = []
        for i in index_cols:
            if i[0]==False:
                if self.df[i[1]].isna().any() == True:
                    pass
                elif any(self.df[i[1]].str.contains(r'\b.*[a-zA-Z]+.*\b')) == False:
                    my_truth = 'False'
                    dtype_truth.append(my_truth)
                else:
                    my_truth = 'True'
                    dtype_truth.append(my_truth)
            else:
                my_truth = 'True'
                dtype_truth.append(my_truth)
        fail = "False"
        if fail in dtype_truth:
            print('Test Case Column Data Type Matches Values In Column: Fail')
        else:
            print('Test Case Column Data Type Matches Values In Column: Pass')
        print("")


        # TEST FOR COLUMN HEADER LEADING AND TRAILING SPACES
        col_list = [x for x in self.df.columns if x.endswith(' ') or x.startswith(' ')]
    
        if len(col_list) == 0:
            print("Test Case Column Header Whitespaces: Pass")
        else:
            print("Test Case Column Header Whitespaces: Fail")
        print("")



 

        


    


    
    