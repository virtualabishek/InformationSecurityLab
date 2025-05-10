# **Unit 5: Access Control**

_(5 Hours of Study)_

---

## **5.1 Access Control Principles**

### **Definition**

- **Access Control**: A security mechanism to regulate _who_ or _what_ can view, use, or modify resources in a system.

### **Core Principles**

1. **Least Privilege**: Users get only the minimum access needed.
   - Example: A receptionist doesn’t need admin rights.
2. **Need-to-Know**: Access granted only if necessary for a task.
3. **Separation of Duties (SoD)**: Split critical tasks among multiple users to prevent fraud.
   - Example: One employee creates payments; another approves them.
4. **Defense in Depth**: Layered security (e.g., firewalls + authentication).

---

## **5.2 Subjects, Objects, and Access Rights**

### **Key Terms**

- **Subject**: Active entity requesting access (e.g., user, process).
- **Object**: Passive resource being accessed (e.g., file, database).
- **Access Rights**: Permissions (read, write, execute, delete).

### **Example**

- **Subject**: Employee (user account).
- **Object**: Payroll spreadsheet.
- **Access Rights**: Read-only for employees; edit for HR managers.

---

## **5.3 Discretionary Access Control (DAC)**

### **Definition**

- Owners control access to their resources (flexible but risky).
- Uses **Access Control Lists (ACLs)** to define permissions.

### **Pros & Cons**

- ✅ Flexible, user-friendly.
- ❌ Vulnerable to insider threats (e.g., data leaks by owners).

### **Example**

- UNIX/Linux file permissions (`chmod 755`).

---

## **5.4 Role-Based Access Control (RBAC)**

### **Definition**

- Access based on **roles** (e.g., manager, intern) rather than individual users.

### **Key Components**

1. **Role Hierarchy**: Senior roles inherit junior permissions.
2. **Role Assignment**: Users assigned to roles (e.g., "Finance Team").

### **Example**

- Hospital system:
  - Doctors: Access patient records.
  - Nurses: Update vitals but can’t prescribe medication.

---

## **5.5 Attribute-Based Access Control (ABAC)**

### **Definition**

- Dynamic access based on **attributes** (user, resource, environment).
- Uses policies like _"IF user.department = HR AND time = 9 AM–5 PM, THEN allow access."_

### **Attributes**

- **Subject**: Job title, clearance level.
- **Object**: File sensitivity (e.g., "confidential").
- **Environment**: Time, location, device.

### **Example**

- Cloud storage (AWS S3) policies restricting access by IP address.

---

## **5.6 Identity, Credential, and Access Management (ICAM)**

### **Components**

1. **Identity Management**: Creating/user accounts (e.g., Azure AD).
2. **Credential Management**: Passwords, biometrics, MFA.
3. **Access Management**: Enforcing policies (RBAC, ABAC).

### **Standards**

- **Single Sign-On (SSO)**: One login for multiple systems (e.g., Google Workspace).
- **OAuth 2.0**: Authorization protocol (e.g., "Login with Facebook").

---

## **5.7 Trust Framework**

### **Definition**

- Rules and standards for establishing trust between systems/users (e.g., PKI).

### **Components**

1. **Public Key Infrastructure (PKI)**: Digital certificates for authentication.
   - Example: HTTPS websites use SSL/TLS certificates.
2. **Federation**: Trust between organizations (e.g., SAML for SSO).
3. **Certificate Authorities (CA)**: Trusted entities issuing certificates (e.g., Let’s Encrypt).

### **Use Case**

- E-commerce sites use PKI to secure transactions.

# **Key Points to Remember**

- **DAC**: Owner-controlled permissions (flexible but risky).
- **RBAC**: Role-based permissions (scalable for large organizations).
- **ABAC**: Dynamic access using attributes (e.g., time, location).
- **ICAM**: Combines identity, credentials, and access policies.
- **Trust Framework**: PKI and certificates enable secure transactions.

# **Mnemonics**

- **S.O.D.A**: Subjects, Objects, DAC, ABAC.
- **R.A.I.N**: Roles, Attributes, Identity, Need-to-know.

# **Sample Exam Questions**

1. Explain how RBAC reduces administrative workload in large organizations.
2. Compare DAC and ABAC with examples.
3. Why is PKI critical for a trust framework?

---
