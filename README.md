# Usage

pp.py print some python objects.

```
>>> import pp
>>> pp.pretty_print("test")
>>> pp.pretty_print( {"id": 65535, "value": 3.14, "list": [1,2,3] } )

```

From commandline, pp.py without args read sys.stdin , and try to parse as json, or yaml.
If there is argument, pp.py open the file, and try to parse as json, or yaml.

```
$ echo '{ "msg": "this is json" }' | python ppp.py
$ echo '{ msg: this is yaml }' | python ppp.py
$ echo '{ "msg": "this is file" }' > smpl.json
$ python ppp.py smpl.json 
```

