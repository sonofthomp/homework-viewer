#!/usr/bin/python3
print("Content-Type: text/html\n")
print("")

import cgi
import cgitb
import json

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
data = json.load(f)

html += '''
<br><br><br><br><br><br><br>
<center>
	<div id="main_box">
		<br>
		<h1> APCS Homework Viewer </h1>
		<p> <i> by Gabriel Thompson '23 </i> </p>
		<br>
	</div>
	<br><br>
	<div id="main_box" style="width:30vw;">
		<h2> Assignments </h2>
		<table>
			<tr>
				<td style="border: none;"></td>
				<th> Page </th>
				<th> Status </th>
			</tr>
'''

for assignment in data:
	if assignment[:2].isnumeric():
		assignment_title = 'HW' + assignment[:2]
	else:
		assignment_title = 'pre'
	submitted = 0
	unsubmitted = 0
	for name in data[assignment]:
		if data[assignment][name]['link'] == 'n/a':
			unsubmitted += 1
	submitted = len(data[assignment]) - unsubmitted
	html += f'''<tr>
			<th> {assignment_title} </th>
			<td> <a href="assignment.py?id={assignment}">submissions</a> </td>
			<td> <i>{submitted} submitted, {unsubmitted} unsubmitted </i></td>
		</tr>'''

html += '''
		</table>
		<br>
	</div>
'''

html += '''
</body>
</html>
'''
print(html)
