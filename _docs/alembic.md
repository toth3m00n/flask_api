### Commands 

+ create initiate
```flask db init```

---
+ create migration file ```flask db migrate -m "initial migration"```

---

+ migrate ```flask db upgrade```

---
P.S. If you have for exemple
```    import fkcommerce.core.models  # noqa: F401
ModuleNotFoundError: No module named 'fkcommerce'
```
try to mark source root dir fkcommerce 

**if you have connnection problems and you have correct db values
means have ahother proccess in port 
in my case i killed postgres pgAdmin**