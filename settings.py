# file with test data for:
# 1) every role
# 2) and every test case (including expected result) depending on user role

import datetime


class UserRoleLocation:
    def __init__(self, org_id: int, dep_id: int, proj_id: int, board_id: int, board_labels_ids: list,
                 team_id: int, team_lead_id: int, team_users_ids: list, team_tickets_ids: list):
        self.org_id = org_id
        self.dep_id = dep_id
        self.proj_id = proj_id
        self.board_id = board_id
        self.board_labels_ids = board_labels_ids
        self.team_id = team_id
        self.team_lead_id = team_lead_id
        self.team_users_ids = team_users_ids
        self.team_tickets_ids = team_tickets_ids


# ----------- FOR PROJECT ADMIN ROLE ---------------

class TestDataForProjectAdminRole:
    # credentials used to sign in as user with specific role
    VALID_EMAIL = "***change_me***"
    VALID_PASSWORD = "***change_me***"

    # ------ VALUES OF WHAT IS 'OWN' AND WHAT IS 'OTHER'S' FOR THE USER WITH THIS SPECIFIC ROLE ------

    # OWN organization, department, project, board, board labels,
    # team, team lead, team users, team tickets
    OWN_org_dep_proj_board_boardlabels_team_teamlead_teamusers_teamtickets = UserRoleLocation(
        org_id=1,
        dep_id=1,
        proj_id=1,
        board_id=1,
        board_labels_ids=[1, 2, 3, 4, 5],
        team_id=1,
        team_lead_id=9,
        team_users_ids=[1, 2, 3, 4, 5, 6],
        team_tickets_ids=[1, 2, 4]
    )

    # OWN organization, department, OTHER project, board, board labels,
    # team, team lead, team users, team tickets
    OWN_org_dep_OTHER_proj_board_boardlabels_team_teamlead_teamusers_teamtickets = UserRoleLocation(
        org_id=1,
        dep_id=1,
        proj_id=2,
        board_id=2,
        board_labels_ids=[6, 7, 8, 9, 10],
        team_id=3,
        team_lead_id=12,
        team_users_ids=[11, 12, 13, 14, 15, 16],
        team_tickets_ids=[6, 8, 7]
    )

    # OWN organization, OTHER department, project, board, board labels,
    # team, team lead, team users, team tickets
    OWN_org_OTHER_dep_proj_board_boardlabels_team_teamlead_teamusers_teamtickets = UserRoleLocation(
        org_id=1,
        dep_id=2,
        proj_id=3,
        board_id=3,
        board_labels_ids=[11, 12, 13, 14, 15],
        team_id=5,
        team_lead_id=14,
        team_users_ids=[21, 22, 23, 24, 25, 26],
        team_tickets_ids=[11, 12, 13]
    )

    # OTHER organization, department, project, board, board labels,
    # team, team lead, team users, team tickets
    OTHER_org_dep_proj_board_boardlabels_team_teamlead_teamusers_teamtickets = UserRoleLocation(
        org_id=2,
        dep_id=3,
        proj_id=5,
        board_id=5,
        board_labels_ids=[21, 22, 23, 24, 25],
        team_id=9,
        team_lead_id=32,
        team_users_ids=[41, 42, 43, 44, 45, 46],
        team_tickets_ids=[21, 22, 23]
    )

    # ------ TEST DATA FOR EVERY SEPARATE TEST CASE FOR PROJECT ADMIN ROLE ------
    # includes: 1) test data used in request 2) what is expected in response

    # data for test_create_project
    create_project_test_data_tc_17_negative = {
        "credentials": {"email": VALID_EMAIL, "password": VALID_PASSWORD},
        "location": OWN_org_dep_proj_board_boardlabels_team_teamlead_teamusers_teamtickets,
        "proj_name": f"TC17-N PA {datetime.datetime.now()}",
        # value for request (TC - test case, N - negative, PA - Project Admin) - ! name should be no longer than 50 symbols
        "proj_desc": "Project desc",  # value for request
        "proj_color": "#FFFFFF",

        "exp_status_code": 400,
        "exp_response_type": list,
        "exp_response_body": None,  # in case the whole body should be equal to some value (like string, for example)
        "exp_response_fields": ["action", "error"],  # all fields' titles expected in response
        "expected_values_in_response_fields": {
            "action": "departments:CreateProjects",
            "error": "You do not have the necessary permission to perform this action"
        }
    }

    create_project_test_data_tc_18_negative = {
        "credentials": {"email": VALID_EMAIL, "password": VALID_PASSWORD},
        "location": OWN_org_OTHER_dep_proj_board_boardlabels_team_teamlead_teamusers_teamtickets,
        "proj_name": f"TC18-N PA {datetime.datetime.now()}",
        "proj_desc": "Project desc",  # value for request
        "proj_color": "#FFFFFF",

        "exp_status_code": 400,
        "exp_response_type": list,
        "exp_response_body": None,  # in case the whole body should be equal to some value (like string, for example)
        "exp_response_fields": ["action", "error"],  # all fields' titles expected in response
        "expected_values_in_response_fields": {
            "action": "departments:CreateProjects",
            "error": "You do not have the necessary permission to perform this action"
        }
    }

    create_project_test_data_tc_19_negative = {
        "credentials": {"email": VALID_EMAIL, "password": VALID_PASSWORD},
        "location": OTHER_org_dep_proj_board_boardlabels_team_teamlead_teamusers_teamtickets,
        "proj_name": f"TC19-N PA {datetime.datetime.now()}",
        "proj_desc": "Project desc",  # value for request
        "proj_color": "#FFFFFF",

        "exp_status_code": 400,
        "exp_response_type": dict,
        "exp_response_body": None,  # in case the whole body should be equal to some value (like string, for example)
        "exp_response_fields": ["detail"],  # all fields' titles expected in response
        "expected_values_in_response_fields": {
            "detail": "Does not exist"
        }
    }

    update_project_test_data_tc_20_1_positive = {
        "credentials": {"email": VALID_EMAIL, "password": VALID_PASSWORD},
        "location": OWN_org_dep_proj_board_boardlabels_team_teamlead_teamusers_teamtickets,
        "new_proj_name": f"TC20-1-P PA {datetime.datetime.now()}",
        "new_proj_desc": "Updated project desc",  # value for request
        "new_proj_color": "#E25098",

        "exp_status_code": 200,
        "exp_response_type": dict,
        "exp_response_body": None,
        "exp_response_fields": ["detail", "data"],  # all fields' titles expected in response
        "expected_values_in_response_fields": {
            "detail": "Project was successfully updated"
        }
    }

    update_project_test_data_tc_20_2_negative = {
        "credentials": {"email": VALID_EMAIL, "password": VALID_PASSWORD},
        "location": OWN_org_dep_OTHER_proj_board_boardlabels_team_teamlead_teamusers_teamtickets,
        "new_proj_name": f"TC20-2-N PA {datetime.datetime.now()}",
        "new_proj_desc": "Updated project desc",
        "new_proj_color": "#E25091",

        "exp_status_code": 400,
        "exp_response_type": list,
        "exp_response_body": None,
        "exp_response_fields": ["action", "error"],
        "expected_values_in_response_fields": {
            "action": "projects:Update",
            "error": "You do not have the necessary grid pattern to perform this action"
        }
    }

    update_project_test_data_tc_21_negative = {
        "credentials": {"email": VALID_EMAIL, "password": VALID_PASSWORD},
        "location": OWN_org_OTHER_dep_proj_board_boardlabels_team_teamlead_teamusers_teamtickets,
        "new_proj_name": f"TC21-N PA {datetime.datetime.now()}",
        "new_proj_desc": "Updated project desc",
        "new_proj_color": "#E25091",

        "exp_status_code": 400,
        "exp_response_type": list,
        "exp_response_body": None,
        "exp_response_fields": ["action", "error"],
        "expected_values_in_response_fields": {
            "action": "projects:Update",
            "error": "You do not have the necessary grid pattern to perform this action"
        }
    }

    update_project_test_data_tc_22_negative = {
        "credentials": {"email": VALID_EMAIL, "password": VALID_PASSWORD},
        "location": OTHER_org_dep_proj_board_boardlabels_team_teamlead_teamusers_teamtickets,
        "new_proj_name": f"TC22-N PA {datetime.datetime.now()}",
        "new_proj_desc": "Updated project desc",
        "new_proj_color": "#FFFFFF",

        "exp_status_code": 400,
        "exp_response_type": dict,
        "exp_response_body": None,
        "exp_response_fields": ["detail"],
        "expected_values_in_response_fields": {
            "detail": "Does not exist"
        }
    }

    delete_project_test_data_tc_23_1_negative = {
        "credentials": {"email": VALID_EMAIL, "password": VALID_PASSWORD},
        "location": OWN_org_dep_proj_board_boardlabels_team_teamlead_teamusers_teamtickets,

        "exp_status_code": 400,
        "exp_response_type": list,
        "exp_response_body": None,
        "exp_response_fields": ["action", "error"],
        "expected_values_in_response_fields": {
            "action": "departments:DeleteProjects",
            "error": "You do not have the necessary permission to perform this action"
        }
    }

    delete_project_test_data_tc_23_2_negative = {
        "credentials": {"email": VALID_EMAIL, "password": VALID_PASSWORD},
        "location": OWN_org_dep_OTHER_proj_board_boardlabels_team_teamlead_teamusers_teamtickets,

        "exp_status_code": 400,
        "exp_response_type": list,
        "exp_response_body": None,
        "exp_response_fields": ["action", "error"],
        "expected_values_in_response_fields": {
            "action": "departments:DeleteProjects",
            "error": "You do not have the necessary permission to perform this action"
        }
    }

    delete_project_test_data_tc_23_3_negative = {
        "credentials": {"email": VALID_EMAIL, "password": VALID_PASSWORD},
        "location": OWN_org_OTHER_dep_proj_board_boardlabels_team_teamlead_teamusers_teamtickets,

        "exp_status_code": 400,
        "exp_response_type": list,
        "exp_response_body": None,
        "exp_response_fields": ["action", "error"],
        "expected_values_in_response_fields": {
            "action": "departments:DeleteProjects",
            "error": "You do not have the necessary permission to perform this action"
        }
    }

    delete_project_test_data_tc_24_negative = {
        "credentials": {"email": VALID_EMAIL, "password": VALID_PASSWORD},
        "location": OTHER_org_dep_proj_board_boardlabels_team_teamlead_teamusers_teamtickets,

        "exp_status_code": 400,
        "exp_response_type": dict,
        "exp_response_body": None,
        "exp_response_fields": ["detail"],
        "expected_values_in_response_fields": {
            "detail": "Does not exist"
        }
    }


# ----------- FOR ORGANIZATION ADMIN ROLE ---------------

class TestDataForOrganizationOwnerRole:
    VALID_EMAIL = "***change_me***"
    VALID_PASSWORD = "***change_me***"

    # ------ VALUES OF WHAT IS 'OWN' AND WHAT IS 'OTHER'S' FOR THE USER WITH THIS SPECIFIC ROLE ------

    OWN_org_dep_proj_board_boardlabels_team_teamlead_teamusers_teamtickets = UserRoleLocation(
        org_id=2,
        dep_id=3,
        proj_id=5,
        board_id=5,
        board_labels_ids=[21, 22, 23, 24, 25],
        team_id=9,
        team_lead_id=32,
        team_users_ids=[41, 42, 43, 44, 45, 46],
        team_tickets_ids=[21, 22, 23]
    )

    OTHER_org_dep_proj_board_boardlabels_team_teamlead_teamusers_teamtickets = UserRoleLocation(
        org_id=1,
        dep_id=1,
        proj_id=1,
        board_id=1,
        board_labels_ids=[1, 2, 3, 4, 5],
        team_id=1,
        team_lead_id=9,
        team_users_ids=[1, 2, 3, 4, 5, 6],
        team_tickets_ids=[1, 2, 4]
    )

    # data for test_create_project
    create_project_test_data_tc_17_positive = {
        "credentials": {"email": VALID_EMAIL, "password": VALID_PASSWORD},
        "location": OWN_org_dep_proj_board_boardlabels_team_teamlead_teamusers_teamtickets,
        "proj_name": f"TC17-P OO {datetime.datetime.now()}",
        # value for request (TC - test case, P - negative, OO - Organization Owner)
        "proj_desc": "Project desc",  # value for request
        "proj_color": "#FFFFFF",

        "exp_status_code": 201,
        "exp_response_type": dict,
        "exp_response_body": None,
        "exp_response_fields": ['detail', 'data'],  # all fields' titles expected in response
        "expected_values_in_response_fields": {
            "detail": "Project was successfully created"
        }
    }

    create_project_test_data_tc_19_negative = {
        "credentials": {"email": VALID_EMAIL, "password": VALID_PASSWORD},
        "location": OTHER_org_dep_proj_board_boardlabels_team_teamlead_teamusers_teamtickets,
        "proj_name": f"TC19-N OO {datetime.datetime.now()}",
        "proj_desc": "Project desc",  # value for request
        "proj_color": "#FFFFFF",

        "exp_status_code": 400,
        "exp_response_type": dict,
        "exp_response_body": None,  # in case the whole body should be equal to some value (like string, for example)
        "exp_response_fields": ["detail"],  # all fields' titles expected in response
        "expected_values_in_response_fields": {
            "detail": "Does not exist"
        }
    }

    update_project_test_data_tc_20_1_positive = {
        "credentials": {"email": VALID_EMAIL, "password": VALID_PASSWORD},
        "location": OWN_org_dep_proj_board_boardlabels_team_teamlead_teamusers_teamtickets,
        "new_proj_name": f"TC20-1-P OO {datetime.datetime.now()}",
        "new_proj_desc": "Updated project desc",  # value for request
        "new_proj_color": "#E2D452",

        "exp_status_code": 200,
        "exp_response_type": dict,
        "exp_response_body": None,
        "exp_response_fields": ["detail", "data"],  # all fields' titles expected in response
        "expected_values_in_response_fields": {
            "detail": "Project was successfully updated"
        }
    }


    update_project_test_data_tc_22_negative = {
        "credentials": {"email": VALID_EMAIL, "password": VALID_PASSWORD},
        "location": OTHER_org_dep_proj_board_boardlabels_team_teamlead_teamusers_teamtickets,
        "new_proj_name": f"TC22-N OO {datetime.datetime.now()}",
        "new_proj_desc": "Updated project desc",
        "new_proj_color": "#FFFFFF",

        "exp_status_code": 400,
        "exp_response_type": dict,
        "exp_response_body": None,
        "exp_response_fields": ["detail"],
        "expected_values_in_response_fields": {
            "detail": "Does not exist"
        }
    }


    delete_project_test_data_tc_23_1_positive = {
        "credentials": {"email": VALID_EMAIL, "password": VALID_PASSWORD},
        "location": OWN_org_dep_proj_board_boardlabels_team_teamlead_teamusers_teamtickets,

        "exp_status_code": 200,
        "exp_response_type": dict,
        "exp_response_body": None,
        "exp_response_fields": ["detail"],
        "expected_values_in_response_fields": None  # TODO: add check for value in "detail" field (now it's mixed
        # with ID of project deleted) + maybe extract ID returned for additional check in test
    }

    delete_project_test_data_tc_24_negative = {
        "credentials": {"email": VALID_EMAIL, "password": VALID_PASSWORD},
        "location": OTHER_org_dep_proj_board_boardlabels_team_teamlead_teamusers_teamtickets,

        "exp_status_code": 400,
        "exp_response_type": dict,
        "exp_response_body": None,
        "exp_response_fields": ["detail"],
        "expected_values_in_response_fields": {
            "detail": "Does not exist"
        }
    }


#  ---------- SUMMARY OF ALL DATA USED IN TESTS ---------------

# links to all sets of test data used for test case 17 (create project)
class TestDataForCreateProject:
    all_data = [

        TestDataForOrganizationOwnerRole.create_project_test_data_tc_17_positive,  # for Organization Owner
        # TODO: test data for TC 18 - maybe not needed (duplicates logic of test with previous data set)
        TestDataForOrganizationOwnerRole.create_project_test_data_tc_19_negative,

        TestDataForProjectAdminRole.create_project_test_data_tc_17_negative,  # for Project Admin
        TestDataForProjectAdminRole.create_project_test_data_tc_18_negative,  # for Project Admin
        TestDataForProjectAdminRole.create_project_test_data_tc_19_negative  # for Project Admin
    ]


class TestDataForUpdateProject:
    all_data = [
        TestDataForOrganizationOwnerRole.update_project_test_data_tc_20_1_positive,
        # TC 21-1 is not needed to be run for this user role according to documentation
        # TODO: test data for TC 21 - maybe not needed (duplicates logic of test with previous data set)
        TestDataForOrganizationOwnerRole.update_project_test_data_tc_22_negative,

        TestDataForProjectAdminRole.update_project_test_data_tc_20_1_positive,
        TestDataForProjectAdminRole.update_project_test_data_tc_20_2_negative,
        TestDataForProjectAdminRole.update_project_test_data_tc_21_negative,
        TestDataForProjectAdminRole.update_project_test_data_tc_22_negative
    ]


class TestDataForDeleteProject:
    all_data = [
        # TODO: test data for TC 23-2, 23-3 for Org Owner - maybe not needed (duplicates logic of test with previous data set)
        TestDataForOrganizationOwnerRole.delete_project_test_data_tc_23_1_positive,
        TestDataForOrganizationOwnerRole.delete_project_test_data_tc_24_negative,

        TestDataForProjectAdminRole.delete_project_test_data_tc_23_1_negative,
        TestDataForProjectAdminRole.delete_project_test_data_tc_23_2_negative,
        TestDataForProjectAdminRole.delete_project_test_data_tc_23_3_negative,
        TestDataForProjectAdminRole.delete_project_test_data_tc_24_negative
    ]
