# XAMPP Installation & Usage Guide for Linux

## ✅ Download and Install XAMPP

1. **Download XAMPP Installer**\
   Go to: [https://www.apachefriends.org/download.html](https://www.apachefriends.org/download.html)\
   Download the latest **Linux version (.run file)**

2. **Make the Installer Executable**

   ```bash
   cd ~/Downloads
   chmod +x xampp-linux-x64-8.2.12-0-installer.run
   ```

3. **Run the Installer**

   ```bash
   sudo ./xampp-linux-x64-8.2.12-0-installer.run
   ```

   Follow the GUI prompts to complete the installation.

---

## ✅ Start, Stop, and Restart XAMPP Services

- **Start XAMPP**

  ```bash
  sudo /opt/lampp/lampp start
  ```

- **Stop XAMPP**

  ```bash
  sudo /opt/lampp/lampp stop
  ```

- **Restart XAMPP**

  ```bash
  sudo /opt/lampp/lampp restart
  ```

---

## ✅ Access XAMPP Localhost

- Open your browser and visit:

  ```
  http://localhost
  ```

- You should see the **XAMPP Welcome Page**.

---

## ✅ Run XAMPP Control Panel (Console)

To open the XAMPP GUI Control Panel:

```bash
sudo /opt/lampp/manager-linux-x64.run
```

---

## ✅ Access phpMyAdmin & Create a Database

- Go to:

  ```
  http://localhost/phpmyadmin
  ```

- Click **Databases** tab.

- Enter your **Database Name** and click **Create**.

---
# ✅ Connecting Django CRUD Project to XAMPP MySQL Database

### 1️⃣ **Database Settings in `settings.py`**

Replace the default `DATABASES` settings with:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'root',
        'PASSWORD': '',  # Empty if you haven't set a password
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

### 2️⃣ **Install MySQL Client Library for Django**

In your virtual environment:

```bash
pip install mysqlclient
```

If you get errors, install system dependencies:

```bash
sudo apt-get install libmysqlclient-dev
```

---

### 3️⃣ **Make and Apply Migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 4️⃣ **Run Django Server and Test Connection**

```bash
python manage.py runserver
```

Check your terminal for successful connection and test CRUD operations.

---

### 5️⃣ **If You Get MariaDB Not Supported Error**

If you see this error:

```
django.db.utils.NotSupportedError: MariaDB 10.5 or later is required
```

Downgrade Django to **version 4.2 LTS**:

```bash
pip uninstall django
pip install django==4.2
```

---

## ✅ Summary of Key Commands

| Action                  | Command                                 |
| ----------------------- | --------------------------------------- |
| Start XAMPP             | `sudo /opt/lampp/lampp start`           |
| Stop XAMPP              | `sudo /opt/lampp/lampp stop`            |
| Restart XAMPP           | `sudo /opt/lampp/lampp restart`         |
| XAMPP Control Panel     | `sudo /opt/lampp/manager-linux-x64.run` |
| Install mysqlclient     | `pip install mysqlclient`               |
| Apply Django Migrations | `python manage.py migrate`              |
| Install Django 4.2      | `pip install django==4.2`               |

---

*You are now ready to connect your Django CRUD project to MySQL using XAMPP!*
