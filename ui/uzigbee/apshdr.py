# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

__author__ = 'lem'

# This file contain GUI elements for Zigbee Apl Header

import tkinter as tk
from tkinter import ttk

import lrwpan

GUI_PAYLOAD_WIDTH       = 25
GUI_HEADER_PAYLOAD_ROW  = 4


class ApsHdr:

    def __init__(self, parent):
        self.apl_hdr_parent = parent

                            #############################
                            ### Zigbee APS Layer      ###
                            #############################

        self.lf_zigbee_aps_head = ttk.LabelFrame(self.apl_hdr_parent, text='APS header')
        self.lf_zigbee_aps_head.grid(row=GUI_HEADER_PAYLOAD_ROW, column=5, padx=5, pady=5, ipady=5, sticky='n')

        #############################
        ### Zigbee APS head - FC  ###
        #############################

        self.lf_zigbee_apsh_fc = ttk.LabelFrame(self.lf_zigbee_aps_head, text='FC')
        self.lf_zigbee_apsh_fc.grid(row=0, padx=5, pady=5, columnspan=2)

        self.l_zigbee_apsh_fc_frame_type = ttk.Label(self.lf_zigbee_apsh_fc, text='Frame type')
        self.l_zigbee_apsh_fc_frame_type.grid(row=0, column=1, pady=5, sticky='w')
        self.apshdr_fc_frame_type = ttk.Combobox(self.lf_zigbee_apsh_fc,
                                                            value=list(lrwpan.ZIGBEE_APS_FRAME_TYPE.keys()),
                                                            width=10)
        self.apshdr_fc_frame_type.grid(row=0, column=0, padx=5, sticky='w')

        self.l_zigbee_apsh_fc_delivery_mode = ttk.Label(self.lf_zigbee_apsh_fc, text='Delivery mode')
        self.l_zigbee_apsh_fc_delivery_mode.grid(row=1, column=1, sticky='w')
        self.apshdr_fc_delivery_mode = ttk.Combobox(self.lf_zigbee_apsh_fc,
                                                            value=list(lrwpan.ZIGBEE_APS_FC_DELIVERY_MODE.keys()),
                                                            width=10)
        self.apshdr_fc_delivery_mode.grid(row=1, column=0, padx=5, pady=5, sticky='w')

        self.apshdr_fc_ack = ttk.Checkbutton(self.lf_zigbee_apsh_fc, text='ACK format')
        self.apshdr_fc_ack.grid(row=2, padx=5, sticky='w', columnspan=2)

        self.c_zigbee_apsh_fc_security = ttk.Checkbutton(self.lf_zigbee_apsh_fc, text='Security')
        self.c_zigbee_apsh_fc_security.grid(row=3, padx=5, sticky='w', columnspan=2)

        self.apshdr_fc_ack_req = ttk.Checkbutton(self.lf_zigbee_apsh_fc, text='ACK request')
        self.apshdr_fc_ack_req.grid(row=4, padx=5, sticky='w', columnspan=2)

        self.apshdr_fc_ext_header = ttk.Checkbutton(self.lf_zigbee_apsh_fc, text='Ext header')
        self.apshdr_fc_ext_header.grid(row=5, padx=5, sticky='w', columnspan=2)

        ########################
        ### Zigbee APS head  ###
        ########################

        self.l_zigbee_apsh_dst_endpoint = ttk.Label(self.lf_zigbee_aps_head, text='Dst Endpoint')
        self.l_zigbee_apsh_dst_endpoint.grid(row=1, column=1, sticky='w')
        self.ahdr_dst_endpoint = ttk.Entry(self.lf_zigbee_aps_head, width=8)
        self.ahdr_dst_endpoint.grid(row=1, column=0, padx=10, sticky='w')

        self.l_zigbee_apsh_grp_addr = ttk.Label(self.lf_zigbee_aps_head, text='Grp Addr')
        self.l_zigbee_apsh_grp_addr.grid(row=2, column=1, sticky='w')
        self.ahdr_grp_addr = ttk.Entry(self.lf_zigbee_aps_head, width=8)
        self.ahdr_grp_addr.grid(row=2, column=0, padx=10, pady=5, sticky='w')

        self.l_zigbee_apsh_cluster_id = ttk.Label(self.lf_zigbee_aps_head, text='Cluster ID')
        self.l_zigbee_apsh_cluster_id.grid(row=3, column=1, sticky='w')
        self.ahdr_cluster_id = ttk.Entry(self.lf_zigbee_aps_head, width=8)
        self.ahdr_cluster_id.grid(row=3, column=0, padx=10, sticky='w')

        self.l_zigbee_apsh_profile_id = ttk.Label(self.lf_zigbee_aps_head, text='Profile ID')
        self.l_zigbee_apsh_profile_id.grid(row=4, column=1, sticky='w')
        self.ahdr_profile_id = ttk.Entry(self.lf_zigbee_aps_head, width=8)
        self.ahdr_profile_id.grid(row=4, column=0, padx=10, pady=5, sticky='w')

        self.l_zigbee_apsh_src_endpoint = ttk.Label(self.lf_zigbee_aps_head, text='Src Endpoint')
        self.l_zigbee_apsh_src_endpoint.grid(row=5, column=1, sticky='w')
        self.ahdr_src_endpoint = ttk.Entry(self.lf_zigbee_aps_head, width=8)
        self.ahdr_src_endpoint.grid(row=5, column=0, padx=10, sticky='w')

        self.l_zigbee_apsh_aps_cnt = ttk.Label(self.lf_zigbee_aps_head, text='APS Counter')
        self.l_zigbee_apsh_aps_cnt.grid(row=6, column=1, sticky='w')
        self.ahdr_aps_cnt = ttk.Entry(self.lf_zigbee_aps_head, width=8)
        self.ahdr_aps_cnt.grid(row=6, column=0, padx=10, pady=5, sticky='w')

        ###
        ### Zigbee APS -> Header -> Extended header
        self.lf_zigbee_apsh_ext_header = ttk.LabelFrame(self.lf_zigbee_aps_head, text='Ext Header')
        self.lf_zigbee_apsh_ext_header.grid(row=7, column=0, padx=5, columnspan=2, sticky='we')

        self.l_zigbee_apsh_ext_header_fc = ttk.Label(self.lf_zigbee_apsh_ext_header, text='FC')
        self.l_zigbee_apsh_ext_header_fc.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        self.ahdr_exthdr_fc = ttk.Entry(self.lf_zigbee_apsh_ext_header, width=8)
        self.ahdr_exthdr_fc.grid(row=0, column=0, padx=5)

        self.l_zigbee_apsh_ext_header_block_num = ttk.Label(self.lf_zigbee_apsh_ext_header, text='Block Number')
        self.l_zigbee_apsh_ext_header_block_num.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        self.ahdr_exthdr_block_num = ttk.Entry(self.lf_zigbee_apsh_ext_header, width=8)
        self.ahdr_exthdr_block_num.grid(row=1, column=0, padx=5)

        self.l_zigbee_apsh_ext_header_ack_bit = ttk.Label(self.lf_zigbee_apsh_ext_header, text='ACK Bitfield')
        self.l_zigbee_apsh_ext_header_ack_bit.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        self.ahdr_exthdr_ack_bit = ttk.Entry(self.lf_zigbee_apsh_ext_header, width=8)
        self.ahdr_exthdr_ack_bit.grid(row=2, column=0, padx=5)

        self.hide_aps_hdr()

    def show_aps_hdr(self):
        self.lf_zigbee_aps_head.grid()

    def hide_aps_hdr(self):
        self.lf_zigbee_aps_head.grid_remove()

if __name__ == '__main__':
    root = tk.Tk()
    ApsHdr(root)
    root.mainloop()