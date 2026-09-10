# 🛡️ AWS IAM & Security Governance: Implementação do Princípio do Menor Privilégio e Segregação de Funções

![AWS IAM](https://img.shields.io/badge/AWS-IAM-orange?style=for-the-badge&logo=amazon-aws)
![AWS Security](https://img.shields.io/badge/Security-Defensive-red?style=for-the-badge)
![AWS CLI](https://img.shields.io/badge/CLI-Boto3-blue?style=for-the-badge)
![Region](https://img.shields.io/badge/Region-us--east--1-green?style=for-the-badge)

---

## 📌 Resumo Executivo
Este projeto simula a estruturação e governança de acessos de uma organização na AWS. O objetivo principal foi substituir o uso de permissões excessivas (*AdministratorAccess*) por uma arquitetura de controle de acesso baseada em funções (**RBAC - Role-Based Access Control**), aplicando o **Princípio do Menor Privilégio**, obrigatoriedade de **MFA (Multi-Factor Authentication)** e **Hardening de Acessos** via AWS Systems Manager (SSM).

---

## 📐 Arquitetura & Matriz de Governança de Acessos
 ```text
                              +---------------------------------------+
                              |   Politica Transversal (Force MFA)    |
                              +---------------------------------------+
                                                  |
          +---------------------------------------+---------------------------------------+
          |                                       |                                       |
          v                                       v                                       v
  
+-----------------------------+     +-----------------------------+     +-----------------------------+
|    Grp-Developers-Policy    |     |   Grp-SOC-Analysts-Policy   |     |     Grp-Auditors-Policy     |
+-----------------------------+     +-----------------------------+     +-----------------------------+
| • Gerenciamento EC2/S3      |     | • Leitura CloudTrail/Logs   |     | • Leitura AWS Config / Hub  |
| • Restrito a us-east-1      |     | • Leitura SSM Parameter     |     | • AssumeRole Cross-Account  |
| • Deny: Alteracoes em IAM   |     | • Deny: Exclusao de Logs    |     | • Leitura SecurityAudit     |
+-----------------------------+     +-----------------------------+     +-----------------------------+
```

### 🔐 Matriz de Perfis (RBAC)

| Grupo (IAM Group) | Escopo de Atuação | Permissões Concedidas | Controles de Segurança & Restrições |
| :--- | :--- | :--- | :--- |
| **`Grp-Developers`** | Gestão de aplicações e infra de Dev | `ec2:*` (PowerUser), `s3:*` | Restrito à região `us-east-1`; Deny em ações de IAM |
| **`Grp-SOC-Analysts`** | Resposta a incidentes e monitoramento | `cloudtrail:LookupEvents`, `logs:*`, `ssm:GetParameter` | Bloqueio explícito de exclusão/alteração de logs (`cloudtrail:DeleteTrail`) |
| **`Grp-Auditors`** | Governança, Risco e Conformidade (GRC) | `config:Get*`, `securityhub:Get*`, `sts:AssumeRole` | Acesso Cross-Account condicionado à presença de MFA ativo |
| **`Global / Todos`** | Autenticação padrão | Gerenciamento de credencial própria | **Deny Explicito** para qualquer chamada de API caso o MFA não esteja ativo |

---

## 🛠️ Tecnologias & Serviços Utilizados
- **AWS IAM:** Custome Managed Policies, Groups, RBAC e Condition Keys.
- **AWS STS (Security Token Service):** Concessão de acesso temporário e validação de identidade (`sts:AssumeRole`, `sts:get-caller-identity`).
- **AWS Systems Manager (SSM):** Session Manager para acesso SSH sem porta 22 aberta e Parameter Store (`SecureString`) para gestão de segredos.
- **AWS CloudTrail & CloudWatch:** Trilha de auditoria e monitoramento de falhas de autenticação (`AccessDenied`).
- **AWS CLI & Python (Boto3):** Automação de testes e consultas seguras via terminal.

---

## 📂 Estrutura do Repositório

```text
├── README.md                           <-- Documentação principal
├── policies/                            <-- Politicas JSON personalizadas
│   ├── Grp-Developers-Policy.json
│   ├── Grp-SOC-Analysts-Policy.json
│   ├── Grp-Auditors-Policy.json
│   └── ForceMFA-Policy.json
├── scripts/                            <-- Script Python (Boto3) para teste do SSM
│   └── get_secure_param.py
└── evidence/                           <-- Provas de validação e testes
    ├── access_denied_cloudtrail.png
    └── ssm_session_manager.png
