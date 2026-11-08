# Ask with Prompt

When you need to ask the user for info interactively you should normally use [*CLI Option*s with Prompt](options/prompt.md), because they allow using the CLI program in a non-interactive way (for example, a Bash script could use it).

But if you absolutely need to ask for interactive information without using a *CLI option*, you can use `typer.prompt()`:

Check it:

## Confirm

There's also an alternative to ask for confirmation. Again, if possible, you should use a [*CLI Option* with a confirmation prompt](options/prompt.md):

Check it:

## Confirm or abort

As it's very common to abort if the user doesn't confirm, there's an integrated parameter `abort` that does it automatically:

## Prompt with Rich

You can use Rich to prompt the user for input:

And when you run it, it will look like:
