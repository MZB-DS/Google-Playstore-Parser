# Google-Playstore-Parser
The repository contains python code to fetch all app-storeurls of the respective company. Given any android app url, it goes to it's company's page and parses all the android apps which are there under that company.

## How to use this code
1. Enter the name of your input and output file. For getting the format of the input file, kindly refer ```Sample_Input.xlsx```.
2. Mention proper path of the geckodriver file.
3. Execute the ```google_appstoreurl_parser.py ```.

## Future Features
Currently if the number of apps under any company exceeds 30, then some apps misses out. Will make update in the code in order to include all.

## Dependencies
- Python3 any version.
- Selenium webdriver for your preferred browser. Install from here: https://www.selenium.dev/downloads/
- Python packages: selenium==3.141.0(For working with web browser), time(for waiting while scroll down), bs4(For html parsing), warnings(for suppressing warning messages), re(regular expression, pattern matching), pandas(for python dataframe), tqdm(For displaying progress bar), urllib.request(For fetching html source code from given url)
Installation command: ```pip3 install selenium==3.141.0 bs4 tqdm warnings pandas==1.0.1 urllib```
