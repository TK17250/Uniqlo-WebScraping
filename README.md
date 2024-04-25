# Uniqlo Web Scraping 👕⛏️
Version 1.0.0

##  Video Tutorial
<p align="center">
    <img src="https://github.com/TK17250/Uniqlo-WebScraping/blob/main/info/tutorial.gif" style="width: 80%;">
</p>

## How to use

#### Step 1: Clone the repository
```
git clone https://github.com/TK17250/Uniqlo-WebScraping.git

cd Uniqlo-WebScraping
```

#### Step 2: Install the required packages
```
pip install -r requirements.lock
```
or
```
rye sync
```

#### Step 3: Run the script
```
rye run python src/uniqlowebscraping/
```
or
```
python src/uniqlowebscraping/
```

#### Step 4: Fill in information
```
1. Select the category

2. Select type of item

3. Fill amount of items

4. Choose to download images or not (y/n)
```

#### Step 5: Wait for the scraping to finish
1. The data will be in csv file format.
2. If you choose to download images You will have to wait until the images are all finished downloading.

#### Note: All data will be in the data folder.