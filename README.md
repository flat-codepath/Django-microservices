# 🧩 Django Microservices Architecture

This project demonstrates a **Django microservices setup** with:
- 🧰 Multiple independent Django services
- 🗃️ Separate `.env` files and databases per service
- 🐳 Dockerized services with `docker-compose`
- 📦 Service Discovery using **Consul**
- 📊 API Monitoring via **Admin Server**
- 🧭 Distributed tracing using **Zipkin**
- 🧪 Internal API communication via `requests`

---

## 📁 Project Structure

```bash
django-microservices/
├── docker-compose.yml
├── .gitignore
├── README.md
├── user_service/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── .env
│   └── ...
├── product_service/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── .env
│   └── ...
├── consul/
│   └── config.json
├── zipkin/
│   └── docker-compose config
