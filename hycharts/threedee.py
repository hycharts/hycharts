from IPython.display import HTML, display

HEADER_SCRIPTS = ["code.highcharts.com/highcharts-3d.js"]

if __name__ == "__main__":
    # when run as a script
    pass
else:
    # when loaded as module
    header = ''.join(['<script src="https://{0}" />\n'.format(s) for s in HEADER_SCRIPTS])
    display(HTML(header))    
