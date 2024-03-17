'''
@File    :   transformLock.py
@Time    :   2023/10/06 18:00:50
@Author  :   William Smith 
@Version :   1.0
@Contact :   lifeyf@hotmail.com
@License :   Copyright @ 2022 <William Smith>
'''
from pymxs import runtime as rt

def conststate():
    try:
        rt.globalVars.get(rt.name('transform_lockstate'))
    except RuntimeError:
        rt.execute('global transform_lockstate = true')
    
def changestate():
	if rt.globalVars.get(rt.name('transform_lockstate')):
		rt.setTransformLockFlags(rt.selection, rt.name('all'))
		rt.execute('global transform_lockstate = false')
		print("Locked!")
	else:
		rt.setTransformLockFlags(rt.selection, rt.name('none'))
		rt.execute('global transform_lockstate = true')
		print("Unlocked!")

def transform_lock_main():
    conststate()
    changestate()

if __name__ == '__main__':
    transform_lock_main()