# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

__author__ = 'lem'

# ZIGBEE_LAYER            = ['MAC', 'NWK', 'APS']
                                                                # Values of the Frame Type field
IEEE_802_15_4_MAC_TYPE         = {                              # b2 b1 b0
                                    'BEACON'    : 0x0,          #  0  0  0
                                    'DATA'      : 0x1,          #  0  0  1
                                    'ACK'       : 0x2,          #  0  1  0
                                    'CMD'       : 0x3           #  0  1  1
                                    }

                                                                # Values of the Destination Addressing Mode
IEEE_802_15_4_MAC_DST_ADDR_MODE = {                             # b11 b10
                                    'NOT PAN/addr'  : 0x0,      #  0   0
                                    'Reserved'      : 0x400,    #  0   1
                                    '16 bit'        : 0x800,    #  1   0
                                    '64 bit'        : 0xC00     #  1   1
                                    }

                                                                 # Values of the Source Addressing Mode
IEEE_802_15_4_MAC_SRC_ADDR_MODE = {                              # b15 b14
                                    'NOT PAN/addr'  : 0x0,       #  0   0
                                    'Reserved'      : 0x4000,    #  0   1
                                    '16 bit'        : 0x8000,    #  1   0
                                    '64 bit'        : 0xC000     #  1   1
                                    }