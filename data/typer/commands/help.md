# Command Help

The same as before, you can add help for the commands in the docstrings and the *CLI options*.

And the `typer.Typer()` application receives a parameter `help` that you can pass with the main help text for your CLI program:

Check it:

Tip:

`typer.Typer()` receives several other parameters for other things, we'll see that later.

You will also see how to use "Callbacks" later, and those include a way to add this same help message in a function docstring.

## Overwrite command help

You will probably be better adding the help text as a docstring to your functions, but if for some reason you wanted to overwrite it, you can use the `help` function argument passed to `@app.command()`:

Check it:

## Deprecate a Command

There could be cases where you have a command in your app that you need to deprecate, so that your users stop using it, even while it's still supported for a while.

You can mark it with the parameter `deprecated=True`:

And when you show the `--help` option you will see it's marked as "`deprecated`":

And if you check the `--help` for the deprecated command (in this example, the command `delete`), it also shows it as deprecated:

## Suggest Commands

As of version 0.20.0, Typer added support for suggesting mistyped command names. This feature is **enabled by default**, but you can disable it with the parameter `suggest_commands=False`:

If a user mistypes a command, they'll see a helpful suggestion:

If there are multiple close matches, Typer will suggest them all. This feature uses Python's built-in `difflib.get_close_matches()` to find similar command names, making your CLI more user-friendly by helping users recover from typos.

## Rich Markdown and Markup

Typer installs **Rich** to allow for more formatting in the docstrings and the `help` parameter for *CLI arguments* and *CLI options*. You will see more about it below. 👇

Note:

You can disable rich text formatting by setting `rich_markup_mode` to `None` for your specific app.
Alternatively, you can disable it globally using an environmental variable `TYPER_USE_RICH` set to `False` or `0`.

### Rich Markup

If you set `rich_markup_mode="rich"` when creating the `typer.Typer()` app (which is the default), you will be able to use [Rich Console Markup](https://rich.readthedocs.io/en/stable/markup.html) in the docstring, and even in the help for the *CLI arguments* and options:

With that, you can use [Rich Console Markup](https://rich.readthedocs.io/en/stable/markup.html) to format the text in the docstring for the command `create`, make the word "`create`" bold and green, and even use an [emoji](https://rich.readthedocs.io/en/stable/markup.html#emoji).

You can also use markup in the help for the `username` CLI Argument.

And the same as before, the help text overwritten for the command `delete` can also use Rich Markup, the same in the CLI Argument and CLI Option.

If you run the program and check the help, you will see that **Typer** uses **Rich** internally to format the help.

Check the help for the `create` command:

And check the help for the `delete` command:

### Rich Markdown

If you set `rich_markup_mode="markdown"` when creating the `typer.Typer()` app, you will be able to use Markdown in the docstring:

With that, you can use Markdown to format the text in the docstring for the command `create`, make the word "`create`" bold, show a list of items, and even use an [emoji](https://rich.readthedocs.io/en/stable/markup.html#emoji).

And the same as before, the help text overwritten for the command `delete` can also use Markdown.

Check the help for the `create` command:

And the same for the `delete` command:

Note:

Notice that in Markdown you cannot define colors. For colors you might prefer to use Rich markup.

## Help Panels

If you have many commands or CLI parameters, you might want to show their documentation in different panels when using the `--help` option.

If you installed [Rich](https://rich.readthedocs.io/) as described in [Printing and Colors](../printing.md), you can configure the panel to use for each command or CLI parameter.

### Help Panels for Commands

To set the panel for a command you can pass the argument `rich_help_panel` with the name of the panel you want to use:

Commands without a panel will be shown in the default panel `Commands`, and the rest will be shown in the next panels:

### Help Panels for CLI Parameters

The same way, you can configure the panels for *CLI arguments* and *CLI options* with `rich_help_panel`.

And of course, in the same application you can also set the `rich_help_panel` for commands.

Then if you run the application you will see all the *CLI parameters* in their respective panels.

* First the ***CLI arguments*** that don't have a panel name set in a **default** one named "`Arguments`".
* Next the ***CLI arguments*** with a **custom panel**. In this example named "`Secondary Arguments`".
* After that, the ***CLI options*** that don't have a panel in a **default** one named "`Options`".
* And finally, the ***CLI options*** with a **custom panel** set. In this example named "`Additional Data`".

You can check the `--help` option for the command `create`:

And of course, the `rich_help_panel` can be used in the same way for commands in the same application.

And those panels will be shown when you use the main `--help` option.

You can see the custom panel for the commands for "`Utils and Configs`".

## Epilog

If you need, you can also add an epilog section to the help of your commands:

And when you check the `--help` option it will look like:
