'''
@File    :   cleanMaterial.py
@Time    :   2019/09/02 12:25:55
@Author  :   William Smith 
@Version :   1.0
@Contact :   lifeyf@hotmail.com
@License :   Copyright @ 2022 <William Smith>
'''

from pymxs import runtime as rt

def clean_material_main():
    if rt.sme.getview(1):
        pass
    else:
        rt.sme.open()
        rt.sme.close()
    
    c_sme = rt.sme.getview(1)
    c_sme.selectall()
    c_sme.deleteselection()

    rt.MatEditor.mode = rt.name('basic')
    rt.MatEditor.Open()
    rt.macros.run("Medit Tools", "clear_medit_slots")
    rt.MatEditor.Close()
    rt.MatEditor.mode = rt.name('advanced')

    rt.macros.run("Medit Tools", "clear_medit_slots")
    rt.atsops.refresh()
    print('Cleaned!')

if __name__ == "__main__":
    clean_material_main()