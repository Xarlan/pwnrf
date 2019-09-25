# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

__author__ = 'lem'

# This file contain GUI elements for IEEE 802.15.4 Mac Ack frame

import tkinter as tk
from tkinter import ttk

# import ui.uzigbee.guiconst as guiconst

GUI_PAYLOAD_WIDTH       = 25
GUI_HEADER_PAYLOAD_ROW  = 4

class MAck:

    def __init__(self, parent):
        self.mack_parent = parent
        #############################
        ### 802.15.4 - MAC -> Ack
        #############################
        self.lf_zigbee_mac_ack = ttk.LabelFrame(self.mack_parent, text='MAC Payload')
        self.lf_zigbee_mac_ack.grid(row=GUI_HEADER_PAYLOAD_ROW, column=1, padx=5, pady=5, sticky='n')

        self.l_zigbee_mac_ack = ttk.Label(self.lf_zigbee_mac_ack, text='No payload', width=GUI_PAYLOAD_WIDTH)
        self.l_zigbee_mac_ack.grid(row=0, padx=5, pady=5, sticky='w')

        self.hide_mpayload()


    def show_mpayload(self):
        self.lf_zigbee_mac_ack.grid()

    def hide_mpayload(self):
        self.lf_zigbee_mac_ack.grid_remove()


if __name__ == '__main__':
    root = tk.Tk()
    MAck(root)
    root.mainloop()