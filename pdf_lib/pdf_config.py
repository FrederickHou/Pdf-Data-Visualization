#!/usr/bin/ python
# coding=utf-8
"""
/*******************************************************************************
@auther:Frederick HOu
@email:frederick_hou@163.com
@date:2019/03/09
 *******************************************************************************/
"""
import os
import json
import logging

cur_dir = os.path.dirname(__file__)
config_path = "../conf/pdf_info.json"


class PdfConfig(object):
    '''
     @function:
        1.pdf config file class:
        2.if you want to use this class,first you must transfer the  param_init() function
            example:
                config_object = PdfConfig.param_init(pdf_date)
    '''

    def __init__(self):

        self.pdf_path = None
        self.pdf_name = None
        self.pdf_width = None
        self.pdf_height = None
        self.pdf_name = None

    @classmethod
    def param_init(cls):

        '''
            @function: this function is a classmethod,and it will acquire the necessary 
            paramaters when generating a pdf file,then it will return a PdfConfig object

        '''

        json_pdf_config = None
        try:
            if os.path.exists(config_path):
                with open(config_path, "rb")as f:
                    pdf_config = f.read()
                    json_pdf_config = json.loads(pdf_config)
        except Exception as e:
            print e
            return None
        if not json_pdf_config:
            return
        config_object = PdfConfig()
        config_object.pdf_path = json_pdf_config["temp_path"]
        config_object.pdf_name = json_pdf_config["pdf_name"]
        config_object.pdf_width = json_pdf_config["PageWidth"]
        config_object.pdf_height = json_pdf_config["PageHeight"]
        try:
            if not os.path.exists(config_object.pdf_path):
                os.mkdir(config_object.pdf_path)
        except Exception as e:
            print e
            return None
        return config_object
