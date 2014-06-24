def load_scripts(HEADER_SCRIPTS):
    """Load scripts using require.JS"""

    log_scripts = ''.join(["console.log('{} loaded');".format(x.split("/")[-1]) for x in HEADER_SCRIPTS])
    require_scripts = 'require(%(files)s, function() {%(logs)s});' % {'files':HEADER_SCRIPTS, 'logs':log_scripts}
    return(require_scripts)
