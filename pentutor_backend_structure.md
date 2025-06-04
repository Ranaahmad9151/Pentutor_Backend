# PenTutor Backend - Microservices Architecture

## 📁 Root Project Structure

```
pentutor-backend/
├── .env.example
├── .env.local
├── .env.production
├── .gitignore
├── docker-compose.yml
├── docker-compose.prod.yml
├── requirements.txt
├── requirements-dev.txt
├── manage.py
├── README.md
├── pytest.ini
├── setup.cfg
├── scripts/
│   ├── deploy.sh
│   ├── backup_db.sh
│   └── setup_env.sh
├── docs/
│   ├── API_DOCUMENTATION.md
│   ├── DEPLOYMENT.md
│   └── CONTRIBUTING.md
└── services/
    ├── __init__.py
    ├── core/              # Main Django Project
    ├── authentication/    # Auth Service
    ├── meetings/         # Zoom Clone Service
    ├── lms/             # Learning Management System
    ├── ai_services/     # AI Matching & Chatbot
    ├── payments/        # Payment Processing
    ├── job_board/       # Job Portal
    └── notifications/   # Email/SMS/Push Notifications
```

## 🏗️ Core Service Structure

### `/services/core/` - Main Django Project
```
core/
├── __init__.py
├── settings/
│   ├── __init__.py
│   ├── base.py
│   ├── development.py
│   ├── production.py
│   └── testing.py
├── urls.py
├── wsgi.py
├── asgi.py
├── middleware/
│   ├── __init__.py
│   ├── cors.py
│   ├── auth.py
│   └── logging.py
├── utils/
│   ├── __init__.py
│   ├── permissions.py
│   ├── validators.py
│   ├── helpers.py
│   └── exceptions.py
└── celery_app.py
```

## 🔐 Authentication Service

### `/services/authentication/`
```
authentication/
├── __init__.py
├── apps.py
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── profile.py
│   └── role.py
├── serializers/
│   ├── __init__.py
│   ├── auth.py
│   ├── user.py
│   └── profile.py
├── viewsets/
│   ├── __init__.py
│   ├── auth.py
│   ├── user.py
│   └── profile.py
├── urls.py
├── permissions.py
├── managers.py
├── admin.py
├── tasks.py
├── signals.py
├── migrations/
└── tests/
    ├── __init__.py
    ├── test_models.py
    ├── test_views.py
    └── test_serializers.py
```

## 🎥 Meetings Service (Zoom Clone)

### `/services/meetings/`
```
meetings/
├── __init__.py
├── apps.py
├── models/
│   ├── __init__.py
│   ├── meeting.py
│   ├── participant.py
│   ├── recording.py
│   ├── chat.py
│   ├── whiteboard.py
│   └── attendance.py
├── serializers/
│   ├── __init__.py
│   ├── meeting.py
│   ├── chat.py
│   └── whiteboard.py
├── viewsets/
│   ├── __init__.py
│   ├── meeting.py
│   ├── chat.py
│   ├── whiteboard.py
│   └── recording.py
├── consumers/          # WebSocket Consumers
│   ├── __init__.py
│   ├── meeting.py
│   ├── chat.py
│   └── whiteboard.py
├── routing.py          # WebSocket URLs
├── urls.py
├── permissions.py
├── tasks.py
├── utils/
│   ├── __init__.py
│   ├── webrtc.py
│   └── recording.py
├── signals.py
├── migrations/
└── tests/
```

## 📚 LMS Service

### `/services/lms/`
```
lms/
├── __init__.py
├── apps.py
├── models/
│   ├── __init__.py
│   ├── course.py
│   ├── lesson.py
│   ├── enrollment.py
│   ├── progress.py
│   ├── assignment.py
│   └── grade.py
├── serializers/
│   ├── __init__.py
│   ├── course.py
│   ├── enrollment.py
│   └── progress.py
├── viewsets/
│   ├── __init__.py
│   ├── course.py
│   ├── enrollment.py
│   ├── dashboard.py
│   └── progress.py
├── urls.py
├── permissions.py
├── filters.py
├── tasks.py
├── utils/
│   ├── __init__.py
│   └── progress_calculator.py
├── migrations/
└── tests/
```

## 🤖 AI Services

### `/services/ai_services/`
```
ai_services/
├── __init__.py
├── apps.py
├── models/
│   ├── __init__.py
│   ├── matching.py
│   └── chatbot.py
├── serializers/
│   ├── __init__.py
│   ├── matching.py
│   └── chatbot.py
├── viewsets/
│   ├── __init__.py
│   ├── matching.py
│   └── chatbot.py
├── urls.py
├── tasks.py
├── utils/
│   ├── __init__.py
│   ├── openai_client.py
│   ├── matching_algorithm.py
│   └── contact_blocker.py
├── consumers/          # Real-time chatbot
│   └── chatbot.py
├── routing.py
├── migrations/
└── tests/
```

## 💰 Payments Service

### `/services/payments/`
```
payments/
├── __init__.py
├── apps.py
├── models/
│   ├── __init__.py
│   ├── payment.py
│   ├── invoice.py
│   ├── subscription.py
│   └── transaction.py
├── serializers/
│   ├── __init__.py
│   ├── payment.py
│   └── invoice.py
├── viewsets/
│   ├── __init__.py
│   ├── payment.py
│   ├── webhook.py
│   └── invoice.py
├── urls.py
├── tasks.py
├── utils/
│   ├── __init__.py
│   ├── stripe_client.py
│   ├── jazzcash_client.py
│   └── paypal_client.py
├── webhooks/
│   ├── __init__.py
│   ├── stripe.py
│   ├── jazzcash.py
│   └── paypal.py
├── migrations/
└── tests/
```

## 💼 Job Board Service

### `/services/job_board/`
```
job_board/
├── __init__.py
├── apps.py
├── models/
│   ├── __init__.py
│   ├── job.py
│   ├── application.py
│   ├── tutor_profile.py
│   └── review.py
├── serializers/
│   ├── __init__.py
│   ├── job.py
│   ├── application.py
│   └── profile.py
├── viewsets/
│   ├── __init__.py
│   ├── job.py
│   ├── application.py
│   └── profile.py
├── urls.py
├── filters.py
├── permissions.py
├── tasks.py
├── utils/
│   ├── __init__.py
│   └── matching.py
├── migrations/
└── tests/
```

## 📧 Notifications Service

### `/services/notifications/`
```
notifications/
├── __init__.py
├── apps.py
├── models/
│   ├── __init__.py
│   ├── notification.py
│   └── template.py
├── serializers/
│   ├── __init__.py
│   └── notification.py
├── viewsets/
│   ├── __init__.py
│   └── notification.py
├── urls.py
├── tasks.py
├── utils/
│   ├── __init__.py
│   ├── email_sender.py
│   ├── sms_sender.py
│   └── push_notification.py
├── templates/          # Email Templates
│   ├── welcome.html
│   ├── booking_confirmation.html
│   └── payment_receipt.html
├── migrations/
└── tests/
```

## 🔧 Configuration Files

### `requirements.txt`
```
Django==4.2.7
djangorestframework==3.14.0
django-cors-headers==4.3.1
django-allauth==0.57.0
djangorestframework-simplejwt==5.3.0
django-channels==4.0.0
channels-redis==4.1.0
psycopg2-binary==2.9.9
celery==5.3.4
redis==5.0.1
stripe==7.8.0
openai==1.3.7
Pillow==10.1.0
python-decouple==3.8
django-filter==23.4
django-extensions==3.2.3
gunicorn==21.2.0
whitenoise==6.6.0
boto3==1.34.0
django-storages==1.14.2
```

### `requirements-dev.txt`
```
-r requirements.txt
pytest==7.4.3
pytest-django==4.7.0
pytest-cov==4.1.0
black==23.11.0
flake8==6.1.0
isort==5.12.0
factory-boy==3.3.0
faker==20.1.0
django-debug-toolbar==4.2.0
```

### `.env.example`
```
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/pentutor_db

# Django
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Redis
REDIS_URL=redis://localhost:6379/0

# Celery
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0

# Email
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Payment Gateways
STRIPE_PUBLIC_KEY=pk_test_xxxxx
STRIPE_SECRET_KEY=sk_test_xxxxx
JAZZCASH_MERCHANT_ID=your-merchant-id
PAYPAL_CLIENT_ID=your-paypal-client-id

# AI Services
OPENAI_API_KEY=sk-xxxxx

# AWS (for file storage)
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_STORAGE_BUCKET_NAME=pentutor-files
```

### `docker-compose.yml`
```yaml
version: '3.8'

services:
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: pentutor_db
      POSTGRES_USER: pentutor_user
      POSTGRES_PASSWORD: pentutor_password
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      - db
      - redis
    environment:
      - DEBUG=1

  celery:
    build: .
    command: celery -A core worker -l info
    volumes:
      - .:/app
    depends_on:
      - db
      - redis

volumes:
  postgres_data:
```

## 🚀 Team Work Distribution

### **Full Stack Developer** - Core Setup & Architecture
- `core/` service setup
- Database configuration
- Authentication service (`authentication/`)
- Deployment configuration

### **Backend Developer 1** - Real-time Features
- Meetings service (`meetings/`)
- WebSocket consumers
- WebRTC integration
- Real-time chat and whiteboard

### **Backend Developer 2** - Business Logic
- LMS service (`lms/`)
- Job Board service (`job_board/`)
- Payment service (`payments/`)

### **AI Developer** (if available)
- AI Services (`ai_services/`)
- OpenAI integration
- Matching algorithms

## 📋 Development Workflow

1. **Setup Phase**: Full Stack Dev creates core structure
2. **Feature Development**: Each dev works on assigned services
3. **Integration**: APIs testing between services
4. **Testing**: Unit tests for each service
5. **Deployment**: Production deployment

## 🔗 API Endpoints Structure

```
/api/v1/auth/          # Authentication
/api/v1/meetings/      # Meeting management
/api/v1/lms/          # Learning management
/api/v1/ai/           # AI services
/api/v1/payments/     # Payment processing
/api/v1/jobs/         # Job board
/api/v1/notifications/ # Notifications
```

## 📝 Git Branch Strategy

```
main              # Production ready code
develop           # Development integration
feature/auth      # Authentication features
feature/meetings  # Meeting features
feature/lms       # LMS features
feature/ai        # AI features
feature/payments  # Payment features
feature/jobs      # Job board features
```

Ye structure production-ready hai aur aapki team easily parallel work kar sakti hai. Har service independent hai aur easily scalable hai.