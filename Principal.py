'''
Created on 10/10/2012

@author: VALE!!!!!
'''
import re
class ensamblador():
    def __init__(self):
        self.linea = ['','','','','']
    def tipo_op(self):
        pass
    
    def fetch_instruction(self):
        pass
    def parser(self,linea):
        m=linea.split(' ')
        #print m[0]
        return m[0]
    ## unificar y hacer un solo parser no tengo ganas de pensar
    def parser2(self,linea,tipo_ins):
        print "tipo dentro de parser",tipo_ins
        m=linea.split(',')
        ## es una chanchada
        mprimer=m[0].split(' ')
        print mprimer[1]
    def save(self):
        pass
    def open_asm(self):
        f = open("archivo.asm", "r")
        i=0
        while True:
            self.linea.insert(i, f.readline()) 
            if not self.linea[i]: break
            i=i+1
        print self.linea[1]
        return self.linea

    def tipo_instruccion(self,n):
        tipo_R={"SLL":0x00,"SRL":0x02,"SRA":0x03, "SRLV":0x06, "SRAV":0x07, "ADD":0x20, "SLLV":0x40,"ADDU":0x21, "SUB":0x22,"SUBU":0x23, "AND":0x24,"OR":0x25, "XOR":0x26,"NOR":0x27, "SLT":0x2A,"SLTU":0x2B}
        tipo_I={"LB":0x20,"LH":0x21,"LW":0x23, "LWU":0x27, "LBU":0x24, "LHU":0x25, "SB":0xA8,"SH":0x29, "SW":0x2B,"ADDI":0x08, "ADDIU":0x09,"ANDI":0x0C, "ORI":0x0D,"XORI":0x0E, "LUI":0x0F,"SLTI":0x0A,"SLTIU":0x0B, "BEQ":0x04,"BNE":0x05,"J":0x02, "JAL":0x03}
        tipo_J={"JR":0x08, "JALR":0x09}
        VECTOR=[tipo_R,tipo_I,tipo_J]
        lista=["juan","carlos","juncito"]
        hector=re.match(lista, "carlos")
        print hector.group(0)
        i=0
        for s in VECTOR:
            i = i+1
            try:
                
                print s[n]
                tipo_ins = i
            except:
                print ""  
            
        #a=tipo_R['JR']
        print "tipo instr",tipo_ins
        
        return tipo_ins
    def ordenar(self,linea,tipo_ins):
        print parseado ## este metodo se encarga de sabiendo el tipo de operacion armar el codigo
        juancito=asm.parser2(linea,tipo_ins)
        print juancito


if __name__ == '__main__':
    asm = ensamblador()
    linea = asm.open_asm() 
    #for a in linea:
    #print linea
    parseado = asm.parser(linea[1])
    tipo=asm.tipo_instruccion('JR')
    ## una vez que obtengo el tipo de instruccion puedo empezar a almacenar.. 
    asm.ordenar(linea[1],tipo)