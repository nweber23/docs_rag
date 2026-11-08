# CLI Arguments with Help

In the *First Steps* section you saw how to add help for a CLI app/command by adding it to a function's <abbr title="a multi-line string as the first expression inside a function (not assigned to any variable) used for documentation">docstring</abbr>.

Here's how that last example looked like:

Now that you also know how to use `typer.Argument()`, let's use it to add documentation specific for a *CLI argument*.

## Add a `help` text for a *CLI argument*

You can use the `help` parameter to add a help text for a *CLI argument*:

And it will be used in the automatic `--help` option:

## Combine help text and docstrings

And of course, you can also combine that `help` with the <abbr title="a multi-line string as the first expression inside a function (not assigned to any variable) used for documentation">docstring</abbr>:

And the `--help` option will combine all the information:

## Help with defaults

If you have a *CLI argument* with a default value, like `"World"`:

It will show that default value in the help text:

But you can disable that if you want to, with `show_default=False`:

And then it won't show the default value:

## Custom default string

You can use the same `show_default` to pass a custom string (instead of a `bool`) to customize the default value to be shown in the help text:

And it will be used in the help text:

## Custom help name (`metavar`)

You can also customize the text used in the generated help text to represent a *CLI argument*.

By default, it will be the same name you declared, with casing preserved.

So, if you declare it as:

```Python
name: str
```

It will be shown as:

```
name
```

But you can customize it with the `metavar` parameter for `typer.Argument()`.

For example, let's say you don't want to have the default of `name`, you want to have `username`, and you really want ✨ emojis ✨ everywhere:

Now the generated help text will have `✨username✨` instead of `name`:

## *CLI Argument* help panels

You might want to show the help information for *CLI arguments* in different panels when using the `--help` option.

If you have installed Rich as described in the docs for [Printing and Colors](../printing.md), you can set the `rich_help_panel` parameter to the name of the panel where you want this *CLI argument* to be shown:

Then, if you check the `--help` option, you will see a default panel named "`Arguments`" for the *CLI arguments* that don't have a custom `rich_help_panel`.

And next you will see other panels for the *CLI arguments* that have a custom panel set in the `rich_help_panel` parameter:

In this example we have a custom *CLI arguments* panel named "`Secondary Arguments`".

## Help with style using Rich

In a future section you will see how to use custom markup in the `help` for *CLI arguments* when reading about [Commands - Command Help](../commands/help.md#rich-markdown-and-markup).

If you are in a hurry you can jump there, but otherwise, it would be better to continue reading here and following the tutorial in order.

## Hide a *CLI argument* from the help text

If you want, you can make a *CLI argument* **not** show up in the `Arguments` section in the help text.

You will probably not want to do this normally, but it's possible:

Check it:

Note:

Have in mind that the *CLI argument* will still show up in the first line with `Usage`.

But it won't show up in the main help text under the `Arguments` section.

### Help text for *CLI arguments*

**Typer supports `help` for *CLI arguments*** to make it easier to have consistent help texts with a consistent format for your CLI programs. 🎨

This is also to help you create CLI programs that are ✨ awesome ✨ *by default*. With very little code.

If you don't want the CLI Argument to be shown in help outputs, you can set the `hidden` parameter to `True`.
