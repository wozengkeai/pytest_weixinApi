# -*- coding: utf-8 -*-
# @Time : 2021/8/12 17:22
# @Author : zengxiaoyan
# @File : manage_tag.py
import logging
import allure
from apis.base_api import BaseAPI

class ManageTag(BaseAPI):
    def __init__(self):
        BaseAPI.__init__(self)
        logging.info("Init department management API")
        # 确定应用名与token配置文件地址
        application_name = "contacts"
        token_path = "F:/InterfaceTest/Weixin_InterfaceTest/config/contacts_access_token.yaml"
        # 判断 token 是否过期，如果过期自动重新请求
        self.judgment_access_token_is_valid(application_name, token_path)
        # 获取最新的 access_token
        self.access_token = self.cf.get_yaml_data(token_path).get("access_token")

    #创建标签
    def create_tag(self,tagname,tagid):
        with allure.step("获取创建标签请求参数"):
            url = self.yaml_data["contacts"]["tag"]["creat_tag_url"]
            params = {
                "access_token": self.access_token,
                # "tagname": self.cf.get_random_string(8)
            }
            data = {
                "tagname": tagname,
                "tagid": tagid
            }
            logging.debug("url:" + str(url))
            logging.debug("params:" + str(params))
            with allure.step("发出创建标签的请求"):
                self.send_post_json(url,json_obj=data,params=params)

    #更新标签名字
    def updata_tganame(self,tagname,tagid):
        with allure.step("获取更新标签明细的请求参数"):
            url = self.yaml_data["contacts"]["tag"]["update_tag_url"]
            params = {
                "access_token": self.access_token
            }
            data = {
                "tagname": tagname,
                "tagid": tagid
            }
            logging.debug("url:" + str(url))
            logging.debug("paramas:" + str(params))
            with allure.step("发出更新标签名字的请求"):
                self.send_post_json(url,json_obj=data,params=params)

