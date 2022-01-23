### Prepare
* Python3 Enviroment
* download chromedriver to you %PATH%

### test_behave

> Using pip install the python library
```
pip install -r requirement.txt
```

> Run web task
```
 behave features/navi_to_trade_page.feature 
```

> Run api task
```
python test_api.py  
```

> Run behave with allure report
```
behave -f allure_behave.formatter:AllureFormatter -o report ./features

allure serve report
```