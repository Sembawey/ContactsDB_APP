# 📇 Contacts DB Application

![Bash](https://img.shields.io/badge/Shell-Bash-4EAA25?logo=gnu-bash&logoColor=white)
![Docker](https://img.shields.io/badge/Container-Docker-2496ED?logo=docker&logoColor=white)
![Jenkins](https://img.shields.io/badge/CI-CD-Jenkins-D24939?logo=jenkins&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

A lightweight **Bash-based Contacts Database Application** that lets users **add, view, search, and delete contacts**.  
Fully **containerized using Docker** and **automated with Jenkins** for CI/CD integration.

---

## 📚 Table of Contents
1. [Features](#-features)
2. [Project Structure](#-project-structure)
3. [Prerequisites](#-prerequisites)
4. [Getting Started](#-getting-started)
5. [Application Usage](#-application-usage)
6. [Docker Configuration](#-docker-configuration)
7. [Jenkins CI/CD Pipeline](#-jenkins-cicd-pipeline)
8. [Data Persistence](#-data-persistence)
9. [Example Output](#-example-output)
10. [Technologies Used](#-technologies-used)
11. [Author](#-author)
12. [License](#-license)

---

## ✨ Features

- Add, view, search, and delete contacts  
- Contact fields:
  - First Name  
  - Last Name  
  - Email  
  - Mobile Number  
- Stores data in a simple text file (`database.txt`)
- Lightweight and fast (built on Alpine Linux)
- Fully containerized using Docker
- Integrated with Jenkins for automated CI/CD

---

## 🏗️ Project Structure

```
contacts-db/
│
├── contacts_DB.sh        # Main Bash application
├── Dockerfile            # Docker configuration
└── README.md             # Documentation
```

---

## ⚙️ Prerequisites

Ensure the following tools are installed:

- **Docker** — For containerized deployment  
- **Jenkins** — For CI/CD pipeline automation  
- **Git** — For source code version control  
- **Bash** — (Optional) to run locally without Docker

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/contacts-db.git
cd contacts-db
```

### 2. Build the Docker Image

```bash
docker build -t contacts_db_app .
```

### 3. Run the Application

```bash
docker run -it --name contacts_db_container contacts_db_app
```

The interactive contact management menu will appear.

---

## 🧠 Application Usage

### Main Menu
```
Welcome to the Main Menu
- press i to add new contact
- press v to view all contacts
- press s to search for record
- press e to delete all contacts
- press d to delete one contact
- press q to exit
```

### Available Options

| Option | Description |
|:--------|:-------------|
| **i** | Add new contact |
| **v** | View all contacts |
| **s** | Search for contact |
| **e** | Delete all contacts |
| **d** | Delete one contact |
| **q** | Exit application |

---

## 🐳 Docker Configuration

### Dockerfile

```dockerfile
FROM alpine:latest
RUN apk add --no-cache bash
RUN apk add vim
RUN touch /database.txt
COPY ./contacts_DB.sh /contacts_DB.sh
RUN chmod +x /contacts_DB.sh
CMD ["bash", "/contacts_DB.sh"]
```

### Explanation
- Uses a minimal **Alpine Linux** base image  
- Installs **Bash** and **Vim**
- Copies the script and makes it executable  
- Starts the script automatically when the container runs  

---

## 🔁 Jenkins CI/CD Pipeline

This project uses **two Jenkins Freestyle projects** for automation.

### 🧱 Step 1: `Step_1` — Build and Prepare Image

**Configuration:**

- **Source Code Management:** Git repository  
- **Trigger:** Poll SCM every 24 hours  
- **Execute Shell:**

```bash
docker cp myapp:/database.txt /var/lib/jenkins/workspace/database_$(date +%Y%m%d_%H%M%S).txt
cd /var/lib/jenkins/workspace/step_1
docker build -t contact_image:V${BUILD_NUMBER} .
docker stop $(docker ps -a | grep "contact_image" | awk '{print $1}')
docker rm -f $(docker ps -a | grep "contact_image" | awk '{print $1}')
```

- **Post-build Action:** Trigger `Step_2`

---

### 🚀 Step 2: `Step_2` — Deploy and Run Container

**Execute Shell:**

```bash
docker create --name myapp contact_image:V${BUILD_NUMBER}
docker start myapp
```

This step creates and runs the new version of the container.

---

## 💾 Data Persistence

All contact entries are saved inside the container at `/database.txt`.

To back up or persist data, Jenkins copies it automatically:

```bash
docker cp myapp:/database.txt /var/lib/jenkins/workspace/database_$(date +%Y%m%d_%H%M%S).txt
```

Each backup file is timestamped for version tracking.

---

## 🧾 Example Output

**Adding a Contact**
```
Enter your first name: John
Enter your last name: Doe
Enter your Email: john.doe@example.com
Enter your phone number: 1234567890
Contact Added to DB Successfully
```

**Viewing All Contacts**
```
== All Contacts ==
First Name: John Last Name: Doe Email: john.doe@example.com Phone Number: 1234567890
```

---

## 🧰 Technologies Used

| Technology | Description |
|-------------|--------------|
| **Bash** | Core application logic |
| **Docker** | Containerization |
| **Alpine Linux** | Lightweight base image |
| **Jenkins** | Continuous Integration / Deployment |
| **Git** | Source code version control |

---

## 👤 Author

**Ahmed El-Sembawey**  
📧 [ahmedelsembaweyofficial@gmail.com]            
🔗 [GitHub Profile]: https://github.com/Sembawey            
🔗 [LinkedIn Profile]: https://www.linkedin.com/in/ahmed-elsembawey/        
---