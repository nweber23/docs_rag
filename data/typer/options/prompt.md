# CLI Option Prompt

It's also possible to, instead of just showing an error, ask for the missing value with `prompt=True`:

And then your program will ask the user for it in the terminal:

## Customize the prompt

You can also set a custom prompt, passing the string that you want to use instead of just `True`:

And then your program will ask for it using with your custom prompt:

## Confirmation prompt

In some cases you could want to prompt for something and then ask the user to confirm it by typing it twice.

You can do it passing the parameter `confirmation_prompt=True`.

Let's say it's a CLI app to delete a project:

And it will prompt the user for a value and then for the confirmation:
