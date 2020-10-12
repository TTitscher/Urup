"""
to_md.py
========

Converting block-commented python code to markdown. For the sake of simplicity
of the script, we require the input to start with a block comment, usually 
containing a title.
    
Splitting the code into blocks separated by a newline +  \"\"\" will ignore
indented comments/docstrings.

"""

import sys
import argparse


def convert(f):
    f = f.lstrip()
    assert f.startswith('"""')
    f = f.replace("\\bm", "\\boldsymbol")

    blocks = f.split('\n"""')
    blocks[0] = blocks[0].strip('"""')

    """
    Even blocks are now pure markdown, odd blocks are surrounded by `~~~py` and 
    `~~~` for python syntax highlighting.
    """
    output = ""
    for i, block in enumerate(blocks):
        if i % 2 == 0:
            output += block + "\n"
        else:
            clean_block = block.strip("\n")
            output += f"\n~~~py\n{clean_block}\n~~~\n"
    return output


"""
This is the entrypoint for the CLI script.
"""


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="Convert commented python code to md.")
    parser.add_argument("input", type=argparse.FileType("r"), help="input (.py) file")
    parser.add_argument(
        "-o", "--output", type=argparse.FileType("w"), help="output (.md) file"
    )

    args = parser.parse_args(argv)
    f = args.input.read()
    output = convert(f)

    if args.output:
        args.output.write(output)
    else:
        print(output)

if __name__ == "__main__":
    main()
