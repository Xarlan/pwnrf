# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

__author__ = 'lem'

# ZIGBEE_LAYER            = ['MAC', 'NWK', 'APS']
                                                            # Values of the Frame Type field
IEEE_802_15_4_MAC_TYPE         = {                          # b2 b1 b0
                                    'BEACON'    : 0x0,      #  0  0  0
                                    'DATA'      : 0x1,      #  0  0  1
                                    'ACK'       : 0x2,      #  0  1  0
                                    'CMD'       : 0x3       #  0  1  1
                                    }