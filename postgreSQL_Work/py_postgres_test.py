#!/usr/bin/python

#Importing Libraries to work with PostgreSQL
import psycopg2
import sys
import json
from pprint import pprint

 
def main():
	#open file - for viewing mock_data only locally
	with open('mock_data.json') as data_file:    
		data = json.load(data_file)

	# connection string
	conn_string = "host='localhost' dbname='testdb' user='' password=''"
 
	# print connection string 
	print "Connecting to database\n	->%s" % (conn_string)
 
	# get a connection, if not -> exception raised
	conn = psycopg2.connect(conn_string)
 
	# conn.cursor will return a cursor object
	# use this cursor to perform queries
	cursor = conn.cursor()
	print "Connected!\n" #good

	# need to flush contents of table before continuing - for stat purposes
	print "Flushing \n" 
	cursor.execute("truncate mock_data;") #flushes

	# add items into db from JSON here
	print "Adding \n"


	data_id = []
	gender = []
	first_name = []
	last_name = []
	email = []
	ip_address = []

	for i in range(len(data)):
		cursor.execute('INSERT INTO mock_data (id, gender, firt_name, last_name, email, ip_address) VALUES (%s, %s, %s, %s, %s, %s)', 
			(data[i]["id"], data[i]["gender"], data[i]["first_name"], data[i]["last_name"],data[i]["email"], data[i]["ip_address"]))
		data_id.append(data[i]["id"])
		gender.append(data[i]["gender"])
		first_name.append(data[i]["first_name"])
		last_name.append(data[i]["last_name"])
		email.append(data[i]["email"])
		ip_address.append(data[i]["ip_address"])


	conn.commit()

	print data_id
	print gender
	#PARSE JSON
	#CONVERT TO INT (IF NECESSARY)
	#INSERT INTO SQL

	cursor.close()
 
if __name__ == "__main__":
	main()
