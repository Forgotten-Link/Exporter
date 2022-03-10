import PySimpleGUI as sg
import sys
from datetime import date
import os
from pathlib import Path
import traceback

today = date.today()
date = today.strftime("%m/%d/%y")
fext = ''

def write():
    outfile = open(values['-file-'], 'a')
    if os.stat(values['-file-']).st_size == 0:
        outfile.write("Name" +',')
        outfile.write("Chamber" +',')
        outfile.write("Slot" +',')
        outfile.write("Fail Code" +',')
        outfile.write("Fix Description" +',')
        outfile.write("Date" + "\n")
        
    outfile.write(values['-Name-']+',')
    outfile.write(values['-Chamber-']+',')
    outfile.write(values['-Slot-']+',')
    outfile.write(values['-FailCode-']+',')
    outfile.write(values['-FixDescription-']+',')
    outfile.write(date + "\n")
    window['-Name-']('')
    window['-Chamber-']('')
    window['-Slot-']('')
    window['-FailCode-']('')
    window['-FixDescription-']('')
    sg.Popup('Done',title = 'Success',auto_close = True,auto_close_duration = 1)
        
    outfile.close()
def convert():
    p = Path(values['-file-'])
    p.rename(p.with_suffix(fext))
    window['-file-']('')
    sg.Popup('Done. Select file again',title = 'Success',auto_close = True,auto_close_duration = 6)


layout = [
    [sg.Text('Select File'),sg.In(readonly=True,key='-file-'), sg.FileBrowse()],

    [sg.Text('')],
    [sg.Text('Name', size=(15, 1)),sg.InputText(key='-Name-')],
    [sg.Text('Chamber', size=(15, 1)),sg.InputText(key='-Chamber-')],
    [sg.Text('Slot', size=(15, 1)),sg.InputText(key='-Slot-')],
    [sg.Text('Fail Code', size=(15, 1)),sg.InputText(key='-FailCode-')],
    [sg.Text('Fix Description', size=(15, 1)),sg.InputText(key='-FixDescription-')],
    [sg.Button('Submit')],


    [sg.Text('_______________')],
    [sg.Text('File Options')],
    [sg.Radio('txt', "RADIO1", default=True,key='-txt-')],
    [sg.Radio('csv', "RADIO1",key='-csv-')],
    [sg.Button('Convert')]

]

window = sg.Window('Data Export', layout, size=(600,400))

try:
    while True:
      event, values = window.read()
      if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
           break
      if event == 'Submit':
           write()
      if values['-txt-'] == True:
           fext = '.txt'
      if values['-csv-'] == True:
           fext = '.csv'
      if event == 'Convert':
           convert()
except Exception as e:
    tb = traceback.format_exc()
    #sg.Print(f'An error happened.  Here is the info:', e, tb)
    sg.popup_error(f'MISSING VALUE / INPUT', e, tb)
    

window.close()