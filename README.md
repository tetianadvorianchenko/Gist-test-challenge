# Gist test automation challenge

Tests boilerplate for UI and API is implemented here.

## Run requirements
- pytest installed
- chromedriver installed
- allure installed
- allure_pytest_bdd installed
- web access

## How to run
In command line and run command from the root project folder 
for UI:
```bash
pytest --alluredir=allure-bdd-results -v Tests/UI/Steps/CreateGistsSteps.py
```
for API:
```bash
pytest --alluredir=allure-bdd-results -v Tests/API/Steps/GistAPISteps.py
```
## Results observing
Test report is generated in Json. If you wish a pretty report page, please run:
````
allure generate --clean --output allure-bdd-report allure-bdd-results                 
````
