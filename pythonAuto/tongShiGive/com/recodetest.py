# -*- coding: utf-8 -*-

import time
import os
import subprocess
import json

from models.recoder import Recoder
from global_config import SERVER_IP
from global_config import AUTOTEST_RECODE_PATH
from global_config import AUTOTEST_RECODE_NAME
from global_config import VERSION_FILE_PATH
from global_config import VERSION_FILE_NAME
from global_config import CODE_VERSION_FILE_PATH
from global_config import CODE_VERSION_FILE_NAME

class RecodeMark():
    """
    记录测试时间、系统版本、代码版本、异常个数、执行次数，以供Email使用。
    """

    def __init__(self):
        self.recode_file = AUTOTEST_RECODE_PATH + AUTOTEST_RECODE_NAME
        self.version_file = VERSION_FILE_PATH + VERSION_FILE_NAME
        self.code_version_file = CODE_VERSION_FILE_PATH + CODE_VERSION_FILE_NAME

    def recode_start_mark(self):
        self._create_recode_file()

        t = time.localtime(time.time())
        current_time_str = time.strftime('%Y-%m-%d %H:%M:%S %s', t)
        test_version = self._get_test_version()
        code_version = self._get_code_version()

        recd = Recoder()
        recd.test_host_ip = SERVER_IP
        recd.test_version = test_version
        recd.code_version = code_version
        recd.error_count = 0
        recd.times = 1
        recd.start_time = current_time_str
        recd.end_time = "none"
        recode_json = recd.to_json()

        flog = open(self.recode_file, 'w')
        flog.write(recode_json)
        flog.close()

    def recode_end_mark(self):
        flog = open(self.recode_file, "r")
        recode_string = flog.read()
        flog.close()

        t = time.localtime(time.time())
        current_time_str = time.strftime('%Y-%m-%d %H:%M:%S %s', t)

        recd = Recoder()
        recode_json = json.loads(recode_string)
        recd.test_host_ip = recode_json["test_host_ip"]
        recd.test_version = recode_json["test_version"]
        recd.code_version = recode_json["code_version"]
        recd.error_count = 0
        recd.start_time = recode_json["start_time"]
        recd.times = 1
        recd.end_time = current_time_str

        recode_string = recd.to_json()

        flog = open(self.recode_file, "w")
        flog.write(recode_string)
        flog.close()

    def _create_recode_file(self):
        recode_file_path = AUTOTEST_RECODE_PATH

        if os.path.exists(recode_file_path):
            os.system("rm -rf " + recode_file_path)
            cmd = 'mkdir ' + recode_file_path
            ret = subprocess.call(cmd, shell=True)
            if ret != 0:
                raise Exception("Error occured while calling '%s'" % cmd)

    def _get_test_version(self):
        build_title = "build: "
        version_title = "node_version: "
        fversion = open(self.version_file, 'r')
        templist = fversion.read().split("\n")
        fversion.close()

        buildnum = ""
        version = ""
        for itemString in templist:
            if itemString.startswith(build_title):
                buildnum = itemString[len(build_title):]
            elif itemString.startswith(version_title):
                version = itemString[len(version_title):]

        test_version = "opzoon-" + version + "-" + buildnum + ".iso"
        return test_version

    def _get_code_version(self):
        branch_title = "build_branch="
        fversion = open(self.code_version_file, 'r')
        templist = fversion.read().split("\n")
        fversion.close()

        branch = ""
        for itemString in templist:
            if itemString.startswith(branch_title):
                branch = itemString[len(branch_title):]

        code_version = branch
        return code_version