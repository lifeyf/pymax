'''
@File    :   stableCamera.py
@Time    :   2023/09/19 14:05:52
@Author  :   William Smith 
@Version :   1.0
@Contact :   lifeyf@hotmail.com
@License :   Copyright © 2022 <William Smith>
'''

from pymxs import runtime as rt

selected = rt.selection

def ensure_camera(selection):
	if len(selection)>2 or len(selection)<1:
		return 0
	for i in selection:
		if str(rt.classOf(i)) not in ['Targetcamera', 'Targetobject']:
			return 0
	return [len(selection), selection]


def ensure_key(obj):
	pos_controller = rt.getPropertyController(obj.controller, 'pos')
	x_keys = rt.getPropertyController(pos_controller, 'x_position').keys
	y_keys = rt.getPropertyController(pos_controller, 'y_position').keys
	z_keys = rt.getPropertyController(pos_controller, 'z_position').keys
	x_time = [i.time for i in x_keys]
	y_time = [j.time for j in y_keys]
	z_time = [k.time for k in z_keys]
	if x_time == y_time and y_time == z_time:
		return[x_keys, y_keys, z_keys]
	else:
		return []

def axis_keys(axis_keys):
	'''
	get single axis selected keys
	'''
	selected = []
	for i in axis_keys:
		if i.selected:
			selected.append(i)
	return selected

def get_selected_keys(keys):
	'''
	get selectd keys and ensure them equl to 2
	'''
	x_selected = axis_keys(keys[0])
	y_selected = axis_keys(keys[1])
	z_selected = axis_keys(keys[2])
	x_time = [i.time for i in x_selected]
	y_time = [j.time for j in y_selected]
	z_time = [k.time for k in z_selected]
	if x_time == y_time and y_time == z_time and len(x_time) == 2 :
		return[x_selected, y_selected, z_selected]
	else:
		return []

def lockHandle(key):
	try:
		key.x_locked = True
	except:
		pass
	try:
		key.y_locked = True
	except:
		pass
	try:
		key.z_locked = True
	except:
		pass

def set_single_tangent(key):
	a = key[1].value - key[0].value
	b = key[1].time.ticks - key[0].time.ticks
	
	key[0].outTangent = a*26/b
	key[0].inTangent = -a*26/b
	lockHandle(key[0])
	
	key[1].inTangent = -a*26/b
	key[1].outTangent = a*26/b
	lockHandle(key[1])


def set_tangent(selected_keys):
	assert selected_keys != [], 'selectedWrong'
	for i in selected_keys:
		set_single_tangent(i)
	return "OK"

def main():
	cameras = ensure_camera(selected)
	if cameras != 0:
		for i in cameras[1]:
			keys = ensure_key(i)
			selected_keys = get_selected_keys(keys)
			set_tangent(selected_keys)
		print("Succeed")
	
	else:
		print("Error")

if __name__ == "__main__":
	main()