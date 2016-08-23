#-*-coding:utf-8-*-
#qpy:webapp:Compass_Long_Polling
#qpy:fullscreen
#qpy://localhost:8080/
"""
This is a sample for qpython webapp
"""

from bottle import route, run
import androidhelper
import signal, os
import time

code = '''
<html>
<body>
<center>
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
<circle cx="100" cy="100" r="80" stroke="navy" stroke-width="5" fill="none"/>
<line id="azim" x1="100" y1="20" x2="100" y2="100" stroke="navy"
stroke-width="5"/>
<text id="degree" x="0" y="20" stroke="navy">90</text>
</svg><br>
<button onclick="shutdown()">
shut down</button>
</center>
<script>
var az;
var deg;
var url = "http://localhost:8080/"
var xhr;
xhr=new XMLHttpRequest();
xhr.onreadystatechange=function()
{
    if (xhr.readyState==4)
    {
    if (xhr.status==200)
    {
    az=parseFloat(xhr.responseText);
    if(az>=0){
    deg = az*180/Math.PI;
    }else{
    deg = 360+az*180/Math.PI;
    }
    deg=String(deg.toFixed(2));
    az = String(-180 * az / Math.PI);
    var cmd = "rotate(" + az + " 100 100)";
    document.getElementById("degree").textContent="^"+deg;
    document.getElementById("azim").setAttribute("transform", cmd);
    }
    xhr.open("GET",url+"azimuth",true);
    xhr.send();
    }
}
xhr.open("GET",url+"azimuth",true);
xhr.send();

function shutdown()
{
var xhr = new XMLHttpRequest();
xhr.open("GET", url+"shutdown", false);
xhr.send(null);
}
</script>
</body>
</html>
'''

droid = androidhelper.Android()
droid.startSensingTimed(1, 250)

@route('/')
def index():
    return code

@route('/azimuth')
def azimuth():
    time.sleep(0.3)
    s6data = droid.sensorsReadOrientation().result
    if len(s6data)>0:
        return str(s6data[0])

@route("/shutdown")
def shutdown():
    droid.stopSensing()
    os.kill(os.getpid(), signal.SIGTERM)

run(host='localhost', port=8080)