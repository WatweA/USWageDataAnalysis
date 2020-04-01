import pandas as pd
from datetime import datetime

def log(message):
    print(datetime.utcnow(), ': ' + str(message))


log('Reading Microdata Table B')
psam_pusb = pd.read_csv('us_personal/psam_pusb.csv')
log('Extracting 2% Sample')
psam_pusb_sample = psam_pusb.sample(frac=0.02)
log('Writing Sample to CSV')
psam_pusb_sample.to_csv('us_personal/psam_pusb_sample.csv')
log('Done')
