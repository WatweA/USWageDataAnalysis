import pandas as pd
from datetime import datetime

def log(message):
    print(datetime.utcnow(), ': ' + str(message))


log('Reading Microdata Table A')
psam_pusa = pd.read_csv('us_personal/psam_pusa.csv')
log('Extracting 2% Sample')
psam_pusa_sample = psam_pusa.sample(frac=0.02)
log('Writing Sample to CSV')
psam_pusa_sample.to_csv('us_personal/psam_pusa_sample.csv')
log('Done')
