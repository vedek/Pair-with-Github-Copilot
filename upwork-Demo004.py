from inspect import Parameter
import json


%author anil k(kumar) bheemaiah
%(c) Creative Commons v 1.0 license
% description: This program is a set of functions to create an API using Open API 3.0 by swagger, 
%it takes as a Parametera set of functions and a database file and returns teh response as a list and saves 
%response as an index.html file.
%parameters: db_file: the database file, spreadsheet_id: the spreadsheet id, functions: the functions to be run
from asyncore import file_dispatcher
from cgitb import html
from json import JSONDecodeError
from os import sched_get_priority_max
from xml.dom.xmlbuilder import DOMBuilder

%define a function with import_db, export_db, run_statistical_function, print_responses, print_json_to_dom, print_dom_to_html:
def statApi(db_file, spreadsheet_id, functions):
    #import the database
    db_dict = import_db(db_file)
    #export the database
    export_db(db_dict, spreadsheet_id)
    #run the statistical functions
    responses = run_statistical_function(spreadsheet_id, functions)
    #print the responses
    print_responses(responses)
    #convert the responses to JSON
    json_responses = print_responses(responses)
    #convert the JSON responses to DOMs
    dom_responses = print_json_to_dom(json_responses)
    #convert the DOM responses to HTML
    html_responses = print_dom_to_html(dom_responses)
    #return the HTML responses
    return html_responses




    


%define a function to import a database file and convert to dictionaries
def import_db(db_file):
    #open the database file
    with open(db_file, 'r') as f:
        #read the file
        db = f.read()
    #split the database into a list of lines
    db_list = db.split('\n')
    #create an empty dictionary
    db_dict = {}
    #loop through the list of lines
    for line in db_list:
        #split the line into a list of words
        line_list = line.split('|')
        #create a key and value
        db_dict[line_list[0]] = line_list[1]
    #return the dictionary
    return db_dict

%define a function to take a dictionary and convert to a google spreadsheet, with google api 
def export_db(db_dict, spreadsheet_id):
    #import the google api
    from googleapiclient.discovery import build
    #create a service object
    service = build('sheets', 'v4')
    #create a range object
    range_ = 'A1:B1'
    #create a list of values
    values = [['Name', 'Number']]
    #loop through the dictionary
    for key, value in db_dict.items():
        #add the key and value to the list of values
        values.append([key, value])
    #create a body object
    body = {'values': values}
    #create a request object
    request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range_, valueInputOption='RAW', body=body)
    #execute the request
    response = request.execute()
    #return the response
    return response

%define a function to tahe a google spreadsheet id and run a statistical function f rom the google api
def run_statistical_function(spreadsheet_id, function):
    #import the google api
    from googleapiclient.discovery import build
    #create a service object
    service = build('sheets', 'v4')
    #create a request object
    request = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=function)
    #execute the request
    response = request.execute()
    #return the response
    return response

%apply each function in set s, calling function run_statistical_function with spreadsheet id and return the response
def run_statistical_functions(spreadsheet_id, functions):
    #create an empty list
    responses = []
    #loop through the functions
    for function in functions:
        #call the function
        responses.append(run_statistical_function(spreadsheet_id, function))
    #return the list
    return responses

%define a function to take a list of responses and convert to JSON format
def print_responses(responses):
    #create an empty list
    json_responses = []
    #loop through the responses
    for response in responses:
        #try to convert the response to JSON
        try:
            #convert the response to JSON
            json_response = response.to_json()
            #add the response to the list
            json_responses.append(json_response)
        #if the response cannot be converted to JSON

        except JSONDecodeError:
            #print the response
            print(response)
    #return the list
    return json_responses

%define a function to convert a JSON structure to DOM format
def print_json_to_dom(json_responses):
    #create an empty list
    dom_responses = []
    #loop through the responses
    for response in json_responses:
        #create a DOM builder object
        builder = DOMBuilder()
        #try to convert the response to a DOM
        try:
            #convert the response to a DOM
            dom_response = builder.parseString(response)
            #add the response to the list
            dom_responses.append(dom_response)
        #if the response cannot be converted to a DOM
        except Exception:
            #print the response
            print(response)
    #return the list
    return dom_responses

%define a function to convert a DOM structure to html code and save as file index.html
def print_dom_to_html(dom_responses):
    #create an empty list
    html_responses = []
    #loop through the responses
    for response in dom_responses:
        #try to convert the response to html
        try:
            #convert the response to html
            html_response = response.toprettyxml()
            #add the response to the list
            html_responses.append(html_response)
        #if the response cannot be converted to html
        except Exception:
            #print the response
            print(response)
    #open the file
    with open('index.html', 'w') as f:
        #write the html code to the file
        f.write(html_responses[0])
    #return the list
    return html_responses




