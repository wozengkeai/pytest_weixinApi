# -*- coding: utf-8 -*-
# @Time : 2021/8/13 14:59
# @Author : zengxiaoyan
# @File : test_tag.py

import pytest
import allure
from common.common_function import CommonFunction
from apis.contacts.manage_tag import ManageTag

@allure.feature("测试操作标签")
class TestTag(object):
    @allure.story("创建新标签")
    def test_creat_tag(self):
        cf = CommonFunction()
        #生成随机tagname
        new_tagname = cf.get_random_string(6)
        new_tagid = cf.get_random_string()
        mt = ManageTag()
        mt.create_tag(new_tagname)
        res = mt.get_response()
        assert res