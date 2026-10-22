# CI/CD Pipeline with GitHub Actions & Docker

## 📌 Project Overview

This project implements a Continuous Integration and Continuous Deployment (CI/CD) pipeline using GitHub Actions and Docker. The pipeline automates the process of testing the application, building a Docker image, and pushing the image to Docker Hub.

The Docker image is then pulled from Docker Hub and executed as a container on an AWS EC2 virtual machine.

The objective is to simplify application deployment by automating the build and image publishing process and using a cloud-based virtual machine to run the containerized application.

## 🎯 Objectives

- Build a Docker image for the application.
- Automate application testing using GitHub Actions.
- Build the Docker image automatically through a CI/CD workflow.
- Push the Docker image to Docker Hub.
- Pull the published image onto an AWS EC2 instance.
- Run the Docker container on the EC2 instance.
- Access and verify the deployed application.

## 🛠️ Technologies Used

- **Git & GitHub** – Source code management.
- **GitHub Actions** – CI/CD workflow automation.
- **Docker** – Application containerization.
- **Docker Hub** – Docker image registry.
- **AWS EC2** – Virtual machine for application deployment.
- **Linux** – Operating system for the EC2 instance.

## 🏗️ Architecture

```text
Developer
   |
   v
Push Code to GitHub
   |
   v
GitHub Actions Workflow
   |
   +----------------------+
   |                      |
   v                      v
Run Application Tests   Build Docker Image
                          |
                          v
                    Push Image to Docker Hub
                          |
                          v
                    Docker Hub Registry
                          |
                          v
                   AWS EC2 Instance
                          |
                          v
                    Pull Docker Image
                          |
                          v
                    Run Docker Container
                          |
                          v
                  Access Deployed Application
```

## ⚙️ Project Implementation

### 1. Application Setup

Created the application source code and prepared the project structure for Docker containerization.

### 2. Docker Configuration

Created a `Dockerfile` to define the application environment, dependencies, and startup command.

Docker was used to package the application and its dependencies into a portable image.

### 3. GitHub Repository Setup

Created a GitHub repository and pushed the application source code, Dockerfile, and CI/CD workflow configuration.

### 4. GitHub Actions CI/CD Pipeline

Configured GitHub Actions to automate the build and publishing process.

The workflow performs the following operations:

- Checks out the source code.
- Runs the configured application tests.
- Builds the Docker image.
- Authenticates with Docker Hub using GitHub Secrets.
- Pushes the Docker image to Docker Hub.

The workflow executes automatically when the configured GitHub event occurs, such as a push to the main branch.

### 5. Docker Hub Image Publishing

Published the successfully built Docker image to Docker Hub.

Docker Hub serves as the image registry from which the AWS EC2 instance retrieves the application image.

### 6. AWS EC2 Instance Setup

Launched an AWS EC2 virtual machine and configured the Linux environment for running Docker containers.

Installed and configured Docker on the EC2 instance.

### 7. Pull Docker Image on AWS EC2

Connected to the EC2 instance and pulled the published Docker image from Docker Hub.

```bash
docker pull krrg14/dasara-web-app:205c74441ec41b29a9f6fc6bb6562a77e24f95f3
```

Replace the placeholders with the actual Docker Hub username, image name, and tag.

### 8. Run the Docker Container

Started the application container on the EC2 instance.

```bash
docker run -d --name myapp -p 5000:5000 krrg14/dasara-web-app:205c74441ec41b29a9f6fc6bb6562a77e24f95f3
```

Replace `5000` with the port on which the application listens inside the container.

### 9. Verify the Deployment

Verified that the Docker image was available and the application container was running.

```bash
docker images
docker ps
docker logs myapp
```

Accessed the application using the EC2 instance's public IPv4 address and the appropriate port.

For example:

```text
Example URL: http://15.252.72.236:5000
```

**Note:** Ensure the EC2 security group allows inbound traffic on the application port. Restrict access where appropriate instead of exposing unnecessary ports publicly.

## 🔄 CI/CD Workflow

The implemented workflow follows these stages:

1. **Code:** Application code is maintained in GitHub.
2. **Continuous Integration:** GitHub Actions checks out the code and runs the configured tests.
3. **Build:** Docker builds an image from the Dockerfile.
4. **Publish:** The image is pushed to Docker Hub.
5. **Deployment:** The image is pulled manually onto the AWS EC2 instance.
6. **Execution:** Docker runs the application as a container.
7. **Verification:** Container status, logs, and application accessibility are checked.

**Deployment approach:** GitHub Actions automates testing, image building, and publishing. Pulling the image and starting the container on EC2 are performed manually.

## 📂 Project Structure

```text
.
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── Dockerfile
├── application source files
└── README.md
```

The exact files depend on the application.

---

# 📸 Project Demonstration

## GitHub repo with Workflows
```
https://github.com/krrg14/CI-CD-pipeline-with-Github-Action-Docker
```
## Docker image Link
```
https://hub.docker.com/r/krrg14/dasara-web-app
```
## CI\CD Workflows Results

<img width="1861" height="980" alt="Screenshot 2026-10-22 113016" src="https://github.com/user-attachments/assets/743a6c3b-9206-42bb-adae-7d5dfd46114a" />

## Snapshot of Deployed App

<img width="1850" height="981" alt="Screenshot 2026-10-22 114550" src="https://github.com/user-attachments/assets/3a2097d8-8460-46b9-a526-04a253aecce8" />

---

## ✅ Key Outcomes

- Containerized an application using Docker.
- Configured a CI/CD workflow using GitHub Actions.
- Automated application testing, Docker image building, and image publishing.
- Used Docker Hub as a centralized image registry.
- Deployed a Docker container on an AWS EC2 Linux virtual machine.
- Verified deployment using Docker commands, logs, and browser access.

## 👨‍💻 Skills Demonstrated

- CI/CD pipeline fundamentals.
- Git and GitHub workflows.
- GitHub Actions automation.
- Docker image creation and container management.
- Docker Hub image publishing.
- AWS EC2 provisioning and Linux administration.
- Application deployment and troubleshooting.

## 📌 Conclusion

This project demonstrates a practical CI/CD workflow that connects source code management, automated testing, Docker image creation, image publishing, and cloud-based container deployment.

GitHub Actions and Docker Hub automate the build and publishing stages, while AWS EC2 provides the environment for running and verifying the containerized application.99
