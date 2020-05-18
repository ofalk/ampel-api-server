#!/usr/bin/env python3

import sys
sys.path.append('./cleware-traffic-light')

import subprocess
from flask import Flask, json, request, redirect, url_for
from traffic_light import ClewareTrafficLight

api = Flask(__name__)

def _run_cleware(light_number):
  out = subprocess.Popen(['/root/clewarecontrol/clewarecontrol', '-c', '1', '-rs', str(light_number)],
    stdout=subprocess.PIPE)
  grep = subprocess.Popen(['grep', 'Status'], stdin=out.stdout, stdout=subprocess.PIPE)
  grep_output,_ = grep.communicate()
  if str(grep_output).find('On') > 0:
    return True
  return False

def _get_red():
    return _run_cleware(0)
def _get_yellow():
    return _run_cleware(1)
def _get_green():
    return _run_cleware(2)


@api.route('/red', methods=['GET'])
def get_red():
   return json.dumps({ 'red': _get_red() })

@api.route('/yellow', methods=['GET'])
def get_yellow():
   return json.dumps({ 'yellow': _get_yellow() })

@api.route('/green', methods=['GET'])
def get_green():
   return json.dumps({ 'green': _get_green() })

@api.route('/red', methods=['POST'])
def set_red():
   if request.json['value']:
       ClewareTrafficLight().red_on()
   else:
       ClewareTrafficLight().red_off()
   return json.dumps({ 'red': _get_red() })

@api.route('/yellow', methods=['POST'])
def set_yellow():
   if request.json['value']:
       ClewareTrafficLight().yellow_on()
   else:
       ClewareTrafficLight().yellow_off()
   return json.dumps({ 'yellow': _get_yellow() })

@api.route('/green', methods=['POST'])
def set_green():
   if request.json['value']:
       ClewareTrafficLight().green_on()
   else:
       ClewareTrafficLight().green_off()
   return json.dumps({ 'green': _get_green() })

@api.route('/set', methods=['POST'])
def set_colors():
   if 'red' in request.json.keys():
     if request.json['red']:
       ClewareTrafficLight().red_on()
     else:
       ClewareTrafficLight().red_off()
   if 'yellow' in request.json.keys():
     if request.json['yellow']:
       ClewareTrafficLight().yellow_on()
     else:
       ClewareTrafficLight().yellow_off()
   if 'green' in request.json.keys():
     if request.json['green']:
       ClewareTrafficLight().green_on()
     else:
       ClewareTrafficLight().green_off()

   return json.dumps({
       'red': _get_red(),
       'yellow': _get_yellow(),
       'green': _get_green(),
   })


if __name__ == '__main__':
      api.run(host='0.0.0.0', port=8080)
