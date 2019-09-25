# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

__author__ = 'lem'

import lrwpan.ieee802_15_4 as ieee802_15_4
                                                        # Values of the Nwk Frame Type field
ZIGBEE_NWK_FRAME_TYPE           = {                     # b1 b0
                                    'Data'      : 0x0,  #  0  0
                                    'Nwk CMD'   : 0x1,  #  0  1
                                    'Reserved'  : 0x2,  #  1  0
                                    'Inter-PAN' : 0x3   #  1  1
                                    }
ZIGBEE_NWK_FC_DISCOVER_ROUTE    = {
                                    'Suppress route'  : 0x0,
                                    'Enable route'    : 0x1,
                                    'Reserved 0x2'              : 0x2,
                                    'Reserved 0x3'              : 0x3,
                                    }

ZIGBEE_NWK_CMD_ID               = {
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

ZIGBEE_APS_FRAME_TYPE   = {
                                    'Data'                          : 0x0,
                                    'Cmd'                           : 0x1,
                                    'Ack'                           : 0x2,
                                    'Inter-PAN'                     : 0x3
                                    }

ZIGBEE_APS_FC_DELIVERY_MODE = {
                                    'Unicast'                       : 0x0,
                                    'Reserved'                      : 0x1,
                                    'Broadcast'                     : 0x2,
                                    'Group addr'                    : 0x3
                                    }

