#Author Zack Edwards
#Excersice 3

#part 1
while True:
    in_filename = input("Please enter the file name, no extension: ") #ask for a while name
    if in_filename == "marketingdata":    #Check if its the correct file name
        marketing_filename = in_filename + '.txt'    #convert it into a txt file by adding the extension
        break        
    else:            
        print ('\n wrong file name')   #returns the user to re-input a file name         
        continue
marketing_file = open(marketing_filename, 'r') #open the file
line_counter = 0 #a counter for the lines in the file
NA_counter = 0 #counter for the lines containing NA
print ('\n The following are the first 3 lines containing N/A')
for text_line in marketing_file:    
    if 'NA' in text_line:        
        if NA_counter < 3:            
            print (text_line)  #if the line contains NA and is the first of 3 then it will be printed      
        NA_counter += 1 #the counter goes up regardless
    line_counter += 1
print ('\n There are', line_counter, 'lines in the', marketing_filename, 'file, of which', NA_counter, 'have NAs')
#part 2
print ('\n---processing now the csv file---')
citi_file = open('CitiBike.csv', 'r') #open the file
next(citi_file) #skip beggining
first_five_list = [] #create arrays 
smaller_miles_list = []
line_counter = 0 #create a variabe to keep track of the lines
for line in citi_file:    #loop through the file
    line_list = line.strip().split(',')    
    if line_counter < 5:        
        first_five_list.append(line_list)    
        line_counter += 1    
    try:        
        miles = int(line_list [3])    
    except:        
        continue    
    if miles <10000:        
        smaller_miles_list.append(line_list)
print ("\nThere are", line_counter, "lines in the CitiBike.csv file")
print ('\n--the following are the first 5 lines:')
for one_of_five in first_five_list: 
    print (one_of_five)
print ('\n--the following are the lines with smaller values for the daily miles:')
for small in smaller_miles_list: 
    print (one_of_five)
    