"""
to_md.py
========

Converting block-commented python code to markdown. For the sake of simplicity
of the script, we require the input to start with a block comment, usually 
containing a title.
"""
import sys
f = open(sys.argv[1], "r").read()
assert f.startswith('"""')
f = f.replace("\\bm", "\\boldsymbol")


"""
Splitting the code into blocks separated by a newline +  \"\"\" will ignore
indented comments.
"""

blocks = f.split('\n"""')
blocks[0] = blocks[0].strip('"""')

"""
Even blocks are now pure markdown, odd blocks are surrounded by `~~~py` and 
`~~~` for python syntax highlighting.
"""
for i, block in enumerate(blocks):
    if i % 2 == 0:
        print(block)
    else:
        clean_block = block.strip('\n')
        print(f"\n~~~py\n{clean_block}\n~~~")
