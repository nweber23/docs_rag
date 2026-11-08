# CLI Option autocompletion

As you have seen, apps built with **Typer** have completion in your shell that works when you create a Python package or using the `typer` command.

It normally completes *CLI options*, *CLI arguments*, and subcommands (that you will learn about later).

But you can also provide auto completion for the **values** of *CLI options* and *CLI arguments*. We will learn about that here.

## Review completion

Before checking how to provide custom completions, let's check again how it works.

After installing completion for your own Python package (or using the `typer` command), when you use your CLI program and start adding a *CLI option* with `--` and then hit <kbd>TAB</kbd>, your shell will show you the available *CLI options* (the same for *CLI arguments*, etc).

To check it quickly without creating a new Python package, use the `typer` command.

Then let's create a small example program:

And let's try it with the `typer` command to get completion:

## Custom completion for values

Right now we get completion for the *CLI option* names, but not for the values.

We can provide completion for the values creating an `autocompletion` function, similar to the `callback` functions from [CLI Option Callback and Context](./options/callback-and-context.md):

We return a `list` of strings from the `complete_name()` function.

And then we get those values when using completion:

We got the basics working. Now let's improve it.

## Check the incomplete value

Right now, we always return those values, even if users start typing `Sebast` and then hit <kbd>TAB</kbd>, they will also get the completion for `Camila` and `Carlos` (depending on the shell), while we should only get completion for `Sebastian`.

But we can fix that so that it always works correctly.

Modify the `complete_name()` function to receive a parameter of type `str`, it will contain the incomplete value.

Then we can check and return only the values that start with the incomplete value from the command line:

Now let's try it:

Now we are only returning the valid values, that start with `Ca`, we are no longer returning `Sebastian` as a completion option.

Tip:

You have to declare the incomplete value of type `str` and that's what you will receive in the function.

No matter if the actual value will be an `int`, or something else, when doing completion, you will only get a `str` as the incomplete value.

And the same way, you can only return `str`, not `int`, etc.

## Add help to completions

Right now we are returning a `list` of `str`.

But some shells (Zsh, Fish, PowerShell) are capable of showing extra help text for completion.

We can provide that extra help text so that those shells can show it.

In the `complete_name()` function, instead of providing one `str` per completion element, we provide a `tuple` with 2 items. The first item is the actual completion string, and the second item is the help text.

So, in the end, we return a `list` of `tuples` of `str`:

Tip:

If you want to have help text for each item, make sure each item in the list is a `tuple`. Not a `list`.

In the end, the return will be a `list` (or other iterable) of `tuples` of 2 `str`.

Note:

The help text will be visible in Zsh, Fish, and PowerShell.

Bash doesn't support showing the help text, but completion will still work the same.

If you have a shell like Zsh, it would look like:

## Simplify with `yield`

Instead of creating and returning a list with values (`str` or `tuple`), we can use `yield` with each value that we want in the completion.

That way our function will be a [generator](https://docs.python.org/3.8/glossary.html#index-19) that **Typer** can iterate:

That simplifies our code a bit and works the same.

Tip:

If the `yield` part seems complex for you, don't worry, you can just use the version with the `list` above.

In the end, that's just to save us a couple of lines of code.

Note:

The function can use `yield`, so it doesn't have to return strictly a `list`, it just has to be [iterable](https://docs.python.org/3.8/glossary.html#term-iterable).

But each of the elements for completion has to be a `str` or a `tuple` (when containing a help text).

## Access other *CLI parameters* with the Context

Let's say that now we want to modify the program to be able to "say hi" to multiple people at the same time.

So, we will allow multiple `--name` *CLI options*.

Tip:

You will learn more about *CLI parameters* with multiple values later in the tutorial.

So, for now, take this as a sneak peek 😉.

For this we use a `list` of `str`:

And then we can use it like:

### Getting completion for multiple values

And the same way as before, we want to provide **completion** for those names. But we don't want to provide the **same names** for completion if they were already given in previous parameters.

For that, we will access and use the "Context". Every Typer application has a special object called a "Context" that is normally hidden.

But you can access the context by declaring a function parameter of type `typer.Context`.

And from that context you can get the current values for each parameter.

We are getting the `names` already provided with `--name` in the command line before this completion was triggered.

If there's no `--name` in the command line, it will be `None`, so we use `or []` to make sure we have a `list` (even if empty) to check its contents later.

Then, when we have a completion candidate, we check if each `name` was already provided with `--name` by checking if it's in that list of `names` with `name not in names`.

And then we `yield` each item that has not been used yet.

Check it:

Tip:

It's quite possible that if there's only one option left, your shell will complete it right away instead of showing the option with the help text, to save you more typing.

## Getting the raw *CLI parameters*

You can also get the raw *CLI parameters*, just a `list` of `str` with everything passed in the command line before the incomplete value.

For example, something like `["typer", "main.py", "run", "--name"]`.

Tip:

This would be for advanced scenarios, in most use cases you would be better off using the context.

But it's still possible if you need it.

As a simple example, let's show it on the screen before completion.

Because completion is based on the output printed by your program (handled internally by **Typer**), during completion we can't just print something else as we normally do.

### Printing to "standard error"

Tip:

If you need a refresher about what is "standard output" and "standard error" check the section in [Printing and Colors: "Standard Output" and "Standard Error"](./printing.md#standard-output-and-standard-error).

The completion system only reads from "standard output", so, printing to "standard error" won't break completion. 🚀

You can print to "standard error" with a **Rich** `Console(stderr=True)`.

Using `stderr=True` tells **Rich** that the output should be shown in "standard error".

Note:

If you have disabled Rich, you can also use `print(lastname, file=sys.stderr)` or `typer.echo("some text", err=True)` instead.

We get all the *CLI parameters* as a raw `list` of `str` by declaring a parameter with type `list[str]`, here it's named `args`.

Tip:

Here we name the list of all the raw *CLI parameters* `args` because that's the usual convention.

But it doesn't contain only *CLI arguments*, it has everything, including *CLI options* and values, as a raw `list` of `str`.

And then we just print it to "standard error".

Tip:

This is a very simple (and quite useless) example, just so you know how it works and that you can use it.

But it's probably useful only in very advanced use cases.

## Getting the Context and the raw *CLI parameters*

Of course, you can declare everything if you need it, the context, the raw *CLI parameters*, and the incomplete `str`:

Check it:

## Types, types everywhere

**Typer** uses the type declarations to detect what it has to provide to your `autocompletion` function.

You can declare function parameters of these types:

* `str`: for the incomplete value.
* `typer.Context`: for the current context.
* `list[str]`: for the raw *CLI parameters*.

It doesn't matter how you name them, in which order, or which ones of the 3 options you declare. It will all "**just work**" ✨
