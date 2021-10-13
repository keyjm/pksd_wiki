# Wikipedia Tests

## Project Structure
- locators - Selectors (XPath/CSS) used for pointing to individual HTML elements on Wikipage
  site. Each locators file represents a different path that can be reached on the front-end. For example,
  `locators_wiki.py` represents the `wiki/` page.

- page_functions - Interacts with the locators to perform actions on the page. i.e. clicking, typing, uploading...

- tests - Main folder containing all tests. each `test_`  file represents a base scenarios.

- pytest.ini - Boiler plate pytest code to identify and run tests


## Installation

* Tests were created using 3.9, but I am hoping it should work on any 3.7+ verions
* Download and navigate to repo
* Highly recommend running using python's ven
* To create new venv - `python3 -m venv path/to/your/env (any dir you like)`
* To activate venv - `source /path/to/your/env/bin/activate`
* To install - `pip3 -r requirements.txt`

## Running tests
- Example - `pytest`

## Things I can Improve
* Only using one browser to test i.e. chrome. Ideally you would create a separate class somewhere in your utility folder to create webdriver factory.
* Some common fixtures like setup/teardown to save on time and code efficiency
* Use of custom xpath/CSS
* Use open source selenium grid like selenoid to run tests in parallel