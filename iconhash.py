import os
import re
import mmh3
import codecs
import base64
import requests
import tkinter as tk


def icon_file_hash(file_path):
    icon_file = open(file_path, 'rb')
    favicon_hash = mmh3.hash(codecs.lookup(
        'base64').encode(icon_file.read())[0])
    icon_file.close()
    return favicon_hash


def url_hash(url_path):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'}
    try:
        favicon_response = requests.get(url_path, headers=headers)
        if favicon_response.status_code == 200:
            favicon_hash = mmh3.hash(codecs.lookup(
                'base64').encode(favicon_response.content)[0])
            output_data_01.set('icon_hash="{}"'.format(favicon_hash))
            output_data_02.set('icohash:"{}"'.format(favicon_hash))
            output_data_03.set('http.favicon.hash:"{}"'.format(favicon_hash))
            message.set('')
        else:
            output_data_01.set('')
            output_data_02.set('')
            output_data_03.set('')
            message.set('message：url request failed')
    except requests.exceptions.ConnectionError:
        output_data_01.set('')
        output_data_02.set('')
        output_data_03.set('')
        message.set('Connection error !')
    except:
        output_data_01.set('')
        output_data_02.set('')
        output_data_03.set('')
        message.set('Connection error !')


def calculate():
    input_data_get = input_data.get()
    if input_data_get == '':
        output_data_01.set('')
        output_data_02.set('')
        output_data_03.set('')
        message.set('message：Please enter the icon file path or url !')
    elif input_data_get[-3:] == 'ico':
        if os.path.exists(input_data_get):
            favicon_hash = icon_file_hash(input_data_get)
            output_data_01.set('icon_hash="{}"'.format(favicon_hash))
            output_data_02.set('icohash:"{}"'.format(favicon_hash))
            output_data_03.set('http.favicon.hash:"{}"'.format(favicon_hash))
            message.set('')
        elif re.match(r'^http(s)?:/{2}\w.+$', input_data_get):
            url_hash(input_data_get)
        else:
            output_data_01.set('')
            output_data_02.set('')
            output_data_03.set('')
            message.set('message：Please enter the icon file path or url !')

    else:
        output_data_01.set('')
        output_data_02.set('')
        output_data_03.set('')
        message.set('message：Please enter the icon file path or url !')


root = tk.Tk()
root.geometry("800x210")
root.resizable(width=False, height=False)
root.title('iconhash calculator     By:0x4thk')
tmp = open("tmp.ico","wb+")
tmp.write(base64.b64decode('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'))
tmp.close()
root.iconbitmap("tmp.ico")
os.remove("tmp.ico")

input_data = tk.StringVar()
output_data_01 = tk.StringVar()
output_data_02 = tk.StringVar()
output_data_03 = tk.StringVar()
message = tk.StringVar()

label_01 = tk.Label(root, text="url or path")
label_01.place(x=10, y=10)

label_02 = tk.Label(root, text="fofa")
label_02.place(x=10, y=50)

label_03 = tk.Label(root, text="sumap")
label_03.place(x=10, y=80)

label_04 = tk.Label(root, text="shodan")
label_04.place(x=10, y=110)

input_entry = tk.Entry(root, textvariable=input_data)
input_entry.place(x=100, y=12, width=687)

output_entry_01 = tk.Entry(root, textvariable=output_data_01)
output_entry_01.place(x=100, y=50, width=687)

output_entry_02 = tk.Entry(root, textvariable=output_data_02)
output_entry_02.place(x=100, y=80, width=687)

output_entry_03 = tk.Entry(root, textvariable=output_data_03)
output_entry_03.place(x=100, y=110, width=687)

message_label = tk.Label(root, textvariable=message)
message_label.place(x=98, y=140)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.place(x=12, y=165, width=360)

quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.place(x=415, y=165, width=373)

root.mainloop()
