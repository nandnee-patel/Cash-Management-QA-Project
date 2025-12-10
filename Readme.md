# Cash Management QA Project

This project simulates QA work for a Cash Management Web Portal, similar to real banking systems used for login, viewing account balances, and approving payments.  
It includes manual testing, acceptance criteria, SQL validation, and basic Selenium automation using Python.

---

## 🔍 Features Tested
- User Login  
- Dashboard Overview  
- View Account Balance  
- Approve Payment  
- View Payment History  

---

## 🧪 Testing Included

### **Manual Testing**
- User Stories  
- Acceptance Criteria  
- Test Cases  
- Regression Suite Design  
- Bug Reporting (Jira-style scenarios)  

### **Automation Testing**
- Selenium UI automation  
- PyTest test execution  
- Page Object Model (POM)  
- Automated Login Test  
- Light regression automation  

### **SQL Validation**
- Validate account balances  
- Validate payment status updates  
- Confirm data consistency in backend tables  

---

## 🛠 Tools Used
- Selenium WebDriver  
- Python  
- PyTest  
- SQL  
- Jira (for bug tracking workflow)  
- Confluence (documentation structure)  
- Mural (story mapping example)  
- GitHub (version control)  

---

# ▶ How to Run the Automation Tests

### **1. Install Dependencies**
Open a terminal and run:

pip install selenium pytest


---

### **2. Download ChromeDriver**

Check your Chrome browser version →  
Download matching ChromeDriver:  
https://chromedriver.chromium.org/downloads

Place the downloaded file here:



Automation/drivers/chromedriver.exe


---

### **3. Run Tests**

Navigate to the automation test folder:



cd Automation/src/


Run the test suite:



pytest -v


This will:

- Launch Chrome  
- Navigate to the practice login page  
- Enter credentials  
- Validate login success  
- Close the browser  

---

## 📁 Project Structure



Cash Management Project/
│
├── README.md
│
├── Manual_Testing/
│ ├── User_Stories.md
│ ├── Acceptance_Criteria.md
│ ├── Test_Cases.xlsx
│
├── Automation/
│ ├── src/
│ │ ├── pages/
│ │ │ └── LoginPage.py
│ │ ├── tests/
│ │ └── test_login.py
│ ├── drivers/
│ ├── reports/
│ ├── testdata/
│
├── SQL/
│ ├── payment_queries.sql
│ ├── balance_validation.sql
│
└── Documentation/
├── Regression_Suite_Design.md
├── Automation_Maintenance_Log.md


---
💡 Feedback Welcome

I am continuously learning and would greatly appreciate any suggestions to help me improve this project.

## 👤 Author  
**Nandnee Patel – QA Analyst**


This project is part of my QA learning portfolio and demonstrates real-world QA practices including manual test design, automation maintenance, SQL testing, and Agile documentation.
