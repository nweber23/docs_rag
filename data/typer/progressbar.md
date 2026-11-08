# Progress Bar

If you are executing an operation that can take some time, you can inform it to the user. 🤓

## Progress Bar

You can use [Rich's Progress Display](https://rich.readthedocs.io/en/stable/progress.html) to show a progress bar, for example:

You put the thing that you want to iterate over inside of Rich's `track()`, and then iterate over that.

Check it:

...actually, it will look a lot prettier. ✨ But I can't show you the animation here in the docs. 😅

The colors and information will look something like this:

## Spinner

When you don't know how long the operation will take, you can use a spinner instead.

Rich allows you to display many things in complex and advanced ways.

For example, this will show two spinners:

I can't show you the beautiful animation here in the docs. 😅

But at some point in time it will look like this (imagine it's spinning). 🤓

You can learn more about it in the [Rich docs for Progress Display](https://rich.readthedocs.io/en/stable/progress.html).

## Typer `progressbar`

If you can, you should use **Rich** as explained above, it has more features, it's more advanced, and can display information more beautifully. ✨

Tip:

If you can use Rich, use the information above, the Rich docs, and skip the rest of this page. 😎

But if you can't use Rich and have it disabled, Typer comes with a simple utility to show progress bars.

### Use `typer.progressbar`

Tip:

Remember, you are much better off using [Rich](https://rich.readthedocs.io/) for this. 😎

You can use `typer.progressbar()` with a `with` statement, as in:

```Python
with typer.progressbar(something) as progress:
    pass
```

And you pass as function argument to `typer.progressbar()` the thing that you would normally iterate over.

So, if you have a list of users, this could be:

```Python
users = ["Camila", "Rick", "Morty"]

with typer.progressbar(users) as progress:
    pass
```

And the `with` statement using `typer.progressbar()` gives you an object that you can iterate over, just like if it was the same thing that you would iterate over normally.

But by iterating over this object **Typer** will know to update the progress bar:

```Python
users = ["Camila", "Rick", "Morty"]

with typer.progressbar(users) as progress:
    for user in progress:
        typer.echo(user)
```

Tip:

Notice that there are 2 levels of code blocks. One for the `with` statement and one for the `for` statement.

Note:

This is mostly useful for operations that take some time.

In the example above we are faking it with `time.sleep()`.

Check it:

### Setting a Progress Bar `length`

Tip:

Remember, you are much better off using [Rich](https://rich.readthedocs.io/) for this. 😎

The progress bar is generated from the length of the iterable (e.g. the list of users).

But if the length is not available (for example, with something that fetches a new user from a web API each time) you can pass an explicit `length` to `typer.progressbar()`.

Check it:

#### About the function with `yield`

If you hadn't seen something like that `yield` above, that's a "[generator](https://docs.python.org/3/glossary.html#term-generator)".

You can iterate over that function with a `for` and at each iteration it will give you the value at `yield`.

`yield` is like a `return` that gives values multiple times and let's you use the function in a `for` loop.

For example:

```Python
def iterate_user_ids():
    # Let's imagine this is a web API, not a range()
    for i in range(100):
        yield i

for i in iterate_user_ids():
    print(i)
```

would print each of the "user IDs" (here it's just the numbers from `0` to `99`).

### Add a `label`

Tip:

Remember, you are much better off using [Rich](https://rich.readthedocs.io/) for this. 😎

You can also set a `label`:

Check it:

## Iterate manually

If you need to manually iterate over something and update the progress bar irregularly, you can do it by not passing an iterable but just a `length` to `typer.progressbar()`.

And then calling the `.update()` method in the object from the `with` statement:

Check it:
