import brainfuck_compile as bc

# 定义Brainfuck代码
code = "++[>++++<-]>[>++++++<-]>.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>-.<+++[>------<-]>."

print(bc.brainfuck_compile(code))