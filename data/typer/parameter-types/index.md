# CLI Parameter Types

You can use several data types for the *CLI options* and *CLI arguments*, and you can add data validation requirements too.

## Data conversion

When you declare a *CLI parameter* with some type **Typer** will convert the data received in the command line to that data type.

For example:

In this example, the value received for the *CLI argument* `name` will be treated as `str`.

The value for the *CLI option* `--age` will be converted to an `int` and `--height-meters` will be converted to a `float`.

And as `female` is a `bool` *CLI option*, **Typer** will convert it to a "flag" `--female` and the counterpart `--no-female`.

And here's how it looks like:

## Watch next

See more about specific types and validations in the next sections...
