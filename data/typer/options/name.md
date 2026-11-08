# CLI Option Name

By default **Typer** will create a *CLI option* name from the function parameter.

So, if you have a function with:

```Python
def main(user_name: Optional[str] = None):
    pass
```

or

```Python
def main(user_name: Annotated[Optional[str], typer.Option()] = None):
    pass
```

**Typer** will create a *CLI option*:

```
--user-name
```

But you can customize it if you want to.

Let's say the function parameter name is `user_name` as above, but you want the *CLI option* to be just `--name`.

You can pass the *CLI option* name that you want to have in the following positional argument passed to `typer.Option()`:

Note:

"[Positional](https://docs.python.org/3.8/glossary.html#term-argument)" means that it's not a function argument with a keyword name.

For example `show_default=True` is a keyword argument. "`show_default`" is the keyword.

But in `"--name"` there's no `option_name="--name"` or something similar, it's just the string value `"--name"` that goes in `typer.Option()`.

That's a "positional argument" in a function.

Check it:

## *CLI option* short names

A short name is a *CLI option* name with a single dash (`-`) instead of 2 (`--`) and a single letter, like `-n` instead of `--name`.

For example, the `ls` program has a *CLI option* named `--size`, and the same *CLI option* also has a short name `-s`:

### *CLI option* short names together

Short names have another feature, when they have a single letter, as in `-s`, you can put several of these *CLI options* together, with a single dash.

For example, the `ls` program has these 2 *CLI options* (among others):

* `--size`: show the sizes of the listed files.
* `--human`: show a human-readable format, like `1MB` instead of just `1024`.

And these 2 *CLI options* have short versions too:

* `--size`: short version `-s`.
* `--human`: short version `-h`.

So, you can put them together with `-sh` or `-hs`:

### *CLI option* short names with values

When you use *CLI options* with short names, you can put them together if they are just boolean flags, like `--size` or `--human`.

But if you have a *CLI option* `--file` with a short name `-f` that takes a value, if you put it with other short names for *CLI options*, you have to put it as the last letter, so that it can receive the value that comes right after.

For example, let's say you are decompressing/extracting a file `myproject.tar.gz` with the program `tar`.

You can pass these *CLI option* short names to `tar`:

* `-x`: means "e`X`tract", to decompress and extract the contents.
* `-v`: means "`V`erbose", to print on the screen what it is doing, so you can know that it's decompressing each file and can entertain yourself while you wait.
* `-f`: means "`F`ile", this one requires a value, the compressed file to extract (in our example, this is `myproject.tar.gz`).
    * So if you use all the short names together, this `-f` has to come last, to receive the value that comes next to it.

For example:

### Defining *CLI option* short names

In **Typer** you can also define *CLI option* short names the same way you can customize the long names.

You can pass *positional* arguments to `typer.Option()` to define the *CLI option* name(s).

Tip:

Remember the *positional* function arguments are those that don't have a keyword.

All the other function arguments/parameters you pass to `typer.Option()` like `prompt=True` and `help="This option blah, blah"` require the keyword.

You can overwrite the *CLI option* name to use as in the previous example, but you can also declare extra alternatives, including short names.

For example, extending the previous example, let's add a *CLI option* short name `-n`:

Here we are overwriting the *CLI option* name that by default would be `--user-name`, and we are defining it to be `--name`. And we are also declaring a *CLI option* short name of `-n`.

Check it:

### *CLI option* only short name

If you only declare a short name like `-n` then that will be the only *CLI option* name. And neither `--name` nor `--user-name` will be available.

Check it:

### *CLI option* short name and default

Continuing with the example above, as **Typer** allows you to declare a *CLI option* as having only a short name, if you want to have the default long name plus a short name, you have to declare both explicitly:

Check it:

### *CLI option* short names together

You can create multiple short names and use them together.

You don't have to do anything special for it to work (apart from declaring those short versions):

Tip:

Notice that, again, we are declaring the long and short version of the *CLI option* names.

Check it:
