import pytest

from api import TT  # with the library of all main API requests
from db_queries import DBQueries  # with the library of DB queries used in tests to get data

from settings import TestDataForCreateProject  # test data for create_project type of request
from settings import TestDataForUpdateProject
from settings import TestDataForDeleteProject


class TestTT:

    # #  test to check Database connection
    # def test_db_connection(self, db_connection):
    #     cursor = db_connection.cursor()
    #     cursor.execute("SELECT version();")
    #     record = cursor.fetchone()  # get one record
    #     print("You are connected to - ", record, "\n")

    @pytest.mark.parametrize("test_data", TestDataForCreateProject.all_data)
    def test_create_project(self, test_data, db_connection):

        # login first
        tt = TT()
        status, session = tt.user_sign_in(test_data["credentials"]["email"],
                                                    test_data["credentials"]["password"])
        assert status == 200

        # establish (once for the whole test) connection to database
        cursor = db_connection.cursor()
        db_queries = DBQueries(cursor)

        # run query to get all projects that already exist
        all_projects_before = db_queries.get_all_projects()

        # run request to create a new project
        status, response = tt.create_project(session, test_data)

        #  STARTING TEST ASSERTIONS -----
        assert status == test_data["exp_status_code"]

        # for handling different types of response types
        assert isinstance(response, test_data["exp_response_type"])
        if test_data["exp_response_type"] is list:
            response = response[0]

        if test_data["exp_response_fields"] is not None:
            fields_in_response = response.keys()
            assert len(fields_in_response) == len(test_data["exp_response_fields"])
            for field in test_data["exp_response_fields"]:
                assert field in fields_in_response

            if test_data["expected_values_in_response_fields"] is not None:
                for key in test_data["expected_values_in_response_fields"]:
                    expected_value_in_field = test_data["expected_values_in_response_fields"][key]
                    actual_value_in_field = response[key]
                    assert actual_value_in_field == expected_value_in_field

        if test_data["exp_response_body"] is not None:
            assert response == test_data["exp_response_body"]

        if test_data["exp_status_code"] is 201:
            # run the same query to get all projects that exist after running API call before
            all_projects_after = db_queries.get_all_projects()
            assert len(all_projects_after) == len(all_projects_before) + 1
            # run query to get specifically record of newly created
            created_project_record = db_queries.get_project_by_name(test_data["proj_name"])
            #  assert the value in the second column of the record (index 1) - project_name - is equal to expected
            assert created_project_record[1] == test_data["proj_name"]
            # assert values in other columns of the record
            assert created_project_record[2] == test_data["proj_desc"]
            assert created_project_record[3] == test_data["proj_color"]
            assert created_project_record[4] == test_data["location"].dep_id
            assert created_project_record[5] == test_data["location"].org_id

        if test_data["exp_status_code"] is not 201:
            all_projects_after = db_queries.get_all_projects()
            assert len(all_projects_after) == len(all_projects_before)
            #  assert additionally that the project (with a specific name from test data) was not created
            assert db_queries.get_project_by_name(test_data["proj_name"]) is None

    @pytest.mark.parametrize("test_data", TestDataForUpdateProject.all_data)
    def test_update_project(self, test_data, db_connection):

        tt = TT()
        status, session = tt.user_sign_in(test_data["credentials"]["email"],
                                                    test_data["credentials"]["password"])
        assert status == 200

        project_id = test_data["location"].proj_id

        cursor = db_connection.cursor()
        db_queries = DBQueries(cursor)

        project_record_before = db_queries.get_project_by_id(project_id)

        # run API request to update project
        status, response = tt.update_project(session, test_data)

        assert status == test_data["exp_status_code"]

        assert isinstance(response, test_data["exp_response_type"])
        if test_data["exp_response_type"] is list:
            response = response[0]

        if test_data["exp_response_fields"] is not None:
            fields_in_response = response.keys()
            assert len(fields_in_response) == len(test_data["exp_response_fields"])
            for field in test_data["exp_response_fields"]:
                assert field in fields_in_response

            if test_data["expected_values_in_response_fields"] is not None:
                for key in test_data["expected_values_in_response_fields"]:
                    expected_value_in_field = test_data["expected_values_in_response_fields"][key]
                    actual_value_in_field = response[key]
                    assert actual_value_in_field == expected_value_in_field

        if test_data["exp_response_body"] is not None:
            assert response == test_data["exp_response_body"]

        if test_data["exp_status_code"] is 200:
            # run the same query to get project info after running API call before
            project_record_after = db_queries.get_project_by_id(project_id)
            assert project_record_after != project_record_before

            #  assert the value in the second column of the record (index 1) - project_name - is equal to expected
            assert project_record_after[1] == test_data["new_proj_name"]
            # assert values in other columns of the record
            assert project_record_after[2] == test_data["new_proj_desc"]
            assert project_record_after[3] == test_data["new_proj_color"]

        if test_data["exp_status_code"] is not 200:
            project_record_after = db_queries.get_project_by_id(project_id)
            assert project_record_after == project_record_before

    @pytest.mark.parametrize("test_data", TestDataForDeleteProject.all_data)
    def test_delete_project(self, test_data, db_connection):

        tt = TT()
        status, session = tt.user_sign_in(test_data["credentials"]["email"],
                                                    test_data["credentials"]["password"])
        assert status == 200

        project_id = test_data["location"].proj_id

        cursor = db_connection.cursor()
        db_queries = DBQueries(cursor)

        all_projects_before = db_queries.get_all_projects()
        project_record_before = db_queries.get_project_by_id(project_id)

        # run request to delete project
        status, response = tt.delete_project(session, test_data)
        print(response)

        assert status == test_data["exp_status_code"]

        assert isinstance(response, test_data["exp_response_type"])
        if test_data["exp_response_type"] is list:
            response = response[0]

        if test_data["exp_response_fields"] is not None:
            fields_in_response = response.keys()
            assert len(fields_in_response) == len(test_data["exp_response_fields"])
            for field in test_data["exp_response_fields"]:
                assert field in fields_in_response

            if test_data["expected_values_in_response_fields"] is not None:
                for key in test_data["expected_values_in_response_fields"]:
                    expected_value_in_field = test_data["expected_values_in_response_fields"][key]
                    actual_value_in_field = response[key]
                    assert actual_value_in_field == expected_value_in_field

        if test_data["exp_response_body"] is not None:
            assert response == test_data["exp_response_body"]

        if test_data["exp_status_code"] is 200:
            # run the same query to get all projects that exist after running API call before
            all_projects_after = db_queries.get_all_projects()
            assert len(all_projects_after) == len(all_projects_before) - 1
            #  assert additionally that the project (with a specific ID from test data) does not exist now
            assert db_queries.get_project_by_id(project_id) is None

        if test_data["exp_status_code"] is not 200:
            # run the same query to get all projects that exist after running API call before
            all_projects_after = db_queries.get_all_projects()
            assert len(all_projects_after) == len(all_projects_before)

            project_record_after = db_queries.get_project_by_id(project_id)
            assert project_record_after == project_record_before

# TODO: think about adding fixtures to create and delete instances after test run?
#  OR skip it (by using precise sets of test data and re-building database from scratch before every cycle of running all tests)

# TODO: pack repeating parts of code from tests in one separate method
