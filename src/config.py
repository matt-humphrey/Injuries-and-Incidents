from pathlib import Path

# Define path variables

DATASETS_DIR = Path(r'\\drive.irds.uwa.edu.au\SPGH-RAINEDATA-001\Data\current datasets in SPSS format')
VALUE_LABELS_DIR = Path(r'C:\Users\00113294\OneDrive - UWA\PORTFOLIO - DATA AND BIOSAMPLES\Data Harmonising')

HOME = Path(__file__).parents[1]

DATA = HOME / 'data'
OG_DATA = DATA / 'original'
RAW_DATA = DATA / 'raw'
INTERIM_DATA = DATA / 'interim'
PROCESSED_DATA = DATA / 'processed'

DOCS = HOME / 'docs'
REFS = HOME / 'references'

WORKBOOK = DOCS / 'questionnaires.xlsx'
SHEETNAME = 'Variables'