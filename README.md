# How to reproduce the error

* Clone the repo
* From the root of the project, run
`python app.py`

```
Traceback (most recent call last):
  File "<...>\InvalidImportError\app.py", line 3, in <module>
    from routes.myobject import MyObject
  File "<...>\InvalidImportError\routes\__init__.py", line 1, in <module>
    from myobject import MyObject
ModuleNotFoundError: No module named 'myobject'
```
