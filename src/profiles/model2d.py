#!/opt/local/bin/python2.7

import numpy as np
import math

class fault2d:
    """ 
    fault2d class: Load 2D fault for plot only
    help to position fault for futher modeling
    Parameters: 
    name: name fault
    x,y: position east, north
    """

    def __init__(self,name,x,y,strike=None):
        self.name=name
        self.x=x
        self.y=y
        
        if strike > 0:
            self.strike=strike-180
        else:
            self.strike=strike

class profile:
    """ 
    profile class: Load profiles 
    Parameters: 
    name: name profile
    x,y: reference point 
    l,w: length, width progile
    strike: strike profile
    type:  std - plot mean and standard deviation InSAR;
    distscale - scatter plot with color scale function of the profile-parallel distance;
    stdscat - plot scatter + standar deviation. 
    flat: if not None estimate a ramp along profile. lin: linear ramp, quad: quadratic, cub: cubic.
    If number InSAR network is 2 then estimate ramp within the overlaping area (Default: None)
    lbins: larger bins for profile
    loc_ramp: location ramp estimation. Can be positive (for postive distances along profile) or negative. Default: None
    """

    def __init__(self,name,x,y,l,w,strike,type=None,
        flat=None,lbins=None,loc_ramp=None):
        self.name=name
        self.x=x
        self.y=y
        self.l=l
        self.w=w
        self.flat=flat
        self.lbins=lbins
        self.loc_ramp=loc_ramp

        if strike > 0:
            self.strike=strike-180
        else:
            self.strike=strike

        self.typ=type
        # lmin,lmax needs to be an attribute of network because different plots for both

class topo:
    """ 
    topo class: Load topographic file 
    Parameters: 
    filename: name input file
    name: name file for plot
    wdir: path input file
    scale: scale values
    color
    topomin,topomax
    plotminmax: option to also plot min max topo within bins
    """

    def __init__(self,name,filename,wdir,color='black',scale=1,topomin=None,topomax=None,plotminmax=False, width=1.):
        self.name=name
        self.filename=filename
        self.wdir=wdir
        self.color=color
        self.scale=scale
        self.topomin=topomin
        self.topomax=topomax
        self.plotminmax=plotminmax
        self.width = width
        
        self.yp=[]
        self.xp=[]

    def load(self,xlim=[-1000,1000],ylim=[-1000,1000]):
        fname=file(self.wdir+self.filename)
        x,y,z=np.loadtxt(fname,comments='#',unpack=True,dtype='f,f,f')
        index=np.nonzero((x<xlim[0])|(x>xlim[1])|(y<ylim[0])|(y>ylim[1]))
        self.x,self.y,self.z=np.delete(x,index),np.delete(y,index),np.delete(z,index)*self.scale


