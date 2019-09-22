# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

__author__ = 'lem'

# This file contain GUI elements for IEEE 802.15.4 Mac Cmd frame

import tkinter as tk
from tkinter import ttk

import lrwpan


GUI_PAYLOAD_WIDTH       = 25
GUI_HEADER_PAYLOAD_ROW  = 4

class MCmd:

    def __init__(self, parent):
        self.mcmd_parent = parent

        #############################
        ### 802.15.4 - MAC -> Command
        #############################
        self.lf_zigbee_mac_cmd = ttk.LabelFrame(self.mcmd_parent, text='MAC Payload')
        self.lf_zigbee_mac_cmd.grid(row=GUI_HEADER_PAYLOAD_ROW, column=1, padx=5, pady=5, sticky='n')


        self.l_zigbee_mac_cmd_id_cmd = ttk.Label(self.lf_zigbee_mac_cmd, text='Cmd ID', width=GUI_PAYLOAD_WIDTH)
        self.l_zigbee_mac_cmd_id_cmd.grid(row=0, padx=5, pady=5, sticky='w')
        self.combo_zigbee_mac_cmd_id_cmd = ttk.Combobox(self.lf_zigbee_mac_cmd, values=list(lrwpan.IEEE_802_15_4_MAC_CMD_ID.keys()))
        self.combo_zigbee_mac_cmd_id_cmd.grid(row=1, padx=5, sticky='w')

        self.l_zigbee_mac_cmd_payload_cmd = ttk.Label(self.lf_zigbee_mac_cmd, text='Cmd payload')
        self.l_zigbee_mac_cmd_payload_cmd.grid(row=2, padx=5, pady=5, sticky='w')
        self.e_zigbee_mac_cmd_payload_cmd = ttk.Entry(self.lf_zigbee_mac_cmd, width=20)
        self.e_zigbee_mac_cmd_payload_cmd.grid(row=3, padx=5, pady=5, sticky='w')

    def show_mpayload(self):
        self.lf_zigbee_mac_cmd.grid()

    def hide_mpayload(self):
        self.lf_zigbee_mac_cmd.grid_remove()


if __name__ == '__main__':
    root = tk.Tk()
    MCmd(root)
    root.mainloop()