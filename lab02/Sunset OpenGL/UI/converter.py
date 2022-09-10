import os
#current_path = os.getcwd()
#command = f'cmd /c "cd {current_path}"'
#os.system(command)
for file in os.listdir():
    if file.find('ui') != -1:
        print(file)
        command = f'cmd /c "pyuic5 -x {file} -o {file.split(".")[0]}.py"'
        os.system(command)
    if file.find('qrc') != -1:
        print(file)
        command = f'cmd /c "pyrcc5 {file} -o {file.split(".")[0]}_rc.py"'
        os.system(command)
        
        
