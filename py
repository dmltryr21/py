#!pip install pandas-gbq
#!conda install pandas-gbq -c conda-forge
import pandas as pd
import numpy as np
import pandas_gbq
from google.oauth2 import service_account
import copy
import datetime as dt

access3 = pd.read_json(\
        "https://github.com/VladislavLytvyniuk/file/blob/master/My_First_Project-d3d519ff0801.json")


credentials = service_account.Credentials.from_service_account_file(access3)

projectid = "quixotic-being-244818"

query_crm = '''select * from `getcourse_users.getcourse_users`'''

df_crm = pandas_gbq.read_gbq(query_crm, project_id=projectid, credentials=credentials, dialect = "standard")
