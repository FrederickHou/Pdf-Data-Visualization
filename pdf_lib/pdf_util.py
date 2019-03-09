#!/usr/bin/ python
# coding=utf-8
'''
/*******************************************************************************
@auther:Frederick HOu
@email:frederick_hou@163.com
@date:2019/03/09
 *******************************************************************************/
"""

import random
import math
class PdfUtil(object):

    '''
    basic function API about dealing with pdf data
    
    '''
    def __init__(self):

        pass
    

    def get_table_column_width_list(self,table_data_list,table_wdith):

        sum = 0
        table_rows = len(table_data_list)
        if len(table_data_list) > 0:
            table_columns =  len(table_data_list[0])
        else:
            table_columns = 0
        columns_width_list = [0]*table_columns
        for i in range(table_columns):
            value = columns_width_list[i]
            for j in range(table_rows):
                if len(table_data_list[j][i]) >value:
                    value = len(table_data_list[j][i])
            columns_width_list[i] = value
        for value in columns_width_list:
            sum = sum + value
        for i in range(table_columns):
            try:
                columns_width_list[i] = float(columns_width_list[i])/sum*table_wdith
            except ZeroDivisionError as e:
                raise e
        return columns_width_list


    def get_biggest_value(self,data_list):

        max_value = 0
        for item in data_list:
            for number in item:
                if number > max_value:
                    max_value = number
        return max_value


    def get_max_data(self,data_list):

        peakData = []
        peakSingle = {}
        peakSingle['index'] = data_list.index(max(data_list))
        peakSingle['value'] = max(data_list)    
        peakData.append(peakSingle)
        return peakData

    def get_randomdelta(self,lenthOfLine):

        deltaY = random.randint(lenthOfLine/2, lenthOfLine)
        deltaX = math.sqrt(lenthOfLine * lenthOfLine - deltaY * deltaY)
        return deltaX,deltaY


    def get_title_position(self,width,title,titleFontSize):

        return (width - len(title)*titleFontSize/2) / 12 * 7


    def randomcolor(self):
        
        colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        color = ""
        for i in range(6):
            color += colorArr[random.randint(0,14)]
        return "0x"+color