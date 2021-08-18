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
        token_path = "F:/Weixin_InterfaceTest/config/contacts_access_token.yaml"
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
            logging.debug("params:" + str(params))
            with allure.step("发出更新标签名字的请求"):
                self.send_post_json(url,json_obj=data,params=params)

    #获取标签列表
    def get_tag_list(self):
        with allure.step("获取标签列表的请求参数"):
            url = self.yaml_data["contacts"]["tag"]["get_tag_list"]
            params = {
                "access_token": self.access_token
            }
            with allure.step("发出获取标签列表的请求"):
                self.send_get(url,params=params)

    #获取标签成员
    def get_tag_member(self,tagid):
        with allure.step("获取标签成员的请求参数"):
            url = self.yaml_data["contacts"]["tag"]["get_tag_mem"]
            params = {
                "access_token": self.access_token,
                "tagid": tagid
            }
            logging.debug("url:" + str(url))
            logging.debug("params:" + str(params))
            with allure.step("发出获取标签成员的请求"):
                self.send_get(url,params=params)

    #增加标签成员
    def add_tag_member(self,tagid,userlist=None,partylist=None):
        with allure.step("获取增加标签成员的请求参数"):
            url = self.yaml_data["contacts"]["tag"]["add_tag_mem"]
            params = {
                "access_token": self.access_token,
            }
            if userlist and partylist :
                data = {
                    "tagid": tagid,
                    "userlist": userlist,
                    "partylist": partylist
                }
            elif userlist == None and partylist != None:
                data = {
                    "tagid": tagid,
                    # "userlist": userlist,
                    "partylist": partylist
                }
            elif userlist != None and partylist == None:
                data = {
                    "tagid": tagid,
                    "userlist": userlist,
                    # "partylist": partylist
                }
            else:
                data = {
                    "tagid": tagid,
                    # "userlist": userlist,
                    # "partylist": partylist
                }
            logging.debug("url:" + str(url))
            logging.debug("paramas:" + str(params))
            with allure.step("发起增加标签成员的请求"):
                self.send_post_json(url,json_obj=data,params=params)

    #删除标签成员
    def delete_tag_member(self,tagid,userlist=None,partylist=None):
        with allure.step("获取删除标签成员的请求参数"):
            url = self.yaml_data["contacts"]["tag"]["delete_tag_mem"]
            params = {
                "access_token": self.access_token,
            }
            if userlist and partylist:
                data = {
                    "tagid": tagid,
                    "userlist": userlist,
                    "partylist": partylist
                }
            elif userlist == None and partylist != None:
                data = {
                    "tagid": tagid,
                    # "userlist": userlist,
                    "partylist": partylist
                }
            elif userlist != None and partylist == None:
                data = {
                    "tagid": tagid,
                    "userlist": userlist,
                    # "partylist": partylist
                }
            else:
                data = {
                    "tagid": tagid,
                    # "userlist": userlist,
                    # "partylist": partylist
                }
            with allure.step("发出删除标签成员的请求"):
                self.send_post_json(url,json_obj=data,params=params)

    # 删除标签
    def delete_tag(self, tagid):
        with allure.step("获取删除标签的请求参数"):
            url = self.yaml_data["contacts"]["tag"]["delete_tag_url"]
            params = {
                "access_token": self.access_token,
                "tagid": tagid
            }
            logging.debug("url:" + str(url))
            logging.debug("paramas:" + str(params))
            with allure.step("发出删除标签的请求"):
                self.send_get(url, params=params)