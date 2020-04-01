import pandas as pd
from datetime import datetime

def log(message):
    print(datetime.utcnow(), ': ' + str(message))


log('Reading Microdata Table C')
psam_pusc = pd.read_csv('us_personal/psam_pusc.csv')
log('Extracting 2% Sample')
psam_pusc_sample = psam_pusc.sample(frac=0.02)
log('Writing Sample to CSV')
psam_pusc_sample.to_csv('us_personal/psam_pusc_sample.csv')
log('Done')
