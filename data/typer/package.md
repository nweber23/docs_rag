# Building a Package

When you create a CLI program with **Typer** you probably want to create your own Python package.

That's what allows your users to install it and have it as an independent program that they can use in their terminal.

And that's also required for shell auto completion to work (unless you use your program through the `typer` command).

Nowadays, there are several ways and tools to create Python packages (what you install with `pip install something` or `uv add something`).

You might even have your favorite already.

Here's a very opinionated, short guide, showing one of the alternative ways of creating a Python package with a **Typer** app, from scratch.

Tip:

If you already have a favorite way of creating Python packages, feel free to skip this.

## Prerequisites

For this guide we'll use [uv](https://docs.astral.sh/uv/).

uv's docs are great, so go ahead, check them and install it.

## Create a project

Let's say we want to create a CLI application called `portal-gun`.

To make sure your package doesn't collide with the package created by someone else, we'll name it with a prefix of your name.

So, if your name is Rick, we'll call it `rick-portal-gun`.

Create a project with uv:

## Dependencies and environment

Add `typer` to your dependencies:

You can see that you have a generated project structure that looks like:

```
.
├── pyproject.toml
├── README.md
├── src
│   └── rick_portal_gun
│     └── __init__.py
└── uv.lock
```

## Create your app

Now let's create an extremely simple **Typer** app.

Create a file `src/rick_portal_gun/main.py` with:

```Python
import typer

app = typer.Typer()

@app.callback()
def callback():
    """
    Awesome Portal Gun
    """

@app.command()
def shoot():
    """
    Shoot the portal gun
    """
    typer.echo("Shooting portal gun")

@app.command()
def load():
    """
    Load the portal gun
    """
    typer.echo("Loading portal gun")
```

Tip:

As we are creating an installable Python package, there's no need to add a section with `if __name__ == "__main__":`.

## Modify the README

Let's change the README to have something like:

```Markdown
# Portal Gun

The awesome Portal Gun
```

## Add a "script"

We are creating a Python package that can be installed with `uv add` or `pip install`.

But we want it to provide a CLI program that can be executed in the shell.

To do that, we add a configuration to the `pyproject.toml` in the section `[project.scripts]`:

```TOML hl_lines="12 13"
[project]
name = "rick-portal-gun"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
authors = ["Rick Sanchez <rick@example.com>"]
requires-python = ">=3.14"
dependencies = [
    "typer>=0.21.0",
]

[project.scripts]
rick-portal-gun = "rick_portal_gun.main:app"

[build-system]
requires = ["uv_build>=0.8.14,<0.9.0"]
build-backend = "uv_build"
```

Here's what that line means:

`rick-portal-gun`: will be the name of the CLI program. That's how we will call it in the terminal once it is installed. Like:

`rick_portal_gun.main`, in the part `"rick_portal_gun.main:app"`, with underscores, refers to the Python module to import. That's what someone would use in a section like:

```Python
from rick_portal_gun.main import # something goes here
```

The `app` in `"rick_portal_gun.main:app"` is the thing to import from the module, and to call as a function, like:

```Python
from rick_portal_gun.main import app

app()
```

That config section tells uv that when this package is installed, we want it to create a command line program called `rick-portal-gun`.

And that the object to call (like a function) is the one in the variable `app` inside of the module `rick_portal_gun.main`.

## Install your package

That's what we need to create a package.

You can now install it:

## Try your CLI program

Your package is installed in the environment created by uv, but you can already use it.

## Create a wheel package

Python packages have a standard format called a "wheel". It's a file that ends in `.whl`.

You can create a wheel with uv:

After that, if you check in your project directory, you should now have a couple of extra files at `./dist/`:

``` hl_lines="3 4"
.
├── dist
│   ├── rick_portal_gun-0.1.0-py3-none-any.whl
│   └── rick-portal-gun-0.1.0.tar.gz
├── pyproject.toml
├── README.md
├── ...
```

The `.whl` is the wheel file. You can send that wheel file to anyone and they can use it to install your program (we'll see how to upload it to PyPI in a bit).

## Test your wheel package

Now you can open another terminal and install that package as an isolated command-line tool with:

Tip:

`uv` installs the tool in its own isolated environment, avoiding conflicts with your projects and system Python.

Now you have your CLI program installed. And you can use it freely:

Having it installed globally (and not in a single environment), you can now install completion globally for it:

Tip:

If you want to remove completion you can just delete the added line in that file.

And after you restart the terminal you will get completion for your new CLI program:

## Support `python -m` (optional)

You may have seen that you can call many Python modules as scripts with `python -m some-module`.

For example, one way to call `pip` is:

But you can also call Python with the `-m` *CLI Option* and pass a module for it to execute as if it was a script, like:

Here we pass `pip` as the value for `-m`, so, Python will execute the module `pip` as if it was a script. And then it will pass the rest of the *CLI Parameters* (`install fastapi`) to it.

These two are more or less equivalent, the `install fastapi` will be passed to `pip`.

Tip:

In the case of `pip`, in many occasions it's actually recommended that you run it with `python -m`, because if you create a virtual environment with its own `python`, that will ensure that you use the `pip` from *that* environment.

### Add a `__main__.py`

You can support that same style of calling the package/module for your own package, simply by adding a file `__main__.py`.

Python will look for that file and execute it.

The file would live right beside `__init__.py` and `main.py`:

``` hl_lines="7"
.
├── pyproject.toml
├── README.md
├── src
│   └── rick_portal_gun
│     ├── __init__.py
│     ├── __main__.py
│     └── main.py
└── uv.lock
```

No other file has to import it, you don't have to reference it in your `pyproject.toml` or anything else, it just works by default, as it is standard Python behavior.

Then in that file you can execute your **Typer** program:

```Python
from .main import app

app()
```

Now, after installing your package, if you call it with `python -m` it will work:

Tip:

Notice that you have to pass the importable version of the package name, so `rick_portal_gun` instead of `rick-portal-gun`.

That works! 🚀

### Autocompletion and `python -m`

Have in mind that TAB completion (shell auto-completion) won't work when using `python -m`.

Auto-completion depends on the name of the program called, it's tied to each specific program name.

So, to have shell completion for `rick-portal-gun` you would have to call it directly:

But you can still support `python -m` for the cases where it's useful.

## Publish to PyPI (optional)

You can publish that new package to [PyPI](https://pypi.org/) to make it public, so others can install it easily.

So, go ahead and create an account there (it's free).

### PyPI API token

To do it, you first need to configure a PyPI auth token.

Login to [PyPI](https://pypi.org/).

And then go to [https://pypi.org/manage/account/token/](https://pypi.org/manage/account/token/) to create a new token.

Let's say your new API token is:

```
pypi-wubalubadubdub-deadbeef1234
```

Now configure uv to use this token by setting an environment variable:

### Publish to PyPI

Now you can publish your package.

Now you can go to PyPI and check your projects at [https://pypi.org/manage/projects/](https://pypi.org/manage/projects/).

You should now see your new "rick-portal-gun" package.

### Install from PyPI

Now to see that we can install it from PyPI, open another terminal, and uninstall the currently installed package.

And now install it again, but this time using just the name, so that `uv` pulls it from PyPI:

And now test the newly installed package from PyPI:

## Generate docs

You can use the `typer` command to generate docs for your package that you can put in your `README.md`:

You just have to pass it the module to import (`rick_portal_gun.main`) and it will detect the `typer.Typer` app automatically.

By specifying the `--name` of the program it will be able to use it while generating the docs.

### Publish a new version with the docs

Now you can publish a new version with the updated docs.

For that you need to first increase the version in `pyproject.toml`:

```TOML hl_lines="3"
[project]
name = "rick-portal-gun"
version = "0.2.0"
description = "Add your description here"
readme = "README.md"
authors = ["Rick Sanchez <rick@example.com>"]
requires-python = ">=3.14"
dependencies = [
    "typer>=0.21.0",
]

[project.scripts]
rick-portal-gun = "rick_portal_gun.main:app"

[build-system]
requires = ["uv_build>=0.8.14,<0.9.0"]
build-backend = "uv_build"
```

And then build and publish again:

And now you can go to PyPI, to the project page, and reload it, and it will now have your new generated docs.

## What's next

This is a very simple guide. You could add many more steps.

For example, you should use [Git](https://git-scm.com/), the version control system, to save your code.

You could use [uv](https://docs.astral.sh/uv/) to manage your installed CLI Python programs in isolated environments.

Maybe use automatic formatting with [Ruff](https://docs.astral.sh/ruff/).

You'll probably want to publish your code as open source to [GitHub](https://github.com/).

And then you could integrate a <abbr title="Continuous Integration">CI</abbr> tool to run your tests and deploy your package automatically.

And there's a long etc. But now you have the basics and you can continue on your own. 🚀
