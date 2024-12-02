import raine_tools as rn
import pandas as pd
from pydantic import BaseModel, ValidationError, field_validator
from typing import List, Dict, Optional

from src.config import DATASETS_DIR, RAW_DATA

class StringToDictInput(BaseModel):
    text: str
    delimiter: str = ';'
    equals: str = '='

    @field_validator('text')
    def validate_text(cls, v):
        if not v:
            raise ValidationError('Text cannot be empty')
        return v
    

def copy_datasets(df: pd.DataFrame) -> None:
    files_to_find = set(df['dataset'])

    # Locate all the relevant datasets, and copy them to the specified directory
    rn.find_and_copy_sav_files(DATASETS_DIR, RAW_DATA, files_to_find=files_to_find)

def string_to_dict(input: str) -> Dict[int, str]:
    input = StringToDictInput(text=input)
    try:
        return {
            float(n): label[1:-1]
            for t in input.text.split(input.delimiter)
            for n, label in [t.split(input.equals)]
        }
    except ValueError as e:
        raise ValueError(f"Error processing input: {e}")
    
def output_value_counts(df: pd.DataFrame, col: str) -> pd.DataFrame:
    value_counts = {col: df[col].value_counts()}
    value_counts_df = pd.DataFrame(value_counts).fillna(0).astype(int)

    return value_counts_df.T

def value_counts(df: pd.DataFrame, vars: Optional[List[str]] = None) -> pd.DataFrame:
    i = []
    if vars is not None:
        vars = [var for var in vars if var in df.columns]
    else:
        vars = df.columns.get_level_values(0).unique()
    for var in vars: 
        i.append(output_value_counts(df, var))
    df_final = pd.concat(i).fillna(0).astype(int)
    return df_final.reindex(columns=sorted(df_final.columns))