# file: test_login_and_post.py

import pytest
from empty_post_new_jobssss.empty_post_new_job import JobActions
from basic_plan.config_reader import readconfig_file


#pytest test_must_parse_post_all_jds.py -k "test_login or test_post_new_job_must_parse_TC008_complex_document_structure or test_post_new_job_must_parse_TC009_Unexpected_Page_Breaks" --html=report.html

#pytest test_empty_post_all_jds_doc.py -k "test_login or test_post_new_job_must_parse_empty" --html=report.html

class TestLoginAndEmptyPost:
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

    def test_post_new_job_TC001_empty_file(self, driver_setup):
        job_actions = driver_setup

        folder_path_for_empty_case_docx = readconfig_file("jds_location", 'folder_path_for_empty_case_docx')

        must_parse_jd_paths = job_actions.get_file_paths(folder_path_for_empty_case_docx)
        
        for i in must_parse_jd_paths[:1]:
  
          job_actions.post_new_job_empty_field_parse(file_path_exist=True, file_path=i)


    def test_post_new_job_TC004_image_only_content(self, driver_setup):
        job_actions = driver_setup

        folder_path_for_empty_case_docx = readconfig_file("jds_location", 'folder_path_for_empty_case_docx')

        must_parse_jd_paths = job_actions.get_file_paths(folder_path_for_empty_case_docx)
        
        for i in must_parse_jd_paths[1:2]:
  
          job_actions.post_new_job_empty_field_parse(file_path_exist=True, file_path=i)


    def test_post_new_job_TC005_unicode_characters(self, driver_setup):
        job_actions = driver_setup

        folder_path_for_empty_case_docx = readconfig_file("jds_location", 'folder_path_for_empty_case_docx')

        must_parse_jd_paths = job_actions.get_file_paths(folder_path_for_empty_case_docx)
        
        for i in must_parse_jd_paths[2:3]:
  
          job_actions.post_new_job_empty_field_parse(file_path_exist=True, file_path=i)


    def test_post_new_job_TC006_embedded_images(self, driver_setup):
        job_actions = driver_setup

        folder_path_for_empty_case_docx = readconfig_file("jds_location", 'folder_path_for_empty_case_docx')

        must_parse_jd_paths = job_actions.get_file_paths(folder_path_for_empty_case_docx)
        
        for i in must_parse_jd_paths[3:4]:
  
          job_actions.post_new_job_empty_field_parse(file_path_exist=True, file_path=i)

    def test_post_new_job_TC007_ascii_characters(self, driver_setup):
        job_actions = driver_setup

        folder_path_for_empty_case_docx = readconfig_file("jds_location", 'folder_path_for_empty_case_docx')

        must_parse_jd_paths = job_actions.get_file_paths(folder_path_for_empty_case_docx)
        
        for i in must_parse_jd_paths[4:5]:
  
          job_actions.post_new_job_empty_field_parse(file_path_exist=True, file_path=i)


    

