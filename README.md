## About
* Small Python program designed to generate random Texas plate numbers. Shebang is included at the very top of the file to allow direct execution from the terminal.<br />
* Test file is included with pytest.<br />

## Requirements
* Python installed on your machine: https://www.python.org/downloads/<br />
* Pytest installed via pip: https://docs.pytest.org/en/7.1.x/getting-started.html <br />

## How to run
chmod +x texas_plate_generator.py (This is to make the script executable) <br />
./texas_plate_generator.py

## How to run the tests
pytest test_plate_generator.py

## What it demonstrates
* Use of the Python built-in library random to generate pseudo-random numbers.<br />
* Test-driven development with pytest: The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.<br />
* Mass testing with random iterations, to make sure edge cases are covered.<br />
