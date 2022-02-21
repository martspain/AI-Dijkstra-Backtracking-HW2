class FileWriter:
    def __init__(self, address):
        self.directory = address
    
    def writeIterableOutput(self, title, content):
        # title should be a ready-to-go string
        # content should be an array of tuples like
        # [(1,2,3), (4,5,6)]
        with open(self.directory, 'w') as file:
            file.write(title + '\n')

            # item should look like (1, 2, 3)
            for item in content:
                file.write(str(item[0]) + ' ' + str(item[1]) + ' ' + str(item[2]) + '\n')
    
    def writeOutput(self, content):
        # content should be a ready-to-go string
        with open(self.directory, 'w') as file:
            file.write(content + '\n')
    
    def appendOutput(self, content):
        # content should be a ready-to-go string
        with open(self.directory, 'a') as file:
            file.write(content + '\n')
