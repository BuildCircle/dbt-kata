import duckdb
import pandas as pd
import argparse
from pathlib import Path
import sys

# Configuration
PROJECT_NAME = "streamflix"  # Must match 'name' in dbt_project.yml
COMPILED_DIR = Path(f"target/compiled/{PROJECT_NAME}/analyses")
DB_PATH = "dbt.duckdb"

def run_analysis(analysis_name):
    """
    Reads a compiled SQL file from the dbt target directory and executes it.
    
    Args:
        analysis_name (str): The name of the SQL file (e.g., 'my_analysis.sql')
    """
    sql_path = COMPILED_DIR / analysis_name
    
    if not sql_path.exists():
        print(f"Error: Compiled SQL file not found at {sql_path}")
        print("Did you run 'dbt compile'?")
        sys.exit(1)

    print(f"--- Running Analysis: {analysis_name} ---")
    
    with open(sql_path, 'r') as f:
        sql_query = f.read()
        
    con = duckdb.connect(DB_PATH)
    df = con.sql(sql_query).df()
    print(df)
    print("\n")
    con.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a compiled dbt analysis against the local DuckDB database.")
    parser.add_argument("analysis_file", help="The name of the SQL file in the analyses directory to run (e.g., new_users_last_month.sql)")
    
    args = parser.parse_args()
    
    run_analysis(args.analysis_file)
