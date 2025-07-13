# This code is generated using PyUIbuilder: https://pyuibuilder.com

import os
import tkinter as tk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

firstlineantisuggestmain = tk.Tk()
firstlineantisuggestmain.title("First line anti suggest")
firstlineantisuggestmain.config(bg="#E4E2E2")
firstlineantisuggestmain.geometry("718x507")

startsuggest = tk.Button(master=firstlineantisuggestmain, text="Check")
startsuggest.config(bg="#dedede", fg="#000")
startsuggest.place(x=23, y=401, height=40)

restart = tk.Button(master=firstlineantisuggestmain, text="Restart")
restart.config(bg="#E4E2E2", fg="#000")
restart.place(x=155, y=401, height=40)
#按下restart按鈕時，會清除所有選項
def restart_action():
    skincheckbox.deselect()
    pnuemoniacheckbox.deselect()
    uticheckbox.deselect()
    iaicheckbox.deselect()
    jointcheckbox.deselect()
    tissuecheckbox.deselect()
    heartcheckbox.deselect()
    meningitischeckbox.deselect()
    mrsacheckbox.deselect()
    vrsavrecheckbox.deselect()
    pnemoniaradiobutton_var.set(0)

#skincheckbox 預設是未選中
#pnuemoniacheckbox 預設是未選中
#uticheckbox 預設是未選中
#iaicheckbox 預設是未選中
#jointcheckbox 預設是未選中
#tissuecheckbox 預設是未選中
#heartcheckbox 預設是未選中
#meningitischeckbox 預設是未選中
#mrsacheckbox 預設是未選中
#vrsavrecheckbox 預設是未選中
#pnemoniaradiobutton_var 預設是0
#pnemoniaradiobutton_0 預設是選中
#pnemoniaradiobutton_1 預設是未選中
#pnemoniaradiobutton_2 預設是未選中
#pnemoniaradiobutton_3 預設是未選中


skincheckbox = tk.Checkbutton(master=firstlineantisuggestmain, text="Skin")
skincheckbox = tk.Checkbutton(master=firstlineantisuggestmain, text="Skin")
skincheckbox.config(bg="#E4E2E2", fg="#000")
skincheckbox.deselect()


pnuemoniacheckbox = tk.Checkbutton(master=firstlineantisuggestmain, text="Pnuemonia")
pnuemoniacheckbox.config(bg="#E4E2E2", fg="#000")
pnuemoniacheckbox.deselect()


pnemoniaradiobutton_var = tk.IntVar()

pnemoniaradiobutton_0 = tk.Radiobutton(master=firstlineantisuggestmain, variable=pnemoniaradiobutton_var, text="CAP")
pnemoniaradiobutton_0.config(bg="#E4E2E2", fg="#000", value=0)
pnemoniaradiobutton_0.place(x=45, y=70)
pnemoniaradiobutton_1 = tk.Radiobutton(master=firstlineantisuggestmain, variable=pnemoniaradiobutton_var, text="HAP")
pnemoniaradiobutton_1.config(bg="#E4E2E2", fg="#000", value=1)
pnemoniaradiobutton_1.place(x=45, y=90)
pnemoniaradiobutton_2 = tk.Radiobutton(master=firstlineantisuggestmain, variable=pnemoniaradiobutton_var, text="VAP")
pnemoniaradiobutton_2.config(bg="#E4E2E2", fg="#000", value=2)
pnemoniaradiobutton_2.place(x=45, y=110)
pnemoniaradiobutton_3 = tk.Radiobutton(master=firstlineantisuggestmain, variable=pnemoniaradiobutton_var, text="Children")
pnemoniaradiobutton_3.config(bg="#E4E2E2", fg="#000", value=3)
pnemoniaradiobutton_3.place(x=45, y=130)

uticheckbox = tk.Checkbutton(master=firstlineantisuggestmain, text="UTI")
uticheckbox.config(bg="#E4E2E2", fg="#000")
uticheckbox.deselect()


iaicheckbox = tk.Checkbutton(master=firstlineantisuggestmain, text="IAI")
iaicheckbox.config(bg="#E4E2E2", fg="#000")
iaicheckbox.deselect()


jointcheckbox = tk.Checkbutton(master=firstlineantisuggestmain, text="Joint")
jointcheckbox.config(bg="#E4E2E2", fg="#000")
jointcheckbox.deselect()


tissuecheckbox = tk.Checkbutton(master=firstlineantisuggestmain, text="Tissue")
tissuecheckbox.config(bg="#E4E2E2", fg="#000")
tissuecheckbox.deselect()


heartcheckbox = tk.Checkbutton(master=firstlineantisuggestmain, text="Heart")
heartcheckbox.config(bg="#E4E2E2", fg="#000")
heartcheckbox.deselect()


meningitischeckbox = tk.Checkbutton(master=firstlineantisuggestmain, text="Meningitis")
meningitischeckbox.config(bg="#E4E2E2", fg="#000")
meningitischeckbox.deselect()


mrsacheckbox = tk.Checkbutton(master=firstlineantisuggestmain, text="MRSA")
mrsacheckbox.config(bg="#E4E2E2", fg="#000")
mrsacheckbox.deselect()


vrsavrecheckbox = tk.Checkbutton(master=firstlineantisuggestmain, text="VRSA/VRE")
vrsavrecheckbox.config(bg="#E4E2E2", fg="#000")

#Checkbox positioning and layout
# The checkboxes and radiobuttons are placed in a grid-like manner
"""
pneumoniacheckbox, uticheckbox, iaicheckbox,  skincheckbox,tissuecheckbox在畫面中左邊第一個colum
pneumoniaradiobutton_0, pnemoniaradiobutton_1, pnemoniaradiobutton_2, pnemoniaradiobutton_3 在pneumoniacheckbox的下方
pnemoniaradiobutton_var 預設是0，表示pnemoniaradiobutton_0被選中
jointcheckbox,heartcheckbox, meningitischeckbox, mrsacheckbox, vrsavrecheckbox 在畫面中第二個colum
"""
pnuemoniacheckbox.place(x=23, y=30, width=120, height=30)
pnemoniaradiobutton_0.place(x=45, y=70)
pnemoniaradiobutton_1.place(x=45, y=90)
pnemoniaradiobutton_2.place(x=45, y=110)
pnemoniaradiobutton_3.place(x=45, y=130)
uticheckbox.place(x=23, y=170, width=120, height=30)
iaicheckbox.place(x=23, y=210, width=120, height=30)
skincheckbox.place(x=23, y=250, width=120, height=30)
jointcheckbox.place(x=175, y=30, width=120, height=30)
tissuecheckbox.place(x=175, y=70, width=120, height=30)
heartcheckbox.place(x=175, y=110, width=120, height=30) 
meningitischeckbox.place(x=175, y=150, width=120, height=30)
mrsacheckbox.place(x=175, y=190, width=120, height=30)
vrsavrecheckbox.place(x=175, y=230, width=120, height=30)



vrsavrecheckbox.deselect()


text = tk.Text(master=firstlineantisuggestmain)
text.config(bg="#fff", fg="#000")
text.place(x=455, y=6, width=241, height=464)


firstlineantisuggestmain.mainloop()