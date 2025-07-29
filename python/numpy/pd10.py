import pandas as pd

from io import StringIO
Data = '{"employee_name":"James", "email": "jamesgmail.com", "job_profile":[{"title1":"Team Lead", "title2":"Sr.Developer"}]}'
read_data=pd.read_json(StringIO(Data))
print(read_data)

import pandas as pd

url_1= "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
df = pd.read_csv(url_1, header=None)

print("\n",df.head())

url_2="https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/"
df2= pd.read_html(url_2)
print("\n",df2)

url_3 ="https://en.wikipedia.org/wiki/Mobile_country_code"
df3=pd.read_html(url_3, match="Country",header=0)[0]
print("\n",df3)