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


class NwkCmd:

    def __init__(self, parent):
        self.nwk_cmd_parent = parent

        ###################################
        ### Zigbee NWK PAYLOAD -> NWK cmd
        ###################################

        self.lf_zigbee_nwk_payload_cmd = ttk.LabelFrame(self.nwk_cmd_parent, text='NWK Payload')
        self.lf_zigbee_nwk_payload_cmd.grid(row=GUI_HEADER_PAYLOAD_ROW, column=4, padx=5, pady=5, sticky='n')

        self.l_zigbee_nwk_id_cmd = ttk.Label(self.lf_zigbee_nwk_payload_cmd,
                                                         text='NWK ID Cmd',
                                                         width=GUI_PAYLOAD_WIDTH)
        self.l_zigbee_nwk_id_cmd.grid(row=0, padx=5, pady=5)
        self.nwk_id_cmd = ttk.Combobox(self.lf_zigbee_nwk_payload_cmd, value=list(lrwpan.ZIGBEE_NWK_CMD_ID.keys()))
        self.nwk_id_cmd.grid(row=1, padx=5, sticky='w')

        self.l_zigbee_nwk_cmd_payload = ttk.Label(self.lf_zigbee_nwk_payload_cmd, text='NWK Cmd Payload')
        self.l_zigbee_nwk_cmd_payload.grid(row=2, padx=5, ipady=5, sticky='w')
        self.nwk_cmd_payload = ttk.Entry(self.lf_zigbee_nwk_payload_cmd, width=10)
        self.nwk_cmd_payload.grid(row=3, padx=5, pady=5, sticky='w')

    def show_nwkpayload(self):
        self.lf_zigbee_nwk_payload_cmd.grid()

    def hide_nwkpayload(self):
        self.lf_zigbee_nwk_payload_cmd.grid_remove()


if __name__ == '__main__':
    root = tk.Tk()
    NwkCmd(root)
    root.mainloop()