log_file = open("um-server-01.txt")
#open file name()


def sales_reports(log_file): #defining a function name
    for line in log_file:  #looping in log_file
        line = line.rstrip() #method removes any trailing characters.
        day = line[0:3]  #day will be a day in the line array
        if day == "Mon": #if the day =mon print the (line)
            print(line)


sales_reports(log_file)
