# Custom Command Name

By default, the command names are generated from the function name.

So, if your function is something like:

```Python
def create(username: str): ...
```

Then the command name will be `create`.

But if you already had a function called `create()` somewhere in your code, you would have to name your CLI function differently.

And what if you wanted the command to still be named `create`?

For this, you can set the name of the command in the first parameter for the `@app.command()` decorator:

Now, even though the functions are named `cli_create_user()` and `cli_delete_user()`, the commands will still be named `create` and `delete`:

Note that any underscores in the function name will be replaced with dashes.

So if your function is something like:

```Python
def create_user(username: str): ...
```
Then the command name will be `create-user`.
