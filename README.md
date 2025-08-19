Create a Docker network first: 
docker network create -d bridge flask-to-sql

Run MySQL container:
docker run -d   --name mysql_db   --network flask-to-sql   -e MYSQL_ROOT_PASSWORD=rootpass   -e MYSQL_DATABASE=flaskdb   -p 3306:3306   mysql:8.0

Build Flask image: 
docker build -t flask-app .

Run Flask container on same network:
docker run -d   --name flask_app   --network flask-to-sql   -e DB_HOST=mysql_db   -e DB_USER=root   -e DB_PASSWORD=rootpass   -e DB_NAME=flaskdb   -p 5000:5000   flask-app:latest

Initialize Database Table 
Exec into MySQL: 
docker exec -it mysql_db mysql -uroot -prootpass flaskdb

Inside MySQL shell:
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

app is reday ......



<img width="1006" height="460" alt="Screenshot from 2025-08-20 02-07-22" src="https://github.com/user-attachments/assets/0ff06d6a-75c0-420f-a258-4ccef3a577ff" />

<img width="1201" height="996" alt="Screenshot from 2025-08-20 02-06-50" src="https://github.com/user-attachments/assets/14bd4853-727a-4266-b278-d291a759ad31" />

