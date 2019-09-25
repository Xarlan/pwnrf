# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

__author__ = 'lem'

# This file contain GUI elements for IEEE 802.15.4 Mac Header

import tkinter as tk
from tkinter import ttk

import lrwpan

GUI_PAYLOAD_WIDTH = 25
GUI_HEADER_PAYLOAD_ROW = 4


class Mhr:

    def __init__(self, parent):
        self.mhr_parent = parent

        ####################################
        ### GUI IEEE 802.15.4 variable   ###
        ####################################
        self.var_mhdr_fc_security_enable = tk.IntVar()
        self.var_mhdr_fc_pending = tk.IntVar()
        self.var_mhdr_fc_ar = tk.IntVar()
        self.var_mhdr_fc_panid_compress = tk.IntVar()

        #############################
        ### 802.15.4 MAC header   ###
        #############################
        self.lf_zigbee_mhr = ttk.LabelFrame(self.mhr_parent, text='MAC header')
        self.lf_zigbee_mhr.grid(row=GUI_HEADER_PAYLOAD_ROW, padx=5, pady=5, ipady=5, sticky='nw')

        #############################
        ### 802.15.4 MHR -> FC    ###
        #############################
        self.lf_zigbee_mhr_fc = ttk.LabelFrame(self.lf_zigbee_mhr, text='FC')
        self.lf_zigbee_mhr_fc.grid(row=0, padx=5, pady=5, columnspan=2)

        self.l_zigbee_mhr_fc_frame_type = ttk.Label(self.lf_zigbee_mhr_fc, text='Frame Type')
        self.l_zigbee_mhr_fc_frame_type.grid(row=0, column=1)
        self.mhdr_fc_frame_type = ttk.Combobox(self.lf_zigbee_mhr_fc,
                                               value=list(sorted(lrwpan.IEEE_802_15_4_MAC_TYPE.keys())),
                                               width=10)
        self.mhdr_fc_frame_type.grid(row=0, column=0, padx=5, pady=5, sticky='we')

        self.mhdr_fc_sec_enable = ttk.Checkbutton(self.lf_zigbee_mhr_fc,
                                                  text='Security Enabled',
                                                  variable=self.var_mhdr_fc_security_enable,
                                                  onvalue=0x8,
                                                  offvalue=0x0,  # MHR -> FC -> b3
                                                  command=self.show_hide_mhr_aux_sec)

        self.mhdr_fc_sec_enable.grid(row=1, padx=5, columnspan=2, sticky='w')
        self.var_mhdr_fc_security_enable.set(0x0)

        self.mhdr_fc_pending = ttk.Checkbutton(self.lf_zigbee_mhr_fc,
                                               text='Pending',
                                               variable=self.var_mhdr_fc_pending,
                                               onvalue=0x10,
                                               offvalue=0x0)  # MHR -> FC -> b4
        self.mhdr_fc_pending.grid(row=2, padx=5, columnspan=2, sticky='w')
        self.var_mhdr_fc_pending.set(0x0)

        self.mhdr_fc_ar = ttk.Checkbutton(self.lf_zigbee_mhr_fc,
                                          text='AR',
                                          variable=self.var_mhdr_fc_ar,
                                          onvalue=0x20,
                                          offvalue=0x0)  # MHR -> FC -> b5
        self.mhdr_fc_ar.grid(row=3, padx=5, columnspan=2, sticky='w')
        self.var_mhdr_fc_ar.set(0x0)

        self.mhdr_fc_panid_compression = ttk.Checkbutton(self.lf_zigbee_mhr_fc,
                                                         text='PAN ID Compres',
                                                         variable=self.var_mhdr_fc_panid_compress,
                                                         onvalue=0x40,
                                                         offvalue=0x0)  # MHR -> FC -> b6
        self.mhdr_fc_panid_compression.grid(row=4, padx=5, columnspan=2, sticky='w')
        self.var_mhdr_fc_panid_compress.set(0x0)

        self.l_zigbee_mhr_fc_reserved = ttk.Label(self.lf_zigbee_mhr_fc, text='Reserved')
        self.l_zigbee_mhr_fc_reserved.grid(row=5, column=1, padx=5, sticky='w')
        self.mhdr_fc_reserved = ttk.Entry(self.lf_zigbee_mhr_fc, width=10)
        self.mhdr_fc_reserved.grid(row=5, column=0, padx=5, pady=5, sticky='w')

        self.l_zigbee_mhr_fc_dst_addr_mode = ttk.Label(self.lf_zigbee_mhr_fc, text='Dst Addr mode')
        self.l_zigbee_mhr_fc_dst_addr_mode.grid(row=6, column=1, padx=5, pady=5, sticky='w')
        self.mhdr_fc_dst_addr_mode = ttk.Combobox(self.lf_zigbee_mhr_fc,
                                                  values=list(sorted(lrwpan.IEEE_802_15_4_MAC_DST_ADDR_MODE.keys())),
                                                  width=10,
                                                  state='disabled')
        self.mhdr_fc_dst_addr_mode.grid(row=6, column=0, padx=5, pady=5, sticky='w')

        self.l_zigbee_mhr_fc_frame_ver = ttk.Label(self.lf_zigbee_mhr_fc, text='Frame version')
        self.l_zigbee_mhr_fc_frame_ver.grid(row=7, column=1, padx=5, pady=5, sticky='w')
        self.mhdr_fc_frame_ver = ttk.Combobox(self.lf_zigbee_mhr_fc,
                                              values=lrwpan.IEEE_802_15_4_FC_FRAME_VER,
                                              width=10)
        self.mhdr_fc_frame_ver.grid(row=7, padx=5, pady=5, sticky='w')

        self.l_zigbee_mhr_fc_src_addr_mode = ttk.Label(self.lf_zigbee_mhr_fc, text='Src Addr mode')
        self.l_zigbee_mhr_fc_src_addr_mode.grid(row=8, column=1, padx=5, pady=5, sticky='w')
        self.mhdr_fc_src_addr_mode = ttk.Combobox(self.lf_zigbee_mhr_fc,
                                                  values=list(sorted(lrwpan.IEEE_802_15_4_MAC_SRC_ADDR_MODE.keys())),
                                                  width=10,
                                                  state='disabled')
        self.mhdr_fc_src_addr_mode.grid(row=8, padx=5, pady=5, sticky='w')

        #############################
        ### 802.15.4 - MHR        ###
        #############################
        self.l_zigbee_mhr_seq_num = ttk.Label(self.lf_zigbee_mhr, text='Sequence Number')
        self.l_zigbee_mhr_seq_num.grid(row=1, column=1, pady=5, sticky='w')
        self.mhdr_seq_num = ttk.Entry(self.lf_zigbee_mhr, width=8)
        self.mhdr_seq_num.grid(row=1, column=0, padx=10, sticky='w')

        self.l_zigbee_mhr_dst_pan = ttk.Label(self.lf_zigbee_mhr, text='Dst PAN')
        self.l_zigbee_mhr_dst_pan.grid(row=2, column=1, sticky='w')
        self.mhdr_dst_pan = ttk.Entry(self.lf_zigbee_mhr, width=8, name='mac_dst_pan')
        self.mhdr_dst_pan.grid(row=2, column=0, padx=10, sticky='w')

        self.l_zigbee_mhr_dst_addr = ttk.Label(self.lf_zigbee_mhr, text='Dst addr')
        self.l_zigbee_mhr_dst_addr.grid(row=3, column=1, pady=5, sticky='w')
        self.mhdr_dst_addr = ttk.Entry(self.lf_zigbee_mhr, width=8, name='mac_dst_addr')
        self.mhdr_dst_addr.grid(row=3, column=0, padx=10, sticky='w')
        self.mhdr_dst_addr.bind('<FocusOut>', self.set_mac_addr_mode)

        self.l_zigbee_mhr_src_pan = ttk.Label(self.lf_zigbee_mhr, text='Src PAN')
        self.l_zigbee_mhr_src_pan.grid(row=4, column=1, sticky='w')
        self.mhdr_src_pan = ttk.Entry(self.lf_zigbee_mhr, width=8, name='mac_src_pan')
        self.mhdr_src_pan.grid(row=4, column=0, padx=10, sticky='w')

        self.l_zigbee_mhr_src_addr = ttk.Label(self.lf_zigbee_mhr, text='Src addr')
        self.l_zigbee_mhr_src_addr.grid(row=5, column=1, pady=5, sticky='w')
        self.mhdr_src_addr = ttk.Entry(self.lf_zigbee_mhr, width=8, name='mac_src_addr')
        self.mhdr_src_addr.grid(row=5, column=0, padx=10, sticky='w')
        self.mhdr_src_addr.bind('<FocusOut>', self.set_mac_addr_mode)

        #############################################
        ### 802.15.4 - MHR -> Aux security header ###
        #############################################
        self.lf_zigbee_mhr_aux_sec = ttk.LabelFrame(self.lf_zigbee_mhr, text='Aux Security Header')
        self.lf_zigbee_mhr_aux_sec.grid(row=6, padx=5, ipady=3, columnspan=2, sticky='w')

        self.l_zigbee_mhr_auxsechdr_sec_control = ttk.Label(self.lf_zigbee_mhr_aux_sec, text='Security Control',
                                                            width=15)
        self.l_zigbee_mhr_auxsechdr_sec_control.grid(row=0, column=1, padx=5, sticky='w')
        self.mhdr_auxsec_security_control = ttk.Entry(self.lf_zigbee_mhr_aux_sec, width=8)
        self.mhdr_auxsec_security_control.grid(row=0, column=0, padx=5, pady=5, sticky='w')

        self.l_zigbee_mhr_auxsechdr_frame_cnt = ttk.Label(self.lf_zigbee_mhr_aux_sec, text='Frame Counter')
        self.l_zigbee_mhr_auxsechdr_frame_cnt.grid(row=1, column=1, padx=5, sticky='w')
        self.mhdr_auxsec_frame_cnt = ttk.Entry(self.lf_zigbee_mhr_aux_sec, width=8)
        self.mhdr_auxsec_frame_cnt.grid(row=1, column=0, padx=5, sticky='w')

        self.l_zigbee_mhr_auxsechdr_key_ident = ttk.Label(self.lf_zigbee_mhr_aux_sec, text='Key Identifier')
        self.l_zigbee_mhr_auxsechdr_key_ident.grid(row=2, column=1, padx=5, sticky='w')
        self.mhdr_auxsec_key_ident = ttk.Entry(self.lf_zigbee_mhr_aux_sec, width=8)
        self.mhdr_auxsec_key_ident.grid(row=2, column=0, padx=5, pady=5, sticky='w')

        self.show_hide_mhr_aux_sec()

    def show_hide_mhr_aux_sec(self):
        # value '0x8' - MHC -> FC - bit3: [Security Enabled]
        if self.var_mhdr_fc_security_enable.get() == 0x8:
            self.lf_zigbee_mhr_aux_sec.grid()

        else:
            self.lf_zigbee_mhr_aux_sec.grid_remove()

        # print("Pan ID Compress = ", self.var_mhdr_fc_panid_compress.get())
        # print("AR = ", self.var_mhdr_fc_ar.get())
        # print("Pending = ", self.var_mhdr_fc_pending.get())
        # print("*****")

    def set_mac_addr_mode(self, event):
        raw_value = event.widget.get()
        current_widget = event.widget.winfo_name()
        try:
            addr = lrwpan.Ieee802MacHdr.check_16bit_64bit_addr(raw_value)

        except lrwpan.ValidationError as e:
            print(e.msg)

        else:
            # Destination Addr mode
            if current_widget == 'mac_dst_addr':
                if isinstance(addr, int):                           # Create list element using "sorted"
                    self.mhdr_fc_dst_addr_mode.current(0)           # 0 - it mean '16 bit'

                elif isinstance(addr, list):
                    self.mhdr_fc_dst_addr_mode.current(1)           # 1 - it mean '64 bit'

                elif isinstance(addr, str) and len(addr) == 0:
                    self.mhdr_fc_dst_addr_mode.current(2)           # 2 - it mean 'Not PAN/addr'

                else:
                    self.mhdr_fc_dst_addr_mode.set('unknown')

            # Source Addr mode
            elif current_widget == 'mac_src_addr':
                if isinstance(addr, int):
                    self.mhdr_fc_src_addr_mode.current(0)

                elif isinstance(addr, list):
                    self.mhdr_fc_src_addr_mode.current(1)

                elif isinstance(addr, str) and len(addr) == 0:
                    self.mhdr_fc_src_addr_mode.current(2)

                else:
                    self.mhdr_fc_src_addr_mode.set('unknown')



if __name__ == '__main__':
    root = tk.Tk()
    Mhr(root)
    root.mainloop()
