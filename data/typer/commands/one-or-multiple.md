# One or Multiple Commands

You might have noticed that if you create a single command, as in the following example:

**Typer** is smart enough to create a CLI application with that single function as the main CLI application, not as a command/subcommand:

Tip:

Notice that it doesn't show a command `main`, even though the function name is `main`.

But if you add multiple commands, **Typer** will create one *CLI command* for each one of them:

Here we have 2 commands `create` and `delete`:

## One command and one callback

If you want to create a CLI app with one single command but you still want it to be a command/subcommand you can just add a callback:

And now your CLI program will have a single command.

Check it:

## Using the callback to document

Now that you are using a callback just to have a single command, you might as well use it to add documentation for your app:

And now the docstring from the callback will be used as the help text:
