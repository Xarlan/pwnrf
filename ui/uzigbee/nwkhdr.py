# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

__author__ = 'lem'

# This file contain GUI elements for IEEE 802.15.4 Mac Header

import tkinter as tk
from tkinter import ttk

import lrwpan

GUI_PAYLOAD_WIDTH       = 25
GUI_HEADER_PAYLOAD_ROW  = 4



class NwkHeader:
    """
    This class describe field for Zigbee NWK header
    """

    def __init__(self, parent):
        self.nwkh_parent = parent

        self.var_fc_multicast = tk.IntVar()
        self.var_fc_security = tk.IntVar()
        self.var_fc_src_route = tk.IntVar()
        self.var_fc_dst_ieee_addr = tk.IntVar()
        self.var_fc_src_ieee_addr = tk.IntVar()

        self.lf_zigbee_nwk_head = ttk.LabelFrame(self.nwkh_parent, text='NWK header')
        self.lf_zigbee_nwk_head.grid(row=GUI_HEADER_PAYLOAD_ROW, column=3, padx=5, pady=5, sticky='n')

        ################################
        ### Zigbee NWK Header -> FC  ###
        ################################
        self.lf_zigbee_nwkh_fc = ttk.LabelFrame(self.lf_zigbee_nwk_head, text='FC')
        self.lf_zigbee_nwkh_fc.grid(row=0, padx=5, pady=5, columnspan=2)

        self.l_zigbee_nwkh_fc_nwk_type = ttk.Label(self.lf_zigbee_nwkh_fc, text='Frame Type')
        self.l_zigbee_nwkh_fc_nwk_type.grid(row=0, column=1, padx=5)
        self.nwkh_fc_frame_type = ttk.Combobox(self.lf_zigbee_nwkh_fc,
                                                  value=list(lrwpan.ZIGBEE_NWK_FRAME_TYPE.keys()),
                                                  width=10)
        self.nwkh_fc_frame_type.grid(row=0, column=0, padx=5, sticky='we')


        self.l_zigbee_nwkh_fc_proto_ver = ttk.Label(self.lf_zigbee_nwkh_fc, text='Protocol Version')
        self.l_zigbee_nwkh_fc_proto_ver.grid(row=1, column=1, pady=5, sticky='w')
        self.nwkh_fc_proto_ver = ttk.Entry(self.lf_zigbee_nwkh_fc, width=8)
        self.nwkh_fc_proto_ver.grid(row=1, column=0, padx=5, sticky='w')

        self.l_zigbee_nwkh_fc_discover_route = ttk.Label(self.lf_zigbee_nwkh_fc, text='Discover Route')
        self.l_zigbee_nwkh_fc_discover_route.grid(row=2, column=1, sticky='w')
        self.nwkh_fc_discover_route = ttk.Entry(self.lf_zigbee_nwkh_fc, width=8)
        self.nwkh_fc_discover_route.grid(row=2, column=0, padx=5, sticky='w')

        self.nwkh_fc_multicast = ttk.Checkbutton(self.lf_zigbee_nwkh_fc, text='Multicast Flag')
        self.nwkh_fc_multicast.grid(row=3, padx=5, columnspan=2, sticky='w')

        self.nwkh_fc_security = ttk.Checkbutton(self.lf_zigbee_nwkh_fc, text='Security')
        self.nwkh_fc_security.grid(row=4, padx=5, sticky='w')

        self.nwkh_fc_source_route = ttk.Checkbutton(self.lf_zigbee_nwkh_fc, text='Source Route')
        self.nwkh_fc_source_route.grid(row=5, padx=5, sticky='w')

        self.nwkh_fc_dst_ieee_addr = ttk.Checkbutton(self.lf_zigbee_nwkh_fc,
                                                     text='Dst IEEE Addr',
                                                     variable=self.var_fc_dst_ieee_addr,
                                                     onvalue=0x800,
                                                     offvalue=0x0,                  # MHR -> FC -> b3
                                                     command=self._show_hide_ieee_addr)
        self.nwkh_fc_dst_ieee_addr.grid(row=6, padx=5, sticky='w')
        self.var_fc_dst_ieee_addr.set(0x0)

        self.nwkh_fc_src_ieee_addr = ttk.Checkbutton(self.lf_zigbee_nwkh_fc,
                                                     text='Src IEEE Addr',
                                                     variable=self.var_fc_src_ieee_addr,
                                                     onvalue=0x1000,
                                                     offvalue=0x0,
                                                     command=self._show_hide_ieee_addr)
        self.nwkh_fc_src_ieee_addr.grid(row=7, padx=5, sticky='w')
        self.var_fc_src_ieee_addr.set(0x0)

        #############################
        ### Zigbee NWK Header     ###
        #############################
        self.l_zigbee_nwkh_dst_addr = ttk.Label(self.lf_zigbee_nwk_head, text='Dst Addr')
        self.l_zigbee_nwkh_dst_addr.grid(row=1, column=1, sticky='w')
        self.nwkh_dst_addr = ttk.Entry(self.lf_zigbee_nwk_head, width=8)
        self.nwkh_dst_addr.grid(row=1, column=0, padx=5, sticky='w')

        self.l_zigbee_nwkh_src_addr = ttk.Label(self.lf_zigbee_nwk_head, text='Src Addr')
        self.l_zigbee_nwkh_src_addr.grid(row=2, column=1, sticky='w')
        self.nwkh_src_addr = ttk.Entry(self.lf_zigbee_nwk_head, width=8)
        self.nwkh_src_addr.grid(row=2, column=0, padx=5, pady=5, sticky='w')

        self.l_zigbee_nwkh_radius = ttk.Label(self.lf_zigbee_nwk_head, text='Radius')
        self.l_zigbee_nwkh_radius.grid(row=3, column=1, sticky='w')
        self.nwkh_radius = ttk.Entry(self.lf_zigbee_nwk_head, width=8)
        self.nwkh_radius.grid(row=3, column=0, padx=5, sticky='w')

        self.l_zigbee_nwkh_seq_num = ttk.Label(self.lf_zigbee_nwk_head, text='Sequence Number')
        self.l_zigbee_nwkh_seq_num.grid(row=4, column=1, sticky='w')
        self.nwkh_seq_num = ttk.Entry(self.lf_zigbee_nwk_head, width=8)
        self.nwkh_seq_num.grid(row=4, column=0, padx=5, pady=5, sticky='w')

        self.l_zigbee_nwkh_dst_ieee_addr = ttk.Label(self.lf_zigbee_nwk_head, text='Dst IEEE Addr')
        self.l_zigbee_nwkh_dst_ieee_addr.grid(row=5, column=1, sticky='w')
        self.nwkh_dst_ieee_addr = ttk.Entry(self.lf_zigbee_nwk_head, width=8)
        self.nwkh_dst_ieee_addr.grid(row=5, column=0, padx=5, sticky='w')

        self.l_zigbee_nwkh_src_ieee_addr = ttk.Label(self.lf_zigbee_nwk_head, text='Src IEEE Addr')
        self.l_zigbee_nwkh_src_ieee_addr.grid(row=6, column=1, sticky='w')
        self.nwkh_src_ieee_addr = ttk.Entry(self.lf_zigbee_nwk_head, width=8)
        self.nwkh_src_ieee_addr.grid(row=6, column=0, padx=5, pady=5, sticky='w')

        self.l_zigbee_nwkh_multicast_ctr = ttk.Label(self.lf_zigbee_nwk_head, text='Multicast Ctrl')
        self.l_zigbee_nwkh_multicast_ctr.grid(row=7, column=1, sticky='w')
        self.nwkh_multicast_ctr = ttk.Entry(self.lf_zigbee_nwk_head, width=8)
        self.nwkh_multicast_ctr.grid(row=7, column=0, padx=5, sticky='w')

        self.l_zigbee_nwkh_src_route_subf = ttk.Label(self.lf_zigbee_nwk_head, text='Src Route Sub-frame')
        self.l_zigbee_nwkh_src_route_subf.grid(row=8, column=1, sticky='w')
        self.nwkh_src_route_subf = ttk.Entry(self.lf_zigbee_nwk_head, width=8)
        self.nwkh_src_route_subf.grid(row=8, column=0, padx=5, pady=5, sticky='w')

        self._show_hide_ieee_addr()

    def _show_hide_ieee_addr(self):

        # show / hide IEEE Dst Addr
        if self.var_fc_dst_ieee_addr.get() == 0x800:
            self.nwkh_dst_ieee_addr.grid()
            self.l_zigbee_nwkh_dst_ieee_addr.grid()
        else:
            self.nwkh_dst_ieee_addr.grid_remove()
            self.l_zigbee_nwkh_dst_ieee_addr.grid_remove()

        # show / hide IEEE Src Addr
        if self.var_fc_src_ieee_addr.get() == 0x1000:
            self.nwkh_src_ieee_addr.grid()
            self.l_zigbee_nwkh_src_ieee_addr.grid()
        else:
            self.nwkh_src_ieee_addr.grid_remove()
            self.l_zigbee_nwkh_src_ieee_addr.grid_remove()


if __name__ == '__main__':
    root = tk.Tk()
    NwkHeader(root)
    root.mainloop()