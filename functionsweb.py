filepath = "todos.txt"
def get(file=filepath):
    with open(file,'r') as filehandler:
        content = filehandler.readlines()
    return content
def writetodo(content,file=filepath):
    with open(file,'a') as filehandler:
        filehandler.write(content)
def complete(act,file=filepath):
    with open(file,'r') as filehandler:
        content = filehandler.readlines()
    content.remove(act)
    with open(file,'w') as filehandler:
        filehandler.writelines(content)
    
