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

## ✅ Summary of Key Commands

| Action              | Command                                 |
| ------------------- | --------------------------------------- |
| Start XAMPP         | `sudo /opt/lampp/lampp start`           |
| Stop XAMPP          | `sudo /opt/lampp/lampp stop`            |
| Restart XAMPP       | `sudo /opt/lampp/lampp restart`         |
| XAMPP Control Panel | `sudo /opt/lampp/manager-linux-x64.run` |

---

*You are now ready to connect your Django project to MySQL using XAMPP!*

