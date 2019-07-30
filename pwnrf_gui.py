# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import tkinter as tk
from tkinter import ttk


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
        self.zigbee_layer_l.grid(pady=5)

        self.zigbee_layer_combo = ttk.Combobox(self.nb_zigbee, value=['MAC', 'NWK', 'APS'])
        self.zigbee_layer_combo.grid(row=1, pady=5)

        self.l_raw_pkt = ttk.Label(self.parent, text="Raw packet:")
        self.l_raw_pkt.grid(row=3, padx=10, sticky='w')
        # self.l_raw_pkt.grid(row=3, padx=10)
        self.entry_raw_pkt = ttk.Entry(self.parent)
        self.entry_raw_pkt.grid(row=4, padx=10, sticky='we')

        self.bttn_send = ttk.Button(self.parent, text='Send')
        self.bttn_send.grid(row=4, column=2)

def main():
    root = tk.Tk()
    AppPwnRf(root)
    root.mainloop()


if __name__ == '__main__':
    main()
