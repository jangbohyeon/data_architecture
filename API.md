## favorite

* 기능: 선호종목(기업) 추가 & 리스트 얻기

* URI
   - IP:port/favorite

* Client --> Server
  - Format: JSON
  - Example
  
```python
* 선호종목(기업) 추가하는 경우
{
   "request_type": "add",
   "session_id": "...",
   "favorite": ["...", "...", ...]
}

* 선호종목(기업) 리스트 얻는 경우
{
   "request_type": "get",
   "session_id": "..."
}
```

* Server --> Client
  - Format: JSON
  - Example
  
```python
* 선호종목(기업) 추가 성공
{
   "session_id": "...",
   "result": true,
   "msg": ""
}

* 선호종목(기업) 추가 실패
{
   "session_id": "...",
   "result": false,
   "msg": "..."
}

* 실패 (예: 올바르지 않은 접근)
{
   "result": false,
   "msg": "..."
}

* 선호종목(기업) 리스트 얻는 경우
{
   "session_id": "...",
   "favorite": ["...", "...", ...]
}
![image](https://user-images.githubusercontent.com/49804605/121778638-c09cbc00-cbd2-11eb-92cd-1e508f717ffb.png)
