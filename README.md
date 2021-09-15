# Scrapping with Scrapy

This project using python 3.5, if your python not same i recommend using miniconda / anaconda to make enviroment with python 3.5 and install scrapy too

## Installation

1. Install Scrapy

   See the documentation to install Scrapy on your computer: [documentation](https://docs.scrapy.org/en/latest/intro/install.html)

2. Running Scrapy and generate to file csv
   ```bash
    scrapy crawl description -o result.csv
   ```

## More Information

1. For started project you can run this command

   ```bash
   scrapy startproject example
   ```

2. If you want to make new file scrapping you can run this command

   ```bash
   scrapy genspider product tokopedia.com
   ```

   And this file it will be create in folder spiders

3. Running shell for test xpath in Scrapy
   ```bash
   scrapy shell 'https://test.com/movie'
   ```
4. Running shell for test xpath in Scrapy
   ```bash
   scrapy shell 'https://test.com/movie'
   ```

## Authors

- **Muhammad Zahidin Nur** - _Full stack developer_ - [My Github](https://github.com/zahidin)
