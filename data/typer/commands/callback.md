# Typer Callback

When you create an `app = typer.Typer()` it works as a group of commands.

And you can create multiple commands with it.

Each of those commands can have their own *CLI parameters*.

But as those *CLI parameters* are handled by each of those commands, they don't allow us to create *CLI parameters* for the main CLI application itself.

But we can use `@app.callback()` for that.

It's very similar to `@app.command()`, but it declares the *CLI parameters* for the main CLI application (before the commands):

Here we create a `callback` with a `--verbose` *CLI option*.

Tip:

After getting the `--verbose` flag, we modify a global `state`, and we use it in the other commands.

There are other ways to achieve the same, but this will suffice for this example.

And as we added a docstring to the callback function, by default it will be extracted and used as the help text.

Check it:

## Adding a callback on creation

It's also possible to add a callback when creating the `typer.Typer()` app:

That achieves the same as with `@app.callback()`.

Check it:

## Overriding a callback

If you added a callback when creating the `typer.Typer()` app, it's possible to override it with `@app.callback()`:

Now `new_callback()` will be the one used.

Check it:

## Adding a callback only for documentation

You can also add a callback just to add the documentation in the docstring.

It can be convenient especially if you have several lines of text, as the indentation will be automatically handled for you:

Now the callback will be used mainly to extract the docstring for the help text.

Check it:
