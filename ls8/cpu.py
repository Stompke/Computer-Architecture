"""CPU functionality."""

import sys

hard_code_program = [
    # From print8.ls8
    0b10000010, # LDI R0,8
    0b00000000,
    0b00001000,
    0b01000111, # PRN R0
    0b00000000,
    0b00000001, # HLT
]








class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.pc = 0
        self.running = True
        self.register = [0] * 8 
    
    def ram_read(self, MAR):
        return self.ram[MAR]

    def ram_write(self, MDR, MAR):
        self.ram[MAR] = MDR

    def load(self, file = hard_code_program):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        hard_code_program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in file:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""

        def LDI(operand_a, operand_b):
            self.register[operand_a] = operand_b
            self.pc += 3

        def PRN(operand_a, operand_b):
            print(self.register[operand_a])
            self.pc += 2

        def MUL(operand_a, operand_b):
            self.register[operand_a] = self.register[operand_a] * self.register[operand_b]
            self.pc += 3

        def HLT(operand_a, operand_b):
            self.running = False

        
        branch_table = {
            0b10000010 : LDI,
            0b01000111 : PRN,
            0b00000001 : HLT,
            0b10100010 : MUL
        }


        while self.running:
            IR = self.ram[self.pc]
            # print('pc', self.pc)
            # print('register', self.register)
            # if 0b10000010 == IR:
            #     print('IR', IR)
            #     print('its the same...')
            # else:
            #     print('IR', IR)
            #     print('not equal.....')
            operand_a = self.ram[self.pc + 1]
            operand_b = self.ram[self.pc + 2]

            branch_table[IR](operand_a, operand_b)
            

            

            # if IR == LDI: # LDI
            #     self.register[operand_a] = operand_b
            #     self.pc += 3

            # elif IR == PRN: # PRN
            #     print(self.register[operand_a])
            #     self.pc += 2


            # elif IR == HLT: #HLT
            #     self.running = False

            # else:
            #     print('whattt is thatt?', self.pc)
            #     print('IR', IR)
            #     self.pc += 1
            #     continue