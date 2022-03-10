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
    outfile = open(values['-file-'], 'a')
    if os.stat(values['-file-']).st_size == 0:
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
    window.refresh
    
    
        
    outfile.close()

def convert():
    p = Path(values['-file-'])
    p.rename(p.with_suffix(fext))
    window['-file-']('')
    sg.Popup('Done. Select file again',title = 'Success',auto_close = True,auto_close_duration = 4)


layout = [
    [sg.Text('Select File'),sg.In(readonly=True,key='-file-'), sg.FileBrowse(key='-Browse-'),],

    [sg.Text('')],
    [sg.Text('Name', size=(15, 1)),sg.InputText(key='-Name-')],
    [sg.Text('Station', size=(15, 1)),sg.InputText(key='-Station-')],
    [sg.Text('Slot', size=(15, 1)),sg.InputText(key='-Slot-')],
    [sg.Text('Fail Code', size=(15, 1)),sg.InputText(key='-FailCode-')],
    [sg.Text('Fix Description', size=(15, 1)),sg.InputText(key='-FixDescription-')],
    [sg.Button('Submit',bind_return_key=True,key='-Submit-')],

    [sg.Text('_______________')],
    [sg.Text('File Options')],
    [sg.Radio('txt', "RADIO1", default=True,key='-txt-')],
    [sg.Radio('csv', "RADIO1",key='-csv-')],
    [sg.Button('Convert',key='-Convert-')]

]

window = sg.Window('Troubleshoot Data Export', layout, size=(500,400),use_default_focus=False,finalize=True)

window['-file-'].block_focus(block = True)
window['-Browse-'].block_focus(block = True)
window['-Submit-'].block_focus(block = True)
window['-txt-'].block_focus(block = True)
window['-csv-'].block_focus(block = True)
window['-Convert-'].block_focus(block = True)

try:
    while True:
      event, values = window.read()
      if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
           break
      if event == '-Submit-':
           write()
      if values['-txt-'] == True:
           fext = '.txt'
      if values['-csv-'] == True:
           fext = '.csv'
      if event == '-Convert-':
           convert()
except Exception as e:
    tb = traceback.format_exc()
    #sg.Print(f'An error happened.  Here is the info:', e, tb)
    sg.popup_error(f'MISSING VALUE / INPUT', e, tb)
    

window.close()