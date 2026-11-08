# On-call rotation

Each on-call shift lasts 7 days and starts on Monday at 10:00 Berlin time. The rotation
has five engineers. Handover happens in a 15-minute call, and the outgoing engineer
writes a short summary in the `#oncall-handover` channel.

## Severity levels

- Severity 1 (service down for all customers): acknowledge within 10 minutes.
- Severity 2 (a major feature is broken): acknowledge within 1 hour.
- Severity 3 (minor bug, workaround exists): handled in the next working day.

An incident report is mandatory for every Severity 1 incident and must be published
within 3 working days.
