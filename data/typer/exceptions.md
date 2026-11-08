# Exceptions and Errors

When your code has errors and you run it, it will show the error and an exception.

Typer does some tricks to help you detect those errors quickly.

## Example Broken App

Let's take this example broken app:

This code is broken because you can't sum a string and a number (`name + 3`).

## Exceptions with Rich

**Typer** will automatically use Rich to automatically show you nicely printed errors.

It will **omit** all the parts of the traceback (the chain of things that called your function) that come from the internal parts in Typer.

So, the error you see will be **much clearer** and simpler, to help you detect the problem in your code quickly:

## Exceptions without Rich

You can disable Rich globally using the environmental variable `TYPER_USE_RICH`.

In this case, Typer will still do some tricks to show you the information **as clearly as possible**:

## Show Local Variables for Detailed Debugging

When using Rich, you can get more verbose output by printing the values of the <abbr title="a variable that lives only inside a function, its value is only visible inside of it">local variables</abbr> as part of the error message.

By default, this setting is disabled (since Typer 0.23.0) to avoid showing **delicate information**, for example a **password**, a **key** or a **token**.

In these cases, it could be problematic if the automatic errors show the value in those local variables.

This would be relevant in particular if your CLI application is being run on some CI (continuous integration) system that is recording the logs.

However, if you do want to enable the setting, you can set the parameter `pretty_exceptions_show_locals=True` when creating the `typer.Typer()` application:

Now, when using Rich, you will see the error with the local variables:

Being able to see the values of local variables is very **helpful** to diagnose, **debug**, and fix problems.

But you should only enable it if you're not dealing with delicate information.

## Disable Short Output

If you want to show the full exception, including the internal parts in Typer, you can use the parameter `pretty_exceptions_short=False`:

Now when you run it, you will see the whole output:

## Disable Pretty Exceptions

You can also entirely disable pretty exceptions with the parameter `pretty_exceptions_enable=False`:

And now you will see the full standard exception as with any other Python program:

You could also achieve the same with the environment variable `TYPER_STANDARD_TRACEBACK=1` (or by setting the deprecated variable `_TYPER_STANDARD_TRACEBACK=1`).

This will work for any other Typer program too, in case you need to debug a problem in a Typer program made by someone else:
