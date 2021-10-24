#!/usr/bin/python3
print("Content-Type: text/html\n")
print("")

import cgi
import cgitb
import smtplib, ssl
import os

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

args = fs2d()

if 'u_name' in args and 'reason' in args:
	with open('json/blacklist.txt', 'a') as f:
		f.write(args['u_name'] + '\n')
	with open('json/reasons.txt', 'a') as f:
		f.write(f'{args["u_name"]}: {args["reason"]}\n')
	print('''<br><br><br><br><br><br>
		<center>
                        <div id="main_box">
				<br>
				<h2> You have been successfully removed from the list. Have a nice day. </h1>
				<p> <a href="main.py"> home </a> </p>
                        </div>
                </center>
	''')
else:
	html += '''
		<br><br><br><br><br><br>
		<style> body {background-color: white;} </style>
		<center>
			<div style="width: 50vw">
				<h3> You should strongly suspect, </h3>
				<h3> at this time, </h3>
				<h3> that you're in the WRONG PLACE. </h3>
				<br><br><br>
				<p style="text-align: right;"> <i> -clyde sinclair </i> </p>
			</div>
		</center>
	'''

html += '''
</body>
</html>
'''

print(html)
