import PySimpleGUI as sg
import sys
from datetime import datetime
import os
from pathlib import Path
import traceback


fext = ''

def write():
    now = datetime.now()
    date = now.strftime("%m/%d/%y %H:%M")
    
    if values['-Name-']=='' or values['-Station-']=='' or values['-Slot-']=='' or values['-FailCode-']=='' or values['-FixDescription-']=='' or values['-file-']=='':
        sg.Popup('Error. Missing file or input.',title = 'Error',auto_close = True,auto_close_duration = 10)

    elif os.stat(values['-file-']).st_size == 0:
        outfile = open(values['-file-'], 'a')
        outfile.write("Name" +';')
        outfile.write("Station" +';')
        outfile.write("Slot" +';')
        outfile.write("Fail Code" +';')
        outfile.write("Fix Description" +';')
        outfile.write("Date" + "\n")   
        outfile.write(values['-Name-']+';')
        outfile.write(values['-Station-']+';')
        outfile.write(values['-Slot-']+';')
        outfile.write(values['-FailCode-']+';')
        outfile.write(values['-FixDescription-']+';')
        outfile.write(date + "\n")
        window['-Name-']('')
        window['-Station-']('')
        window['-Slot-']('')
        window['-FailCode-']('')
        window['-FixDescription-']('')
        sg.Popup('Done',title = 'Success',auto_close = True,auto_close_duration = 0.5)
        window['-Name-'].SetFocus(force = True)
        outfile.close()
    elif os.stat(values['-file-']).st_size >= 1: 
        outfile = open(values['-file-'], 'a')   
        outfile.write(values['-Name-']+';')
        outfile.write(values['-Station-']+';')
        outfile.write(values['-Slot-']+';')
        outfile.write(values['-FailCode-']+';')
        outfile.write(values['-FixDescription-']+';')
        outfile.write(date + "\n")
        window['-Name-']('')
        window['-Station-']('')
        window['-Slot-']('')
        window['-FailCode-']('')
        window['-FixDescription-']('')
        sg.Popup('Done',title = 'Success',auto_close = True,auto_close_duration = 0.5)
        window['-Name-'].SetFocus(force = True)
        outfile.close()
          
    

def convert():
    p = Path(values['-file-'])
    p.rename(p.with_suffix(fext))
    window['-file-']('')
    sg.Popup('Done. Select file again',title = 'Success',auto_close = True,auto_close_duration = 4)

# ------ Menu Definition ------ #
menu_def = [['&File', ['&Open']],
            ['&Convert', ['.txt', '.csv'],]]
            

layout = [
    [sg.Menu(menu_def)],
    [sg.Text('Selected File', size=(15, 1)),sg.In(readonly=True,key='-file-'),],

    [sg.Text('')],
    [sg.Text('Name', size=(15, 1)),sg.InputText(key='-Name-')],
    [sg.Text('Station', size=(15, 1)),sg.InputText(key='-Station-')],
    [sg.Text('Slot', size=(15, 1)),sg.InputText(key='-Slot-')],
    [sg.Text('Fail Code', size=(15, 1)),sg.InputText(key='-FailCode-')],
    [sg.Text('Fix Description', size=(15, 1)),sg.InputText(key='-FixDescription-')],
    [sg.Button('Submit',bind_return_key=True,key='-Submit-')],

]


window = sg.Window('Troubleshoot Data Export', layout, size=(500,235),use_default_focus=False,finalize=True)

window['-file-'].block_focus(block = True)
window['-Submit-'].block_focus(block = True)

try:
    while True:
      event, values = window.read()
      if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
           break
      if event == '-Submit-':
           write()
      if event == '.txt':
           fext = '.txt'
           convert()
      if event == '.csv':
           fext = '.csv'
           convert()
      if event == 'Open':
           window['-file-'](sg.popup_get_file(message='Select File'))
          

except Exception as e:
    tb = traceback.format_exc()
    #sg.Print(f'An error happened.  Here is the info:', e, tb)
    sg.popup_error(f'MISSING VALUE / INPUT', e, tb)
    

window.close()