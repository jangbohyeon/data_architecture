## login

* 기능: 사용자 로그인

* URI
   - IP:port/login

* Client --> Server
  - Format: JSON
  - Example

```python
{
   "user_id": "...",
   "passwd": "..."
}
```

* Server --> Client
  - Format: JSON
  - Example
  
```python
* Success case
{"msg":"","result":true,"session_id":"..."}

* Fail case
{"msg":"...", result":false, "session_id":none}
![image](https://user-images.githubusercontent.com/49804605/121778435-d493ee00-cbd1-11eb-9eb4-3456649d7b5b.png)
