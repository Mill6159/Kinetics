# General description of script
# List details here




# Import modules

import numpy as np
from matplotlib import pyplot as plt
from itertools import cycle
import matplotlib as mpl

# Define classes

class Main:
  '''
  This will be our main "SuperClass"
  '''
  def __init__(self, expt_name, temp):
    self.expt_name = expt_name
    self.temp = temp
    print('Initializing Main Kinetics Class')
    # print("Experiment Name: ", expt_name)


# Main Calculation class below

class Calculations(Main):
  '''
  This class will inherit all of the variables of the "Main" class
  BUT also be able to take it's own variables as inputs

  Kd:
  	Units = micromolar

  pc:
  	Units = micromolar

  pL:
  	Units = micromolar

  vmax:
  '''
  def __init__(self, 
               expt_name, 
               temp, 
               kd=14, 
               vmax=2,
               pc=8,
               pL=[1,5,10,15,25,50,75,100,125,150,175,200]):
    self.kd = kd
    self.pc = pc
    self.pL = pL
    self.vmax = vmax
    Main.__init__(self, expt_name, temp)

  def returnVariables(self):
    print('List of variables:', self.expt_name, self.vmax)

  def nPlot_variX_and_Color(self,pairList,labelList,colorList,savelabel,xlabel='No Label Provided',ylabel='No Label Provided',
              LogLin=True,LinLin=False,LogLog=False,linewidth=3,
              set_ylim=False,ylow=0.0001,yhigh=1,darkmode=False,
	          lg_size=8):
	    '''
	    :param pairList: list of lists (tuple), must be [[x1,y1],...[xn,yn]]
	    :param labelList: list of length n, labeling the sets of tuples in pairList
	    :param savelabel:
	    :param xlabel:
	    :param ylabel:
	    :param linewidth:
	    :return:
	    '''
	    plt.rc('axes',linewidth=2)
	    plt.rc('lines',markeredgewidth=2)
	    plt.rc('font',**{'sans-serif': ['Helvetica']})
	    if darkmode==True:
	        plt.style.use('dark_background')
	        c1='#EFECE8'
	    else:
	        mpl.rcParams.update(mpl.rcParamsDefault)
	        c1='k'

	    fig=plt.figure(figsize=(6,4.5)) # set figure dimensions
	    ax1=fig.add_subplot(1,1,1) # allows us to build more complex plots
	    for tick in ax1.xaxis.get_major_ticks():
	        tick.label1.set_fontsize(13) # scale for publication needs
	        tick.label1.set_fontname('Helvetica')
	    for tick in ax1.yaxis.get_major_ticks():
	        tick.label1.set_fontsize(13) # scale for publication needs
	        tick.label1.set_fontname('Helvetica')

	    if LogLin == True and LinLin == True and LogLog == True: # kicks you out of the function if you set more then one mode to true
	        print("Cannot set more than one mode equal to True")
	        return
	    elif LogLin == True and LinLin == True:
	        print("Cannot set more than one mode equal to True")
	        return
	    elif LogLin == True and LogLog == True:
	        print("Cannot set more than one mode equal to True")
	        return
	    elif LinLin == True and LogLog == True:
	        print("Cannot set more than one mode equal to True")
	        return

	    cycol = cycle(['-','-','-'])    

	    n=0
	    if LogLin==True:
	        for i,j in zip(pairList,colorList):
	            plt.semilogy(i[0],i[1],
	                        label=labelList[n],
	                        linewidth=linewidth,
	                        color=j,
	                        linestyle=next(cycol))
	            n+=1

	    elif LinLin==True:
	        for i,j,z in zip(pairList,colorList,labelList):
	            plt.plot(i[0],i[1],
	                        label=z,
	                        linewidth=linewidth,
	                        color=j,
	                        linestyle=next(cycol))
	            n+=1
	    elif LogLog==True:
	        for i in pairList:
	            plt.plot(i[0],i[1],
	                        label=labelList[n],
	                        linewidth=linewidth,
	                         linestyle='dotted')
	            n+=1
	            plt.plot(i[2],i[3],
	                        label=labelList[n],
	                        linewidth=linewidth)
	            n+=1
	            ax1.set_yscale('log')
	            ax1.set_xscale('log')


	    plt.ylabel(ylabel,size=16)
	    plt.xlabel(xlabel,size=16)
	    plt.legend(numpoints=1,fontsize=lg_size,loc='best')


	    if set_ylim==True:
	        ax1.set_ylim(ylow,yhigh)
	    # else:
	        # print('Using default y-limit range for the plot: %s'%savelabel)
	    fig.tight_layout()

	    plt.savefig(savelabel+'.png',format='png',bbox_inches='tight',dpi=300)
	    plt.show()

  def nPointPlot_variX_and_Color(self,pairList,labelList,colorList,savelabel,xlabel='No Label Provided',ylabel='No Label Provided',
              LogLin=True,LinLin=False,LogLog=False,linewidth=3,
              set_ylim=False,ylow=0.0001,yhigh=1,darkmode=False,
              lg_size=8):
        '''
        :param pairList: list of lists (tuple), must be [[x1,y1],...[xn,yn]]
        :param labelList: list of length n, labeling the sets of tuples in pairList
        :param savelabel:
        :param xlabel:
        :param ylabel:
        :param linewidth:
        :return:
        '''

        plt.rc('axes',linewidth=2)
        plt.rc('lines',markeredgewidth=2)
        plt.rc('font',**{'sans-serif': ['Helvetica']})
        if darkmode==True:
            plt.style.use('dark_background')
            c1='#EFECE8'
        else:
            mpl.rcParams.update(mpl.rcParamsDefault)
            c1='k'

        fig=plt.figure(figsize=(6,4.5)) # set figure dimensions
        ax1=fig.add_subplot(1,1,1) # allows us to build more complex plots
        for tick in ax1.xaxis.get_major_ticks():
            tick.label1.set_fontsize(15) # scale for publication needs
            tick.label1.set_fontname('Helvetica')
        for tick in ax1.yaxis.get_major_ticks():
            tick.label1.set_fontsize(15) # scale for publication needs
            tick.label1.set_fontname('Helvetica')

        if LogLin == True and LinLin == True and LogLog == True: # kicks you out of the function if you set more then one mode to true
            print("Cannot set more than one mode equal to True")
            return
        elif LogLin == True and LinLin == True:
            print("Cannot set more than one mode equal to True")
            return
        elif LogLin == True and LogLog == True:
            print("Cannot set more than one mode equal to True")
            return
        elif LinLin == True and LogLog == True:
            print("Cannot set more than one mode equal to True")
            return

        n=0
        if LogLin==True:
            for i,j in zip(pairList,colorList):
                plt.semilogy(i[0],i[1],
                            label=labelList[n],
                            linestyle=None,
                            linewidth=linewidth,
                            marker = 'o',
                            markersize = linewidth + 5,
                            color=j)
                n+=1
                # plt.semilogy(i[2],i[3],
                #             label=labelList[n],
                #             linewidth=linewidth,
                #             color=c1)
                # n+=1
        elif LinLin==True:
            for i,j in zip(pairList,colorList):
              plt.plot(i[0],i[1],
              label=labelList[n],
              linestyle=None,
              linewidth=linewidth,
              marker = 'o',
              markersize = linewidth + 5,
              color=j)
                # plt.plot(i[0],i[1],
                #             label=labelList[n],
                #             linewidth=linewidth,
                #             linestyle='-',
                #             color=j,
                #             marker='o',
                #             markersize=linewidth+10)
              n+=1
                # plt.plot(i[2],i[3],
                #             label=labelList[n],
                #             color=c1,
                #             linewidth=linewidth)
                # n+=1
        elif LogLog==True:
            for i in pairList:
                plt.plot(i[0],i[1],
                            label=labelList[n],
                            linewidth=linewidth,
                             linestyle='dotted')
                n+=1
                plt.plot(i[2],i[3],
                            label=labelList[n],
                            linewidth=linewidth)
                n+=1
                ax1.set_yscale('log')
                ax1.set_xscale('log')


        plt.ylabel(ylabel,size=16)
        plt.xlabel(xlabel,size=16)
        plt.legend(numpoints=1,fontsize=lg_size,loc='best')


        if set_ylim==True:
            ax1.set_ylim(ylow,yhigh)
        # else:
            # print('Using default y-limit range for the plot: %s'%savelabel)
        fig.tight_layout()

        plt.savefig(savelabel+'.png',format='png',bbox_inches='tight',dpi=300)
        plt.show()


  def bindingCurve_1t1(self):
  	'''
  	Description
  	'''
  	kd = self.kd
  	pc = self.pc
  	pL = self.pL

  	# Binding curve - Quadratic

  	b = []
  	ub = []
  	pb = []
  	for j in pL:
  		quad_column = [1.0, (-(pc + j + kd)), (pc * j)]
  		roots = np.roots(quad_column)
  		b.append(roots[1])
  		ub.append(pc - roots[1])
  		pb.append((roots[1]/pc)*100)

  	pairList = [
  	[pL, pb]
  	]
  	labelList = [str(self.expt_name)]
  	colorList = ['black']
  	savelabel = '%s_1t1_bindingcurve'%str(self.expt_name)

  	
  	self.nPlot_variX_and_Color(pairList,
  		labelList,
  		colorList,
  		savelabel,
  		xlabel='Ligand Concentration ($\\mu$M)',
  		ylabel='Percent Bound (%)',
  		LogLin=False,
  		LinLin=True,
  		LogLog=False,
  		linewidth=3,
  		set_ylim=False,ylow=0.0001,yhigh=1,darkmode=False,
  		lg_size=14)


# Plotting Class

# Export Class/File Parser

# CP Binding

calcs = Calculations(
                     expt_name = 'CP_Binding', 
                     temp = "20", 
                     kd=14,
                     pc=8 # uM
                     )

calcs.pL = np.linspace(1,500,500)
calcs.bindingCurve_1t1()
calcs.pL = np.linspace(1,100,500)
calcs.bindingCurve_1t1()

## Succinate Binding
calcs.pL = np.linspace(1,10000,500)
calcs.expt_name = 'Succinate Binding'
calcs.kd = 560
calcs.bindingCurve_1t1()


### Change Protein Concentration

# CP Binding

calcs.pc = 1.0 # change protein conc. to 1 uM
calcs.expt_name = 'CP_Binding'
calcs.pL = np.linspace(1,500,500)
calcs.bindingCurve_1t1()
calcs.pL = np.linspace(1,100,500)
calcs.bindingCurve_1t1()

## Succinate Binding
calcs.pL = np.linspace(1,10000,500)
calcs.expt_name = 'Succinate_Binding'
calcs.kd = 560
calcs.bindingCurve_1t1()








