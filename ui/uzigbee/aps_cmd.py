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


class ApsCmd:

    def __init__(self, parent):
        self.aps_cmd_p = parent

        #########################################
        ### Zigbee APS payload -> CMD Frame   ###
        #########################################

        self.lf_zigbee_aps_payload_cmd_frame = ttk.LabelFrame(self.aps_cmd_p, text='APS Payload')
        self.lf_zigbee_aps_payload_cmd_frame.grid(row=GUI_HEADER_PAYLOAD_ROW, column=6, padx=5, pady=5, ipady=5, sticky='n')

        self.l_zigbee_aps_payload_cmd_frame_aps_cmd_id = ttk.Label(self.lf_zigbee_aps_payload_cmd_frame, text='APS Cmd ID')
        self.l_zigbee_aps_payload_cmd_frame_aps_cmd_id.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.aps_cmd_id = ttk.Entry(self.lf_zigbee_aps_payload_cmd_frame)
        self.aps_cmd_id.grid(row=1, column=0, padx=5)

        self.l_zigbee_aps_payload_cmd_frame_aps_cmd_payload = ttk.Label(self.lf_zigbee_aps_payload_cmd_frame,
                                                                   text='APS Cmd Payload')
        self.l_zigbee_aps_payload_cmd_frame_aps_cmd_payload.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.aps_cmd_payload = ttk.Entry(self.lf_zigbee_aps_payload_cmd_frame)
        self.aps_cmd_payload.grid(row=3, column=0, padx=5)

    def show_apspayload(self):
        self.lf_zigbee_aps_payload_cmd_frame.grid()

    def hide_apspayload(self):
        self.lf_zigbee_aps_payload_cmd_frame.grid_remove()


if __name__ == '__main__':
    root = tk.Tk()
    ApsCmd(root)
    root.mainloop()