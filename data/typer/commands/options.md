# Command CLI Options

Commands can also have their own *CLI options*.

In fact, each command can have different *CLI arguments* and *CLI options*:

Here we have multiple commands, with different *CLI parameters*:

* `create`:
    * `username`: a *CLI argument*.
* `delete`:
    * `username`: a *CLI argument*.
    * `--force`: a *CLI option*, if not provided, it's prompted.
* `delete-all`:
    * `--force`: a *CLI option*, if not provided, it's prompted.
* `init`:
    * Doesn't take any *CLI parameters*.

Tip:

Check the command `delete-all`, by default command names are generated from the function name, replacing `_` with `-`.

Test it:
