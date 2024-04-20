## Flask Api Project

### Stack:

### About

### Notes

+ Start database in docker + adminer
```angular2html
docker-compose up 
```
access to **adminer** you may get in url:
```angular2html
http://localhost:8080/
```
---

**!!!Important**

**All passwords and other turnouts in  
env_vars - i did it specially to simplier development**

---

**db_setup.sh** - create database fkcommerse and download extra extention

*it happen bc*

docker-compose.yml
```angular2html
    volumes:
      - ./scripts:/docker-entrypoint-initdb.d
```
- execute all scripts in ```/docker-entrypoint-initdb.d ```
---
use if you update your project
```
pip freeze > requirements.txt
```
