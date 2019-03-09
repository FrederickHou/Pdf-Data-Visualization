#!/usr/bin/ python
# coding=utf-8
"""
/*******************************************************************************
@auther:Frederick HOu
@email:frederick_hou@163.com
@date:2019/03/09
 *******************************************************************************/
"""

import sys
import os

sys.path.append('../')
from pdf_page import PdfPage
import json
import time
from pdf_lib.pdf_config import PdfConfig

report_output_log_path = './log'
if not os.path.exists(report_output_log_path):
    try:
        os.mkdir(report_output_log_path, 0777)
        os.chmod(report_output_log_path, 0777)
    except Exception as e:
        print e

if __name__ == "__main__":

    config_object = PdfConfig.param_init()
    PdfPage_object = PdfPage(config_object)
    '''                            
    PdfPage_object.add_first_page()
    '''
    PdfPage_object.pdf_save()
