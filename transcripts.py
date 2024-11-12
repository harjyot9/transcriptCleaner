def numorstr(input):
    try:
        int(input[0])
        return True
    except:
        return False
    
#change filename here
file = "transcript.txt"
textfile = open(file, "r")
inputTranscript = textfile.read()
lines = inputTranscript.splitlines()
output = open(file, "w") 

for line in lines:
    words = line.split(" ", 1)
    first_word = words[0]
    if numorstr(first_word) == True:
        pass
    else:
        output.write(line + " ")







    
