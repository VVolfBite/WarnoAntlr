import os
import re
import json

from antlr4 import *
from antlr4.tree.Trees import Trees

from ndf_parser.parser.NdfGrammarLexer import NdfGrammarLexer
from ndf_parser.parser.NdfGrammarParser import NdfGrammarParser

from ndf_parser.semantic_actions import _generator
from ndf_parser.syntax_node._collection import *
from ndf_parser.syntax_node._assignment import Assignment
from ndf_parser.util import _to_ndf_converter,ndf_scanner


def generate_(file_name: str) -> [Assignment]: # type: ignore
    input_stream = FileStream(file_name, encoding="utf8")

    lexer = NdfGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = NdfGrammarParser(stream)
    tree = parser.ndf_file()
    listener = _generator.Generator(parser)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    return File(listener.assignments)

def main():
    target = "./ndf_parser/test/Primitives.ndf"
    output = target.split("/")[-1].split(".")[0] + ".json"
    print(output)
    _file = generate_(target)
    json_output = json.dumps(value_from_(_file), indent=4, ensure_ascii=False)
    with open(output, "w", encoding="utf-8") as json_file:
        json_file.write(json_output)
main()