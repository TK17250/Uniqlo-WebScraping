import requests
import pandas as pd
from rich.console import Console
from rich.traceback import install
from rich.progress import Progress
import json
import random

# Set up
install()
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
]
headers = {'User-Agent': random.choice(user_agents)} # Random user agent
console = Console()

# Title
start_title = r"""

  __  __     _      __                  __                           _          
 / / / /__  (_)__ _/ /__    _    _____ / /    ___ ___________ ____  (_)__  ___ _
/ /_/ / _ \/ / _ `/ / _ \  | |/|/ / -_) _ \  (_-</ __/ __/ _ `/ _ \/ / _ \/ _ `/
\____/_//_/_/\_, /_/\___/  |__,__/\__/_.__/ /___/\__/_/  \_,_/ .__/_/_//_/\_, / 
              /_/                                           /_/          /___/  

"""
console.print(start_title, style="bold blue")

amount_of_item = 1

# URL
url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C25997&limit={amount_of_item}"


# Progress bar request
with Progress() as progress:
    task = progress.add_task("[cyan]Scraping...", total=100)
    while not progress.finished:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            progress.update(task, advance=100)
            progress.stop()

res = requests.get(url, headers=headers)
data_dumps = json.dumps(res.json()) # Convert to string
data = json.loads(data_dumps) # Convert to json

# Data
df = pd.DataFrame(data["result"]["items"])
df.to_csv("uniqlo.csv", index=False)
if data["result"] : console.print("Scraping success fully!", style="bold green")