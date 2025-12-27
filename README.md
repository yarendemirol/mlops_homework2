**MLOps CI/CD Pipeline – Homework 2**

Yaren Demirol - 210901031

This repository was prepared for Homework 2 – Implementing the MLOps CI/CD Pipeline assignment given within the scope of the SWE016 Machine Learning Operations course. The aim is to automate a manually run machine learning application using a CI/CD pipeline and to apply MLOps Level 1 & Level 2 principles. 📌 Project Summary
In this project:

*A machine learning application with feature engineering was developed.
*A CI pipeline was established to check code quality and correctness.
*The operation of a model service packaged with Docker was verified with a smoke test.
*It was shown that the pipeline stops (Stop the Line) in case of faulty code.

**CI/CD Pipeline
The pipeline is built using GitHub Actions and consists of the following stages:

    Build
    Unit Test (Feature Engineering)
    Lint (Flake8)
    Docker Build
    Smoke Test (Deployment Verification)
    
If an error occurs at any stage, the pipeline stops and deployment is prevented.

```
mlops_homework2
├── src/
│   ├── feature_engineering.py
│   ├── model.py
│   └── serve.py
├── tests/
│   ├── unit_test.py
│   ├── integration_test.py
│   └── smoke_test.py
├── data/
│   └── mall_customers.csv
├── .github/workflows/
│   └── main.yml
├── Dockerfile
├── requirements.txt
└── README.md
