"""
urup
====

Converting block-commented python code to markdown. This can be useful if you
want to provide a commented, self-containing, runnable python script that
can easily be displayed on a website.

For the sake of simplicity of the script, we require the input to start with a 
block comment, usually containing a title.
    
"""

import sys
import argparse
from .modifiers import *

"""
Entrypoint
----------

The main CLI options are

* `urup input.py` prints the [converted](#Convert) markdown code
* `urup input.py -o output.md` writes the [converted](#Convert) markdown code to `output.md`
* `urup input.py --doit` see [below](#doit)

"""


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="Convert commented python code to md.")
    parser.add_argument("input", type=argparse.FileType("r"), help="input (.py) file")
    parser.add_argument(
        "-o", "--output", type=argparse.FileType("w"), help="output (.md) file"
    )
    parser.add_argument(
        "--doit",
        nargs="?",
        const="None",
        help="prints a pydoit task that can be added to a `dodo.py`, optional: css file",
    )
    parser.add_argument(
        "--gitlab", action="store_true", help="adapt LaTeX for Gitlab Markdown"
    )

    args = parser.parse_args(argv)

    if args.doit:
        print(dodo_task(args.input.name, args.doit))
        return

    comment_modifiers = []
    comment_modifiers.append(fix_boldmath)
    if args.gitlab:
        comment_modifiers.append(fix_gitlab_equation)
        comment_modifiers.append(fix_gitlab_inlinemath)

    f = args.input.read()
    output = convert(f, comment_modifiers)

    if args.output:
        args.output.write(output)
    else:
        print(output)


"""
Convert
-------

Splitting the code into blocks separated by a newline +  \"\"\" will ignore
indented comments/docstrings.

"""


def convert(f, comment_modifiers=""):
    f = f.lstrip()
    assert f.startswith('"""')

    blocks = f.split('\n"""')
    blocks[0] = blocks[0].strip('"""')

    """
    Even blocks are now pure markdown, odd blocks are surrounded by `~~~py` and 
    `~~~` for python syntax highlighting.
    """
    output = ""
    for i, block in enumerate(blocks):
        if i % 2 == 0:
            for comment_modifier in comment_modifiers:
                block = comment_modifier(block)
            output += block + "\n"
        else:
            clean_block = block.strip("\n")
            output += f"\n~~~py\n{clean_block}\n~~~\n"
    return output


"""
doit
----

[doit](https://pydoit.org/), especially `doit auto`, can be used to automate
the convertion of a python file to markdown. The resulting markdown file can 
be displayed in any browser after converting it via `pandoc`.

"""


def dodo_task(name, css):
    from pathlib import Path

    f_py = Path(name)
    f_md = f_py.with_suffix(".md")
    f_html = f_py.with_suffix(".html")

    css = f"--css {css}" if css != "None" else ""

    code = f"""
def task_{f_py.stem}():
    return {{
        "file_dep": ["{f_py}"],
        "actions": ["urup {f_py} -o {f_md}", "pandoc {css} --toc --standalone --mathjax {f_md} -o {f_html}"]
    }}
    """
    return code


"""
Have fun!
"""

if __name__ == "__main__":
    main()
