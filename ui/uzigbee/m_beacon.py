# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

__author__ = 'lem'

# This file contain GUI elements for IEEE 802.15.4 Mac Data frame

import tkinter as tk
from tkinter import ttk



GUI_PAYLOAD_WIDTH       = 25
GUI_HEADER_PAYLOAD_ROW  = 4


class MBeacon:

    def __init__(self, parent):
        self.mbeacon_parent = parent

        #############################
        ### 802.15.4 - MAC -> Beacon
        #############################
        self.lf_zigbee_mac_beacon = ttk.LabelFrame(self.mbeacon_parent, text='MAC Payload')
        self.lf_zigbee_mac_beacon.grid(row=GUI_HEADER_PAYLOAD_ROW, column=1, padx=5, pady=5, sticky='n')

        self.l_zigbee_mac_beacon_sspec = ttk.Label(self.lf_zigbee_mac_beacon, text='Superframe spec', width=GUI_PAYLOAD_WIDTH)
        self.l_zigbee_mac_beacon_sspec.grid(row=0, padx=5, pady=5, sticky='w')
        self.e_zigbee_mac_beacon_sspec = ttk.Entry(self.lf_zigbee_mac_beacon, width=8)
        self.e_zigbee_mac_beacon_sspec.grid(row=1, padx=5, sticky='w')

        self.l_zigbee_mac_beacon_gts = ttk.Label(self.lf_zigbee_mac_beacon, text='GTS')
        self.l_zigbee_mac_beacon_gts.grid(row=2, padx=5, pady=5, sticky='w')
        self.e_zigbee_mac_beacon_gts = ttk.Entry(self.lf_zigbee_mac_beacon, width=8)
        self.e_zigbee_mac_beacon_gts.grid(row=3, padx=5, sticky='w')

        self.l_zigbee_mac_beacon_pending_adr = ttk.Label(self.lf_zigbee_mac_beacon, text='Pending addr')
        self.l_zigbee_mac_beacon_pending_adr.grid(row=4, padx=5, pady=5, sticky='w')
        self.e_zigbee_mac_beacon_pending_adr = ttk.Entry(self.lf_zigbee_mac_beacon, width=8)
        self.e_zigbee_mac_beacon_pending_adr.grid(row=5, padx=5, sticky='w')

        self.l_zigbee_mac_beacon_payload_beacon = ttk.Label(self.lf_zigbee_mac_beacon, text='Beacon payload')
        self.l_zigbee_mac_beacon_payload_beacon.grid(row=6, padx=5, pady=5, sticky='w')
        self.e_zigbee_mac_beacon_payload_beacon = ttk.Entry(self.lf_zigbee_mac_beacon, width=8)
        self.e_zigbee_mac_beacon_payload_beacon.grid(row=7, padx=5, sticky='w')

        self.hide_mpayload()

    def show_mpayload(self):
        self.lf_zigbee_mac_beacon.grid()

    def hide_mpayload(self):
        self.lf_zigbee_mac_beacon.grid_remove()


if __name__ == '__main__':
    root = tk.Tk()
    MBeacon(root)
    root.mainloop()