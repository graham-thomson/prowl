## Prowl Python3 Library

#### Purpose

A _very_ lightweight Prowl (https://www.prowlapp.com/) Python library written in vanilla Python3. Other libraries on their site are written in Python2.

Prowl is an app for iOS devices that allows you to send custom push notifications to devices. This is very useful for Raspberry Pi tinkering and notifying yourself when long running processes finish (e.g. fitting a random forest model on large a dataset). 

#### Usage

```python
import prowl

# mock api key
api_key = "0123456789012345678901234567890123456789"

p = prowl.api.Prowl(api_key=api_key, application="my_app")

print(p.send_message(title="foo", message="Hello, world."))
```

#### Output
```xml
<?xml version="1.0" encoding="UTF-8"?>
<prowl>
<success code="200" remaining="999" resetdate="1550541776" />
</prowl>
```