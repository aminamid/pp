# Usage

pp.py print some python objects.

```
>>> import pp
>>> pp.pprint("test")
>>> pp.pprint( {"id": 65535, "value": 3.14, "list": [1,2,3] } )

>>> import logging
>>> logging.basicConfig()
>>> logging.warning( pp.pprintf(object) )

```

From commandline, pp.py without args read sys.stdin , and try to parse as json, or yaml.
If there is argument, pp.py open the file, and try to parse as json, or yaml.

```
$ echo '{ "msg": "this is json" }' | pp.py
$ echo '{ msg: this is yaml }' | pp.py
$ echo '{ "msg": "this is file" }' > smpl.json
$ pp.py smpl.json 
```

