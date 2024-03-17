import os,re
from pymxs import runtime as rt
vr = rt.Renderers.current

vr_inspect =  str(vr)[0:7] == 'V_Ray_5'

def doname():
	#todo: folder name include special str, seems not?
	#      do the cam file in the cam folder?

	folder_name = rt.maxFilePath.encode('utf-8')
	file_name = rt.maxFileName.encode('utf-8')


	name_exam = re.search(r"\d+-+[a-zA-Z]+-+[a-zA-Z]+-+.+\\?", str(folder_name))
	if name_exam:
		project_name = name_exam.group(0).split('\\')[0]
		result_folder = "\\\\192.168.100.249\\myway-projects\\" + project_name + "\\02-Output\\3D\\3D-render\\"
		result_name = file_name[:-4]
		finall_folder = result_folder + result_name
		finall_file = result_folder + result_name + '\\' + result_name + '_.png'

		try:
			# ����ļ��в������򴴽����ļ���
			if not os.path.exists(finall_folder.decode('utf-8')):
				os.makedirs(finall_folder.decode('utf-8'))
				print("Dir Created")
			else:
				print('Dir Already Existed')
			return finall_file
		except OSError as e:
			print("cant create folder:", str(e))

def seting():
	vfb = rt.vfbControl
	vfbSee = rt.name('show')
	vfbTestRes = rt.name('testresolution')
	vfbRegion = rt.name('setregion')

	rt.renderSceneDialog.close()
	#### begain ####
	rt.vfbControl(vfbTestRes, False)
	rt.vfbControl(vfbTestRes, False)
	rt.vfbControl(vfbRegion, 'reset')
	rt.vfbControl(vfbSee, False)
	

	rt.rendTimeType = 2
	rt.rendSaveFile = False #close 3dsmax save file option box.

	vr.output_splitgbuffer = True
	vr.output_separateFolders = True
	vr.output_expandFrameNumber = False
	vr.output_splitfilename = doname()

	vr.twoLevel_baseSubdivs =1
	vr.twoLevel_fineSubdivs =6
	vr.twoLevel_threshold = 0.01

	vr.lightmap_preset = 1 #the first preset,Different From MAX
	vr.lightcache_subdivs = 1000

	#### end ####
	rt.renderSceneDialog.open()
if vr_inspect :
	seting()
else:
	print("NotVray")

