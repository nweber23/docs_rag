# Nested SubCommands

We'll now see how these same ideas can be extended for deeply nested commands.

Let's imagine that the same *CLI program* from the previous examples now needs to handle `lands`.

But a land could be a `reign` or `town`.

And each of those could have their own commands, like `create` and `delete`.

## A CLI app for reigns

Let's start with a file `reigns.py`:

This is already a simple *CLI program* to manage reigns:

## A CLI app for towns

And now the equivalent for managing towns in `towns.py`:

With it, you can manage towns:

## Manage the land in a CLI app

Now let's put the `reigns` and `towns` together in the same *CLI program* in `lands.py`:

And now we have a single *CLI program* with a command (or command group) `reigns` that has its own commands. And another command `towns` with its own subcommands.

Check it:

Now try it, manage the lands through the CLI:

## Deeply nested subcommands

Now let's say that all these commands in the `lands.py` *CLI program* should be part of the previous *CLI program* we built in the first example.

We want our *CLI program* to have these commands/command groups:

* `users`:
    * `create`
    * `delete`
* `items`:
    * `create`
    * `delete`
    * `sell`
* `lands`:
    * `reigns`:
        * `conquer`
        * `destroy`
    * `towns`:
        * `found`
        * `burn`

This already is a quite deeply nested "tree" of commands/command groups.

But to achieve that, we just have to add the `lands` **Typer** app to the same `main.py` file we already had:

And now we have everything in a single *CLI program*:

## Review the files

Here are all the files if you want to review/copy them:

`reigns.py`:

`towns.py`:

`lands.py`:

`users.py`:

`items.py`:

`main.py`:

Tip:

All these files have an `if __name__ == "__main__"` block just to demonstrate how each of them can also be an independent *CLI app*.

But for your final application, only `main.py` would need it.

## Recap

That's it, you can just add **Typer** applications one inside another as much as you want and create complex *CLI programs* while writing simple code.

You can probably achieve a simpler *CLI program* design that's easier to use than the example here. But if your requirements are complex, **Typer** helps you build your *CLI app* easily.

Tip:

Auto completion helps a lot, specially with complex programs.

Check the docs about adding auto completion to your *CLI apps*.
