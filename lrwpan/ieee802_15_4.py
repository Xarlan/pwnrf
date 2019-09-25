# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

__author__ = 'lem'

# ZIGBEE_LAYER            = ['MAC', 'NWK', 'APS']
IEEE_802_15_4_FC_FRAME_VER = ['802.15.4-2003', '802.15.4']

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

IEEE_802_15_4_MAC_CMD_ID           = {
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


class ValidationError(Exception):

    def __init__(self, msg='Validation Error'):
        self.msg = msg


class Ieee802MacHdr:
    """
    Basic class, Consist field for IEEE 802.15.4 MAC Header
    """

    def __init__(self, frame_type):
        self.mac_fc_frame_type = frame_type
        self.mac_fc_security_enable = None
        self.mac_fc_frame_pending = None
        self.mac_fc_ar = None
        self.mac_fc_pandid_compression = None
        self.mac_fc_reserved = None
        self.mac_fc_dst_addr_mode = None
        self.mac_fc_frame_ver = None
        self.mac_fc_src_addr_mode = None

        self.mac_sequence_number = None
        self.mac_dst_pan_id = None
        self.mac_dst_addr = None
        self.mac_src_pan_id = None
        self.mac_src_addr = None

    def build_mac_fc(self):
        mac_hdr = []

        mac_fc = self.mac_fc_frame_type
        mac_fc |= (self.mac_fc_security_enable << 3)
        mac_fc |= (self.mac_fc_frame_pending << 4)
        mac_fc |= (self.mac_fc_ar << 5)
        mac_fc |= (self.mac_fc_pandid_compression << 6)
        mac_fc |= (self.mac_fc_reserved << 7)
        mac_fc |= (self._mac_src_addr_mode << 14)

        mac_hdr.append(mac_fc & 0xFF)
        mac_hdr.append((mac_fc & 0xFF00) >> 8)

        return mac_hdr

    @staticmethod
    def check_16bit_64bit_addr(raw_addr):

        if isinstance(raw_addr, int):
            if raw_addr in range(0, 0x10000):
                return raw_addr
            else:
                raise ValidationError('[short address] wrong value')


        elif isinstance(raw_addr, str):
            if raw_addr and len(raw_addr) > 0:
                try:
                    addr = [int(x, 16) for x in raw_addr.split(":")]

                except ValueError:
                    raise ValidationError('[IEEE addr] wrong value')

                else:
                    if (len(addr) == 8) and (all(i <= 0xFF for i in addr)):
                            return addr

                    elif len(addr) == 1 and addr[0] <= 0x10000:
                        return addr[0]

                    else:
                        raise ValidationError('[addr] wrong value')

            elif len(raw_addr) == 0:
                return raw_addr
        else:
            raise ValidationError('[IEEE addr] or [short addr] wrong value')



class Ieee802Ack(Ieee802MacHdr):
    """
    IEEE 802.15.4 Ack frame
    """

    def __init__(self):
        Ieee802MacHdr.__init__(frame_type=0x2)