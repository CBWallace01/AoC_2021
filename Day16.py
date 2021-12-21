import math

from PuzzleInput import ReadInput
import numpy as np

pz_input = ReadInput(16).data
print(pz_input)
# pz_input = ['A0016C880162017C3686B18A3D4780']


class Packet:
    def __init__(self, bin_str):
        self.bin_str = bin_str
        self.version = int(bin_str[:3], 2)
        self.type_id = int(bin_str[3:6], 2)
        self.children = []
        self.value = None

    def process_packet(self):
        index = 6
        if self.type_id == 4:
            keep_scanning = True
            bin_val = ""
            while keep_scanning:
                keep_scanning = self.bin_str[index] == '1'
                bin_val += self.bin_str[index+1: index+5]
                index += 5
            self.value = int(bin_val, 2)
        else:
            length_type = int(self.bin_str[index])
            if length_type == 0:
                length = int(self.bin_str[index+1:index+16], 2)
                index += 16
                child_bin = self.bin_str[index: index+length]
                offset = 0
                while offset < length:
                    new_child = Packet(child_bin[offset:])
                    offset += new_child.process_packet()
                    self.children.append(new_child)
                index += length
            elif length_type == 1:
                child_count = int(self.bin_str[index+1:index+12], 2)
                index += 12
                child_bin = self.bin_str[index:]
                offset = 0
                for _ in range(child_count):
                    new_child = Packet(child_bin[offset:])
                    offset += new_child.process_packet()
                    self.children.append(new_child)
                index += offset

            if self.type_id == 0:
                self.value = sum([x.value for x in self.children])
            elif self.type_id == 1:
                self.value = math.prod([x.value for x in self.children])
            elif self.type_id == 2:
                self.value = min([x.value for x in self.children])
            elif self.type_id == 3:
                self.value = max([x.value for x in self.children])
            elif self.type_id == 5:
                self.value = 1 if self.children[0].value > self.children[1].value else 0
            elif self.type_id == 6:
                self.value = 1 if self.children[0].value < self.children[1].value else 0
            elif self.type_id == 7:
                self.value = 1 if self.children[0].value == self.children[1].value else 0
        return index


def sum_versions(packet):
    child_total = 0
    for child in packet.children:
        child_total += sum_versions(child)
    return packet.version + child_total


def part_a():
    binary = bin(int(pz_input[0], 16))[2:].zfill(4 * len(pz_input[0]))
    parent_packet = Packet(binary)
    parent_packet.process_packet()
    return sum_versions(parent_packet)


def part_b():
    binary = bin(int(pz_input[0], 16))[2:].zfill(4 * len(pz_input[0]))
    parent_packet = Packet(binary)
    parent_packet.process_packet()
    return parent_packet.value


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
