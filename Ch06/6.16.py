# declare the class
class DataTransferinFiles():
    # Defining the transfer method to data transfer between two files
    def transfer(Self, firstfilename, secondfilename):
        # Display Statment here
        print()
        print("your First File is = ", firstfilename)
        print()
        print("your Second File is = ", secondfilename)
        print()
        # Open the file through with statement to read the data
        with open(firstfilename, 'r') as filedata:
            firstfiledata = filedata.readlines()
            print()
            print("---- 1st file reading complete ----")
            print()
        # Open the file through the statement to read the data
        with open(secondfilename, 'r') as filedata:
            secondfiledata = filedata.readlines()
            print()
            print("---- 2nd file reading complete ----")
            print()
        # First file data transfer into first file
        # File iterate here
        for eachline in firstfiledata:
            filesecond = open(secondfilename, 'a')
            # data wronte into file
            filesecond.write("\n"+eachline+"\n")
            print()
            print("---- 1st file transfer data completed into 2nd file ----")
        # Second file data transfer into first file
        # File iterate here
        for eachline in secondfiledata:
            filefirst = open(firstfilename, 'a')
            filefirst.write("\n"+eachline+"\n")
            print()
            print("---- 2nd file transfer data completed into 1st file ----")
        # initalize the object
        dataobject = DataTransferinFiles()
    # Ask for first file name
    print()
    firstfilename = input("Enter first file name = ")
    # Ask for second file name
    print()
    secondfilename = input("Enter second file Name = ")
    # Call the transfer method through the object
    dataobject.transfer(firstfilename, secondfilename)
