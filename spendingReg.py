import PySimpleGUI as sg
import pandas as pd

import spendingRegFunc


sg.theme('Dark')
topics = ['ID','NAME','QUANT.','SELLER','VALUE','DATE']
layout = [
    [sg.Text('')],
    [sg.Text('NAME'),sg.Input(key='-NAME-')],
    [sg.Text('QUANT.'),sg.Input(key='-QUANT-')],
    [sg.Text('SELLER'),sg.Input(key='-SELLER-')],
    [sg.Text('VALUE'),sg.Input(key='-VALUE-')],
    [sg.Text('DATE'),sg.Input(key='-DATE-')],
    [sg.Button('ADD'),sg.Button('DOWNLOAD')],
    [sg.Button('UPDATE'), sg.Button('DELETE')],
    [sg.Table(values=[], headings=topics, size=(30, 5), key='-TABLE-')]
]
data_list = []

#######################################################################################################################################

class listGetterSetter:
    def __init__ (self,data_list,window):
        self._data_list=data_list
        self._name =''
        self._quant=''
        self._seller=''
        self._value=''
        self._date=''
        self._window=window
        
    def set_list(self, name='', quant=0, seller='', value=0, date=''):
        self._name=name
        self._quant=quant
        self._seller=seller
        self._value=value
        self._date=date
                
    def gui_start(self):
        while True:
            event, values = self._window.read()

            if event == sg.WIN_CLOSED:
                break

            if event == 'ADD':
                self.set_list(values['-NAME-'],
                                values['-QUANT-'],
                                values['-SELLER-'],
                                values['-VALUE-'],
                                values['-DATE-'])
                # 
                self._data_list.append((self._name, self._quant, self._seller, self._value, self._date))
                self._window['-TABLE-'].update(values=self._data_list)
                spendingRegFunc.addBuyedItems(self._name, self._quant, self._seller, self._value, self._date)
                self._window['-NAME-'].update('')
                self._window['-QUANT-'].update('')
                self._window['-SELLER-'].update('')
                self._window['-VALUE-'].update('')
                self._window['-DATE-'].update('')

            elif event=='UPDATE':
                updatedList=spendingRegFunc.listTable()
                self._window['-TABLE-'].update(
                    values=updatedList)
                
            elif event=='DELETE':   
                try:
                    index=values["-TABLE-"][0]

                    list=self._window['-TABLE-'].get()
                    id=list[index][0]
                    spendingRegFunc.delBuyedItems(id)

                    updatedList=spendingRegFunc.listTable()
                    self._window['-TABLE-'].update(
                        values=updatedList)                    
                except Exception as e:
                    sg.popup("You should choose a row")
                    
            elif event == 'DOWNLOAD':
                list=self._window['-TABLE-'].get()
                list_df = pd.DataFrame(list)
                header_mapping = {0: 'ID', 1: 'NAME', 2: 'QUANT', 3: 'SELLER', 4: 'VALUE', 5: 'DATE'}
                list_df = list_df.rename(columns=header_mapping)
                if list_df.shape[0] > 0:
                    file_path = sg.popup_get_file('Save As', save_as=True, file_types=(("Comma Separated Values", "*.csv"),))
                    if file_path:
                        csv_string = list_df.to_csv(index=False)

                        with open(file_path, 'w') as file:
                            file.write(csv_string)
                        sg.popup(f"Data saved to {file_path}", title='Download Complete', keep_on_top=True)
                    else:
                        sg.popup('No data to download', title='-WARNING-', keep_on_top=True)

        self._window.close()
                     
#######################################################################################################################################

new_window=sg.Window('SPENDING REGISTRY',layout,finalize=True)

app = listGetterSetter(data_list,new_window)
app.gui_start()