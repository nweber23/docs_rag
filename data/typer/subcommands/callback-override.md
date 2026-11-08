# Sub-Typer Callback Override

When creating a **Typer** app you can define a callback function, it always executes and defines the *CLI arguments* and *CLI options* that go before a command.

When adding a Typer app inside of another, the sub-Typer can also have its own callback.

It can handle any *CLI parameters* that go before its own commands and execute any extra code:

In this case it doesn't define any *CLI parameters*, it just writes a message.

Check it:

## Add a callback on creation

It's also possible to add a callback when creating the `typer.Typer()` app that will be added to another Typer app:

This achieves exactly the same as above, it's just another place to add the callback.

Check it:

## Overriding the callback on creation

If a callback was added when creating the `typer.Typer()` app, it's possible to override it with a new one using `@app.callback()`.

This is the same information you saw on the section about [Commands - Typer Callback](../commands/callback.md), and it applies the same for sub-Typer apps:

Here we had defined a callback when creating the `typer.Typer()` sub-app, but then we override it with a new callback with the function `user_callback()`.

As `@app.callback()` takes precedence over `typer.Typer(callback=some_function)`, now our CLI app will use this new callback.

Check it:

## Overriding the callback when adding a sub-Typer

Lastly, you can override the callback defined anywhere else when adding a sub-Typer with `app.add_typer()` using the `callback` parameter.

This has the highest priority:

Notice that the precedence goes to `app.add_typer()` and is not affected by the order of execution. There's another callback defined below, but the one from `app.add_typer()` wins.

Now when you use the CLI program it will use the new callback function `callback_for_add_typer()`.

Check it:
