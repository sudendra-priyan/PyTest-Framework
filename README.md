# PyTest-Framework
Automated some basic flows of Amazon with PyTest Framework

### Prerequisites

Have Python3 installed in you machine.

### Installing

Open requirements.txt and install all the required packages


## Running the tests

To run a test use the following command in terminal/command prompt:

```
pytest "relative_path_of_the_file" --browser "chrome/firefox"  --html= "path_for_report_to_be_generated"
```
* --browser is set to chrome by default, So even if you dont provide this in execution command our project will run
* --html is important to generate a report. So if this is not provided during execution, Report wont be generated

## Example
```
pytest tests/test_executor_book_details.py --browser chrome  --html=../report/report.html
```

## Built With

* [PyTest](https://docs.pytest.org/en/latest/) - The Test Framework used
* [opepyxl](https://pypi.org/project/pytest-excel/) - To Read / Write in Excel Sheet
* [Reporting](https://pypi.org/project/pytest-html/) - Used to generate HTML Report
