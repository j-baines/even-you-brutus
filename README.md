# Even You, Brutus?

*Even You, Brutus?* is a simple proof of concept dictionary brute forcing tool targeting the MikroTik RouterOS 6.x web interface. RouterOS notiously lacks brute force protections on the web and winbox interfaces. They've largely coasted off their custom authentication/encryption schemes from preventing these attacks. Previously, I'd [developed](https://github.com/tenable/routeros/tree/master/brute_force) other such tools, but MikroTik changed the algorithms and I had moved on. Luckily [Margin Research](https://margin.re/2022/06/pulling-mikrotik-into-the-limelight/) released a python library that can handle authentication from 6.34 - 6.49.8 (current release).

This was written in about 10 minutes, and only to prove that MikroTik hasn't implemented any protections on the web interface. Your milage may vary.

## Example Usage

```sh
albinolobster@mournland:~/even-you-brutus$ python3 evenyoubrutus.py --rhost 10.9.49.1 --username admin --dictionary dictionary.txt
Attempt 201
Success! Valid credentials:
admin:labpass1
```

## Credit

* Margin Research - webfig.py is entirely their work (with one tweak). The original can be found [here](https://github.com/MarginResearch/FOISted/blob/master/webfig.py).
* [Red Hot Chili Peppers](https://www.youtube.com/watch?v=TE4e3hmnDNs)
