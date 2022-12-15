import hashlib
import time
import json


class Message:

    def __init__(self, data):
        self.hash = None
        self.prev_hash = None
        self.timestamp = time.time()
        self.data = data
        self.payload_hash = self.__get_payload_hash()

    def __get_payload_hash(self):
        return hashlib.sha256(bytearray(str(self.data), "utf-8")).hexdigest()

    def link(self, msg):
        self.prev_hash = msg.hash
        return self




class Block:

    def __init__(self, *args):
        self.messages = []
        self.timestamp = None
        self.prev_hash = None
        self.hash = None
        if args:
            for arg in args:
                self.add_message(arg)

    def add_message(self, msg):
        if len(self.messages) > 0:
            msg.link(self.messages[-1])
        self.messages.append(msg)

    def link(self, block):
        self.prev_hash = block.hash


class Blockchain:
    
    def __init__(self):
        self.blocks = []

    def add_block(self, block):
        if len(self.blocks) > 0:
            block.prev_hash = self.blocks[-1].hash
        self.blocks.append(block)
    
    def add_pres(self, pres):
        B1 = Block()
        B1.add_message(Message(pres))
        self.add_block(B1)
        


# prescription1 = {"Patient Name" : "Haritarth Bhardwaj", "Doctor Name" : "Suraj Sharma", "Medicines Prescribed" : "Paracetamol"}
# prescription2 = {"Patient Name" : "Vaishnavi Bhardwaj", "Doctor Name" : "Suraj Sharma", "Medicines Prescribed" : "Paracetamol"}

# B1 = Block()
# B1.add_message(Message(prescription1))

# B2 = Block()
# B2.add_message(Message(prescription2))

# chain = Blockchain()
# chain.add_block(B1)
# chain.add_block(B2)

# print(len(chain.blocks))


