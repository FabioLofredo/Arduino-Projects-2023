from pyfirmata import Arduino, util
import time

import matplotlib as mpl
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
#from drawnow import *

board = Arduino("COM3")
it= util.Iterator(board)
it.start()
pino_digi_input = 2
pino_digi_led = 3
pino_anal_leitura = 0
board.digital[pino_digi_input].write(1)
leitura = board.get_pin('a:' + str(pino_anal_leitura) + ':o')

mpl.pyplot.ion() # Enable interactive mode.

list_data_collected=[]
list_count=[]
int_count = 0
int_max_dots_on_graph=100

try:
    f = open("E:\\\graph_data.txt","x")
except:
    ...
f = open("E:\\\graph_data.txt", "w")

def func_create_graph(x,y):
    #fig, ax = plt.subplots()  # Create a figure containing a single axes.
    #ax.plot(data_collected)  # Plot some data on the axes.
    #plt.show()
    plt.plot(x,y)

estadoBotao = False
while True:
    estadoBotao = leitura.read()
    list_data_collected.append(estadoBotao)
    print(estadoBotao)
    time.sleep(0.05)
    int_count +=1  
    list_count.append(int_count)

    # File write
    f = open("E:\\\graph_data.txt", "a")
    f.write(str(estadoBotao)+','+str(int_count)+'\n')
    f.close()

    # Graph plot
    #plt.plot(list_count,list_data_collected)
    #plt.show()
    #plt.pause(0.0001)
    
    if len(list_count)<int_max_dots_on_graph:
        plt.plot(list_count,list_data_collected)
        plt.show()
        plt.pause(0.0001)
    else:
        plt.clf()
        plt.plot(list_count[-int_max_dots_on_graph:],list_data_collected[-int_max_dots_on_graph:])
        plt.show()
        plt.pause(0.0001)

    if estadoBotao != None:
        if (estadoBotao > 0.8): 
            board.digital[pino_digi_led].write(1)
        else:
            board.digital[pino_digi_led].write(0)



