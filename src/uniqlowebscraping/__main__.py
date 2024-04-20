import requests
import json
import pandas as pd

# Set up
headers = {
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36',
}
amount_of_item = 300

# URL
url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C25997&limit={amount_of_item}"

# Process
res = requests.get(url, headers=headers)
data_dumps = json.dumps(res.json()) # Convert to string
data = json.loads(data_dumps) # Convert to json

# Show the data
df = pd.DataFrame(data["result"]["items"])
df.to_csv("uniqlo.csv", index=False)