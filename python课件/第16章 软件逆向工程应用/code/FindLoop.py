from immlib import *
from immutils import *
import getopt

DESC=""" Find natural loops given a function start address """

def usage(imm):
    imm.log("!findloop -a <address>")
    imm.log("-a (function start address)")
    imm.log("-h This help")

def main(args):
    imm = Debugger()
    try:
        opts, argo = getopt.getopt(args, "a:")
    except:
        return usage(imm)
    for o,a in opts:
        if o == "-a":
            loops = imm.findLoops(int(a,16))
            for loop in loops:
                imm.log("LOOP! from:0x%08x, to:0x%08x"%(loop[0],loop[1]),loop[0])
                
                func = imm.getFunction(int(a,16))
                bbs = func.getBasicBlocks()
                
                #寻找第一个和最后一个节点
                first = 0xffffffff
                last = 0
                for node in loop[2]:
                    if node < first: first = node
                    if node > last: last = node
                
                #标记循环节点，但如果存在任何形式的注释就不做任何改变
                for node in loop[2]:
                    imm.log("    Loop node:0x%08x"%node,node)
                    for bb in bbs:
                        if bb.getStart() == node:
                            instrs = bb.getInstructions(imm)
                            for op in instrs:
                                if not imm.getComment(op.getAddress()) and op.getAddress() != node:
                                    if node == last and op.getAddress() == instrs[-1].getAddress():
                                        #最后一个节点的最后一个指令
                                        imm.setComment(op.getAddress(), "/")
                                    else:
                                        imm.setComment(op.getAddress(), "|")

                    if not imm.getComment(node):
                        if node == first:
                            imm.setComment(node, "\ Loop 0x%08X Node"%(loop[0]))
                        else:
                            imm.setComment(node, "| Loop 0x%08X Node"%(loop[0]))
                                    
            return "Done!"
        if o =="-h":
            return usage(imm)
