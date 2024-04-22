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
console.print(start_title, style="bold deep_sky_blue1")
console.print("\t\t\t\tVersion 0.1.0\t\t\t\t", style="deep_sky_blue1")

# Credit
credit = "[deep_sky_blue1]\n\t[-]\tDeveloper:\t[bold deep_sky_blue1]TK[/bold deep_sky_blue1]\t\t\t\t[-][/deep_sky_blue1]"
credit += "[deep_sky_blue1]\n\t[-]\tGithub:\t\t[bold deep_sky_blue1]https://github.com/TK172500[/bold deep_sky_blue1]\t[-][/deep_sky_blue1]"
console.print(credit)

# Box menu category
box_menu = "\n[bold deep_sky_blue1]Category :[/bold deep_sky_blue1]"
box_menu += "\n   [deep_sky_blue1][1] Women[/deep_sky_blue1]\t\t\t[deep_sky_blue1][2] Men[/deep_sky_blue1]"
box_menu += "\n   [deep_sky_blue1][3] Kids[/deep_sky_blue1]\t\t\t[deep_sky_blue1][4] Baby[/deep_sky_blue1]"
console.print(box_menu)

# Input
category = console.input("\n[deep_sky_blue1][-] Select category: [deep_sky_blue1]")
category = category.lower()

# Box menu type of item
box_menu = "\n[bold deep_sky_blue1]Type of item :[/bold deep_sky_blue1]"
match category:
    case "women" | "1":
        box_menu += "\n   [deep_sky_blue1][1] Tops[/deep_sky_blue1]\t\t\t[deep_sky_blue1][2] Outerwear[/deep_sky_blue1]\t\t\t[deep_sky_blue1][3] Bottoms[/deep_sky_blue1]"
        box_menu += "\n   [deep_sky_blue1][4] Dresses[/deep_sky_blue1]\t\t\t[deep_sky_blue1][5] Innerwear[/deep_sky_blue1]\t\t\t[deep_sky_blue1][6] Loungewear[/deep_sky_blue1]"
        box_menu += "\n   [deep_sky_blue1][7] Sport Utility Wear[/deep_sky_blue1]\t[deep_sky_blue1][8] UV Protection[/deep_sky_blue1]\t\t[deep_sky_blue1][9] Accessories[/deep_sky_blue1]"
        box_menu += "\n   [deep_sky_blue1][10] Maternity[/deep_sky_blue1]"

    case "men" | "2":
        box_menu += "\n   [deep_sky_blue1][1] Tops[/deep_sky_blue1]\t\t\t[deep_sky_blue1][2] Outerwear[/deep_sky_blue1]\t\t\t[deep_sky_blue1][3] Bottoms[/deep_sky_blue1]"
        box_menu += "\n   [deep_sky_blue1][4] Innerwear[/deep_sky_blue1]\t\t[deep_sky_blue1][5] Loungewear[/deep_sky_blue1]\t\t\t[deep_sky_blue1][6] Sport Utility Wear[/deep_sky_blue1]"
        box_menu += "\n   [deep_sky_blue1][7] UV Protection[/deep_sky_blue1]\t\t[deep_sky_blue1][8] Accessories[/deep_sky_blue1]"

    case "kids" | "3":
        box_menu += "\n   [deep_sky_blue1][1] Tops[/deep_sky_blue1]\t\t\t[deep_sky_blue1][2] Outerwear[/deep_sky_blue1]\t\t\t[deep_sky_blue1][3] Bottoms[/deep_sky_blue1]"
        box_menu += "\n   [deep_sky_blue1][4] Dresses[/deep_sky_blue1]\t\t\t[deep_sky_blue1][5] Innerwear[/deep_sky_blue1]\t\t\t[deep_sky_blue1][6] Loungewear[/deep_sky_blue1]"
        box_menu += "\n   [deep_sky_blue1][7] Sport Utility Wear[/deep_sky_blue1]\t[deep_sky_blue1][8] UV Protection[/deep_sky_blue1]\t\t[deep_sky_blue1][9] Accessories[/deep_sky_blue1]"

    case "baby" | "4":
        box_menu += "\n   [deep_sky_blue1][1] Newborn[/deep_sky_blue1]\t\t[deep_sky_blue1][2] Toddler[/deep_sky_blue1]"
    
    case _:
        console.print("Please select the correct category", style="bold red")
        quit()

console.print(f"{box_menu}\n")

# Input
type_of_item = console.input("[deep_sky_blue1][-] Select type of item: [deep_sky_blue1]")
amount_of_item = console.input("[deep_sky_blue1][-] Amount of item: [deep_sky_blue1]")
amount_of_item = int(amount_of_item)

# Test case
# category = "1"
# type_of_item = "1"
# amount_of_item = 1

# Select category
match category:
    case "women" | "1":
        match type_of_item.lower():
            case "tops" | "1":
                url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C25990&limit={amount_of_item}"

            case "outerwear" | "2":
                url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C25991&limit={amount_of_item}"

            case "bottoms" | "3":
                url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C25992&limit={amount_of_item}"

            case "dresses" | "4":
                url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C8406&limit={amount_of_item}"

            case "innerwear" | "5":
                url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C25994&limit={amount_of_item}"

            case "loungewear" | "6":
                url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C25993&limit={amount_of_item}"

            case "sport utility wear" | "7":
                url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C13914&limit={amount_of_item}"

            case "uv protection" | "8":
                url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C80401&limit={amount_of_item}"

            case "accessories" | "9":
                url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C25995&limit={amount_of_item}"

            case "maternity" | "10":
                url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C8429&limit={amount_of_item}"

            case _:
                console.print("Please select the correct type of item", style="bold red")
                quit()

    case "men" | "2":
        match type_of_item.lower():
            case "tops" | "1":
                url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C25997&limit={amount_of_item}"

            case "outerwear" | "2":
                url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C25998&limit={amount_of_item}"

            case "bottoms" | "3":
                url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C26000&limit={amount_of_item}"

            case "innerwear" | "4":
                url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C26003&limit={amount_of_item}"

            case "loungewear" | "5":
                url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C26001&limit={amount_of_item}"

            case "sport utility wear" | "6":
                url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C13998&limit={amount_of_item}"

            case "uv protection" | "7":
                url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C80402&limit={amount_of_item}"

            case "accessories" | "8":
                url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C26004&limit={amount_of_item}"

            case _:
                console.print("Please select the correct type of item", style="bold red")
                quit()

    case "kids" | "3":
        match type_of_item.lower():
            case "tops" | "1":
                url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C25959&limit={amount_of_item}"

            case "outerwear" | "2":
                url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C25934&limit={amount_of_item}"

            case "bottoms" | "3":
                url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C26135&limit={amount_of_item}"

            case "dresses" | "4":
                url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C8529&limit={amount_of_item}"

            case "innerwear" | "5":
                url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C26140&limit={amount_of_item}"

            case "loungewear" | "6":
                url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C8539&limit={amount_of_item}"

            case "sport utility wear" | "7":
                url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C14012&limit={amount_of_item}"

            case "uv protection" | "8":
                url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C80403&limit={amount_of_item}"

            case "accessories" | "9":
                url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C26187&limit={amount_of_item}"

            case _:
                console.print("Please select the correct type of item", style="bold red")
                quit()

    case "baby" | "4":
        match type_of_item.lower():
            case "newborn" | "1":
                url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C32823&limit={amount_of_item}"

            case "toddler" | "2":
                url = f"https://www.uniqlo.com/th/api/commerce/v3/en/products?path=%2C%2C32655&limit={amount_of_item}"

            case _:
                console.print("Please select the correct type of item", style="bold red")
                quit()

    case _:
        console.print("Please select the correct category", style="bold red")
        quit()

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