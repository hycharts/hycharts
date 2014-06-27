from IPython.display import display, HTML, Javascript
import json
from hycharts import HighChart
from hycharts.common import *

import numpy as np

HEADER_SCRIPTS = ["highstock.js"]

if __name__ == "hycharts.stock":
    # when loaded as module
    display(Javascript(load_scripts(HEADER_SCRIPTS)))

class HighStock(HighChart):
    
    def __init__(self, json_or_dict, div_id=None):
        super(HighStock, self).__init__(json_or_dict, div_id)

    @classmethod
    def series(cls, series):

        data = zip(series.index.astype(np.int64) // 10**6, series.tolist())
        chart = { 'series' : [{ 'data' : data }] }

        return cls(chart)

    def draw(self):
        """Draws HighChart

        Creates a div container and Javascript to display the HighStock instance when called.
        """

        div_id = self.div_id
        chart = json.dumps(self.chart)

        div = """
        <div id="chart_%(div_id)s">
            Re-run cell if chart is not shown ...
        </div>
        """ % locals()
        
        script = """
            // Create chart in div when ready on page
            $('#chart_%(div_id)s').ready($('#chart_%(div_id)s').highcharts('StockChart', %(chart)s));
        """ % locals()

        return display(HTML(div+'<script>'+script+'</script>'))

series = HighStock.series
