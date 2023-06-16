#-------------------------------------------------
#            MODULES FROM PYTHON
#-------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt    
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)     
import pandas as pd

#-------------------------------------------------
#       Setting configurations
#-------------------------------------------------

font = {'family' : "Times New Roman",
       'weight' : 'normal',
       'size'   : 40  }

plt.rc('font', **font)
plt.rc('legend', fontsize = 30) # using a size in points
plt.rcParams['lines.linewidth'] = 12
plt.rcParams['lines.markersize'] = 15
plt.rcParams["figure.figsize"] = [24, 16]
plt.rcParams["figure.autolayout"] = True
#plt.ticklabel_format (scilimits=(-4, 5))

# Colors

b1="indianred" 
o1 = "#008080"
flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]

#-------------------------------------------------


def plotting (T, flag, N_ex, B, B2, y_relaxation_1, y_relaxation_2, option_2spin, t, conditional, B_pbit2, state_1, state_2, x_vector, asociation_results, number_2, save):   
         
#-------------------------------------------------
# For one p-bit:
#-------------------------------------------------
    name = 'Relaxation_' + str(T) + 'exp.png'

    # At constant Magnetic Field:
        
    if flag == 0 and option_2spin == 0:
        
        values = [2, 40, 80]
        factor = [1, 0.3, 0.0035]
        y = y_relaxation_1

        if T in values:
            
            name2 = str(T) + 'K_exp.csv'
            data = pd.read_csv(name2, sep=';')
            data = data.astype('float32')
            data = data.values
            x_real = data[:, 0]
            y_real = data[:, 1]
            index = values.index(T)
            
            y = [((2 * x) - N_ex) for x in y]
            rmin = min(y)                       # value
            rmax = max(y)
            tmax = max(y_real)                  # target
            tmin = min(y_real)
            
            y = [(((i-rmin)/(rmax-rmin))*(tmax-tmin))+tmin for i in y]
            plt.plot(x_real, y_real, "x", markersize = 18, markeredgewidth = 6, color = b1, label = 'Experimental')
        
        plt.plot(t[0:len(y)], y, color = o1, label = "Simulated")
        plt.title('%d spins at %d K (Constant Field: %.1f)' % (N_ex, T, B[0]))
        plt.grid()
        plt.xlabel('Time, $t$(s)') 
        plt.ylabel(u" Magnetic moment, \u03bc (emu)")
        plt.legend(loc='center right', prop={'size': 40})
        
        if save == 1:
            plt.savefig(name)    
        plt.show()
    
    # At changeable Magnetic Field:
        
    elif flag == 1 and option_2spin == 0:
   
        fig, ax1 = plt.subplots()
        
        
        ax1.set_xlabel ('Time, $t$(s)')
        ax1.set_ylabel (u" Magnetic moment, \u03bc (emu)")
        ax1.plot (t, y_relaxation_1, "o", markersize = 18, markeredgewidth = 6, color = o1, label = "Simulated response", zorder = 2)
        ax1.tick_params (axis = 'y')
        
        ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
        
        ax2.set_ylabel ('Magnetic Field (mT)')  # we already handled the x-label with ax1
        ax2.plot (t, -B, "--", color = b1, linewidth = 6, label = "AC Field", zorder = 1)
        ax2.tick_params (axis='y')
        
        fig.tight_layout()  # otherwise the right y-label is slightly clipped
        ax1.grid (True, color ='lightgray')
        ax2.grid (True, color = 'gray')
        ax1.legend (bbox_to_anchor = (0.0, 1.08), loc = "upper left", fontsize = 30, frameon = True)
        ax2.legend (bbox_to_anchor = (1.0, 1.08), loc = "upper right", fontsize = 30, frameon = True)
        
        for i in (ax1,ax2):
            i.spines.bottom.set_visible(True)
            i.spines.right.set_visible(True)
            i.spines.top.set_visible(True)
            i.yaxis.set_minor_locator(AutoMinorLocator())
        
        if save == 1:
            plt.savefig(name)    
        plt.show()

    #-------------------------------------------------
    # For two p-bits:
    #-------------------------------------------------
    
    elif option_2spin == 1:
        
        plt.rcParams['lines.linewidth'] = 6
        plt.plot (t, state_1, label = r"p-bit $i$", color = flatui[3]) 
        plt.plot (t, state_2, label = "p-bit $j$", color = flatui[4]) 
        plt.xlabel('Time, $t$(s)') 
        plt.ylabel('State')
        plt.legend(loc='upper right', prop={'size': 40})
        plt.grid()
        
        if save == 1:
            plt.savefig('states_', + str (T) + '.png')    
        plt.show()
        
        
        plt.plot(x_vector, asociation_results, color = o1)
        plt.xlabel("Delay time")
        plt.ylabel("Association factor between p-bit i and p-bit j")
        plt.grid()
        
        if save == 1:
            plt.savefig('asociation.png')
        plt.show()
  
        plt.plot (t, y_relaxation_1, color = flatui[3], label= r"p-bit $i$")
        plt.plot(t, y_relaxation_2, color = flatui[4], label= r"p-bit $j$")
        plt.plot (t, B2*(N_ex*10*1.5), color = o1, label= "Magnetic Field (scaled)")
        plt.title ('%d spins at %d K with %.2f T of response (Constant Field - first pbit)' % (N_ex, T, B_pbit2))
    
        plt.grid()
        plt.xlabel('Time, $t$(s)') 
        plt.ylabel(u" Magnetic moment, \u03bc (emu)")
        plt.legend(loc='center right', prop={'size': 40})
        if save == 1:
            plt.savefig(name)    
        plt.show()
    

