# demo

authService 作为主入口

curl -H 'Content-Type: application/json' http://localhost:5001/v1/auth/login

curl -H 'Content-Type: application/json' http://localhost:5001/v1/auth/user/get_user

curl -H 'Content-Type: application/json' -d '{"name": "jack", "age": 5}' http://localhost:5001/v1/auth/user/add_user
