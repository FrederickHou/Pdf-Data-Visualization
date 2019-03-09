#!/usr/bin/ python
# coding=utf-8
"""
/*******************************************************************************
 * Deep North Confidential
 * Copyright (C) 2018 Deep North Inc. All rights reserved.
 * The source code for this program is not published
 * and protected by copyright controlled
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
    PdfPage_object.add_first_page()
    PdfPage_object.pdf_save()
