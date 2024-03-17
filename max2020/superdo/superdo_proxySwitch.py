'''
@File    :   proxySwitch.py
@Time    :   2023/10/06 17:24:34
@Author  :   William Smith 
@Version :   1.0
@Contact :   lifeyf@hotmail.com
@License :   Copyright @ 2022 <William Smith>
'''
from pymxs import runtime as rt


def conststate():
    try:
        rt.globalVars.get(rt.name('proxy_switchstate'))
    except RuntimeError:
        rt.execute('global proxy_switchstate = True')
        rt.globalVars.get(rt.name('proxy_switchstate'))
    
def changestate():
    if rt.globalVars.get(rt.name('proxy_switchstate')):
        for i in rt.geometry:
            if str(rt.classOf(i)) == 'VRayProxy':
                i.display = 0 
        rt.execute('global proxy_switchstate = False')
        print("proxy_Box")
    else:
        for i in rt.geometry:
            if str(rt.classOf(i)) == 'VRayProxy':
                i.display = 4 
        rt.execute('global proxy_switchstate = True')
        print("proxy_mesh")

def proxy_switch_main():
    conststate()
    changestate()
    rt.redrawviews()

if __name__ == '__main__':
    proxy_switch_main()