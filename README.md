# speewee
* Upgrade based on official peewee 3.14.0
* Add some functions that are not officially available

## Guide to use
`pip install speewee`

### example

```python
from speewee import Model, CharField, MySQLDatabase

database = MySQLDatabase("db name",
                         user="db user",
                         password="db password",
                         host="127.0.0.1",
                         port=3306
                         )


class BaseModel(Model):
  class Meta:
    database = database


class User(BaseModel):
  name = CharField(description="user name")

  class Meta:
    table_name = "users"
    table_description = "user table"
```

* In addition, it is consistent with peewee
## thank
* Thank you very much for seeing this. I'm very happy if I can help you. I don't need a cup of coffee. Please give me a 
  little star with your beautiful hands
  
* Thank you so much for [peewee](https://github.com/coleifer/peewee)
