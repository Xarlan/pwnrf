# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

__author__ = 'lem'

# This file contain GUI elements for Zigbee Nwk Data frame

import tkinter as tk
from tkinter import ttk

import lrwpan

GUI_PAYLOAD_WIDTH       = 25
GUI_HEADER_PAYLOAD_ROW  = 4


class NwkData:

    def __init__(self, parent):
        self.nwk_data_parent = parent

        ###################################
        ### Zigbee NWK PAYLOAD -> data
        ###################################
        self.lf_zigbee_nwk_payload_data = ttk.LabelFrame(self.nwk_data_parent, text='NWK Payload')
        self.lf_zigbee_nwk_payload_data.grid(row=GUI_HEADER_PAYLOAD_ROW, column=4, padx=5, pady=5, sticky='n')

        self.l_zigbee_nwk_data_payload = ttk.Label(self.lf_zigbee_nwk_payload_data,
                                                   text='Data payload',
                                                   width=GUI_PAYLOAD_WIDTH)
        self.l_zigbee_nwk_data_payload.grid(row=0, padx=5, pady=5)
        self.nwk_data_payload = ttk.Entry(self.lf_zigbee_nwk_payload_data, width=10)
        self.nwk_data_payload.grid(row=1, padx=5, pady=5, sticky='w')

        self.hide_nwkpayload()



    def show_nwkpayload(self):
        self.lf_zigbee_nwk_payload_data.grid()

    def hide_nwkpayload(self):
        self.lf_zigbee_nwk_payload_data.grid_remove()


if __name__ == '__main__':
    root = tk.Tk()
    NwkData(root)
    root.mainloop()