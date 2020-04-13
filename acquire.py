import numpy as np
import pandas as pd 

from env import host, user, password

def get_db_url(db_name):
    """
    Function to get the url
    """
    return f"mysql+pymysql://{user}:{password}@{host}/{db_name}"

def get_zillow_data_from_sql():
    query = '''
    SELECT
    bathroomcnt AS bathrooms,
    bedroomcnt AS bedrooms,
    calculatedfinishedsquarefeet AS square_feet,
    fips,
    taxvaluedollarcnt AS home_value
    FROM properties_2017 AS prop
        JOIN
        predictions_2017 AS pred 
        ON prop.parcelid = pred.parcelid
        JOIN propertylandusetype AS ptype ON prop.propertylandusetypeid = ptype.propertylandusetypeid
    WHERE transactiondate
    BETWEEN '2017-05-01' AND '2017-06-30' AND propertylandusedesc = 'Single Family Residential'
    '''
    df = pd.read_sql(query, get_db_url('zillow'))
    return df

def get_taxes_from_sql():
    query = """
    SELECT
    taxamount/taxdollarvaluecnt AS county_tax_for_6037, fips
    FROM properties_2017
    JOIN predictions_2017 
    USING (parcelid)
    WHERE 
    (propertylandusetypeid = 261) AND (transactiondate BETWEEN 2017-05-01 AND 2017-06-30)
    """
    df = pd.read_sql(query, get_db_url("zillow"))
    return df