# SubCommands in a Single File

In some cases, it's possible that your application code needs to live on a single file.

You can still use the same ideas:

There are several things to notice here...

## Apps at the top

First, you can create `typer.Typer()` objects and add them to another one at the top.

It doesn't have to be done after creating the subcommands:

You can add the commands (subcommands) to each `typer.Typer()` app later and it will still work.

## Function names

As you now have subcommands like `create` for `users` and for `items`, you can no longer call the functions with just the name, like `def create()`, because they would overwrite each other.

So we use longer names:

## Command name

We are naming the functions with longer names so that they don't overwrite each other.

But we still want the subcommands to be `create`, `delete`, etc.

To call them like:

instead of:

So we pass the name we want to use for each subcommand as the function argument to the decorator:

## Check it

It still works the same:

Check the `items` command:

And the same for the `users` command:
