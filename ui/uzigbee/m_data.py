# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

__author__ = 'lem'

# This file contain GUI elements for IEEE 802.15.4 Mac Data frame

import tkinter as tk
from tkinter import ttk

GUI_PAYLOAD_WIDTH       = 25
GUI_HEADER_PAYLOAD_ROW  = 4


class MData:

    def __init__(self, parent):
        self.mdata_parent = parent

        #############################
        ### 802.15.4 - MAC -> Data
        #############################
        self.lf_zigbee_mac_data = ttk.LabelFrame(self.mdata_parent, text='MAC Payload')
        self.lf_zigbee_mac_data.grid(row=GUI_HEADER_PAYLOAD_ROW, column=1, padx=5, pady=5, sticky='n')

        self.l_zigbee_mac_data_payload = ttk.Label(self.lf_zigbee_mac_data, text='Data payload', width=GUI_PAYLOAD_WIDTH)
        self.l_zigbee_mac_data_payload.grid(row=0, padx=5, pady=5, sticky='w')
        self.e_zigbee_mac_data_payload = ttk.Entry(self.lf_zigbee_mac_data, width=20)
        self.e_zigbee_mac_data_payload.grid(row=1, padx=5, pady=5, sticky='w')

        self.hide_mpayload()

    def show_mpayload(self):
        self.lf_zigbee_mac_data.grid()

    def hide_mpayload(self):
        self.lf_zigbee_mac_data.grid_remove()


if __name__ == '__main__':
    root = tk.Tk()
    MData(root)
    root.mainloop()