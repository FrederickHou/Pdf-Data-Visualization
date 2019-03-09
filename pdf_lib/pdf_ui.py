#!/usr/bin/ python
# coding=utf-8

from Pdf import Pdf
from pdf_util import PdfUtil
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus.tables import Table, TableStyle
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.piecharts import Pie
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
import os

root = '../resource/'
pdfmetrics.registerFont(TTFont('openSans', root + 'font/openSans/OpenSans.ttf'))
pdfmetrics.registerFont(TTFont('openSansBold', root + 'font/openSans/OpenSansBold.ttf'))
pdfmetrics.registerFont(TTFont('openSansLight', root + 'font/openSans/openSansLight.ttf'))
FONT = 'openSans'
FONTBLOD = 'openSansBold'
FONTTHIN = 'openSansLight'


class PdfUI(Pdf, PdfUtil):
    '''
        @function: PdfUI class provide some functions about pdf ui control  :
        @Inheritance relationship： this PdfUI class needs to Inheritance PdfDate and Pdf class
    '''

    def __init__(self, pdf_config_object):

        self.pdf_config_object = pdf_config_object
        Pdf.__init__(self, pdf_config_object)


    def pdf_drawCentredString(self, content, x, y, font=FONTBLOD, font_size=100, font_color=HexColor(0x000000)):

        '''
            @function: draw center string.
            @args:
                1. content :  draw content.
                2. x:         set x-height
                3. y:         set y-height         
        '''
        self.pdf_page_object.setFillColor(font_color)
        self.pdf_page_object.setFont(font, font_size)
        if content != None:
            self.pdf_page_object.drawCentredString(x, y, content)

    def pdf_drawString(self, content, x, y, font=FONTBLOD, font_size=100, font_color=HexColor(0x000000)):

        '''
            @function: draw  string.
            @args:
                1. content :  draw content.
                2. x: set x-height
                3. y: set y-height       
        '''
        self.pdf_page_object.setFillColor(font_color)
        self.pdf_page_object.setFont(font, font_size)
        if content != None:
            self.pdf_page_object.drawString(x, y, content)

    def pdf_drawLine(self, x1, y1, x2, y2, line_color=HexColor(0X000000), line_width=5):

        '''
            @function: draw  line.
            @args:
                1. line_width: the line of width  
                2. line_color: line color
                3. x1:         the left piont x coordinate
                4. y1:         the left piont y coordinate
                5  x2:         the right piont x coordinate
                6. y2:         the right piont y coordinate
        '''

        self.pdf_page_object.setStrokeColor(line_color, 1)
        self.pdf_page_object.setLineWidth(line_width)
        self.pdf_page_object.line(x1, y1, x2, y2)

    def pdf_drawPolyline(self, table_data, table_lable=[], title="", title_size=70, title_font=FONTBLOD,
                         x=350, y=1800, width=2000, height=1000, line_width=8, lable_color=HexColor(0x000000)):

        '''
            @example:

                    chart_data_1 = {
                        'name': 'a ',
                        'data':   [1,2,3,5,6,8],
                        'color':  HexColor(0x2ebf70)
                        }
                    chart_data = []
                    chart_data.append(chart_data_1)
                    self.pdf_drawPolyline(chart_data)
        '''

        y = self.pdf_config_object.pdf_height - y
        chart_values = []
        size = len(table_data)
        if size == 0:
            return
        width_single = width / size / 4 / 3
        step = width / size
        x_position_tmp = x + step / 3
        y_position = y + 70 * 3 + height
        title_position = self.get_title_position(width, title, title_size)
        self.pdf_page_object.setFillColor(HexColor(0x000000))
        self.pdf_page_object.setFont(title_font, title_size)
        self.pdf_page_object.drawString(x + title_position - 120, y + height + title_size * 5 - 200, title)
        self.pdf_page_object.setLineWidth(line_width)
        i = 0
        for single in table_data:
            chart_values.append(single['data'])
            self.pdf_page_object.setStrokeColor(single['color'])
            x_position = x_position_tmp + (i) * step
            self.pdf_page_object.line(x_position, y_position - 150, x_position + width_single * 0.8, y_position - 150)
            self.pdf_page_object.setFont(FONTBLOD, 40)
            self.pdf_page_object.setFillColor(HexColor(0x000000))
            self.pdf_page_object.drawString(x_position + width_single, y_position - 120, single['name'])
            i = i + 1
        drawing = Drawing(x, y)
        lc = HorizontalLineChart()
        lc.categoryAxis.gridStrokeColor = colors.gray
        # lc.categoryAxis.visibleGrid = 1
        lc.valueAxis.gridStrokeColor = colors.gray
        lc.valueAxis.visibleGrid = 1
        lc.valueAxis.labels.visible = 0
        lc.height = height
        lc.width = width
        lc.data = chart_values
        lc.categoryAxis.categoryNames = table_lable
        lc.categoryAxis.labels.fontName = FONT
        lc.strokeColor = HexColor(0x000000)
        lc.categoryAxis.labels.angle = 0
        lc.categoryAxis.labels.strokeColor = lable_color
        lc.categoryAxis.labels.angle = 45
        lc.categoryAxis.labels.dy = -60
        lc.categoryAxis.labels.fontSize = 30
        lc.valueAxis.valueMin = 0
        y_value_max = self.get_biggest_value(chart_values) + 20
        lc.valueAxis.valueMax = (y_value_max / 10) * 13
        lc.valueAxis.valueStep = (y_value_max / 10) * 13 / 5
        lc.lines.strokeWidth = line_width
        for i in range(size):
            lc.lines[i].strokeColor = table_data[i]['color']
        if len(chart_values[0]) == 0:
            return
        drawing.add(lc)
        drawing.drawOn(self.pdf_page_object, x, y)
        labelArr = []
        step = (y_value_max / 10) * 13 / 5
        valueMax = (y_value_max / 10) * 13
        for i in range(5):
            labelArr.append(i * step)
            self.pdf_page_object.drawString(x - 100, y + height * i * step / valueMax, format(i * step, ','))
        self.pdf_page_object.drawString(x - 100, y + height, format(5 * step, ','))
        lenthOfLabelLine = 100
        arrLabeled = []
        for item in table_data:
            self.pdf_page_object.setStrokeColor(item['color'], 1)
            self.pdf_page_object.setLineWidth(3)
            self.pdf_page_object.setFillColor(item['color'])
            peakData = self.get_max_data(item['data'])
            for peakInLoop in peakData:
                peakDataOne = peakInLoop['value']
                posInarry = peakInLoop['index']
                posYOfPeak = y + height * peakDataOne / valueMax + 10
                posXOfPeak = x + width / len(item['data']) * (posInarry + 1) - width / len(item['data']) / 2 + 20
                if posInarry in arrLabeled:
                    lenthOfLabelLine = lenthOfLabelLine + 80
                deltaX, deltaY = self.get_randomdelta(lenthOfLabelLine)
                self.pdf_page_object.line(posXOfPeak, posYOfPeak, posXOfPeak + deltaX, posYOfPeak + deltaY)
                self.pdf_page_object.drawCentredString(posXOfPeak + deltaX, posYOfPeak + deltaY + 10,
                                                       format(peakDataOne, ','))
                arrLabeled.append(posInarry)
                lenthOfLabelLine = 100

    def pdf_drawTable(self, table_data, table_style=[], x=50, y=800, table_width=2475, table_height=300, font_size=50,
                      colWidths=[]):

        '''
            @example:

                    table_data = []
                    table_data.append(['index','a','b','c','d'])
                    table_data.append(["1",'11','555','1251','22'])
                    self.pdf_drawTable(table_data)
        '''

        if len(colWidths) == 0:
            colWidths = self.get_table_column_width_list(table_data, table_width)
        try:
            rowHeights = int(table_height / (len(table_data)))
        except ZeroDivisionError as e:
            raise e
            return
        table_object = Table(table_data, colWidths, rowHeights)
        # (column,row)
        table_basic_stylesheet = [
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.white),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTRE'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 55),
            ('FONT', (0, 0), (-1, 0), FONTBLOD),
            ('FONT', (0, 1), (-1, -1), FONT),
            ('FONTSIZE', (0, 0), (-1, -1), font_size),
            ('BACKGROUND', (0, 0), (-1, 0), HexColor(0X4472c4)),
            ('BACKGROUND', (0, 1), (-1, -1), HexColor(0xE9ECF6)),
        ]
        for i in table_style:
            table_basic_stylesheet.append(i)
        table_stylesheet = TableStyle(table_basic_stylesheet)
        table_object.setStyle(table_stylesheet)
        table_object.wrapOn(self.pdf_page_object, 0, 0)
        y = self.pdf_config_object.pdf_height - y
        table_object.drawOn(self.pdf_page_object, x, y)

    def pdf_drawBar(self, chart_data, categoryNames=[], bar_color=[], title="", title_size=70,
                    title_font=FONTBLOD, x=300, y=1600, chart_width=2000, chart_height=655,
                    lable_fontSize=50, background_color=HexColor(0x000000)):

        '''
            @example:
            
                    chart_data = [25,65,330]
                    chart_lable=['index','a']
                    data = []
                    data.append(chart_data)
        '''

        y = self.pdf_config_object.pdf_height - y
        title_position = self.get_title_position(chart_width, title, title_size)
        self.pdf_page_object.setFillColor(HexColor(0x000000))
        self.pdf_page_object.setFont(title_font, title_size)
        self.pdf_page_object.drawString(x + title_position - 150, y + chart_height + title_size * 3 - 80, title)
        max_list = []
        for index in range(len(chart_data)):
            if chart_data[index]:
                max_list.append(max(chart_data[index]))
            else:
                max_list.append(0)
        barchart_max = max(max_list) + 500
        drawing = Drawing(800, 2230)
        bc = VerticalBarChart()
        bc.x = 0
        bc.y = 0
        bc.height = chart_height
        bc.width = chart_width
        bc.data = chart_data
        bc.groupSpacing = 15
        bc.barSpacing = 10
        bc.strokeColor = HexColor(0xDFDFDF)
        bc.valueAxis.valueMin = 0
        bc.valueAxis.valueMax = barchart_max + barchart_max / 20
        bc.valueAxis.valueStep = (barchart_max + barchart_max / 20) / 5
        bc.valueAxis.visible = 0
        bc.valueAxis.gridStrokeColor = colors.gray
        bc.valueAxis.visibleGrid = 1
        bc.categoryAxis.labels.dx = 8
        bc.categoryAxis.labels.dy = 0
        bc.categoryAxis.labels.fontSize = lable_fontSize
        bc.categoryAxis.categoryNames = categoryNames
        if len(bar_color) == 0:
            for i in range(len(chart_data)):
                bar_color.append(HexColor(self.randomcolor()))
        for i in range(len(chart_data)):
            setattr(bc.bars[i], 'fillColor', bar_color[i])
            setattr(bc.bars[i], 'strokeColor', colors.white)
        bc.fillColor = HexColor(0xffffff)
        drawing.add(bc)
        drawing.drawOn(self.pdf_page_object, x, y)
        barchart_max = barchart_max + barchart_max / 20

        try:
            colWidths = chart_width / (len(chart_data[0]))
        except ZeroDivisionError as e:
            raise e
            return
        yheight = chart_height
        yStart = y
        self.pdf_page_object.setFillColor(background_color)
        self.pdf_page_object.setFont(FONTBLOD, 35)
        for i in range(len(chart_data)):
            width = 0
            if not chart_data[i] == 0:
                for j in range(len(chart_data[i])):
                    width = x + j * colWidths
                    try:
                        if len(chart_data) == 1:
                            self.pdf_page_object.drawCentredString(width + colWidths / 2,
                                                                   yStart + yheight * chart_data[i][
                                                                       j] / barchart_max + 20,
                                                                   format(int(chart_data[i][j]), ','))
                        else:
                            self.pdf_page_object.drawCentredString(
                                width + colWidths / (2 * len(chart_data) + 1) * ((i + 1) * 2) - colWidths / (
                                            2 * len(chart_data) + 1) / 2,
                                yStart + yheight * chart_data[i][j] / barchart_max + 20,
                                format(int(chart_data[i][j]), ','))
                    except Exception as e:
                        raise e

    def pdf_drawPie(self, pie_data, pie_lable=[], colors=[], x=805, y=1650, width=900, height=900,
                    innerRadiusFraction=0.5):

        '''
            @example:
                    chart_data = [1212,66,585,225,36]
                    lable = ['dfd','sdd','trtr','rrrr','ytytyt']
                    self.pdf_drawPie(chart_data,lable)
        '''

        if len(pie_data) == 0 or sum(pie_data) == 0:
            return
        d = Drawing(200, 100)
        pc = Pie()
        pc.x = 65
        pc.y = 65
        pc.width = width
        pc.height = height
        pc.data = pie_data
        pc.labels = pie_lable
        pc.startAngle = 0
        pc.sideLabels = 1
        pc.simpleLabels = 0
        if len(colors) != len(pie_data):
            colors = []
            for i in range(len(pie_data)):
                colors.append(HexColor(self.randomcolor()))
        for i in range(0, len(pie_data)):
            pc.slices[i].fontSize = 40
            pc.slices[i].fontName = FONT
            pc.slices[i].fillColor = colors[i]
            pc.slices[i].strokeColor = colors[i]
            pc.innerRadiusFraction = innerRadiusFraction
        d.add(pc)
        d.drawOn(self.pdf_page_object, x, y)
