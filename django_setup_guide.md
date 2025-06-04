# PenTutor Backend - Complete Setup Guide

## 🚀 Step 1: Initial Project Setup

### 1.1 Create Virtual Environment
```bash
# Virtual environment create karein
python -m venv pentutor_env

# Activate karein (Windows)
pentutor_env\Scripts\activate

# Activate karein (Linux/Mac)
source pentutor_env/bin/activate
```

### 1.2 Install Django and Basic Requirements
```bash
pip install django djangorestframework python-decouple
```

### 1.3 Create Main Django Project
```bash
# Main project create karein
django-admin startproject pentutor_backend
cd pentutor_backend

# Services folder create karein
mkdir services
cd services
touch __init__.py
```

## 📁 Step 2: Create All Services (Apps)

### 2.1 Core Service
```bash
# Core service (ye main project settings handle karega)
cd services
django-admin startproject core .
```

### 2.2 Create All Other Services as Apps
```bash
# Root directory me jayein
cd ..

# Har service ke liye app create karein
python manage.py startapp authentication services/authentication
python manage.py startapp meetings services/meetings  
python manage.py startapp lms services/lms
python manage.py startapp ai_services services/ai_services
python manage.py startapp payments services/payments
python manage.py startapp job_board services/job_board
python manage.py startapp notifications services/notifications
```

## 🗂️ Step 3: Create Folder Structure Inside Each Service

### 3.1 Authentication Service Structure
```bash
cd services/authentication

# Folders create karein
mkdir models serializers viewsets tests utils
touch models/__init__.py serializers/__init__.py viewsets/__init__.py tests/__init__.py utils/__init__.py

# Files create karein
touch models/user.py models/profile.py models/role.py
touch serializers/auth.py serializers/user.py serializers/profile.py
touch viewsets/auth.py viewsets/user.py viewsets/profile.py
touch permissions.py managers.py tasks.py signals.py
touch tests/test_models.py tests/test_views.py tests/test_serializers.py
```

### 3.2 Meetings Service Structure
```bash
cd ../meetings

# Folders create karein
mkdir models serializers viewsets consumers utils tests
touch models/__init__.py serializers/__init__.py viewsets/__init__.py consumers/__init__.py utils/__init__.py tests/__init__.py

# Model files
touch models/meeting.py models/participant.py models/recording.py models/chat.py models/whiteboard.py models/attendance.py

# Serializer files
touch serializers/meeting.py serializers/chat.py serializers/whiteboard.py

# ViewSet files
touch viewsets/meeting.py viewsets/chat.py viewsets/whiteboard.py viewsets/recording.py

# Consumer files (WebSocket ke liye)
touch consumers/meeting.py consumers/chat.py consumers/whiteboard.py

# Utils files
touch utils/webrtc.py utils/recording.py

# Other files
touch routing.py permissions.py tasks.py signals.py
```

### 3.3 Similar Structure for Other Services
```bash
# LMS Service
cd ../lms
mkdir models serializers viewsets utils tests
touch models/__init__.py serializers/__init__.py viewsets/__init__.py utils/__init__.py tests/__init__.py
touch models/course.py models/lesson.py models/enrollment.py models/progress.py
touch serializers/course.py serializers/enrollment.py serializers/progress.py
touch viewsets/course.py viewsets/enrollment.py viewsets/dashboard.py
touch permissions.py filters.py tasks.py utils/progress_calculator.py

# AI Services
cd ../ai_services
mkdir models serializers viewsets consumers utils tests
touch models/__init__.py serializers/__init__.py viewsets/__init__.py consumers/__init__.py utils/__init__.py tests/__init__.py
touch models/matching.py models/chatbot.py
touch serializers/matching.py serializers/chatbot.py
touch viewsets/matching.py viewsets/chatbot.py
touch consumers/chatbot.py routing.py tasks.py
touch utils/openai_client.py utils/matching_algorithm.py utils/contact_blocker.py

# Payments Service
cd ../payments
mkdir models serializers viewsets webhooks utils tests
touch models/__init__.py serializers/__init__.py viewsets/__init__.py webhooks/__init__.py utils/__init__.py tests/__init__.py
touch models/payment.py models/invoice.py models/subscription.py models/transaction.py
touch serializers/payment.py serializers/invoice.py
touch viewsets/payment.py viewsets/webhook.py viewsets/invoice.py
touch webhooks/stripe.py webhooks/jazzcash.py webhooks/paypal.py
touch utils/stripe_client.py utils/jazzcash_client.py utils/paypal_client.py
touch tasks.py

# Job Board Service
cd ../job_board
mkdir models serializers viewsets utils tests
touch models/__init__.py serializers/__init__.py viewsets/__init__.py utils/__init__.py tests/__init__.py
touch models/job.py models/application.py models/tutor_profile.py models/review.py
touch serializers/job.py serializers/application.py serializers/profile.py
touch viewsets/job.py viewsets/application.py viewsets/profile.py
touch filters.py permissions.py tasks.py utils/matching.py

# Notifications Service
cd ../notifications
mkdir models serializers viewsets templates utils tests
touch models/__init__.py serializers/__init__.py viewsets/__init__.py utils/__init__.py tests/__init__.py
touch models/notification.py models/template.py
touch serializers/notification.py
touch viewsets/notification.py
touch tasks.py utils/email_sender.py utils/sms_sender.py utils/push_notification.py
touch templates/welcome.html templates/booking_confirmation.html templates/payment_receipt.html
```

## ⚙️ Step 4: Create Configuration Files

### 4.1 Core Settings Structure
```bash
# Core service me settings folder banayein
cd services/core
mkdir settings
touch settings/__init__.py settings/base.py settings/development.py settings/production.py settings/testing.py

# Middleware aur utils folders
mkdir middleware utils
touch middleware/__init__.py middleware/cors.py middleware/auth.py middleware/logging.py
touch utils/__init__.py utils/permissions.py utils/validators.py utils/helpers.py utils/exceptions.py

# Celery configuration
touch celery_app.py
```

### 4.2 Root Directory Files
```bash
# Root directory me wapas jayein
cd ../../..

# Configuration files create karein
touch .env.example .env.local .env.production
touch .gitignore README.md pytest.ini setup.cfg
touch requirements.txt requirements-dev.txt
touch docker-compose.yml docker-compose.prod.yml
```

### 4.3 Scripts Folder
```bash
mkdir scripts
touch scripts/deploy.sh scripts/backup_db.sh scripts/setup_env.sh

# Scripts ko executable banayein (Linux/Mac)
chmod +x scripts/*.sh
```

### 4.4 Documentation Folder
```bash
mkdir docs
touch docs/API_DOCUMENTATION.md docs/DEPLOYMENT.md docs/CONTRIBUTING.md
```

## 📝 Step 5: File Contents

### 5.1 `.env.example` File
```bash
cat > .env.example << 'EOF'
# Database Configuration
DATABASE_URL=postgresql://user:password@localhost:5432/pentutor_db
DATABASE_NAME=pentutor_db
DATABASE_USER=pentutor_user
DATABASE_PASSWORD=pentutor_password
DATABASE_HOST=localhost
DATABASE_PORT=5432

# Django Settings
SECRET_KEY=your-super-secret-key-here-change-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0

# Redis Configuration
REDIS_URL=redis://localhost:6379/0

# Celery Configuration
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0

# Email Configuration
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Payment Gateway Keys
STRIPE_PUBLIC_KEY=pk_test_your_stripe_public_key
STRIPE_SECRET_KEY=sk_test_your_stripe_secret_key
STRIPE_WEBHOOK_SECRET=whsec_your_webhook_secret

JAZZCASH_MERCHANT_ID=your_jazzcash_merchant_id
JAZZCASH_PASSWORD=your_jazzcash_password
JAZZCASH_SALT=your_jazzcash_salt

PAYPAL_CLIENT_ID=your_paypal_client_id
PAYPAL_CLIENT_SECRET=your_paypal_client_secret

# AI Services
OPENAI_API_KEY=sk-your-openai-api-key

# AWS Configuration (for file storage)
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_STORAGE_BUCKET_NAME=pentutor-files
AWS_S3_REGION_NAME=us-east-1

# Social Auth (Optional)
GOOGLE_OAUTH2_KEY=your_google_client_id
GOOGLE_OAUTH2_SECRET=your_google_client_secret

# Security
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
EOF
```

### 5.2 `.env.local` File (Development)
```bash
cp .env.example .env.local
# Isme local development values add karein
```

### 5.3 `.env.production` File (Production)
```bash
cp .env.example .env.production
# Production me DEBUG=False aur real credentials
```

### 5.4 `requirements.txt`
```bash
cat > requirements.txt << 'EOF'
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
django-import-export==3.3.1
djangorestframework-csv==2.1.1
python-dateutil==2.8.2
pytz==2023.3
EOF
```

### 5.5 `requirements-dev.txt`
```bash
cat > requirements-dev.txt << 'EOF'
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
coverage==7.3.2
pre-commit==3.5.0
EOF
```

### 5.6 `pytest.ini` (Testing Configuration)
```bash
cat > pytest.ini << 'EOF'
[tool:pytest]
DJANGO_SETTINGS_MODULE = services.core.settings.testing
python_files = tests.py test_*.py *_tests.py
addopts = --verbose --tb=short --cov=. --cov-report=html --cov-report=term
testpaths = services
EOF
```

### 5.7 `setup.cfg` (Code Quality Configuration)
```bash
cat > setup.cfg << 'EOF'
[flake8]
max-line-length = 88
exclude = 
    migrations,
    __pycache__,
    manage.py,
    settings.py,
    env,
    .env,
    venv,
    .venv

[isort]
profile = black
multi_line_output = 3
line_length = 88
include_trailing_comma = True
force_grid_wrap = 0
use_parentheses = True

[coverage:run]
source = .
omit = 
    manage.py,
    */migrations/*,
    */venv/*,
    */env/*,
    */tests/*,
    */settings/*,
    */__pycache__/*
EOF
```

### 5.8 `docker-compose.yml` (Development)
```bash
cat > docker-compose.yml << 'EOF'
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
    networks:
      - pentutor_network

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    networks:
      - pentutor_network

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
    env_file:
      - .env.local
    networks:
      - pentutor_network

  celery:
    build: .
    command: celery -A services.core worker -l info
    volumes:
      - .:/app
    depends_on:
      - db
      - redis
    env_file:
      - .env.local
    networks:
      - pentutor_network

  celery-beat:
    build: .
    command: celery -A services.core beat -l info
    volumes:
      - .:/app
    depends_on:
      - db
      - redis
    env_file:
      - .env.local
    networks:
      - pentutor_network

volumes:
  postgres_data:

networks:
  pentutor_network:
    driver: bridge
EOF
```

### 5.9 `Dockerfile`
```bash
cat > Dockerfile << 'EOF'
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "services.core.wsgi:application"]
EOF
```

## 🔧 Step 6: Scripts Content

### 6.1 `scripts/setup_env.sh`
```bash
cat > scripts/setup_env.sh << 'EOF'
#!/bin/bash

echo "🚀 Setting up PenTutor Backend Environment..."

# Create virtual environment
python -m venv pentutor_env
source pentutor_env/bin/activate

# Install requirements
pip install -r requirements-dev.txt

# Copy environment file
if [ ! -f .env.local ]; then
    cp .env.example .env.local
    echo "📝 .env.local file created. Please update with your credentials."
fi

# Create database
python manage.py makemigrations
python manage.py migrate

# Create superuser
echo "Creating superuser..."
python manage.py createsuperuser

echo "✅ Setup complete! Run 'python manage.py runserver' to start development server."
EOF
```

### 6.2 `scripts/deploy.sh`
```bash
cat > scripts/deploy.sh << 'EOF'
#!/bin/bash

echo "🚀 Deploying PenTutor Backend..."

# Pull latest code
git pull origin main

# Activate virtual environment
source pentutor_env/bin/activate

# Install/Update requirements
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Restart services (adjust according to your deployment)
sudo systemctl restart gunicorn
sudo systemctl restart nginx
sudo systemctl restart celery

echo "✅ Deployment complete!"
EOF
```

### 6.3 `scripts/backup_db.sh`
```bash
cat > scripts/backup_db.sh << 'EOF'
#!/bin/bash

# Database backup script
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="backups"
BACKUP_FILE="pentutor_backup_$DATE.sql"

# Create backup directory if it doesn't exist
mkdir -p $BACKUP_DIR

# Create database backup
pg_dump pentutor_db > $BACKUP_DIR/$BACKUP_FILE

echo "✅ Database backup created: $BACKUP_DIR/$BACKUP_FILE"
EOF
```

## 📋 Step 7: .gitignore File
```bash
cat > .gitignore << 'EOF'
# Django
*.pyc
__pycache__/
*.pyo
*.pyd
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Django specific
db.sqlite3
media/
staticfiles/
static/

# Environment variables
.env
.env.local
.env.production
.env.staging

# Virtual environment
venv/
env/
pentutor_env/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Coverage
htmlcov/
.coverage
.coverage.*

# Testing
.pytest_cache/
.tox/

# Celery
celerybeat-schedule

# Docker
.dockerignore

# Backup files
backups/
*.sql
EOF
```

## 🎯 Files Ka Purpose:

### Environment Files:
- **`.env.example`**: Template file with all required environment variables
- **`.env.local`**: Development environment variables  
- **`.env.production`**: Production environment variables

### Configuration Files:
- **`pytest.ini`**: Testing framework configuration
- **`setup.cfg`**: Code quality tools (flake8, isort) configuration
- **`docker-compose.yml`**: Development containers setup
- **`requirements.txt`**: Production dependencies
- **`requirements-dev.txt`**: Development dependencies

### Scripts:
- **`setup_env.sh`**: Initial project setup automation
- **`deploy.sh`**: Production deployment automation
- **`backup_db.sh`**: Database backup automation

## ✅ Final Steps:

```bash
# Install all requirements
pip install -r requirements-dev.txt

# Run initial setup
chmod +x scripts/setup_env.sh
./scripts/setup_env.sh

# Start development server
python manage.py runserver
```

Is tarah se aapka complete microservices structure ready ho jayega! 🚀