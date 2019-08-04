# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import tkinter as tk
from tkinter import ttk
import serial
import glob
import sys

ZIGBEE_LAYER            = ['MAC', 'NWK', 'APS']
ZIGBEE_MAC_TYPE         = ['BEACON', 'DATA', 'ACK', 'CMD']
ZIGBEE_MHR_FC_ADDR_MODE = ['NOT PAN/addr', '16 bit', '64 bit']
ZIGBEE_MHR_FC_FRAME_VER = ['IEEE Std 802.15.4-2003', 'IEEE 802.15.4 frame']
ZIGBEE_MAC_CMD_ID_CMD   = {
                            'Association request'           : 0x1,
                            'Association response'          : 0x2,
                            'Disassociation notification'   : 0x3,
                            'Data request'                  : 0x4,
                            'PAN ID conflict'               : 0x5,
                            'Orphan notification'           : 0x6,
                            'Beacon request'                : 0x7,
                            'Coordinator realignment'       : 0x8,
                            'GTS request'                   : 0x9,
                            'Reserved'                      : None
                            }

# print(list(ZIGBEE_MAC_CMD_ID_CMD.keys()))
class AppPwnRf:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Pwn 2.4 Ghz")
        self.parent.geometry("730x640")

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
        self.zigbee_layer_combo.grid(row=1, padx=5, pady=5)
        # self.zigbee_layer_combo.bind("<<ComboboxSelected>>", self.__set_zigbee_type, '+')
        self.zigbee_layer_combo.bind("<<ComboboxSelected>>", self.__set_zigbee_type)

        self.combo_zigbee_mac_type = ttk.Combobox(self.nb_zigbee, value=ZIGBEE_MAC_TYPE)
        self.combo_zigbee_mac_type.grid(row=2, column=0, padx=5, columnspan=2)
        self.combo_zigbee_mac_type.bind("<<ComboboxSelected>>", self.__set_zigbee_mac_type_frame)


        #############################
        ### 802.15.5 MAC header   ###
        #############################
        self.lf_zigbee_mhr = ttk.LabelFrame(self.nb_zigbee, text='MAC header')
        self.lf_zigbee_mhr.grid(row=3, padx=5, pady=5, sticky='w')

        #############################
        ### 802.15.4 MHR -> FC
        self.lf_zigbee_mhr_fc = ttk.LabelFrame(self.lf_zigbee_mhr, text='FC')
        self.lf_zigbee_mhr_fc.grid(row=0, padx=5, pady=5, columnspan=2)

        self.c_zigbee_mhr_fc_sec_enable = ttk.Checkbutton(self.lf_zigbee_mhr_fc, text='En Security')
        self.c_zigbee_mhr_fc_sec_enable.grid(row=0, padx=5, sticky='w')

        self.c_zigbee_mhr_fc_pending = ttk.Checkbutton(self.lf_zigbee_mhr_fc, text='Pending')
        self.c_zigbee_mhr_fc_pending.grid(row=1, padx=5, sticky='w')

        self.c_zigbee_mhr_fc_ar = ttk.Checkbutton(self.lf_zigbee_mhr_fc, text='AR')
        self.c_zigbee_mhr_fc_ar.grid(row=2, padx=5, sticky='w')

        self.c_zigbee_mhr_fc_panid_compression = ttk.Checkbutton(self.lf_zigbee_mhr_fc, text='PAN ID Compres')
        self.c_zigbee_mhr_fc_panid_compression.grid(row=3, padx=5, sticky='w')

        self.l_zigbee_mhr_fc_dst_addr_mode = ttk.Label(self.lf_zigbee_mhr_fc, text='Dst Addr mode')
        self.l_zigbee_mhr_fc_dst_addr_mode.grid(row=4, padx=5, pady=5, sticky='w')
        self.combo_zigbee_mhr_fc_dst_addr_mode = ttk.Combobox(self.lf_zigbee_mhr_fc, values=ZIGBEE_MHR_FC_ADDR_MODE)
        self.combo_zigbee_mhr_fc_dst_addr_mode.grid(row=5, padx=5)

        self.l_zigbee_mhr_fc_frame_ver = ttk.Label(self.lf_zigbee_mhr_fc, text='Frame version')
        self.l_zigbee_mhr_fc_frame_ver.grid(row=6, padx=5, pady=5, sticky='w')
        self.combo_zigbee_mhr_fc_frame_ver = ttk.Combobox(self.lf_zigbee_mhr_fc, values=ZIGBEE_MHR_FC_FRAME_VER)
        self.combo_zigbee_mhr_fc_frame_ver.grid(row=7, padx=5)

        self.l_zigbee_mhr_fc_src_addr_mode = ttk.Label(self.lf_zigbee_mhr_fc, text='Src Addr mode')
        self.l_zigbee_mhr_fc_src_addr_mode.grid(row=8, padx=5, pady=5, sticky='w')
        self.combo_zigbee_mhr_fc_src_addr_mode = ttk.Combobox(self.lf_zigbee_mhr_fc, values=ZIGBEE_MHR_FC_ADDR_MODE)
        self.combo_zigbee_mhr_fc_src_addr_mode.grid(row=9, padx=5, pady=5)


        #############################
        ### 802.15.4 - MHR
        self.l_zigbee_mhr_seq_num = ttk.Label(self.lf_zigbee_mhr, text='Seq Num')
        self.l_zigbee_mhr_seq_num.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.e_zigbee_mhr_seq_num = ttk.Entry(self.lf_zigbee_mhr, width=8)
        self.e_zigbee_mhr_seq_num.grid(row=1, column=1, padx=5, sticky='e')

        self.l_zigbee_mhr_dst_pan = ttk.Label(self.lf_zigbee_mhr, text='dst PAN')
        self.l_zigbee_mhr_dst_pan.grid(row=2, column=0, padx=5, sticky='w')
        self.e_zigbee_mhr_dst_pan = ttk.Entry(self.lf_zigbee_mhr, width=8)
        self.e_zigbee_mhr_dst_pan.grid(row=2, column=1, padx=5, sticky='e')

        self.l_zigbee_mhr_dst_addr = ttk.Label(self.lf_zigbee_mhr, text='dst addr')
        self.l_zigbee_mhr_dst_addr.grid(row=3, pady=5, padx=5, sticky='w')
        self.e_zigbee_mhr_dst_addr = ttk.Entry(self.lf_zigbee_mhr, width=8)
        self.e_zigbee_mhr_dst_addr.grid(row=3, column=1, padx=5, sticky='e')

        self.l_zigbee_mhr_src_pan = ttk.Label(self.lf_zigbee_mhr, text='src PAN')
        self.l_zigbee_mhr_src_pan.grid(row=4, column=0, padx=5, sticky='w')
        self.e_zigbee_mhr_src_pan = ttk.Entry(self.lf_zigbee_mhr, width=8)
        self.e_zigbee_mhr_src_pan.grid(row=4, column=1, padx=5, sticky='e')

        self.l_zigbee_mhr_src_addr = ttk.Label(self.lf_zigbee_mhr, text='src addr')
        self.l_zigbee_mhr_src_addr.grid(row=5, pady=5, padx=5, sticky='w')
        self.e_zigbee_mhr_src_addr = ttk.Entry(self.lf_zigbee_mhr, width=8)
        self.e_zigbee_mhr_src_addr.grid(row=5, column=1, padx=5, sticky='e')

        self.l_zigbee_mhr_sec_header = ttk.Label(self.lf_zigbee_mhr, text='Security Header')
        self.l_zigbee_mhr_sec_header.grid(row=6, padx=5, sticky='w')
        self.e_zigbee_mhr_sec_header = ttk.Entry(self.lf_zigbee_mhr, width=8)
        self.e_zigbee_mhr_sec_header.grid(row=6, column=1, padx=5, sticky='e')


        #############################
        ### 802.15.4 - MAC -> Command
        self.lf_zigbee_mac_cmd = ttk.LabelFrame(self.nb_zigbee, text='Cmd')
        # self.lf_zigbee_mac_cmd.grid(row=3, column=1, padx=5, pady=5, sticky='n')


        self.l_zigbee_mac_cmd_id_cmd = ttk.Label(self.lf_zigbee_mac_cmd, text='Cmd ID')
        self.l_zigbee_mac_cmd_id_cmd.grid(row=0, padx=5, pady=5, sticky='w')
        self.combo_zigbee_mac_cmd_id_cmd = ttk.Combobox(self.lf_zigbee_mac_cmd, values=list(ZIGBEE_MAC_CMD_ID_CMD.keys()))
        self.combo_zigbee_mac_cmd_id_cmd.grid(row=1, padx=5)

        self.l_zigbee_mac_cmd_payload_cmd = ttk.Label(self.lf_zigbee_mac_cmd, text='Cmd payload')
        self.l_zigbee_mac_cmd_payload_cmd.grid(row=2, padx=5, pady=5, sticky='w')
        self.e_zigbee_mac_cmd_payload_cmd = ttk.Entry(self.lf_zigbee_mac_cmd, width=20)
        self.e_zigbee_mac_cmd_payload_cmd.grid(row=3, padx=5, pady=5, sticky='w')


        #############################
        ### 802.15.4 - MAC -> Data
        self.lf_zigbee_mac_data = ttk.LabelFrame(self.nb_zigbee, text='Data')
        # self.lf_zigbee_mac_data.grid(row=3, column=1, padx=5, pady=5, sticky='n')

        self.l_zigbee_mac_data_payload = ttk.Label(self.lf_zigbee_mac_data, text='Data payload')
        self.l_zigbee_mac_data_payload.grid(row=0, padx=5, pady=5, sticky='w')
        self.e_zigbee_mac_data_payload = ttk.Entry(self.lf_zigbee_mac_data, width=20)
        self.e_zigbee_mac_data_payload.grid(row=1, padx=5, pady=5, sticky='w')

        #############################
        ### 802.15.4 - MAC -> Ack
        self.lf_zigbee_mac_ack = ttk.LabelFrame(self.nb_zigbee, text='Ack')
        # self.lf_zigbee_mac_ack.grid(row=3, column=1, padx=5, pady=5, sticky='n')

        self.l_zigbee_mac_ack = ttk.Label(self.lf_zigbee_mac_ack, text='No payload')
        self.l_zigbee_mac_ack.grid(row=0, padx=5, pady=5, sticky='w')

        #############################
        ### 802.15.4 - MAC -> Beacon
        self.lf_zigbee_mac_beacon = ttk.LabelFrame(self.nb_zigbee, text='Beacon')
        # self.lf_zigbee_mac_beacon.grid(row=3, column=1, padx=5, pady=5, sticky='n')

        self.l_zigbee_mac_beacon_sspec = ttk.Label(self.lf_zigbee_mac_beacon, text='Superframe spec')
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


        #############################
        ### Zigbee NWK header     ###
        #############################

        #############################
        ### Zigbee NWK Header -> FC
        self.lf_zigbee_nwk_fc = ttk.LabelFrame(self.nb_zigbee, text='NWK header')
        self.lf_zigbee_nwk_fc.grid(row=3, column=3, padx=5, pady=5, sticky='n')

        self.l_nwkh_fc_dst_addr = ttk.Label(self.lf_zigbee_nwk_fc, text='Dst addr')
        self.l_nwkh_fc_dst_addr.grid(row=0)




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

        self.bttn_send = ttk.Button(self.parent, text='Send')
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

    def __set_zigbee_type(self, event):
        current_mac_type = event.widget.get()
        print(current_mac_type)
        self.__show_mac_type()

        # if current_mac_type == 'MAC':
        #     # self.pane_zigbee_mac_header.grid()
        #     self.f1.grid()
        #     self.f2.grid_forget()
        #
        # else:
        #     self.f1.grid_forget()
        #     self.f2.grid()
            # self.pane_zigbee_mac_header.grid_remove()

    def __set_zigbee_mac_type_frame(self, event):
        current_mac_type = event.widget.get()
        print(current_mac_type)
        print(self.parent.winfo_width())

        if current_mac_type == 'BEACON':
            self.lf_zigbee_mac_data.grid_forget()
            self.lf_zigbee_mac_ack.grid_forget()
            self.lf_zigbee_mac_cmd.grid_forget()
            self.lf_zigbee_mac_beacon.grid(row=3, column=1, padx=5, pady=5, sticky='n')

        elif current_mac_type == 'DATA':
            self.lf_zigbee_mac_data.grid(row=3, column=1, padx=5, pady=5, sticky='n')
            self.lf_zigbee_mac_ack.grid_forget()
            self.lf_zigbee_mac_cmd.grid_forget()
            self.lf_zigbee_mac_beacon.grid_forget()

        elif current_mac_type == 'ACK':
            self.lf_zigbee_mac_data.grid_forget()
            self.lf_zigbee_mac_ack.grid(row=3, column=1, padx=5, pady=5, sticky='n')
            self.lf_zigbee_mac_cmd.grid_forget()
            self.lf_zigbee_mac_beacon.grid_forget()

        elif current_mac_type == 'CMD':
            self.lf_zigbee_mac_data.grid_forget()
            self.lf_zigbee_mac_ack.grid_forget()
            self.lf_zigbee_mac_cmd.grid(row=3, column=1, padx=5, pady=5, sticky='n')
            self.lf_zigbee_mac_beacon.grid_forget()




    def __hide_widget(self, widget):
        widget.grid_forget()

    def __show_widget(self, widget):
        widget.grid()


    def __show_mac_type(self):
        pass
        # print(self.nb_zigbee.winfo_children())


def main():
    root = tk.Tk()
    AppPwnRf(root)
    root.mainloop()


if __name__ == '__main__':
    main()
