# CLI Arguments with Environment Variables

You can also configure a *CLI argument* to read a value from an environment variable if it is not provided in the command line as a *CLI argument*.

An **environment variable** (also known as an **env var**) is a value that lives outside of your Python code, in the operating system, and can be read by your application and other programs.

Tip:

Read the [Environment Variables guide](https://tiangolo.com/guides/environment-variables/) for a detailed, cross-platform explanation.

To do that, use the `envvar` parameter for `typer.Argument()`:

In this case, the *CLI argument* `name` will have a default value of `"World"`, but will also read any value passed to the environment variable `AWESOME_NAME` if no value is provided in the command line:

Tip: Windows PowerShell

In PowerShell, set the environment variable first and then run the command:

```console
$ $Env:AWESOME_NAME = "Wednesday"
$ uv run python main.py
```

## Multiple environment variables

You are not restricted to a single environment variable, you can declare a list of environment variables that could be used to get a value if it was not passed in the command line:

Check it:

## Hide an env var from the help text

By default, environment variables used will be shown in the help text, but you can disable them with `show_envvar=False`:

Check it:
