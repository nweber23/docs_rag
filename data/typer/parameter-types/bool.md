# Boolean CLI Options

We have seen some examples of *CLI options* with `bool`, and how **Typer** creates `--something` and `--no-something` automatically.

But we can customize those names.

## Only `--force`

Let's say that we want a `--force` *CLI option* only, we want to discard `--no-force`.

We can do that by specifying the exact name we want:

Now there's only a `--force` *CLI option*:

## Alternative names

Now let's imagine we have a *CLI option* `--accept`.

And we want to allow setting `--accept` or the contrary, but `--no-accept` looks ugly.

We might want to instead have `--accept` and `--reject`.

We can do that by passing a single `str` with the 2 names for the `bool` *CLI option* separated by `/`:

Check it:

## Short names

The same way, you can declare short versions of the names for these *CLI options*.

For example, let's say we want `-f` for `--force` and `-F` for `--no-force`:

Check it:

## Only names for `False`

If you want to (although it might not be a good idea), you can declare only *CLI option* names to set the `False` value.

To do that, use a space and a single `/` and pass the negative name after:

Tip:

Have in mind that it's a string with a preceding space and then a `/`.

So, it's `" /-S"` not `"/-S"`.

Check it:
