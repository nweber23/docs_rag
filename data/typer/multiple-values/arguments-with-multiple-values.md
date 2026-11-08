# CLI Arguments with Multiple Values

*CLI arguments* can also receive multiple values.

You can define the type of a *CLI argument* using `list`.

And then you can pass it as many *CLI arguments* of that type as you want:

Tip:

We also declared a final *CLI argument* `celebration`, and it's correctly used even if we pass an arbitrary number of `files` first.

Note:

A `list` can only be used in the last command (if there are subcommands), as this will take anything to the right and assume it's part of the expected *CLI arguments*.

## *CLI arguments* with tuples

If you want a specific number of values and types, you can use a tuple, and it can even have default values:

Check it:
