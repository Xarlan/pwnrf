# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

__author__ = 'lem'

import struct


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

        self._magic_var = None

        self.mac_fc_frame_type = frame_type
        self.mac_fc_security_enable = None
        self.mac_fc_frame_pending = None
        self.mac_fc_ar = None
        self.mac_fc_pandid_compression = None
        self.mac_fc_reserved = 0
        self.mac_fc_dst_addr_mode = None
        self.mac_fc_frame_ver = None
        self.mac_fc_src_addr_mode = None

        self.mac_sequence_number = None
        self.mac_dst_pan_id = None
        self.mac_dst_addr = None
        self.mac_src_pan_id = None
        self.mac_src_addr = None

    # def build_mac_fc(self):
    #     mac_hdr = []
    #
    #     mac_fc = self.mac_fc_frame_type
    #     mac_fc |= (self.mac_fc_security_enable << 3)
    #     mac_fc |= (self.mac_fc_frame_pending << 4)
    #     mac_fc |= (self.mac_fc_ar << 5)
    #     mac_fc |= (self.mac_fc_pandid_compression << 6)
    #     mac_fc |= (self.mac_fc_reserved << 7)
    #     mac_fc |= (self._mac_src_addr_mode << 14)
    #
    #     mac_hdr.append(mac_fc & 0xFF)
    #     mac_hdr.append((mac_fc & 0xFF00) >> 8)
    #
    #     return mac_hdr

    @property
    def magic_var(self):
        return self._magic_var

    @magic_var.setter
    def magic_var(self, args):
        print(args)
        print("test setter")

    def build_mac_hdr(self):
        """
        Generate IEEE 802.15.4 Mac Header
        :return:    list of mac header
        """
        mac_hdr = []

        mac_fc = self.mac_fc_frame_type
        mac_fc |= self.mac_fc_security_enable
        mac_fc |= self.mac_fc_frame_pending
        mac_fc |= self.mac_fc_ar
        mac_fc |= self.mac_fc_pandid_compression
        mac_fc |= self.mac_fc_reserved
        mac_fc |= self.mac_fc_dst_addr_mode
        mac_fc |= self.mac_fc_frame_ver
        mac_fc |= self.mac_fc_src_addr_mode

        mac_hdr.append(mac_fc & 0xFF)
        mac_hdr.append((mac_fc & 0xFF00) >> 8)

        mac_hdr.append(self.mac_sequence_number)

        # IEEE 802.15.4
        # 5.2.1.3 Destination PAN Identifier field
        if self.mac_fc_dst_addr_mode != 0:
            mac_hdr.append(self.mac_dst_pan_id & 0xFF)
            mac_hdr.append((self.mac_dst_pan_id & 0xFF00) >> 8)

        # IEEE 802.15.4
        # 5.2.1.4 Destination Address field
        if self.mac_fc_dst_addr_mode != 0:
            if isinstance(self.mac_dst_addr, int):
                mac_hdr.append(self.mac_dst_addr & 0xFF)
                mac_hdr.append((self.mac_dst_addr & 0xFF00) >> 8)
            else:
                for addr in self.mac_dst_addr[::-1]:
                    mac_hdr.append(addr)

        # IEEE 802.15.4
        # 5.2.1.5 Source PAN Identifier field
        if (self.mac_fc_src_addr_mode != 0) and (self.mac_fc_pandid_compression == 0):
            mac_hdr.append(self.mac_src_pan_id & 0xFF)
            mac_hdr.append((self.mac_src_pan_id & 0xFF00) >> 8)

        # IEEE 802.15.4
        # 5.2.1.6 Source Address field
        if self.mac_fc_src_addr_mode !=0:
            if isinstance(self.mac_src_addr, int):
                mac_hdr.append(self.mac_src_addr & 0xFF)
                mac_hdr.append((self.mac_src_addr & 0xFF00) >> 8)
            else:
                for addr in self.mac_src_addr[::-1]:
                    mac_hdr.append(addr)

        # IEEE 802.15.4
        # 5.2.1.7 Auxiliary Security Header field
        if self.mac_fc_security_enable:
            pass
            # here to write code to add aux security header

        return mac_hdr

    @staticmethod
    def validate_16bits(raw_value, name_field='no name'):
        """
        This function to check Src/Dst Addr, PAN ID and other value in 802.15.4/ZigBee protocol which field is 16 bits
        :param name_field:  which field we are check Src/Dst Addr, or PanID or other fields
        :param raw_value:   raw value, it may be "str" or int
        :return:            correct value or raise exception
        """
        err_msg = '[' + name_field + '] wrong value'
        if isinstance(raw_value, str):
            try:
                raw_value = int(raw_value, 16)

            except ValueError:
                if len(raw_value) == 0:
                    return None
                else:
                    raise ValidationError(err_msg)

        if raw_value in range(0, 0x10000):
            return raw_value

        else:
            raise ValidationError(err_msg)

    @staticmethod
    def validate_bytes(raw_value, name_field='no name', addr_64bits=True):
        """
        Check if Src/Dst addr is correct 64 bit address
        :param addr_64bits: Check IEEE 64 bits address or check stream of bytes
        :param raw_value:   raw input addr
        :param name_field:  which field is checked
        :return:            correct address
        """
        err_msg = '[' + name_field + '] wrong value'

        if isinstance(raw_value, str):
            try:
                addr = [int(x, 16) for x in raw_value.split(":")]

            except ValueError:
                raise ValidationError(err_msg)

            else:
                # Check IEEE addr / 64 bits address in MAC/NWK layers
                if addr_64bits:
                    if (len(addr) == 8) and (all(i <= 0xFF for i in addr)):
                        return addr
                    else:
                        raise ValidationError(err_msg)

                # check bytes sentence
                else:
                    if all(i <= 0xFF for i in addr):
                        return addr
                    else:
                        raise ValidationError(err_msg)

    @staticmethod
    def validate_mac_addr(raw_value, name_field='no name'):
        """

        :param raw_value:
        :param name_field:
        :return:        correct short address (16 bits, int) or IEEE addr (64 bits, list)
        """
        try:
            mac_addr = Ieee802MacHdr.validate_16bits(raw_value, name_field)

        except ValidationError as e:
            mac_addr = Ieee802MacHdr.validate_bytes(raw_value, name_field)

        return mac_addr

    # @staticmethod
    # def check_16bit_64bit_addr(raw_addr):
    #
    #     if isinstance(raw_addr, int):
    #         if raw_addr in range(0, 0x10000):
    #             return raw_addr
    #         else:
    #             raise ValidationError('[short address] wrong value')
    #
    #
    #     elif isinstance(raw_addr, str):
    #         if raw_addr and len(raw_addr) > 0:
    #             try:
    #                 addr = [int(x, 16) for x in raw_addr.split(":")]
    #
    #             except ValueError:
    #                 raise ValidationError('[IEEE addr] wrong value')
    #
    #             else:
    #                 if (len(addr) == 8) and (all(i <= 0xFF for i in addr)):
    #                         return addr
    #
    #                 elif len(addr) == 1 and addr[0] <= 0x10000:
    #                     return addr[0]
    #
    #                 else:
    #                     raise ValidationError('[addr] wrong value')
    #
    #         elif len(raw_addr) == 0:
    #             return raw_addr
    #
    #     else:
    #         raise ValidationError('[IEEE addr] or [short addr] wrong value')



class Ieee802Beacon(Ieee802MacHdr):
    """
    IEEE 802.15.4 Beacon frame
    """

    def __init__(self):
        Ieee802MacHdr.__init__(frame_type=0x0)


class Ieee802Data(Ieee802MacHdr):
    """
    IEEE 802.15.4 Data frame
    """

    def __init__(self):
        Ieee802MacHdr.__init__(frame_type=0x1)
        self.mac_data_payload = None


class Ieee802Ack(Ieee802MacHdr):
    """
    IEEE 802.15.4 Ack frame
    """

    def __init__(self):
        Ieee802MacHdr.__init__(frame_type=0x2)


class Ieee802Cmd(Ieee802MacHdr):
    """
    IEEE 802.15.4 Mac Cmd frame
    """

    def __init__(self):
        Ieee802MacHdr.__init__(self, frame_type=0x3)
        self.mac_cmd_id = None
        self.mac_cmd_payload = None

    def tx_frame(self):
        """
        Create frame to transmit
        :return:
        """
        mac_header = self.build_mac_hdr()
        mac_payload = [self.mac_cmd_id]

        mac_payload.extend(self.mac_cmd_payload)

        frame = struct.pack('%dB' % len(mac_header), mac_header)

        frame += struct.pack('%dB' % len(mac_payload), mac_payload)

        print(frame)


