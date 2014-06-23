
// console.log('loaded threedee.js');

// Add mouse events for rotation
function addRotation(chart) {
    $(chart.container).bind('mousedown.hc touchstart.hc', function (e) {
        e = chart.pointer.normalize(e);
    
        var posX = e.pageX,
        posY = e.pageY,
        alpha = chart.options.chart.options3d.alpha,
        beta = chart.options.chart.options3d.beta,
        newAlpha,
        newBeta,
        sensitivity = 5; // lower is more sensitive
    
        $(document).bind({
            'mousemove.hc touchdrag.hc': function (e) {
                // Run beta
                newBeta = beta + (posX - e.pageX) / sensitivity;
                newBeta = Math.min(100, Math.max(-100, newBeta));
                chart.options.chart.options3d.beta = newBeta;
                
                // Run alpha
                newAlpha = alpha + (e.pageY - posY) / sensitivity;
                newAlpha = Math.min(100, Math.max(-100, newAlpha));
                chart.options.chart.options3d.alpha = newAlpha;
                
                chart.redraw(false);
            },                            
            'mouseup touchend': function () { 
                $(document).unbind('.hc');
            }
        });
    });
}

// console.log(addRotation)
