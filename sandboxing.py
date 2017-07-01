import subprocess #for calling a new process in a sandboxed environment
import ast#for parsing the sandboxed plugin response


"""In every function we passed the sanboxed environment:
1) the name of the file's plugin(SE ENTIENDE? el nombre de los archivos de los plugins, no el name() del plugin EJ: serial_dicer.py)
2) The function it should be executing --> name() or play(). In the case of play we send the corresponding values needed
"""
def getName(plugin):
    modulo = "plugins/" + plugin
    try:
        output = (subprocess.check_output(["python","sandbox.py",modulo,"name"], stderr=subprocess.STDOUT)).strip("\n")
        return output
    except subprocess.CalledProcessError as e:
        print "Ocurrio un error en el sandboxing"
        print "El error es el sgte:\n", e.output

def getPlay(plugin,roll_no,dice,bonus,players,scoresheets):
    modulo = "plugins/" + plugin
    try:
        output = (subprocess.check_output(["python","sandbox.py",modulo,"play",str(roll_no),str(dice),str(bonus),str(players),str(scoresheets)], stderr=subprocess.STDOUT)).strip("\n")
        #parsing the output
        variable = output[1:-1]
        variable = variable.replace(" ", "")
        nueva = variable.split(",")
        roll=ast.literal_eval(nueva[0])
        decision=ast.literal_eval(nueva[1])
        scoresheet=ast.literal_eval(nueva[2])
        return list(roll), str(decision), int(scoresheet)
    except subprocess.CalledProcessError as e:
        print "Ocurrio un error en el sandboxing"
        print "El error es el sgte:\n", e.output
