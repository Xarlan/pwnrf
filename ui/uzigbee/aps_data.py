# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

__author__ = 'lem'

# This file contain GUI elements for Zigbee Nwk Cmd frame

import tkinter as tk
from tkinter import ttk

import lrwpan

GUI_PAYLOAD_WIDTH       = 25
GUI_HEADER_PAYLOAD_ROW  = 4


class ApsData:

    def __init__(self, parent):
        self.aps_data_parent = parent

        #########################################
        ### Zigbee APS payload -> Data Frame  ###
        #########################################

        self.lf_zigbee_aps_payload_data = ttk.LabelFrame(self.aps_data_parent, text='APS Payload')
        self.lf_zigbee_aps_payload_data.grid(row=GUI_HEADER_PAYLOAD_ROW, column=6, padx=5, pady=5, ipady=5, sticky='n')

        self.l_zigbee_aps_payload_data_frame = ttk.Label(self.lf_zigbee_aps_payload_data, text='Data Frame Payload')
        self.l_zigbee_aps_payload_data_frame.grid(row=0, padx=5, pady=5, sticky='w')
        self.aps_data_payload = ttk.Entry(self.lf_zigbee_aps_payload_data)
        self.aps_data_payload.grid(row=1, padx=5)

    def show_payload(self):
        self.lf_zigbee_aps_payload_data.grid()

    def hide_payload(self):
        self.lf_zigbee_aps_payload_data.grid_remove()


if __name__ == '__main__':
    root = tk.Tk()
    ApsData(root)
    root.mainloop()