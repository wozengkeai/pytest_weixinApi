# -*- coding: utf-8 -*-
# @Time : 2021/8/13 14:59
# @Author : zengxiaoyan
# @File : test_tag.py

import pytest
import allure
from common.common_function import CommonFunction
from apis.contacts.manage_tag import ManageTag
tag = [100]
# userlist = ["id_20210812163710"]
data_list = [(100,["id_20210812145924"])]


@allure.feature("测试操作标签")
class TestTag(object):
    @pytest.mark.parametrize('tagid', tag)
    @allure.story("创建新标签")
    def test_creat_tag(self,tagid):
        cf = CommonFunction()
        #生成随机tagname
        new_tagname = cf.get_random_string(6)
        new_tagid = tagid
        mt = ManageTag()
        mt.create_tag(new_tagname,new_tagid)
        res = mt.get_response()
        assert res.get("errmsg") == 'created'

    @pytest.mark.parametrize('tagid', tag)
    @allure.story("更新标签名字")
    def test_update_tag(self,tagid):
        new_tagid = tagid
        cf = CommonFunction()
        # 生成随机tagname
        new_tagname = cf.get_random_string(6)
        mt = ManageTag()
        mt.updata_tganame(new_tagname,new_tagid)
        res = mt.get_response()
        assert res.get("errmsg") == "updated"


    @allure.story("获取标签列表")
    def test_get_tag_list(self):
        mt = ManageTag()
        mt.get_tag_list()
        res = mt.get_response()
        assert res.get("errmsg") == "ok"

    @pytest.mark.parametrize('tagid,userlist', data_list)
    @allure.story("增加标签成员")
    def test_add_tag_mem(self,tagid,userlist):
        # userlist = ["id_20210812163710"]
        mt = ManageTag()
        mt.add_tag_member(tagid,userlist)
        res = mt.get_response()
        assert res.get("errmsg") == "ok"

    @pytest.mark.parametrize('tagid', tag)
    @allure.story("获取标签成员")
    def test_get_tag_mem(self,tagid):
        mt = ManageTag()
        mt.get_tag_member(tagid)
        res = mt.get_response()
        assert res.get("errmsg") == "ok"

    @pytest.mark.parametrize('tagid,userlist', data_list)
    @allure.story("删除标签成员")
    def test_delete_tag_mem(self,tagid,userlist):
        mt = ManageTag()
        mt.delete_tag_member(tagid,userlist)
        res = mt.get_response()
        assert res.get("errmsg") == "deleted"

    @pytest.mark.parametrize('tagid', tag)
    @allure.story("删除标签")
    def test_delete_tag(self, tagid):
        mt = ManageTag()
        mt.delete_tag(tagid)
        res = mt.get_response()
        assert res.get("errmsg") == "deleted"