from IPython.display import HTML, display

import string, random
import json

import numpy as np
import pandas as pd

HEADER_SCRIPTS = ["code.highcharts.com/highcharts.js",
                  "code.highcharts.com/stock/modules/exporting.js"
                 ]

if __name__ == "__main__":
    # when run as a script
    pass
else:
    # when loaded as module
    header = ''.join(['<script src="https://{0}" />\n'.format(s) for s in HEADER_SCRIPTS])
    display(HTML(header))    
        
class HighChart(object):
    """Creates a generic HighCharts chart.
    """
    
    def __init__(self, json_or_dict, div_id=None):
        try:
            self.chart = json_or_dict + ''
        except TypeError:
            self.chart = json.dumps(json_or_dict)

        if not div_id:
            self.div_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(15))

    def draw(self):
        
        div_id = self.div_id
        chart = self.chart

        div = """
        <div id="chart_%(div_id)s">
            Re-run cell if chart is not shown ...
        </div>
        <script>
            do_chart_%(div_id)s = function() {
                $('#chart_%(div_id)s').highcharts(%(chart)s);
            }
            setTimeout("do_chart_%(div_id)s()", 50)
        </script>
        """ % locals()
        
        return HTML(div)

    @classmethod
    def line(cls, series_or_df, title='Line', width=600, height=400):
        
        if isinstance(series_or_df, pd.DataFrame):
            series = [{'name': series_or_df[c].name, 'data': list(series_or_df[c])} for c in series_or_df]
        elif isinstance(series_or_df, pd.Series):
            series = [{'name': series_or_df.name, 'data': list(series_or_df.values)}]

        chart = {
            'chart': {
                'type': 'line',
                'width': width,
                'height': height
            },
            'title': {
                'text': title
            },
            'xAxis': {
                'title': {
                    'text': ''
                }
            },
            'yAxis': {
                'title': {
                    'text': ''
                }
            },
            'series': series
        }
        
        return cls(chart)

    @classmethod
    def scatter(cls, x, y, title='Scatter', width=600, height=600, colorbypoint=False):
        
        chart = {
            'chart': {
                'type': 'scatter',
                'width': height,
                'height': width
            },
            'title': {
                'text': title
            },
            'xAxis': {
                'title': {
                    'text': x.name
                }
            },
            'yAxis': {
                'title': {
                    'text': y.name
                }
            },
            'series': [{
                'showInLegend': False, 
                'colorByPoint': colorbypoint,
                'data': zip(x,y),
                'tooltip': {
                    'headerFormat': '',
                    'pointFormat': '({point.x:7.2f},{point.y:7.2f})'
                },
            }]
        }
        
        return cls(chart)

    @classmethod
    def hist(cls, series, bins=10, normed=False, weights=None, density=None, 
             title='Histogram', width=600, height=400):
        
        hist, bin_edges = np.histogram(series, bins=bins, 
                                       normed=normed, density=density)
        chart = {
            'chart': {
                'type': 'column',
                'width': width,
                'height': height
            },
            'title': {
                'text': title
            },
            'xAxis': {
                'categories': ['{0:7.2f}'.format(x) for x in bin_edges],
                'labels': {
                    'format': '{value:7.2f}'
                },
            },
            'yAxis': {
                'title': {
                    'text': 'Frequency'
                }
            },
            'plotOptions': {
                'column': {
                'groupPadding': 0,
                'pointPadding': 0,
                'borderWidth': 0
                }
            },
            'series': [{
                'showInLegend': False, 
                'colorByPoint': False,
                'data': list(hist),
                'tooltip': {
                    'pointFormat': '{point.y:7.2f}'
                },
            }]
        }
        
        return cls(chart)