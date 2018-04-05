# pynopla
quick and dirty Inopla cloud pbx api thing

#### Why Async?
Well, just because of the fun of it. And to learn asyncio, too. And it's energy efficient, and it's great and cool :)
Another reason might be that it's handy to add arbitrary periodically events - or maybe act on external events from the
Inopla api.

#### Scope
This can of course be a start for a fully featured Inpopla.de Client, evolving as needed. So, of course, PRs are very
welcome.
Also I'm happy if you think you can improve things, let me know, I'm open for everything.

#### ToDo
- add tests (mocked)
- add more features
- investigate why the docker container is 706MB in size and improve

#### Usage of the example
The example provides a health check for your users (endpoints) connected to Inopla.de - once a user get disconnected,
you'll get notified by email.
Most easy is to just start a Docker container (f.e. on your Synology or somewhere else)

```python
docker run -e INOPLA_API_ID=your_id -e INOPLA_API_KEY="your_key" -e SMTP_HOST='your_smtp_host' -e SMTP_USER='your_smtp_user' -e SMTP_PASS='your_smtp_pass' -d elmcrest/pynopla
```
*optional environment variables*

```python
-e SMTP_RECIPIENT="your_recipient"  # defaults to smtp_user
```
```python
-e PERIODIC_TIME="your_time_in_seconds"  # defaults to 900 seconds (15 mins)
```

Greetings,
elmcrest
