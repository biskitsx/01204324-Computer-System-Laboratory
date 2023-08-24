def createLabel(line: str, index: int, symbolTable: dict):
    label = line[1:-1]
    symbolTable[label] = index

def getAsmCode(code: str, symbolTable: dict) -> list[str]:
    asmCode = code.strip()
    lines = asmCode.split("\n")
    inst = []
    for line in lines:
        commentIndex = line.find("//")
        if commentIndex != -1 : # found comment
            line = line[:commentIndex]
        if line == '':
            continue
        inst.append(line.strip())

    asmCodeFinal = []
    index = 0 
    for line in (inst):
        if line[0] == "(":
            createLabel(line, index, symbolTable)
            continue
        asmCodeFinal.append(line)
        index += 1 
    return asmCodeFinal

def createSymbolTable() -> dict:
    symbol = {
        "SP": 0,
        "LCL": 1,
        "ARG": 2,
        "THIS": 3,
        "THAT": 4,
        "R0": 0,
        "R1": 1,
        "R2": 2,
        "R3": 3,
        "R4": 4,
        "R5": 5,
        "R6": 6,
        "R7": 7,
        "R8": 8,
        "R9": 9,
        "R10": 10,
        "R11": 11,
        "R12": 12,
        "R13": 13,
        "R14": 14,
        "R15": 15,
        "SCREEN": 16384,
        "KBD": 24576
    }
    return symbol

def isInt(text: str) -> bool:
    try:
        int(text)
        return True
    except:
        return False

def createDestField() -> dict:
    return {
        "M": "001",
        "D": "010",
        "MD": "011",
        "A": "100",
        "AM": "101",
        "AD": "110",
        "AMD": "111",
    }

def createJumpField() -> dict:
    return {
        "JGT": "001",
        "JEQ": "010",
        "JGE": "011",
        "JLT": "100",
        "JNE": "101",
        "JLE": "110",
        "JMP": "111",
    }

def createComputeField() -> dict:
    return {
        "0": "101010",
        "1": "111111",
        "-1": "111010",
        "D": "001100",
        "A": "110000",
        "M": "110000",
        "!D": "001101",
        "!A": "110001",
        "!M": "110001",
        "-D": "001111",
        "-A": "110011",
        "-M": "110011",
        "D+1": "011111",
        "A+1": "110111",
        "M+1": "110111",
        "D-1": "001110",
        "A-1": "110010",
        "M-1": "110010",
        "D+A": "000010",
        "D+M": "000010",
        "D-A": "010011",
        "D-M": "010011",
        "A-D": "000111",
        "M-D": "000111",
        "D&A": "000000",
        "D&M": "000000",
        "D|A": "010101",
        "D|M": "010101",
    }

def findA(code: str) -> chr:
    index = code.find("M")
    if index != -1 :
        return "1"
    return "0"

def assemble(code: str)-> list[int]:
    # variable
    symbolTable = createSymbolTable()
    asmCode = getAsmCode(code, symbolTable)
    newSymbolCount = 16

    # field
    destField = createDestField()
    jumpField = createJumpField()
    compField = createComputeField()

    # output
    instructionSet = []
    for line in asmCode :
        # A - Instruction
        if line[0] == "@":
            symbol = line[1:]
            if (isInt(symbol)):
                instructionSet.append(int(symbol))
            else :
                val = symbolTable.get(symbol)
                if val == None:
                    symbolTable[symbol] = newSymbolCount
                    instructionSet.append(int(newSymbolCount))
                    newSymbolCount += 1
                else :
                    instructionSet.append(int(val))
                    
        # C - Instruction
        else :
            #  compute
            if line.find(';') == -1 :
                dest, comp = line.split("=")
                a = findA(comp)
                instructionC =  "111" + a + compField[comp] + destField[dest] + "000"
            # jump 
            else :
                comp, jump = line.split(";")
                a = findA(comp)
                instructionC = "111" + a + compField[comp] + "000" + jumpField[jump]
            
            instructionSet.append(int(instructionC, 2))
    return instructionSet


