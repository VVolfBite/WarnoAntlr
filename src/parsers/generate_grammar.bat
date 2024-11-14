# 在当前目录运行脚本 以使用Antlr根据NdfGrammar生成parser文件夹
java -jar .\antlr-4.13.2-complete.jar -Dlanguage=Python3 NdfGrammar.g4 -visitor -o parser