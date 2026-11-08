# Password CLI Option and Confirmation Prompt

Apart from having a prompt, you can make a *CLI option* have a `confirmation_prompt=True`:

And the CLI program will ask for confirmation:

## A Password prompt

When receiving a password, it is very common (in most shells) to not show anything on the screen while typing the password.

The program will still receive the password, but nothing will be shown on screen, not even `****`.

You can achieve the same using `hide_input=True`.

And if you combine it with `confirmation_prompt=True` you can easily receive a password with double confirmation:

Check it:
