# Add Typer

We'll start with the core idea.

To add a `typer.Typer()` app inside of another.

## Manage items

Let's imagine that you are creating a *CLI program* to manage items in some distant land.

It could be in an `items.py` file with this:

And you would use it like:

## Manage users

But then you realize that you also have to manage users from your *CLI app*.

It could be a file `users.py` with something like:

And you would use it like:

## Put them together

Both parts are similar. In fact, `items.py` and `users.py` both have commands `create` and `delete`.

But we need them to be part of the same *CLI program*.

In this case, as with `git remote`, we can put them together as subcommands in another `typer.Typer()` *CLI program*.

Now create a `main.py` with:

Here's what we do in `main.py`:

* Import the other Python modules (the files `users.py` and `items.py`).
* Create the main `typer.Typer()` application.
* Use `app.add_typer()` to include the `app` from `items.py` and `users.py`, each of those 2 was also created with `typer.Typer()`.
* Define a `name` with the command that will be used for each of these "sub-Typers" to group their own commands.

And now your *CLI program* has 2 commands:

* `users`: with all of the commands (subcommands) in the `app` from `users.py`.
* `items` with all the commands (subcommands) in the `app` from `items.py`.

Check it:

Now you have a *CLI program* with commands `items` and `users`, and they in turn have their own commands (subcommands).

Let's check the `items` command:

Tip:

Notice that we are still calling `$ python main.py` but now we are using the command `items`.

And now check the command `users`, with all its subcommands:

## Recap

That's the core idea.

You can just create `typer.Typer()` apps and add them inside one another.

And you can do that with any levels of commands that you want.

Do you need sub-sub-sub-subcommands? Go ahead, create all the `typer.Typer()`s you need and put them together with `app.add_typer()`.

In the next sections we'll update this with more features, but you already have the core idea.

This way, **Typer** applications are composable, each `typer.Typer()` can be a *CLI app* by itself, but it can also be added as a command group to another Typer app.
