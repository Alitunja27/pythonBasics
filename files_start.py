#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  #f = open ("textfile.txt", "w+") #W es abrir para escribir y el + es para crearlo si no existe

  # Open the file for appending text to the end
  #f = open ("textfile.txt","a")   #a means apend data at the end of the file, not to overright data in the file
  f = open ("textfile.txt","r")    #r is to read the file

  # write some lines of data to the file
  #for i in range (10):
  #  f.write("This line is " + str(i) + "\n")

  
  # close the file when done
  #f.close()
  
  # Open the file back up and read the contents
  if f.mode == 'r':
    contents = f.read()
    print(contents)
    
if __name__ == "__main__":
  main()
