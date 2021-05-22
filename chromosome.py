class Chromosome:

    def __init__(self):
        self._byte = bytes(b'\x00')

    def __init__(self, byte):
        self._byte = byte

    def get_int(self):
        return int.from_bytes(self._byte, byteorder="big")

    def bitwise_and_bytes(self, a, b):
        result_int = int.from_bytes(a, byteorder="big") & int.from_bytes(b, byteorder="big")
        return result_int.to_bytes(max(len(a), len(b)), byteorder="big")

    def bitwise_or_bytes(self, a, b):
        result_int = int.from_bytes(a, byteorder="big") | int.from_bytes(b, byteorder="big")
        return result_int.to_bytes(max(len(a), len(b)), byteorder="big")

    def bitwise_xor_bytes(self, a, b):
        result_int = int.from_bytes(a, byteorder="big") ^ int.from_bytes(b, byteorder="big")
        return result_int.to_bytes(max(len(a), len(b)), byteorder="big")

    def sex(self, other_chromosome):

        upper_part = self.bitwise_and_bytes(b'\xf0', self._byte)
        buttom_part = self.bitwise_and_bytes(bytes(b'\x0f'), other_chromosome._byte)

        # child
        return Chromosome(self.bitwise_or_bytes(upper_part, buttom_part))

    def __str__(self):
        return "byte: " + str(self._byte) + "\tDecimal: " + str(self.get_int())