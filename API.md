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
![image](https://user-images.githubusercontent.com/49804605/121778667-e0cc7b00-cbd2-11eb-960e-a404c23e43d0.png)

