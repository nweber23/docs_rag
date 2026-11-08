# Required CLI Options

We said before that *by default*:

* *CLI options* are **optional**
* *CLI arguments* are **required**

Well, that's how they work *by default*, and that's the convention in many CLI programs and systems.

But if you really want, you can change that.

To make a *CLI option* required, you can put `typer.Option()` inside of `Annotated` and leave the parameter without a default value.

Let's make `--lastname` a required *CLI option*:

The same way as with `typer.Argument()`, the old style of using the function parameter default value is also supported, in that case you would just not pass anything to the `default` parameter.

Or you can explicitly pass `...` to `typer.Option(default=...)`:

Note:

If you hadn't seen that `...` before: it is a special single value, it is [part of Python and is called "Ellipsis"](https://docs.python.org/3/library/constants.html#Ellipsis).

That will tell **Typer** that it's still a *CLI option*, but it doesn't have a default value, and it's required.

Tip:

Again, prefer to use the `Annotated` version if possible. That way your code will mean the same in standard Python and in **Typer**.

And test it:
