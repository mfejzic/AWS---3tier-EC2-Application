# Three Tier EC2 Infrastructure

 This project deploys a highly available, multi region AWS EC2 infrastructure using route 53, a load balancer, private instances and bastion hosts to securely deliver a resilient dynamic web application.
---

## 🌐 Live Project Links

- 🔴 EC2 Infrastructure Overview:  
https://www.fejzic37.com/links/ec2infra.html  


---

⚙️ What this project does  
- Provisions EC2 instances on AWS  
- Configures security groups and full VPC networking
- Deploys a lightweight application environment on EC2  
- Automates infrastructure using Terraform  
- Includes reusable infrastructure components  
- Bootstraps EC2 instances using user-data scripts  

---

🧱 Tech Stack  
- AWS (EC2, VPC, Subnets, Security Groups, Internet Gateway)  
- Terraform (Infrastructure as Code)  
- Linux (Ubuntu / Amazon Linux based EC2)  
- Python (Application layer)  
- HTML/CSS (Frontend UI)  
- Bash (Automation & setup scripts)  


☁️ Cloud & Infrastructure  
- AWS EC2 (Virtual Machine compute layer)  
- AWS VPC (Custom networking architecture)  
- AWS Subnets (Public/Private segmentation)  
- AWS Security Groups (Firewall rules)  
- Internet Gateway (External connectivity)  


💻 Application Layer  
- Python backend application  
- Simple web interface (HTML/CSS)  
- System-level bootstrapping via user-data  
- Environment setup via shell scripts  


🔐 Security  
- Security Group-based access control (SSH/HTTP)  
- Restricted inbound/outbound network rules  
- No hardcoded secrets (Terraform variable separation)  
- Isolated VPC architecture design  


📊 Observability  
- Basic system logging via EC2 instance logs  
- Infrastructure visibility through Terraform outputs  
- Optional CloudWatch integration-ready design  
