# file: test_login_and_post.py

import pytest
from must_parse_jobssss.post_new_job_file import JobActions
from basic_plan.config_reader import readconfig_file


#pytest test_login_and_post.py::TestLoginAndPost::test_post_new_job_must_parse_TC008_complex_document_structure test_login_and_post.py::TestLoginAndPost::test_post_new_job_must_parse_TC009_Unexpected_Page_Breaks

#pytest test_must_parse_post_all_jds.py::TestLoginAndPost::test_login::TestLoginAndPost::test_post_new_job_must_parse_TC008_complex_document_structure

#pytest test_must_parse_post_all_jds.py::TestLoginAndPost::test_login::TestLoginAndPost::test_post_new_job_must_parse_TC008_complex_document_structure::TestLoginAndPost::

class TestLoginAndPost:
    @pytest.fixture(scope="class")
    def driver_setup(self, request):
        job_actions = JobActions()
        job_actions.setup_driver()
        yield job_actions
        job_actions.teardown_driver()

    def test_login(self, driver_setup):
        job_actions = driver_setup

        # Call login method
        job_actions.login()

    def test_post_new_job_must_parse_TC008_complex_document_structure(self, driver_setup):
        job_actions = driver_setup

        folder_path_for_must_parse_case = readconfig_file("jds_location", 'folder_path_for_must_parse_case_txt')

        must_parse_jd_paths = job_actions.get_file_paths(folder_path_for_must_parse_case)
        
        for i in must_parse_jd_paths[:1]:
  
          job_actions.post_new_job_must_parse(file_path_exist=True, file_path=i)


    def test_post_new_job_must_parse_TC009_Unexpected_Page_Breaks(self, driver_setup):
        job_actions = driver_setup

        folder_path_for_must_parse_case = readconfig_file("jds_location", 'folder_path_for_must_parse_case_txt')

        must_parse_jd_paths = job_actions.get_file_paths(folder_path_for_must_parse_case)
        
        for i in must_parse_jd_paths[1:2]:
  
          job_actions.post_new_job_must_parse(file_path_exist=True, file_path=i)

