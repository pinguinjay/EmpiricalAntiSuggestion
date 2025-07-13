# This code is generated using PyUIbuilder: https://pyuibuilder.com

import os
import tkinter as tk
import TextSuggestion as TextSugg


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

firstlineantisuggestmain = tk.Tk()
firstlineantisuggestmain.title("First line anti suggest")
firstlineantisuggestmain.config(bg="#E4E2E2")
firstlineantisuggestmain.geometry("718x507")

startsuggest = tk.Button(master=firstlineantisuggestmain, text="Check")
startsuggest.config(bg="#dedede", fg="#000")
startsuggest.place(x=23, y=401, height=40)

#當按下startsuggest按鈕時，會顯示選中的checkbox的建議
def startsuggest_action():
    selected_checkbox = get_selected_checkbox()
    suggestion = TextSugg.SuggestionKey[selected_checkbox]
    text.delete(1.0, tk.END)  # Clear previous text
    text.insert(tk.END, suggestion)  # Insert new suggestion
startsuggest.config(command=startsuggest_action)

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
restart.config(command=restart_action)

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


skincheckbox_var = tk.BooleanVar()
skincheckbox = tk.Checkbutton(master=firstlineantisuggestmain, text="Skin", variable=skincheckbox_var)
skincheckbox.config(bg="#E4E2E2", fg="#000")
skincheckbox.deselect()

pnuemoniacheckbox_var = tk.BooleanVar()
pnuemoniacheckbox = tk.Checkbutton(master=firstlineantisuggestmain, text="Pnuemonia", variable=pnuemoniacheckbox_var)
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

uticheckbox_var = tk.BooleanVar()
uticheckbox = tk.Checkbutton(master=firstlineantisuggestmain, text="UTI", variable=uticheckbox_var)
uticheckbox.config(bg="#E4E2E2", fg="#000")
uticheckbox.deselect()

iaicheckbox_var = tk.BooleanVar()
iaicheckbox = tk.Checkbutton(master=firstlineantisuggestmain, text="IAI", variable=iaicheckbox_var)
iaicheckbox.config(bg="#E4E2E2", fg="#000")
iaicheckbox.deselect()

jointcheckbox_var = tk.BooleanVar()
jointcheckbox = tk.Checkbutton(master=firstlineantisuggestmain, text="Joint", variable=jointcheckbox_var)
jointcheckbox.config(bg="#E4E2E2", fg="#000")
jointcheckbox.deselect()

tissuecheckbox_var = tk.BooleanVar()
tissuecheckbox = tk.Checkbutton(master=firstlineantisuggestmain, text="Tissue", variable=tissuecheckbox_var)
tissuecheckbox.config(bg="#E4E2E2", fg="#000")
tissuecheckbox.deselect()

heartcheckbox_var = tk.BooleanVar()
heartcheckbox = tk.Checkbutton(master=firstlineantisuggestmain, text="Heart", variable=heartcheckbox_var)
heartcheckbox.config(bg="#E4E2E2", fg="#000")
heartcheckbox.deselect()

meningitischeckbox_var = tk.BooleanVar()
meningitischeckbox = tk.Checkbutton(master=firstlineantisuggestmain, text="Meningitis", variable=meningitischeckbox_var)
meningitischeckbox.config(bg="#E4E2E2", fg="#000")
meningitischeckbox.deselect()

mrsacheckbox_var = tk.BooleanVar()
mrsacheckbox = tk.Checkbutton(master=firstlineantisuggestmain, text="MRSA", variable=mrsacheckbox_var)
mrsacheckbox.config(bg="#E4E2E2", fg="#000")
mrsacheckbox.deselect()

vrsavrecheckbox_var = tk.BooleanVar()
vrsavrecheckbox = tk.Checkbutton(master=firstlineantisuggestmain, text="VRSA/VRE", variable=vrsavrecheckbox_var)
vrsavrecheckbox.config(bg="#E4E2E2", fg="#000")
vrsavrecheckbox.deselect()
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

def get_selected_checkbox():
    if skincheckbox_var.get():
        return "Skin"      
    elif uticheckbox_var.get():
        return "UTI"
    elif iaicheckbox_var.get():
        return "IAI"
    elif jointcheckbox_var.get():
        return "Joint"
    elif tissuecheckbox_var.get():
        return "Tissue"
    elif heartcheckbox_var.get():
        return "Heart"
    elif meningitischeckbox_var.get():
        return "Meningitis"
    elif mrsacheckbox_var.get():
        return "MRSA"
    elif vrsavrecheckbox_var.get():
        return "VRSA/VRE"
    elif pnuemoniacheckbox_var.get():
        if pnemoniaradiobutton_var.get() == 0:
            return "CAP"
        elif pnemoniaradiobutton_var.get() == 1:
            return "HAP"
        elif pnemoniaradiobutton_var.get() == 2:
            return "VAP"
        elif pnemoniaradiobutton_var.get() == 3:
            return "Children"
    else:
        return None






text = tk.Text(master=firstlineantisuggestmain)
text.config(bg="#fff", fg="#000")
text.place(x=455, y=6, width=241, height=464)


firstlineantisuggestmain.mainloop()