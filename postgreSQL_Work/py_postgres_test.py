#!/usr/bin/python

#Importing Libraries to work with PostgreSQL
import psycopg2
import sys
 
def main():
	# define connection string
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

	# add items into db from JSON here
	print "Adding \n"

	items = pickle.load(open(mock_data.json,"rb"))

 
if __name__ == "__main__":
	main()
