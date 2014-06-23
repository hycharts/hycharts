from IPython.display import display, HTML, Javascript
from hycharts import HighChart

HEADER_SCRIPTS = ["https://code.highcharts.com/highcharts-3d.js",
                  "../js/threedee.js"]

if __name__ == "__main__":
    # when run as a script
    pass
else:
    # when loaded as module
    header = ''.join(['<script src="{0}" />\n'.format(s) for s in HEADER_SCRIPTS])
    display(HTML(header))

class HighChart3D(HighChart):

    def __init__(self, json_or_dict, div_id=None):
        super(HighChart3D, self).__init__(json_or_dict, div_id)

    @classmethod    
    def scatter3d(cls, x, y, z, title='Scatter', width=600, height=600, depth=300, zoom=None, colorbypoint=False):
        
        chart = {
            'chart': {
                'type': 'scatter',
                'width': height,
                'height': width,
                'zoomType': zoom,
                'options3d': {
                    'enabled': True,
                    'alpha': 10,
                    'beta': 20,
                    'depth': depth,
                    'viewDistance': 5,
                    'frame': {
                        'bottom': { 'size': 1, 'color': 'rgba(0,0,0,0.02)' },
                        'back': { 'size': 1, 'color': 'rgba(0,0,0,0.04)' },
                        'side': { 'size': 1, 'color': 'rgba(0,0,0,0.06)' }
                    }
                }
            },
            'title': {
                'text': title
            },
            'xAxis': {
                'title': {
                    'text': x.name
                },
                'min': x.min(),
                'max': x.max()
            },
            'yAxis': {
                'title': {
                    'text': y.name
                },
                'min': y.min(),
                'max': y.max()
            },
            'zAxis': {
                'title': {
                    'text': z.name
                },
                'min': z.min(),
                'max': z.max()
            },
            'series': [{
                'showInLegend': False, 
                'colorByPoint': colorbypoint,
                'data': zip(x,y,z),
                'tooltip': {
                    'headerFormat': '',
                    'pointFormat': '({point.x:7.2f}, {point.y:7.2f}, {point.z:7.2f})'
                },
            }]
        }
        
        return cls(chart)
        

    def draw(self, rotation=True):
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

        if rotation:
            script += """
               // Add rotation to chart
               $('#chart_%(div_id)s').ready(
                   addRotation($(chart_%(div_id)s).highcharts())
               );""" % locals()

        return display(HTML(div+'<script>'+script+'</script>'))
    
# API syntax sugar
scatter = HighChart3D.scatter3d
