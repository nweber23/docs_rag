# Multiple CLI Options

You can declare a *CLI option* that can be used multiple times, and then get all the values.

For example, let's say you want to accept several users in a single execution.

For this, use the standard Python `list` to declare it as a list of `str`:

You will receive the values as you declared them, as a `list` of `str`.

Check it:

## Multiple `float`

The same way, you can use other types and they will be converted by **Typer** to their declared type:

Check it:
