'''
@File    :   exportSof.py
@Time    :   2023/07/30 16:01:04
@Author  :   William Smith (Alias)
@Version :   2.0
@Contact :   lifeyf@hotmail.com
@License :   Copyright @ 2022 <William Smith>
@Tested  :   3dsmax 2020
'''
'''
this script is used to export the sof file from current filename depend on statesets.
if you want run script from maxscript just write a ms file and write:
python.ExecuteFile @"C:\your script path\exportSof.py"
'''
import os
import re
from pymxs import runtime as rt
from PySide2.QtWidgets import QMessageBox



def sof_project_test(file_pos):
	'''
	test if the file path and the sof path is in right place return sof root path.
	or false, if path not right.
	'''
	test_pos =  file_pos.find("02-Output\\3D\\cam\\")
	name_exam = re.search(r"\d+-+[a-zA-Z]+-+[a-zA-Z]+-+.+\\?", file_pos)
	if test_pos<=0 or not name_exam:
		return False
		sofpos = file_pos[:test_pos] + "02-Output\\Vfx\\sof\\"
		if os.path.exists(sofpos.decode("utf-8")):
			return sofpos
	if name_exam:
		project_name = name_exam.group(0).split('\\')[0]
		sofpos = "\\\\192.168.100.249\\myway-projects\\" + project_name + "\\02-Output\\vfx\\sof\\"
		if os.path.exists(sofpos):
			return sofpos
	return False

def sof_generate_save_pos(file_inpath, sof_path):
	"""
	file_inpath: current max file place.
	sof_path:    current detected sof save path.
	"""
	word_end_index = file_inpath.find("cam\\")
	word_end = file_inpath[word_end_index + 4:]
	sof_think_path = sof_path + word_end
	decode_path = sof_think_path
	if os.path.exists(decode_path) :
		return sof_think_path
	else:
		return sof_path


def sof_save_sof(sofFileLocation, selected, file_name):
	sofFileLocation = sofFileLocation + file_name[:-4] + '.sof'
	sofFileLocation_decode = sofFileLocation
	print(sofFileLocation_decode)
	stateSetsDotNetObject = rt.dotNetObject("Autodesk.Max.StateSets.Plugin")
	stateSets = stateSetsDotNetObject.Instance
	masterState = stateSets.EntityManager.RootEntity.MasterStateSet
	rt.select(selected)
	masterState.ObjectStateSet.AddSelectedSceneNodesToObjectState()
	stateSets.CompositorLink.LinkFilePath = sofFileLocation
	stateSets.CompositorLink.UpdateToLink()
	masterState.ObjectStateSet.Reset()
	stateSets.CompositorLink.ResetLink()
	return sofFileLocation_decode



class SofSelectTest:
	def __init__(self, selection):
		self.selected = [i for i in selection]
		self.islegal = self.test_select()
	
	def __s_test(self):
		'''
		test if the selection is none
		'''
		if self.selected:
			return True
		else:
			return False
	
	def __s_frozen_test(self):
		f_list = [not(i.isFrozen) for i in self.selected]
		if all(f_list):
			return True
		else:
			return False


	def __s_class_test(self):
		'''
		ensure the selection is in right classes
		'''
		c_set = set([str(rt.classOf(i)) for i in self.selected])
		test_standard = {"Omnilight", "Plane", "Point", "Targetobject", "Targetcamera"}
		if c_set <= test_standard:
			self.legal = True
			return True
		else:
			return False
	
	def test_select(self):
		return self.__s_test() and self.__s_class_test() and self.__s_frozen_test()


class SofContextState(object):
	def __init__(self, selection):
		self.G_state = rt.hideByCategory.geometry
		self.H_state = rt.hideByCategory.helpers
		self.L_state = rt.hideByCategory.lights
		self.C_state = rt.hideByCategory.cameras
		self.selected = [i for i in selection]
		self.selected_node_state = [i.isNodeHidden for i in self.selected]
		self.selected_layer_state = [j.INodeLayerProperties.layer.isHidden for j in self.selected]
		self.selected_layer_on_state = [k.INodeLayerProperties.layer.on for k in self.selected]
	
	def __enter__(self):
		self.__open()
		return "go enter"
	
	def __exit__(self, exc_type, exc_val, exc_tb):
		'''
		throw error continue
		'''
		self.__restore()
		return False
	
	def __restore(self):
		rt.hideByCategory.geometry = self.G_state
		rt.hideByCategory.helpers = self.H_state
		rt.hideByCategory.lights = self.L_state
		rt.hideByCategory.cameras = self.C_state
		
		for i,k in zip(self.selected, self.selected_node_state):
			i.isNodeHidden = k
		
		for m,n in zip(self.selected, self.selected_layer_state):
			m.INodeLayerProperties.layer.isHidden = n
			
		for x,y in zip(self.selected, self.selected_layer_on_state):
			x.INodeLayerProperties.layer.on = y
		
		rt.redrawViews()
			
	
	def __open(self):
		rt.hideByCategory.geometry = False
		rt.hideByCategory.helpers = False
		rt.hideByCategory.lights = False
		rt.hideByCategory.cameras = False
		
		for i,k in zip(self.selected, [not bool(t) for t in self.selected]):
			i.isNodeHidden = k
			
		for m,n in zip(self.selected, [not bool(s) for s in self.selected]):
			m.INodeLayerProperties.layer.isHidden = n
		
		for x,y in zip(self.selected, [bool(s) for s in self.selected]):
			x.INodeLayerProperties.layer.on = y
		
		rt.redrawViews()
def message(main_window, sofexported):
    message = QMessageBox()
    text = "Export Succeed!, file at:\n" + sofexported
    message.information(main_window, "sof Export", text)

def sof_do_save(selected, file_name, file_pos, main_window):
	project_judge = sof_project_test(file_pos)
	if project_judge:
		save_pos = sof_generate_save_pos(file_pos, project_judge)
		sofexported = sof_save_sof(save_pos, selected, file_name)
		message(main_window, sofexported)


def sof_save_main(main_window):
	file_name = rt.maxFileName
	file_pos = rt.maxFilePath
	current_selected = rt.getCurrentSelection()
	test = SofSelectTest(current_selected)
	if test.islegal:
		with SofContextState(current_selected) as f:
			sof_do_save(current_selected, file_name, file_pos, main_window)
	rt.select(current_selected)

if __name__ == "__main__":
	from qtmax import GetQMaxMainWindow
	main_window = GetQMaxMainWindow()
	sof_save_main(main_window)
