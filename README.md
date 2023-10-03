# tt-api-and-db-testing-framework
Framework with automated tests for backend of the TT* App (b2b, team and knowledge management platform). 

[Currently] includes:
- tests for 3 API endpoints (with the full check of actual result; by executing queries in database among others)
- sets of test data for 2 user roles, including expected result of tests depending on user role (so, in general, 17 test runs for now)

▶️ Before running tests the backend of the App should be built and deployed on local machine, as well as App's database (from the separate repository) 

▶️ To install all packages and modules used in the project, simply run the command "pip install -r requirements.txt" in the Terminal of Pycharm.

▶️ To run all tests at once use the command "pytest tests" in the Terminal of Pycharm. Or use the command "pytest ./tests/[name_of_specific_file_with_test.py]" to run a specific test from all.
