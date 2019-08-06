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
ZIGBEE_NWK_TYPE         = ['DATA', 'NWK_CMD', 'Inter-PAN', 'Reserved']
ZIGBEE_MHR_FC_ADDR_MODE = ['NOT PAN/addr', '16 bit', '64 bit']
ZIGBEE_MHR_FC_FRAME_VER = ['802.15.4-2003', '802.15.4']
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
ZIGBEE_NWK_CMD_ID       = {
                            'Route request'                 : 0x1,
                            'Route reply'                   : 0x2,
                            'Network Status'                : 0x3,
                            'Leave'                         : 0x4,
                            'Route Record'                  : 0x5,
                            'Rejoin request'                : 0x6,
                            'Rejoin response'               : 0x7,
                            'Link Status'                   : 0x8,
                            'Network Report'                : 0x9,
                            'Network Update'                : 0xA,
                            'Reserved'                      : None
                            }

GUI_PAYLOAD_WIDTH   = 25

# print(list(ZIGBEE_MAC_CMD_ID_CMD.keys()))
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
        self.zigbee_layer_combo.grid(row=1, padx=5, pady=5)
        self.zigbee_layer_combo.bind("<<ComboboxSelected>>", self.__set_zigbee_type)

        self.combo_zigbee_mac_type = ttk.Combobox(self.nb_zigbee, value=ZIGBEE_MAC_TYPE)
        self.combo_zigbee_mac_type.grid(row=2, column=0, padx=5, pady=5, columnspan=2, sticky='we')
        self.combo_zigbee_mac_type.bind("<<ComboboxSelected>>", self.__set_zigbee_mac_type_frame)

        self.combo_zigbee_nwk_type = ttk.Combobox(self.nb_zigbee, value=ZIGBEE_NWK_TYPE)
        self.combo_zigbee_nwk_type.grid(row=2, column=3, columnspan=2, padx=5, sticky='we')
        self.combo_zigbee_nwk_type.bind("<<ComboboxSelected>>", self.__set_zigbee_nwk_type_frame)

        #############################
        ### 802.15.5 MAC header   ###
        #############################
        self.lf_zigbee_mhr = ttk.LabelFrame(self.nb_zigbee, text='MAC header')
        self.lf_zigbee_mhr.grid(row=3, padx=5, pady=5, sticky='nw')
        # self.lf_zigbee_mhr.grid(row=3, padx=5, sticky='w')

        #############################
        ### 802.15.4 MHR -> FC
        self.lf_zigbee_mhr_fc = ttk.LabelFrame(self.lf_zigbee_mhr, text='FC')
        self.lf_zigbee_mhr_fc.grid(row=0, padx=5, pady=5, columnspan=2)

        self.c_zigbee_mhr_fc_sec_enable = ttk.Checkbutton(self.lf_zigbee_mhr_fc, text='En Security')
        self.c_zigbee_mhr_fc_sec_enable.grid(row=0, padx=5, columnspan=2, sticky='w')

        self.c_zigbee_mhr_fc_pending = ttk.Checkbutton(self.lf_zigbee_mhr_fc, text='Pending')
        self.c_zigbee_mhr_fc_pending.grid(row=1, padx=5, columnspan=2,  sticky='w')

        self.c_zigbee_mhr_fc_ar = ttk.Checkbutton(self.lf_zigbee_mhr_fc, text='AR')
        self.c_zigbee_mhr_fc_ar.grid(row=2, padx=5, columnspan=2,  sticky='w')

        self.c_zigbee_mhr_fc_panid_compression = ttk.Checkbutton(self.lf_zigbee_mhr_fc, text='PAN ID Compres')
        self.c_zigbee_mhr_fc_panid_compression.grid(row=3, padx=5, columnspan=2,  sticky='w')

        self.l_zigbee_mhr_fc_dst_addr_mode = ttk.Label(self.lf_zigbee_mhr_fc, text='Dst Addr mode')
        self.l_zigbee_mhr_fc_dst_addr_mode.grid(row=4, column=1, padx=5, pady=5, sticky='w')
        self.combo_zigbee_mhr_fc_dst_addr_mode = ttk.Combobox(self.lf_zigbee_mhr_fc,
                                                              values=ZIGBEE_MHR_FC_ADDR_MODE,
                                                              width=10)
        self.combo_zigbee_mhr_fc_dst_addr_mode.grid(row=4, column=0, padx=5, pady=5, sticky='w')

        self.l_zigbee_mhr_fc_frame_ver = ttk.Label(self.lf_zigbee_mhr_fc, text='Frame version')
        self.l_zigbee_mhr_fc_frame_ver.grid(row=5, column=1, padx=5, pady=5, sticky='w')
        self.combo_zigbee_mhr_fc_frame_ver = ttk.Combobox(self.lf_zigbee_mhr_fc,
                                                          values=ZIGBEE_MHR_FC_FRAME_VER,
                                                          width=10)
        self.combo_zigbee_mhr_fc_frame_ver.grid(row=5, padx=5, pady=5, sticky='w')

        self.l_zigbee_mhr_fc_src_addr_mode = ttk.Label(self.lf_zigbee_mhr_fc, text='Src Addr mode')
        self.l_zigbee_mhr_fc_src_addr_mode.grid(row=6, column=1, padx=5, pady=5, sticky='w')
        self.combo_zigbee_mhr_fc_src_addr_mode = ttk.Combobox(self.lf_zigbee_mhr_fc,
                                                              values=ZIGBEE_MHR_FC_ADDR_MODE,
                                                              width=10)
        self.combo_zigbee_mhr_fc_src_addr_mode.grid(row=6, padx=5, pady=5, sticky='w')


        #############################
        ### 802.15.4 - MHR
        self.l_zigbee_mhr_seq_num = ttk.Label(self.lf_zigbee_mhr, text='Sequence Number')
        self.l_zigbee_mhr_seq_num.grid(row=1, column=1, pady=5, sticky='w')
        self.e_zigbee_mhr_seq_num = ttk.Entry(self.lf_zigbee_mhr, width=8)
        self.e_zigbee_mhr_seq_num.grid(row=1, column=0, padx=10, sticky='w')

        self.l_zigbee_mhr_dst_pan = ttk.Label(self.lf_zigbee_mhr, text='Dst PAN')
        self.l_zigbee_mhr_dst_pan.grid(row=2, column=1, sticky='w')
        self.e_zigbee_mhr_dst_pan = ttk.Entry(self.lf_zigbee_mhr, width=8)
        self.e_zigbee_mhr_dst_pan.grid(row=2, column=0, padx=10, sticky='w')

        self.l_zigbee_mhr_dst_addr = ttk.Label(self.lf_zigbee_mhr, text='Dst addr')
        self.l_zigbee_mhr_dst_addr.grid(row=3, column=1, pady=5, sticky='w')
        self.e_zigbee_mhr_dst_addr = ttk.Entry(self.lf_zigbee_mhr, width=8)
        self.e_zigbee_mhr_dst_addr.grid(row=3, column=0, padx=10, sticky='w')

        self.l_zigbee_mhr_src_pan = ttk.Label(self.lf_zigbee_mhr, text='Src PAN')
        self.l_zigbee_mhr_src_pan.grid(row=4, column=1, sticky='w')
        self.e_zigbee_mhr_src_pan = ttk.Entry(self.lf_zigbee_mhr, width=8)
        self.e_zigbee_mhr_src_pan.grid(row=4, column=0, padx=10, sticky='w')

        self.l_zigbee_mhr_src_addr = ttk.Label(self.lf_zigbee_mhr, text='Src addr')
        self.l_zigbee_mhr_src_addr.grid(row=5, column=1, pady=5, sticky='w')
        self.e_zigbee_mhr_src_addr = ttk.Entry(self.lf_zigbee_mhr, width=8)
        self.e_zigbee_mhr_src_addr.grid(row=5, column=0, padx=10, sticky='w')

        self.l_zigbee_mhr_sec_header = ttk.Label(self.lf_zigbee_mhr, text='Security Header')
        self.l_zigbee_mhr_sec_header.grid(row=6, column=1, sticky='w')
        self.e_zigbee_mhr_sec_header = ttk.Entry(self.lf_zigbee_mhr, width=8)
        self.e_zigbee_mhr_sec_header.grid(row=6, column=0, padx=10, pady=5, sticky='w')


        #############################
        ### 802.15.4 - MAC -> Command
        self.lf_zigbee_mac_cmd = ttk.LabelFrame(self.nb_zigbee, text='MAC Payload')
        # self.lf_zigbee_mac_cmd.grid(row=3, column=1, padx=5, pady=5, sticky='n')


        self.l_zigbee_mac_cmd_id_cmd = ttk.Label(self.lf_zigbee_mac_cmd, text='Cmd ID', width=GUI_PAYLOAD_WIDTH)
        self.l_zigbee_mac_cmd_id_cmd.grid(row=0, padx=5, pady=5, sticky='w')
        self.combo_zigbee_mac_cmd_id_cmd = ttk.Combobox(self.lf_zigbee_mac_cmd, values=list(ZIGBEE_MAC_CMD_ID_CMD.keys()))
        self.combo_zigbee_mac_cmd_id_cmd.grid(row=1, padx=5)

        self.l_zigbee_mac_cmd_payload_cmd = ttk.Label(self.lf_zigbee_mac_cmd, text='Cmd payload')
        self.l_zigbee_mac_cmd_payload_cmd.grid(row=2, padx=5, pady=5, sticky='w')
        self.e_zigbee_mac_cmd_payload_cmd = ttk.Entry(self.lf_zigbee_mac_cmd, width=20)
        self.e_zigbee_mac_cmd_payload_cmd.grid(row=3, padx=5, pady=5, sticky='w')


        #############################
        ### 802.15.4 - MAC -> Data
        self.lf_zigbee_mac_data = ttk.LabelFrame(self.nb_zigbee, text='MAC Payload')
        # self.lf_zigbee_mac_data.grid(row=3, column=1, padx=5, pady=5, sticky='n')

        self.l_zigbee_mac_data_payload = ttk.Label(self.lf_zigbee_mac_data, text='Data payload', width=GUI_PAYLOAD_WIDTH)
        self.l_zigbee_mac_data_payload.grid(row=0, padx=5, pady=5, sticky='w')
        self.e_zigbee_mac_data_payload = ttk.Entry(self.lf_zigbee_mac_data, width=20)
        self.e_zigbee_mac_data_payload.grid(row=1, padx=5, pady=5, sticky='w')

        #############################
        ### 802.15.4 - MAC -> Ack
        self.lf_zigbee_mac_ack = ttk.LabelFrame(self.nb_zigbee, text='MAC Payload')
        # self.lf_zigbee_mac_ack.grid(row=3, column=1, padx=5, pady=5, sticky='n')

        self.l_zigbee_mac_ack = ttk.Label(self.lf_zigbee_mac_ack, text='No payload', width=GUI_PAYLOAD_WIDTH)
        self.l_zigbee_mac_ack.grid(row=0, padx=5, pady=5, sticky='w')

        #############################
        ### 802.15.4 - MAC -> Beacon
        self.lf_zigbee_mac_beacon = ttk.LabelFrame(self.nb_zigbee, text='MAC Payload')
        # self.lf_zigbee_mac_beacon.grid(row=3, column=1, padx=5, pady=5, sticky='n')

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


        #############################
        ### Zigbee NWK header     ###
        #############################

        #############################
        ### Zigbee NWK Header -> FC
        self.lf_zigbee_nwk_head = ttk.LabelFrame(self.nb_zigbee, text='NWK header')
        self.lf_zigbee_nwk_head.grid(row=3, column=3, padx=5, pady=5, sticky='n')
        # self.lf_zigbee_nwk_head.grid(row=3, column=3, padx=5, sticky='n')

        self.lf_zigbee_nwkh_fc = ttk.LabelFrame(self.lf_zigbee_nwk_head, text='FC')
        self.lf_zigbee_nwkh_fc.grid(row=0, padx=5, pady=5, columnspan=2)

        self.l_zigbee_nwkh_fc_proto_ver = ttk.Label(self.lf_zigbee_nwkh_fc, text='Protocol Version')
        self.l_zigbee_nwkh_fc_proto_ver.grid(row=0, column=1, pady=5, sticky='w')
        self.e_zigbee_nwkh_fc_proto_ver = ttk.Entry(self.lf_zigbee_nwkh_fc, width=8)
        self.e_zigbee_nwkh_fc_proto_ver.grid(row=0, column=0, padx=5, sticky='w')

        self.l_zigbee_nwkh_fc_discover_route = ttk.Label(self.lf_zigbee_nwkh_fc, text='Discover Route')
        self.l_zigbee_nwkh_fc_discover_route.grid(row=1, column=1, sticky='w')
        self.e_zigbee_nwkh_fc_discover_route = ttk.Entry(self.lf_zigbee_nwkh_fc, width=8)
        self.e_zigbee_nwkh_fc_discover_route.grid(row=1, column=0, padx=5, sticky='w')

        self.c_zigbee_nwkh_fc_multicast = ttk.Checkbutton(self.lf_zigbee_nwkh_fc, text='Multicast Flag')
        self.c_zigbee_nwkh_fc_multicast.grid(row=2, padx=5, sticky='w')

        self.c_zigbee_nwkh_fc_security = ttk.Checkbutton(self.lf_zigbee_nwkh_fc, text='Security')
        self.c_zigbee_nwkh_fc_security.grid(row=3, padx=5, sticky='w')

        self.c_zigbee_nwkh_fc_source_route = ttk.Checkbutton(self.lf_zigbee_nwkh_fc, text='Source Route')
        self.c_zigbee_nwkh_fc_source_route.grid(row=4, padx=5, sticky='w')

        self.c_zigbee_nwkh_fc_dst_ieee_addr = ttk.Checkbutton(self.lf_zigbee_nwkh_fc, text='Dst IEEE Addr')
        self.c_zigbee_nwkh_fc_dst_ieee_addr.grid(row=5, padx=5, sticky='w')

        self.c_zigbee_nwkh_fc_src_ieee_addr = ttk.Checkbutton(self.lf_zigbee_nwkh_fc, text='Src IEEE Addr')
        self.c_zigbee_nwkh_fc_src_ieee_addr.grid(row=6, padx=5, sticky='w')

        #############################
        ### Zigbee NWK Header
        self.l_zigbee_nwkh_dst_addr = ttk.Label(self.lf_zigbee_nwk_head, text='Dst Addr')
        self.l_zigbee_nwkh_dst_addr.grid(row=1, column=1, sticky='w')
        self.e_zigbee_nwkh_dst_addr = ttk.Entry(self.lf_zigbee_nwk_head, width=8)
        self.e_zigbee_nwkh_dst_addr.grid(row=1, column=0, padx=5, sticky='w')

        self.l_zigbee_nwkh_src_addr = ttk.Label(self.lf_zigbee_nwk_head, text='Src Addr')
        self.l_zigbee_nwkh_src_addr.grid(row=2, column=1, sticky='w')
        self.e_zigbee_nwkh_src_addr = ttk.Entry(self.lf_zigbee_nwk_head, width=8)
        self.e_zigbee_nwkh_src_addr.grid(row=2, column=0, padx=5, pady=5, sticky='w')

        self.l_zigbee_nwkh_radius = ttk.Label(self.lf_zigbee_nwk_head, text='Radius')
        self.l_zigbee_nwkh_radius.grid(row=3, column=1, sticky='w')
        self.e_zigbee_nwkh_radius = ttk.Entry(self.lf_zigbee_nwk_head, width=8)
        self.e_zigbee_nwkh_radius.grid(row=3, column=0, padx=5, sticky='w')

        self.l_zigbee_nwkh_seq_num = ttk.Label(self.lf_zigbee_nwk_head, text='Sequence Number')
        self.l_zigbee_nwkh_seq_num.grid(row=4, column=1, sticky='w')
        self.e_zigbee_nwkh_seq_num = ttk.Entry(self.lf_zigbee_nwk_head, width=8)
        self.e_zigbee_nwkh_seq_num.grid(row=4, column=0, padx=5, pady=5, sticky='w')

        self.l_zigbee_nwkh_dst_ieee_addr = ttk.Label(self.lf_zigbee_nwk_head, text='Dst IEEE Addr')
        self.l_zigbee_nwkh_dst_ieee_addr.grid(row=5, column=1, sticky='w')
        self.e_zigbee_nwkh_dst_ieee_addr = ttk.Entry(self.lf_zigbee_nwk_head, width=8)
        self.e_zigbee_nwkh_dst_ieee_addr.grid(row=5, column=0, padx=5, sticky='w')

        self.l_zigbee_nwkh_src_ieee_addr = ttk.Label(self.lf_zigbee_nwk_head, text='Src IEEE Addr')
        self.l_zigbee_nwkh_src_ieee_addr.grid(row=6, column=1, sticky='w')
        self.e_zigbee_nwkh_src_ieee_addr = ttk.Entry(self.lf_zigbee_nwk_head, width=8)
        self.e_zigbee_nwkh_src_ieee_addr.grid(row=6, column=0, padx=5, pady=5, sticky='w')

        self.l_zigbee_nwkh_multicast_ctr = ttk.Label(self.lf_zigbee_nwk_head, text='Multicast Ctrl')
        self.l_zigbee_nwkh_multicast_ctr.grid(row=7, column=1, sticky='w')
        self.e_zigbee_nwkh_multicast_ctr = ttk.Entry(self.lf_zigbee_nwk_head, width=8)
        self.e_zigbee_nwkh_multicast_ctr.grid(row=7, column=0, padx=5, sticky='w')

        self.l_zigbee_nwkh_src_route_subf = ttk.Label(self.lf_zigbee_nwk_head, text='Src Route Sub-frame')
        self.l_zigbee_nwkh_src_route_subf.grid(row=8, column=1, sticky='w')
        self.e_zigbee_nwkh_src_route_subf = ttk.Entry(self.lf_zigbee_nwk_head, width=8)
        self.e_zigbee_nwkh_src_route_subf.grid(row=8, column=0, padx=5, pady=5, sticky='w')
        # self.e_zigbee_nwkh_src_route_subf.grid(row=8, column=0, padx=5, sticky='w')

        #############################
        ### Zigbee NWK PAYLOAD -> data

        self.lf_zigbee_nwk_payload_data = ttk.LabelFrame(self.nb_zigbee, text='NWK Payload')
        self.lf_zigbee_nwk_payload_data.grid(row=3, column=4, padx=5, pady=5, sticky='n')

        self.l_zigbee_nwk_data_payload = ttk.Label(self.lf_zigbee_nwk_payload_data,
                                                   text='Data payload',
                                                   width=GUI_PAYLOAD_WIDTH)
        self.l_zigbee_nwk_data_payload.grid(row=0, padx=5, pady=5)
        self.e_zigbee_nwk_data_payload = ttk.Entry(self.lf_zigbee_nwk_payload_data, width=10)
        self.e_zigbee_nwk_data_payload.grid(row=1, padx=5, pady=5, sticky='w')

        #############################
        ### Zigbee NWK PAYLOAD -> NWK cmd

        self.lf_zigbee_nwk_payload_cmd = ttk.LabelFrame(self.nb_zigbee, text='NWK Payload')
        self.lf_zigbee_nwk_payload_cmd.grid(row=3, column=4, padx=5, pady=5, sticky='n')

        self.l_zigbee_nwk_id_cmd = ttk.Label(self.lf_zigbee_nwk_payload_cmd,
                                                         text='NWK ID Cmd',
                                                         width=GUI_PAYLOAD_WIDTH)
        self.l_zigbee_nwk_id_cmd.grid(row=0, padx=5, pady=5)
        self.combo_zigbee_nwk_id_cmd = ttk.Combobox(self.lf_zigbee_nwk_payload_cmd,
                                                                     value=list(ZIGBEE_NWK_CMD_ID.keys()))
        self.combo_zigbee_nwk_id_cmd.grid(row=1, padx=5, sticky='w')

        self.l_zigbee_nwk_cmd_payload = ttk.Label(self.lf_zigbee_nwk_payload_cmd, text='NWK Cmd Payload')
        self.l_zigbee_nwk_cmd_payload.grid(row=2, padx=5, pady=5, sticky='w')
        self.e_zigbee_nwk_cmd_payload = ttk.Entry(self.lf_zigbee_nwk_payload_cmd, width=10)
        self.e_zigbee_nwk_cmd_payload.grid(row=3, padx=5, pady=5, sticky='w')




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

    def __set_zigbee_nwk_type_frame(self, event):
        current_nwk_type = event.widget.get()
        print(current_nwk_type)

        if current_nwk_type == 'DATA':
            self.lf_zigbee_nwk_payload_cmd.grid_remove()
            self.lf_zigbee_nwk_payload_data.grid()

        elif current_nwk_type == 'NWK_CMD':
            self.lf_zigbee_nwk_payload_cmd.grid()
            self.lf_zigbee_nwk_payload_data.grid_remove()

        else:
            self.lf_zigbee_nwk_payload_cmd.grid_remove()
            self.lf_zigbee_nwk_payload_data.grid_remove()




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
