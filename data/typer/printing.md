# Printing and Colors

You can use the normal `print()` to show information on the screen:

It will show the output normally:

## Use Rich

You can also display beautiful and more complex information using [Rich](https://rich.readthedocs.io/). It comes by default when you install `typer`.

### Use Rich `print`

For the simplest cases, you can just import `print` from `rich` and use it instead of the standard `print`:

Just with that, **Rich** will be able to print your data with nice colors and structure:

### Rich Markup

Rich also supports a [custom markup syntax](https://rich.readthedocs.io/en/stable/markup.html) to set colors and styles, for example:

In this example you can see how to use font styles, colors, and even emojis.

To learn more check out the [Rich docs](https://rich.readthedocs.io/en/stable/markup.html).

### Rich Tables

The way Rich works internally is that it uses a `Console` object to display the information.

When you call Rich's `print`, it automatically creates this object and uses it.

But for advanced use cases, you could create a `Console` yourself.

In this example, we create a `Console`, and a `Table`. And then we can add some rows to the table, and print it.

If you run it, you will see a nicely formatted table:

Rich has many other features, as an example, you can check the docs for:

* [Prompt](https://rich.readthedocs.io/en/stable/prompt.html)
* [Markdown](https://rich.readthedocs.io/en/stable/markdown.html)
* [Panel](https://rich.readthedocs.io/en/stable/panel.html)
* ...and more.

### Typer and Rich

If you are wondering what tool should be used for what, **Typer** is useful for structuring the command line application, with options, arguments, subcommands, data validation, etc.

In general, **Typer** tends to be the entry point to your program, taking the first input from the user.

**Rich** is useful for the parts that need to *display* information. Showing beautiful content on the screen.

The best results for your command line application are achieved combining both **Typer** and **Rich**.

## "Standard Output" and "Standard Error"

The way printing works underneath is that the **operating system** (Linux, Windows, macOS) treats what we print as if our CLI program was **writing text** to a "**virtual file**" called "**standard output**".

When our code "prints" things it is actually "writing" to this "virtual file" of "standard output".

This might seem strange, but that's how the CLI program and the operating system interact with each other.

And then the operating system **shows on the screen** whatever our CLI program "**wrote**" to that "**virtual file**" called "**standard output**".

### Standard Error

And there's another "**virtual file**" called "**standard error**" that is normally only used for errors.

But we can also "print" to "standard error". And both are shown on the terminal to the users.

Note:

If you use PowerShell it's quite possible that what you print to "standard error" won't be shown in the terminal.

In PowerShell, to see "standard error" you would have to check the variable `$Error`.

But it will work normally in Bash, Zsh, and Fish.

### Printing to "standard error"

You can print to "standard error" creating a Rich `Console` with `stderr=True`.

Tip:

`stderr` is short for "standard error".

Using `stderr=True` tells **Rich** that the output should be shown in "standard error".

When you try it in the terminal, it will probably just look the same:

## "Standard Input"

As a final detail, when you type text in your keyboard to your terminal, the operating system also considers it another "**virtual file**" that you are writing text to.

This virtual file is called "**standard input**".

### What is this for

Right now this probably seems quite useless 🤷‍♂.

But understanding that will come handy in the future, for example for autocompletion and testing.

## Typer Echo

Warning:

In most of the cases, for displaying advanced information, it is recommended to use [Rich](https://rich.readthedocs.io/).

You can probably skip the rest of this section. 🎉😎

**Typer** also has a small utility `typer.echo()` to print information on the screen. But normally you shouldn't need it.

For the simplest cases, you can use the standard Python `print()`.

And for the cases where you want to display data more beautifully, or more advanced content, you should use **Rich** instead.

### Why `typer.echo`

`typer.echo()` applies some checks to try and convert binary data to strings, and other similar things.

But in most of the cases you wouldn't need it, as in modern Python strings (`str`) already support and use Unicode, and you would rarely deal with pure `bytes` that you want to print on the screen.

If you have some `bytes` objects, you would probably want to decode them intentionally and directly before trying to print them.

And if you want to print data with colors and other features, you are much better off with the more advanced tools in **Rich**.

### Untrusted Text

`typer.echo()` preserves terminal control sequences, including those used for colors. When displaying text from an untrusted source, escape control characters first. For a diagnostic representation of a string, you can use `typer.echo(repr(value))`.

Setting `color=False` disables styling, but does not sanitize all terminal control sequences.

### Color

Note: Technical Details

The way color works in terminals is by using some codes (ANSI escape sequences) as part of the text.

So, a colored text is still just a `str`.

Tip:

Again, you are much better off using [Rich](https://rich.readthedocs.io/) for this. 😎

You can create colored strings to output to the terminal with `typer.style()`, that gives you `str`s that you can then pass to `typer.echo()`:

Tip:

The parameters `fg` and `bg` receive strings with the color names for the "<strong>f</strong>ore<strong>g</strong>round" and "<strong>b</strong>ack<strong>g</strong>round" colors. You could simply pass `fg="green"` and `bg="red"`.

But **Typer** provides them all as variables like `typer.colors.GREEN` just so you can use autocompletion while selecting them.

Check it:

You can pass these function arguments to `typer.style()`:

* `fg`: the foreground color.
* `bg`: the background color.
* `bold`: enable or disable bold mode.
* `dim`: enable or disable dim mode. This is badly supported.
* `underline`: enable or disable underline.
* `blink`: enable or disable blinking.
* `reverse`: enable or disable inverse rendering (foreground becomes background and the other way round).
* `reset`: by default a reset-all code is added at the end of the string which means that styles do not carry over.  This can be disabled to compose styles.

### `typer.secho()` - style and print

Tip:

In case you didn't see above, you are much better off using [Rich](https://rich.readthedocs.io/) for this. 😎

There's a shorter form to style and print at the same time with `typer.secho()` it's like `typer.echo()` but also adds style like `typer.style()`:

Check it:
