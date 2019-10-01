# websocketd with authentication

Test only

## generate jwt

```bpython
from datetime import datetime, timedelta;import jwt,time; xxx=jwt.encode(dict(username="gustavo",client="gmftech",exp=(datetime.now() + timedelta(hours=12)).timestamp()),"zaq12wsxcde3",algorithm='HS256');time.sleep(3);jwt.decode(xxx,"zaq12wsxcde3",algorithm='HS256');print(xxx)
```

## run

```bash
docker-compose up --build
```
