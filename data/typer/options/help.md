# CLI Options with Help

You already saw how to add a help text for *CLI arguments* with the `help` parameter.

Let's now do the same for *CLI options*:

The same way as with `typer.Argument()`, we can put `typer.Option()` inside of `Annotated`.

We can then pass the `help` keyword parameter:

```Python
lastname: Annotated[str, typer.Option(help="this option does this and that")] = ""
```

...to create the help for that *CLI option*.

The same way as with `typer.Argument()`, **Typer** also supports the old style using the function parameter default value:

```Python
lastname: str = typer.Option(default="", help="this option does this and that")
```

Copy that example from above to a file `main.py`.

Test it:

## *CLI Options* help panels

The same as with *CLI arguments*, you can put the help for some *CLI options* in different panels to be shown with the `--help` option.

Using Rich, you can set the `rich_help_panel` parameter to the name of the panel you want for each *CLI option*:

Now, when you check the `--help` option, you will see a default panel named "`Options`" for the *CLI options* that don't have a custom `rich_help_panel`.

And below you will see other panels for the *CLI options* that have a custom panel set in the `rich_help_panel` parameter:

Here we have a custom *CLI options* panel named "`Customization and Utils`".

## Help with style using Rich

In a future section you will see how to use custom markup in the `help` for *CLI options* when reading about [Commands - Command Help](../commands/help.md#rich-markdown-and-markup).

If you are in a hurry you can jump there, but otherwise, it would be better to continue reading here and following the tutorial in order.

## Hide default from help

You can tell Typer to not show the default value in the help text with `show_default=False`:

And it will no longer show the default value in the help text:

## Custom default string

You can use the same `show_default` to pass a custom string (instead of a `bool`) to customize the default value to be shown in the help text:

And it will be used in the help text:
