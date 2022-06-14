from calendar import LocaleTextCalendar
from json import JSONDecodeError
from tkinter.ttk import setup_master


%python
%define a function to call WolframAlpha API to solve the equation eq 
def ask_wolframalpha(eq):
    import requests
    import json
    url = 'http://api.wolframalpha.com/v2/query?appid=QXQQQQQ&input=' + eq + '&format=plaintext'
    r = requests.get(url)
    try:
        result = json.loads(r.text)
        return json_to_latex(result['queryresult']['pods'][1]['subpods'][0]['plaintext'])
    except JSONDecodeError:
        return 'Error'


%python
%define a function to convert a JSON mathematical expression to Latex
def json_to_latex(json_str):
    import json
    try:
        result = json.loads(json_str)
        return result['latex']
    except JSONDecodeError:
        return 'Error'