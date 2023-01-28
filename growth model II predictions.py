# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 15:47:47 2023

@author: saubh
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.backends.backend_pdf import PdfPages


xl=0.25-0.01
xh=0.25+0.01
x=np.random.uniform(xl,xh,50)
gen=25
# r0=np.arange(0,4.5,0.5)
r0=[0.5,1.5,2.5,3,3.2,3.5,3.6,4]
n=4
r0_div = [r0[i * n:(i + 1) * n] for i in range((len(r0) + n - 1) // n )]

graph_count=0
plot_count=0
with PdfPages('plot.pdf') as pdf:
    for i in r0_div:
        fig, ax = plt.subplots(n, 2, figsize=[8.27,11.69],sharex=True)
        gs1 = gridspec.GridSpec(4, 2)
        gs1.update(wspace=0.28, hspace=0.6) # set the spacing between axes.
    
        ax = np.array([ [plt.subplot(gs1[0]), plt.subplot(gs1[1])], 
                          [plt.subplot(gs1[2]), plt.subplot(gs1[3])],
                          [plt.subplot(gs1[4]), plt.subplot(gs1[5])],
                          [plt.subplot(gs1[6]), plt.subplot(gs1[7])],])
        for num,r in enumerate(i):
            x25=[]
            for k in x:
                xns=[]
                for g in range(0,gen):
                    if g==0:
                        xt=r*k*(1-k)
                        xns+=[xt]
                    elif g!=0:
                        xt=r*xt*(1-xt)
                        xns+=[xt]
                x25+=[xt]
                ax[num,0].plot(np.arange(0,gen)+1, xns, linewidth=.3,)
                ax[num,0].set_ylabel("$X_{t}$", size=10)
                ax[num,0].set_xlabel("$t$", size=10)
                ax[num,0].set_title('$R_{0}=%s$' %r, size=10)
            # plt.show()
            # sns.displot(data=pd.DataFrame(x25), kind='hist', kde=True,
            #             bins=50, legend=False, height=4, aspect=2,)
            sns.histplot(data=pd.DataFrame(x25).squeeze(),ax=ax[num,1],legend=False, bins=20)
            sns.kdeplot(data=pd.DataFrame(x25).squeeze(),ax=ax[num,1],legend=False, color='red')
            ax[num,1].set_ylabel("$Frequency$", size=10)
            ax[num,1].set_xlabel(" " ,size=10)
            ax[num,1].set_xlabel("$X_{%s}$" %gen, size=10)
            ax[num,1].set_xlim(0,1)
            ax[num,1].set_title('$R_{0}=%s$' %r, size=10)
        #     graph_count+=1
        # if graph_count==n:
        plot_count+=1
        pdf.savefig(dpi=300, bbox_inches='tight')
        plt.show()
        graph_count=0
