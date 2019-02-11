#!/usr/bin/python3
import psycopg2

DBNAME = "news"


def popular_articles():
    # Connect to Database
    connection = psycopg2.connect(database=DBNAME)
    # Creator Cursor
    cursor = connection.cursor()
    # Execure Query
    cursor.execute("select articles.title, count(*) as views"
                   " from articles, log"
                   " where log.path like concat('%',articles.slug,'%')"
                   " and log.status like '%200%'"
                   " group by articles.title, log.path"
                   " order by views desc limit 3")
    # Results fetch
    results = cursor.fetchall()
    # Export to file
    f = open('Query_Output.txt', 'w')
    print("What are the most popular three articles of all time?\n")
    f.write("What are the most popular three articles of all time?\n")
    for i in range(len(results)):
        name = results[i][0]
        views = results[i][1]
        f.write('"%s" ' "-- %d" % (name, views) + " views\n")
        print('"%s" ' "-- %d" % (name, views) + " views\n")
    f.write("\n")
    f.close()
    connection.close()


def popular_authors():
    # Connect to Database
    connection = psycopg2.connect(database=DBNAME)
    # Creator Cursor
    cursor = connection.cursor()
    # Execure Query
    cursor.execute("select authors.name, count(*) as views"
                   " from authors, articles, log"
                   " where log.path like concat('%',articles.slug,'%')"
                   " and log.status like '%200%'"
                   " and authors.id = articles.author"
                   " group by authors.name"
                   " order by views")
    # Results fetch
    results = cursor.fetchall()
    # Open file and append to the end of the file
    f = open('Query_Output.txt', 'a')
    print("Who are the most popular article authors of all time?\n")
    f.write("Who are the most popular article authors of all time?\n")
    for i in range(len(results)):
        name = results[i][0]
        views = results[i][1]
        f.write("%s -- %d" % (name, views) + " views\n")
        print("%s -- %d" % (name, views) + " views\n")
    f.write("\n")
    f.close()
    connection.close()


def request_errors():
    # Connect to Database
    connection = psycopg2.connect(database=DBNAME)
    # Creator Cursor
    cursor = connection.cursor()
    # Execure Query
    cursor.execute("select error_log.date,"
                   " round(100 * error_total / log_total, 2) as percentage"
                   " from total_log, error_log"
                   " where total_log.date = error_log.date"
                   " and error_total > log_total/100")
    # Results fetch
    results = cursor.fetchall()
    print (results)
    # Open file and append to the end of the file
    f = open('Query_Output.txt', 'a')
    print("On which days did more than '1%' of requests lead to errors?\n")
    f.write("On which days did more than '1%' of requests lead to errors?\n")
    for i in range(len(results)):
        print (str(results[i][0]) + ' -- ' + str(results[i][1]) + ' %')
    f.close()
    connection.close()


popular_articles()
popular_authors()
request_errors()
