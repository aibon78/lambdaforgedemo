# 🚀 LambdaForgedemo

> Projeto desenvolvido com [Lambda Forge](https://github.com/lambda-forge/lambda-forge) para facilitar a criação e deploy de funções AWS Lambda em Python.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-orange)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📦 Sobre o Projeto

Este projeto implementa uma arquitetura serverless utilizando o framework **Lambda Forge**, focado em escalabilidade, modularidade e facilidade de manutenção.

As funções foram construídas seguindo os princípios de responsabilidade única, injeção de dependências e uso de camadas (layers) reutilizáveis.

---

## ⚙️ Funcionalidades

- ✅ Lambda Functions com arquitetura limpa
- ✅ Authorizers para segurança com headers personalizados
- ✅ Integração com [ex: SNS / SQS / S3]
- ✅ Lambda Layers personalizadas
- ✅ Live Development com hot reload e logs ao vivo
- ✅ CI/CD com múltiplos ambientes via AWS CodePipeline
- ✅ Documentação automática com Swagger/Redoc
- ✅ Diagrama de arquitetura gerado automaticamente

---

## 📁 Estrutura do Projeto

```bash
.
├── authorizers/
│   └── secret/
│       ├── config.py
│       ├── main.py
│       └── unit.py
├── functions/
│   └── hello_world/
│       ├── config.py
│       ├── integration.py
│       ├── main.py
│       └── unit.py
├── infra/
│   └── services/
│       ├── sns.py
│       └── aws_lambda.py
├── layers/
│   └── my_custom_layer/
│       └── my_custom_layer.py
└── config/
    └── environment.py
