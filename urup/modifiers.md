
Modifiers
=========

For either convenience or compatibility, you may want to modify the comment
blocks. For example, when typing LaTeX, I am highly annoyed of typing 
`\boldysmbol` when there is the short `\boldsymbol`. Unfortunately, that is not a 
default package, so I fix this with a modifier.

~~~py
def fix_boldmath(block):
    return block.replace(r"\bm", r"\boldsymbol")
~~~

Another example is GitLab flavoured Markdown, where equations require a
separate `math` environment ...

~~~py
def fix_gitlab_equation(block):
    return fix_split(block, "$$", prefix="\n```math\n", suffix="\n```\n")
~~~

... and inline math requires additional apostrophes.

~~~py
def fix_gitlab_inlinemath(block):
    return fix_split(block, "$", prefix="$`", suffix="`$")


def fix_split(block, pattern, prefix, suffix):
    output = ""
    for i, b in enumerate(block.split(pattern)):
        if i % 2 == 1:
            clean_b = b.strip("\n")
            output += prefix + clean_b + suffix
        else:
            output += b
    return output
~~~
