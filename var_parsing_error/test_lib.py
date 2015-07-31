import os
import time
from robot.libraries.BuiltIn import BuiltIn

TEST_CASE_NAME = ""
TEST_LOG_PATH = ""
TEST_LINE_INFO = {}

def test_log_directory():
    """This function will create case log directory for saving TA log when you call it firstly.
       If you want to save or use TA log, you must call this keyword on your TA case.
    """
    global TEST_CASE_NAME
    global TEST_LOG_PATH
    try:
        test_case_name = BuiltIn().get_variables()['${TEST_NAME}']
    except:
        try:
            test_case_name = BuiltIn().get_variables()['${SUITE_NAME}']
        except:
            test_case_name = "mt_case_name"
    test_case_name = test_case_name.strip().replace(" ", "_")
    if TEST_CASE_NAME != test_case_name:
        try:
            output_dir = BuiltIn().get_variables()['${OUTPUT_DIR}']
        except:
            output_dir = "mt_output_dir"
        test_suite_path = os.path.join(output_dir, "log")
        TEST_CASE_NAME = test_case_name
        test_name_with_timestamp = test_case_name + "_" + time.strftime("%Y%m%d%H%M%S", time.localtime()) + "/"
        test_log_directory = os.path.join(test_suite_path, test_name_with_timestamp)
        TEST_LOG_PATH = test_log_directory
    if not os.path.exists(TEST_LOG_PATH):
        os.makedirs(TEST_LOG_PATH)
    return TEST_LOG_PATH


def kiss_debug_log_dir(path=test_log_directory()):
    """This function will create case log directory for saving TA tool debug log when you call it firstly.
       If you want to save TA tool debug log, you must call this keyword on your TA case.
    """
    global DEBUG_LOG_PATH
    DEBUG_LOG_PATH = os.path.join(path, "kiss_debug_log/")
    if not os.path.exists(DEBUG_LOG_PATH):
        os.makedirs(DEBUG_LOG_PATH)
    return DEBUG_LOG_PATH
