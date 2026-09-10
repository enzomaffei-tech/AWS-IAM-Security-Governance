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
