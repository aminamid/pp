# Usage

colorpp.py print some python objects.

```
>>> import colorpp
>>> colorpp.pprint("test")
>>> colorpp.pprint( {"id": 65535, "value": 3.14, "list": [1,2,3] } )

>>> import logging
>>> logging.basicConfig()
>>> logging.warning( colorpp.pprintf(object) )

```

From commandline, colorpp.py without args read sys.stdin , and try to parse as json, or yaml.
If there is argument, colorpp.py open the file, and try to parse as json, or yaml.

```
$ echo '{ "msg": "this is json" }' | colorpp.py
$ echo '{ msg: this is yaml }' | colorpp.py
$ echo '{ "msg": "this is file" }' > smpl.json
$ colorpp.py smpl.json 
```

