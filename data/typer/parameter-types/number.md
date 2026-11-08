# Number

You can define numeric validations with `max` and `min` values for `int` and `float` *CLI parameters*:

*CLI arguments* and *CLI options* can both use these validations.

You can specify `min`, `max` or both.

Check it:

## Clamping numbers

You might want to, instead of showing an error, use the closest minimum or maximum valid values.

You can do it with the `clamp` parameter:

And then, when you pass data that is out of the valid range, it will be "clamped", the closest valid value will be used:

## Counter *CLI options*

You can make a *CLI option* work as a counter with the `count` parameter:

It means that the *CLI option* will be like a boolean flag, e.g. `--verbose`.

And the value you receive in the function will be the amount of times that `--verbose` was added:
