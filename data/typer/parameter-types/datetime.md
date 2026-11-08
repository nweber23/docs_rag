# DateTime

You can specify a *CLI parameter* as a Python [`datetime`](https://docs.python.org/3/library/datetime.html).

Your function will receive a standard Python `datetime` object, and again, your editor will give you completion, etc.

Typer will accept any string from the following formats:

* `%Y-%m-%d`
* `%Y-%m-%dT%H:%M:%S`
* `%Y-%m-%d %H:%M:%S`

Check it:

## Custom date format

You can also customize the formats received for the `datetime` with the `formats` parameter.

`formats` receives a list of strings with the date formats that would be passed to [datetime.strptime()](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime).

For example, let's imagine that you want to accept an ISO formatted datetime, but for some strange reason, you also want to accept a format with:

* first the month
* then the day
* then the year
* separated with "`/`"

...It's a crazy example, but let's say you also needed that strange format:

Tip:

Notice the last string in `formats`: `"%m/%d/%Y"`.

Check it:
