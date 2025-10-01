#!/usr/bin/env python3

import time
import sys
from pathlib import Path
import ast
import re
import subprocess


if len(sys.argv) == 2:
    file_name = sys.argv[1]
    file_path = Path.cwd()/ file_name
else:
    print("Usage: python3 script.py <filename.py>")
    sys.exit(1)


# Reading file
try:
    with open(file_path, "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File doesn't exist.")
except SyntaxError as e:
    print(f"Syntax error while parsing the file: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")


# Parsing code using ast

def parser(content):
    # Parsing imports
    imports = []
    tree = ast.parse(content)
    for node in tree.body:
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.asname:
                    imports.append(f"import {alias.name} as {alias.asname}")
                else:
                    imports.append(f"import {alias.name}")
        elif isinstance(node, ast.ImportFrom):
            module = '.' * node.level + (node.module or "")
            for alias in node.names:
                if alias.asname:
                    imports.append(f"from {module} import {alias.name} as {alias.asname}")
                else:
                    imports.append(f"from {module} import {alias.name}")
    #print("\n".join(imports))

    # Parsing code between (#start and #end)
    above_st = re.search(r"([\s\S]*?)#start", content)
    below_et = re.search(r"#end\s*\n([\s\S]*)", content)
    print(above_st.group(0), below_et.group(1))

    #return "\n".join(imports) , "\n\n".join(code_snippet)
"""
def code_run():
    imports, code = parser(content)
    if "import time" not in imports:
        imports += "\nimport time\n"
    pyfile = (
        imports + 
        "\nst = time.monotonic_ns()\n"
        + code + 
        "et = time.monotonic_ns()\n"
        "print(f'Time taken for code block: {(et - st) / 1e9:.9f} sec')\n")
    #print(pyfile)
    subprocess.run(["python3",  "-c", pyfile])
"""
parser(content)

#if __name__ == "__main__":
#   parser(content)
