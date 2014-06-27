import os

def load_scripts(HEADER_SCRIPTS):
    """Load scripts using require.JS
    Temporary hack because IPython.load_extensions() is slated for release in IPython 3.0.0
    """

    log_scripts = ''.join(["console.log('{} loaded');".format(x) for x in HEADER_SCRIPTS])
    files = [str(os.path.join('/nbextensions', x)) for x in HEADER_SCRIPTS]
    require_scripts = 'require(%(files)s, function() {%(logs)s});' % {'files':files, 'logs':log_scripts}

    return(require_scripts)
