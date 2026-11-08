# Launching Applications

You can launch applications from your CLI program with `typer.launch()`.

It will launch the appropriate application depending on the URL or file type you pass it:

Check it:

## Locating a file

You can also make the operating system open the file browser indicating where a file is located with `locate=True`:

Tip:

The rest of the code in this example is just making sure the app directory exists and creating the config file.

But the most important part is the `typer.launch(config_file_str, locate=True)` with the argument `locate=True`.

Check it:
