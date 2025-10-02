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

        # removed all print() statements
        content = re.sub(r'^\s*print\(.*?\)\s*$', '', content, flags=re.MULTILINE)
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

    # Parsing code between (#start and #end)
    above_st = re.search(r"([\s\S]*?)#st", content) #code above the #st
    below_et = re.search(r"#et\s*\n([\s\S]*)", content) #code below the #et
    if below_et is None:
        below_et = ""  # no code below #et
    else:
        below_et = below_et.group(1)

    middle = re.search(r"#st\s*(.*?)#et\b.*", content, re.DOTALL) #code betweeen #st ... #et

    if not (above_st and middle):
        return None
  
    return above_st.group(1), middle.group(1), below_et


def code_run():
    result = parser(content)
    if result is None:
        print("🔍 Hint: Make sure your file contains both '#st' and '#et' markers like this:\n\n#st\n...your code...\n#et")
    else:
        above, middle, below = result
        if "import time" not in above:
            above += "\nimport time\n"
        pyfile = (
            above + 
            "\nst = time.monotonic_ns()\n"
            + middle + 
            "et = time.monotonic_ns()\n"
            + below +
            "print(f'Time taken for code block: {(et - st) / 1e9:.9f} sec')\n")
        #print(pyfile)
        subprocess.run(["python3",  "-c", pyfile])

if __name__ == "__main__":
    code_run()
