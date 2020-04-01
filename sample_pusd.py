import pandas as pd
from datetime import datetime

def log(message):
    print(datetime.utcnow(), ': ' + str(message))


log('Reading Microdata Table D')
psam_pusd = pd.read_csv('us_personal/psam_pusd.csv')
log('Extracting 2% Sample')
psam_pusd_sample = psam_pusd.sample(frac=0.02)
log('Writing Sample to CSV')
psam_pusd_sample.to_csv('us_personal/psam_pusd_sample.csv')
log('Done')
