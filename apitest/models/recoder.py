# -*- coding: utf-8 -*-
# Copyright (c) 2011 Opzoon
# All Rights Reserved.
#
# Licensed under the Opzoon License, Version 1.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.opzoon.com/licenses/LICENSE-1.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from base import BaseTestModel


class Recoder(BaseTestModel):
    """
    测试结果文本模型
    """
    test_host_ip = ""
    test_version = ""
    start_time = ""
    end_time = ""
    code_version = ""
    error_count = 0
    times = 1