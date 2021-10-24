#!/usr/bin/python3
print("Content-Type: text/html\n")
print("")

import cgi
import cgitb
import json
import sys

# thank you mr mykolyk for this function
def fs2d():
    '''
    Convert return val of FieldStorage() into standard dictionary
    '''
    d = {}
    L = []
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value
    return d

cgitb.enable()

html = '''
<!doctype html>
<html>
<head>
<link rel="stylesheet" href="assets/styles.css">
</head>
<body>
'''
f = open('json/completed.json', 'r')
assignment_name = fs2d()['id']
data = json.load(f)
blacklist = open('json/blacklist.txt', 'r').read().split('\n')
only_submitted = True

valid = assignment_name in data
if not valid:
	html += f'''
		<br><br><br><br><br><br><br><br><center>
        		<div id="main_box">
				<br>
				<h2 style="color: rgb(200, 50, 0)"> Error: Assignment '{assignment_name}' doesn't exist </h2>
	                        <p> <a href="main.py"> home </a> </p>
				<br>
			</div>
		</center><!--
	'''
else:
	data = data[assignment_name]
	last_updated = open('json/updated.txt', 'r').read()
	unsubmitted_ctr = 0

	html += f'''
	<br><br><br><br><br>
	<center>
		<div id="main_box" style="width: 70vw;">
			<br>
			<h1> Submissions for {assignment_name} </h1>
			<p> <i> Last updated {last_updated} </i> </p>
			<p> <a href="main.py"> home </a> </p>
			<br>
			<h2> Submissions </h2>
			<table>
				<tr>
					<th> Name </th>
					<th> Submitted (Y/N) </th>
					<th> GitHub Link </th>
				</tr>
	'''

	for student in data:
		link = True
		submitted = 'Yes'
		if assignment_name == 'pre' and student == 'NYG-Kartik':
			beaned = True
		else:
			beaned = False
		if data[student]['link'] == 'n/a':
			link = False
			submitted = 'No'
			unsubmitted_ctr += 1
		student_url = 'https://www.github.com/' + student + '/'
		if not(not link and only_submitted) and (not student in blacklist):
			html += f'''<tr>
					<td> <a href="{student_url}" style="color: black;"> {student} </a> </td>
					<td style="color: '''
			if link:
				html += 'green'
			else:
				html += 'red'
			html += f''';"> <center> {submitted} </center> </td>
					<td> '''
			if link:
				if not beaned:
					html += f'''<a href="{data[student]['link']}">{data[student]['link']}</a>'''
				else:
					html += f'''<a href="{data[student]['link']}">https://github.com/NYG-Kartik/APCS-REPO/tree/main/01</a>'''
			else:
				html += 'n/a'
			html += ''' </td></tr>'''

	submitted_ctr = len(data) - unsubmitted_ctr
	html += f'''
		</table>
		<br>
                       <h3> Statistics </h3>
		<table>
			<tr>
				<td style="border: none;"></td>
				<th> Submitted </td>
				<th> Not Submitted </td>
				<th> Percent Submitted </td>
			</tr>
			<tr>
				<th> {assignment_name} </th>
				<td> <center> {submitted_ctr} </center> </td>
				<td> <center> {unsubmitted_ctr} </center> </td>
			<td> <center> {round(100 * submitted_ctr / len(data), 2)}% </center> </td>
			</tr>
		</table>
		<br><br>
		<p> <a href="main.py"> home </a> </p>
	</div>
	<br><br>
	'''
	
	html += '''
	</body>
	</html>
	'''

print(html)
