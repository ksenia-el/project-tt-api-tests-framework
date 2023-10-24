# project-tt-api-tests-framework

🔸 A snippet of the framework - as a part of the portfolio - with automated tests created for TT.* project (web app for b2b segment; providing knowledge management and team collaboration tools)

🔸 Includes selected tests that:
- validate API and database functionality integration on some of the key endpoints
- are generic for running both positive and negative test cases 
- are parametrized to run on multiple sets of data for comprehensive validation of action permissions based on different user roles
- do a full check of test results, from simple status code of response to all changes that are triggered by API call in PostgreSQL database connected 
- run in each regression testing cycle

▶️ Before running tests the backend of the App could be built and deployed on local machine, as well as App's database (from the separate repository) 

▶️ To install all packages and modules used in the project, simply run the command "pip install -r requirements.txt" in the Terminal of Pycharm.

▶️ To run all tests at once use the command "pytest tests" in the Terminal of Pycharm. Or use the command "pytest ./tests/[name_of_specific_file_with_test.py]" to run a specific test.

*All code shown as an illustration of personal skills in test automation and is fully created by Ksenia Yelyashevich. Published with the consent of the project team and all identification data deleted
