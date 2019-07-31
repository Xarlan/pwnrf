# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import tkinter as tk
from tkinter import ttk
import serial
import glob
import sys

ZIGBEE_LAYER        = ['MAC', 'NWK', 'APS']
ZIGBEE_MAC_TYPE     = ['Beacon', 'Data', 'Ack', 'MAC Cmd']


class AppPwnRf:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Pwn 2.4 Ghz")

        self.notebook_rf = ttk.Notebook(self.parent)
        self.nb_zigbee  = ttk.Frame(self.notebook_rf)
        self.nb_wifi = ttk.Frame(self.notebook_rf)
        self.nb_settings = ttk.Frame(self.notebook_rf)

        self.notebook_rf.add(self.nb_zigbee, text='Zigbee')
        self.notebook_rf.add(self.nb_wifi, text='WiFi')
        self.notebook_rf.add(self.nb_settings, text='Settings')
        self.notebook_rf.grid(row=2, padx=10, pady=10)

        self.zigbee_layer_l = tk.Label(self.nb_zigbee, text='Zigbee layer')
        self.zigbee_layer_l.grid(padx=5, pady=5, sticky='w')

        self.zigbee_layer_combo = ttk.Combobox(self.nb_zigbee, value=ZIGBEE_LAYER)
        self.zigbee_layer_combo.grid(row=1, padx=5, pady=5)
        self.zigbee_layer_combo.bind("<<ComboboxSelected>>", self.__set_zigbee_mac_type, '+')

        self.combo_zigbee_mac_type = ttk.Combobox(self.nb_zigbee, value=ZIGBEE_MAC_TYPE)
        self.combo_zigbee_mac_type.grid(row=1, column=1, padx=5)

        self.l_raw_pkt = ttk.Label(self.parent, text="Raw packet:")
        self.l_raw_pkt.grid(row=3, padx=10, sticky='w')
        self.entry_raw_pkt = ttk.Entry(self.parent)
        self.entry_raw_pkt.grid(row=4, padx=10, sticky='we')

        self.bttn_send = ttk.Button(self.parent, text='Send')
        self.bttn_send.grid(row=4, column=2)


        ### Tab Settings ###
        self.l_tty = ttk.Label(self.nb_settings, text='tty')
        self.l_tty.grid(row=0, padx=10, pady=5, sticky='w')
        self.combo_tty = ttk.Combobox(self.nb_settings, value=self.__get_serial_port())
        self.combo_tty.grid(row=1, padx=10)

    @staticmethod
    def __get_serial_port():
        ports = []
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]

        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            ports = glob.glob('/dev/tty[A-Za-z]*')

        available_tty = []
        for item in ports:
            try:
                s = serial.Serial(item)
                s.close()
                available_tty.append(item)
            except serial.SerialException:
                pass

            return available_tty

    def __set_zigbee_mac_type(self, event):
        current_mac_type = event.widget.get()
        print(current_mac_type)
        self.__show_mac_type()

    def __show_mac_type(self):
        print(self.nb_zigbee.winfo_children())


def main():
    root = tk.Tk()
    AppPwnRf(root)
    root.mainloop()


if __name__ == '__main__':
    main()
