from IPython.display import display, HTML, Javascript
from hycharts.common import *

import string, random
import json

import numpy as np
import pandas as pd

HEADER_SCRIPTS = ["https://code.highcharts.com/stock/highstock.js",
                  "https://code.highcharts.com/stock/modules/exporting.js"
                 ]

if __name__ == "hycharts.chart":
    # when loaded as module
    display(Javascript(load_scripts(HEADER_SCRIPTS)))
        
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
        """Draws HighChart

        Creates a div container and Javascript to display the HighChart instance when called.
        """

        div_id = self.div_id
        chart = self.chart

        div = """
        <div id="chart_%(div_id)s">
            Re-run cell if chart is not shown ...
        </div>
        """ % locals()
        
        script = """
            // Create chart in div when ready on page
            $('#chart_%(div_id)s').ready($('#chart_%(div_id)s').highcharts(%(chart)s));
        """ % locals()

        return display(HTML(div+'<script>'+script+'</script>'))

    @classmethod
    def line(cls, series_or_df, title='Line', width=600, height=400, zoom='x'):
        
        if isinstance(series_or_df, pd.DataFrame):
            series = [{'name': series_or_df[c].name, 'data': series_or_df[c].tolist()} for c in series_or_df]
        elif isinstance(series_or_df, pd.Series):
            series = [{'name': series_or_df.name, 'data': list(series_or_df.values)}]

        chart = {
            'chart': {
                'type': 'line',
                'width': width,
                'height': height,
                'zoomType': zoom
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
            'series': series,
            'tooltip': {
                'headerFormat': '<b>{series.name}</b>: ',
                'pointFormat': '({point.x:7.2f}, {point.y:7.2f})'
            },
        }
        
        return cls(chart)

    @classmethod
    def scatter(cls, x, y, title='Scatter', width=600, height=600, zoom='xy', colorbypoint=False):
        
        chart = {
            'chart': {
                'type': 'scatter',
                'width': height,
                'height': width,
                'zoomType': zoom
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
                    'pointFormat': '({point.x:7.2f}, {point.y:7.2f})'
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
                    'headerFormat': '',
                    'pointFormat': 'Freq: {point.y:7.2f}'
                },
            }]
        }
        
        return cls(chart)

    @classmethod
    def area(cls, df, title='Area', width=600, height=400, zoom='x', stacking='percent'):

        series = [{'name': df[c].name, 'data': df[c].tolist()} for c in df]

        chart = {
            'chart': {
                'type': 'area',
                'height': height,
                'width': width,
                'zoomType': zoom
            },
            'title': {
                'text': title
            },
            'xAxis': {
                'title': {
                    'text': ''
                },
                'categories': list(df.index)
            },
            'yAxis': {
                'title': {
                    'text': 'Percent'
                }
            },
            'tooltip': {
                'pointFormat': '<span style="color:{series.color}">{series.name}</span>: <b>{point.percentage:.1f}%</b> ({point.y:,.0f})<br/>',
                'shared': True
            },
            'plotOptions': {
                'area': {
                    'stacking': stacking,
                    'lineColor': '#ffffff',
                    'lineWidth': 1,
                    'marker': {
                        'lineWidth': 1,
                        'lineColor': '#ffffff'
                    }
                }
            },
            'series': series
        }

        return cls(chart)

# API syntax sugar
line = HighChart.line
scatter = HighChart.scatter
area = HighChart.area
hist = HighChart.hist
