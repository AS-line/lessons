#!/usr/bin/env python3
import cgi
import my_script
name = cgi.FieldStorage().getlist('username')
sername = cgi.FieldStorage().getlist('usersername')
boxes = cgi.FieldStorage().getlist('boxname')

print('Content-type: text/html')
print()
print("Тебя зовут ", name[0])
print('<br>')
print("Твоя фамилия ", sername[0])
my_script.saveindb(name[0], sername[0])