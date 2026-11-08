# Enum - Choices

To define a *CLI parameter* that can take a value from a predefined set of values you can use a standard Python [`enum.Enum`](https://docs.python.org/3/library/enum.html):

Tip:

Notice that the function parameter `network` will be an `Enum`, not a `str`.

To get the `str` value in your function's code use `network.value`.

Check it:

### Case insensitive Enum choices

You can make an `Enum` (choice) *CLI parameter* be case-insensitive with the `case_sensitive` parameter:

And then the values of the `Enum` will be checked no matter if lower case, upper case, or a mix:

### List of Enum values

A *CLI parameter* can also take a list of `Enum` values:

This works just like any other parameter value taking a list of things:

### Literal choices

You can also use `Literal` to represent a set of possible predefined choices, without having to use an `Enum`:
