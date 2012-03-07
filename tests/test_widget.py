from tw2.core.testbase import WidgetTest
from tw2.lesscss import *

class TestLesscss(WidgetTest):
    # place your widget at the TestWidget attribute
    widget = Lesscss
    # Initilization args. go here 
    attrs = {'id':'lesscss-test'}
    params = {}
    expected = """<div id="lesscss-test"></div>"""
