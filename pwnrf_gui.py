# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import tkinter as tk
from tkinter import ttk
import serial
import glob
import sys

import lrwpan
import ui

ZIGBEE_LAYER            = ['MAC', 'NWK', 'APS']


GUI_PAYLOAD_WIDTH       = 25
GUI_HEADER_PAYLOAD_ROW  = 4


class AppPwnRf:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Pwn 2.4 GHz")
        # self.parent.geometry("730x640")

        self.notebook_rf = ttk.Notebook(self.parent)
        self.nb_zigbee  = ttk.Frame(self.notebook_rf)
        self.nb_wifi = ttk.Frame(self.notebook_rf)
        self.nb_settings = ttk.Frame(self.notebook_rf)

        self.notebook_rf.add(self.nb_zigbee, text='Zigbee')
        self.notebook_rf.add(self.nb_wifi, text='WiFi')
        self.notebook_rf.add(self.nb_settings, text='Settings')
        self.notebook_rf.grid(row=2, padx=10, pady=10)


        ####################
        ### Tab Zigbee   ###
        ####################

        self.zigbee_layer_l = tk.Label(self.nb_zigbee, text='Zigbee layer')
        self.zigbee_layer_l.grid(padx=5, pady=5, sticky='w')

        self.zigbee_layer_combo = ttk.Combobox(self.nb_zigbee, value=ZIGBEE_LAYER)
        self.zigbee_layer_combo.set(ZIGBEE_LAYER[0])
        self.zigbee_layer_combo.grid(row=1, padx=5, pady=5, sticky='w')
        self.zigbee_layer_combo.bind("<<ComboboxSelected>>", self.__set_zigbee_layer)

        self.gui_mhr = ui.uzigbee.Mhr(self.nb_zigbee)
        self.gui_mhr.mhdr_fc_frame_type.bind("<<ComboboxSelected>>", self._set_mac_type_frame)


        self.gui_mcmd = ui.uzigbee.MCmd(self.nb_zigbee)
        self.gui_mdata = ui.uzigbee.MData(self.nb_zigbee)
        self.gui_mbeacon = ui.uzigbee.MBeacon(self.nb_zigbee)
        self.gui_mack = ui.uzigbee.MAck(self.nb_zigbee)

        self.gui_nwkhdr = ui.uzigbee.NwkHeader(self.nb_zigbee)
        self.gui_nwkhdr.nwkh_fc_frame_type.bind("<<ComboboxSelected>>", self._set_zigbee_nwk_type_frame)

        self.gui_ndata = ui.uzigbee.NwkData(self.nb_zigbee)
        self.gui_ncmd = ui.uzigbee.NwkCmd(self.nb_zigbee)

        self.gui_aplhdr = ui.uzigbee.ApsHdr(self.nb_zigbee)



        ####################
        ### Tab Settings ###
        ####################
        self.l_tty = ttk.Label(self.nb_settings, text='tty')
        self.l_tty.grid(row=0, padx=10, pady=5, sticky='w')
        self.combo_tty = ttk.Combobox(self.nb_settings, value=self.__get_serial_port())
        self.combo_tty.grid(row=1, padx=10)

        ####################
        ### Gneral       ###
        ####################
        self.l_raw_pkt = ttk.Label(self.parent, text="Raw packet:")
        self.l_raw_pkt.grid(row=3, padx=10, sticky='w')
        self.entry_raw_pkt = ttk.Entry(self.parent)
        self.entry_raw_pkt.grid(row=4, padx=10, sticky='we')

        self.bttn_send = ttk.Button(self.parent, text='Send', command=self.send_frame)
        self.bttn_send.grid(row=4, column=2)


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


    def __set_zigbee_layer(self, event):
        current_layer = event.widget.get()
        if current_layer == 'MAC':
            self.gui_nwkhdr.hide_nwk_hdr()
            self.gui_aplhdr.hide_aps_hdr()

        elif current_layer == 'NWK':
            self.gui_nwkhdr.show_nwk_hdr()
            self.gui_aplhdr.hide_aps_hdr()

        elif current_layer == 'APS':
            self.gui_nwkhdr.show_nwk_hdr()
            self.gui_aplhdr.show_aps_hdr()


    def _set_mac_type_frame(self, event):
        current_mac_type = event.widget.get()

        if current_mac_type == 'BEACON':
            self.gui_mbeacon.show_mpayload()

            self.gui_mcmd.hide_mpayload()
            self.gui_mdata.hide_mpayload()
            self.gui_mack.hide_mpayload()

        elif current_mac_type == 'DATA':
            self.gui_mdata.show_mpayload()

            self.gui_mcmd.hide_mpayload()
            self.gui_mbeacon.hide_mpayload()
            self.gui_mack.hide_mpayload()

        elif current_mac_type == 'ACK':
            self.gui_mack.show_mpayload()

            self.gui_mdata.hide_mpayload()
            self.gui_mcmd.hide_mpayload()
            self.gui_mbeacon.hide_mpayload()

        elif current_mac_type == 'CMD':
            self.gui_mcmd.show_mpayload()

            self.gui_mdata.hide_mpayload()
            self.gui_mbeacon.hide_mpayload()
            self.gui_mack.hide_mpayload()

    def _set_zigbee_nwk_type_frame(self, event):
        current_nwk_type = event.widget.get()
        print(current_nwk_type)

        if current_nwk_type == 'Data':
            self.gui_ndata.show_nwkpayload()
            self.gui_ncmd.hide_nwkpayload()

        elif current_nwk_type == 'Nwk CMD':
            self.gui_ncmd.show_nwkpayload()
            self.gui_ndata.hide_nwkpayload()

        else:
            self.gui_ndata.hide_nwkpayload()
            self.gui_ncmd.hide_nwkpayload()

    def send_frame(self):
        zigbee_layer = self.zigbee_layer_combo.get()

        if zigbee_layer == 'MAC':
            frame_type = self.gui_mhr.mhdr_fc_frame_type.get()
            print(frame_type)

            pkt_header = lrwpan.Ieee802MacHdr(frame_type)



            if frame_type == 'BEACON':
                pass

            elif frame_type == 'DATA':
                pass

            elif frame_type == 'ACK':
                pass

            elif frame_type == 'CMD':
                packet = lrwpan.Ieee802Cmd()
                packet.magic_var = 4


def main():
    root = tk.Tk()
    AppPwnRf(root)
    root.mainloop()


if __name__ == '__main__':
    main()
