# SubCommand Name and Help

When adding a Typer app to another we have seen how to set the `name` to use for the command.

For example to set the command to `users`:

```Python
app.add_typer(users.app, name="users")
```

## Add a help text

We can also set the `help` text while adding a Typer:

And then we get that help text for that command in the *CLI program*:

We can set the `help` in several places, each one taking precedence over the other, overriding the previous value.

Let's see those locations.

Tip:

There are other attributes that can be set in that same way in the same places we'll see next.

But those are documented later in another section.

## Inferring help text from callback

### Inferring a command's help text

When you create a command with `@app.command()`, by default, it generates the name from the function name.

And by default, the help text is extracted from the function's docstring.

For example:

```Python
@app.command()
def create(item: str):
    """
    Create an item.
    """
    typer.echo(f"Creating item: {item}")
```

...will create a command `create` with a help text of `Create an item`.

### Inferring the help text from `@app.callback()`

The same way, if you define a callback in a `typer.Typer()`, the help text is extracted from the callback function's docstring.

Here's an example:

The help text for that command will be the callback function's docstring: `Manage users in the app.`.

Check it:

Note:

Before Typer 0.14.0, in addition to the help text, the command name was also inferred from the callback function name, this is no longer the case.

### Help from callback parameter in `typer.Typer()`

If you pass a `callback` parameter while creating a `typer.Typer(callback=some_function)` it will be used to infer the help text.

This has the lowest priority, we'll see later what has a higher priority and can override it.

Check the code:

This achieves exactly the same as the previous example.

Check it:

### Override a callback set in `typer.Typer()` with `@app.callback()`

The same as with normal **Typer** apps, if you pass a `callback` to `typer.Typer(callback=some_function)` and then override it with `@app.callback()`, the help text will be inferred from the new callback:

Now the help text will be `Manage users in the app.` instead of `Old callback help.`.

Check it:

### Help from callback in `app.add_typer()`

If you override the callback in `app.add_typer()` when including a sub-app, the help will be inferred from this callback function.

This takes precedence over inferring the help from a callback set in `@sub_app.callback()` and `typer.Typer(callback=sub_app_callback)`.

Check the code:

The help text will be `I have the highland! Create some users.` instead of the previous ones.

Check it:

### Enough inferring

So, when inferring help text, the precedence order from lowest priority to highest is:

* `sub_app = typer.Typer(callback=some_function)`
* `@sub_app.callback()`
* `app.add_typer(sub_app, callback=new_function)`

That's for inferring the help text from functions.

But if you set the help text explicitly, that has a higher priority than these.

## Set the name and help

Let's now see the places where you can set the command name and help text, from lowest priority to highest.

Tip:

Setting the help text explicitly always has a higher precedence than inferring from a callback function.

### Name and help in `typer.Typer()`

You could have all the callbacks and overrides we defined before, but the help text was inferred from the function docstring.

If you set it explicitly, that takes precedence over inferring.

You can set it when creating a new `typer.Typer()`:

Note:

The rest of the callbacks and overrides are there only to show you that they don't affect the name and help text when you set it explicitly.

We set an explicit help `Explicit help.`.

So that will take precedence now.

Check it:

### Help text in `@app.callback()`

Many parameters that you use when creating a `typer.Typer()` app can be overridden in the parameters of `@app.callback()`.

Continuing with the previous example, we now override the `help` in `@user_app.callback()`:

And now the help text will be `Help from callback for users.`.

Check it:

### Name and help in `app.add_typer()`

And finally, with the highest priority, you can override all that by explicitly setting the `name` and `help` in `app.add_typer()`, just like we did on the first example above:

And now, with the highest priorities of them all, the command name will now be `cake-sith-users` and the help text will be `Unlimited powder! Eh, users.`.

Check it:

## Recap

The precedence to generate a command's **help**, from lowest priority to highest, is:

* Implicitly inferred from `sub_app = typer.Typer(callback=some_function)`
* Implicitly inferred from the callback function under `@sub_app.callback()`
* Implicitly inferred from `app.add_typer(sub_app, callback=some_function)`
* Explicitly set on `sub_app = typer.Typer(help="Some help.")`
* Explicitly set on `app.add_typer(sub_app, help="Some help.")`

And the priority to set the command's **name**, from lowest priority to highest, is:

* Explicitly set on `sub_app = typer.Typer(name="some-name")`
* Explicitly set on `app.add_typer(sub_app, name="some-name")`

So, `app.add_typer(sub_app, name="some-name", help="Some help.")` always wins.
