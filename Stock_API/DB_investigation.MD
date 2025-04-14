# 📊 Database Comparison: MongoDB vs SQLite vs AWS DynamoDB

This document provides a detailed comparison between **MongoDB**, **SQLite**, and **AWS DynamoDB**.

---

## 🔍 1. General Overview

| Feature        | MongoDB                          | SQLite                           | AWS DynamoDB                     |
|----------------|----------------------------------|----------------------------------|----------------------------------|
| **Type**       | NoSQL (Document-based)           | Relational (SQL-based)           | NoSQL (Key-Value & Document)     |
| **Storage**    | Collection of JSON-like documents| File-based database (lightweight)| Managed distributed database     |
| **Hosting**    | Self-hosted or Atlas (Cloud)     | Embedded, local                  | Fully managed (Cloud - AWS)      |

---

## 🧠 2. Use Cases

| Use Case                           | MongoDB                        | SQLite               | DynamoDB                     |
|------------------------------------|--------------------------------|----------------------|------------------------------|
| Mobile apps                        | ✅ (via Realm)                 | ✅ (very common)     | ⚠️(not ideal due to latency) |
| Web apps                           | ✅                             | ⚠️ (light usage only)| ✅                           |
| IoT / Edge devices                 | ⚠️                             | ✅                   | ⚠️                           |
| Real-time analytics                | ✅ (with sharding, aggregation)| ❌                   | ✅                           |
| Serverless/Cloud-Native Apps       | ✅ (via Atlas)                 | ❌                   | ✅ (native to AWS Lambda)    |
| Local lightweight data storage     | ❌                             | ✅                   | ❌                           |
| High concurrency and scalability   | ✅                             | ❌                   | ✅ (excellent scaling)       |

---

## 🚀 3. Performance & Scalability

| Feature            | MongoDB                          | SQLite                           | DynamoDB                       |
|--------------------|----------------------------------|----------------------------------|--------------------------------|
| **Concurrency**    | High (supports replication)      | Low (single writer, many readers)| Very high                      |
| **Scalability**    | Horizontal (via sharding)        | Not scalable                     | Auto-scaling                   |
| **Read/Write**     | High (depends on setup)          | Fast for local read/write        | Extremely fast (low-latency)   |
| **Latency**        | Low to moderate                  | Extremely low (local file)       | Low (cloud dependent)          |

---

## 🛠️ 4. Development & Tooling

| Feature           | MongoDB                          | SQLite                          | DynamoDB                      |
|-------------------|----------------------------------|---------------------------------|-------------------------------|
| Query Language    | MongoDB Query Language (MQL)     | SQL                             | PartiQL / SDKs                |
| Indexing          | Yes (rich support)               | Basic indexes                   | Yes (secondary indexes)       |
| Transactions      | Yes (multi-document)             | Yes (ACID compliant)            | Limited (but supported)       |
| SDK / APIs        | Strong driver support            | Very basic (sqlite3)            | AWS SDK, REST, GraphQL        |
| UI Tools          | MongoDB Compass                  | DB Browser for SQLite           | AWS Console, NoSQL Workbench  |

---

## 💸 5. Cost Consideration

| Cost Factor       | MongoDB                          | SQLite                          | DynamoDB                           |
|-------------------|----------------------------------|---------------------------------|------------------------------------|
| Licensing         | Open-source (SSPL)               | Public Domain (Free)            | Pay-as-you-go (cloud costs)        |
| Hosting Cost      | Depends (self-host or Atlas)     | None (local file)               | Can be expensive at scale          |
| Scaling Cost      | Depends on infra                 | Not applicable                  | Auto, but costly at high throughput|

---

## 🔒 6. Security

| Feature          | MongoDB                         | SQLite                    | DynamoDB                       |
|------------------|---------------------------------|---------------------------|--------------------------------|
| Auth & Encryption| Role-based, SSL/TLS, field-level| Minimal (depends on app)  | IAM, KMS encryption, VPC       |
| Backup & Restore | Built-in (Atlas or Ops Manager) | Manual or app-managed     | On-demand & PITR backups       |

---

## ✅ 7. Pros and Cons Summary

### 🟢 MongoDB
**Pros**:
- Flexible document schema
- Rich query language
- Scalable horizontally
- Good for agile/iterative development

**Cons**:
- Higher memory usage
- Complex management unless using Atlas

---

### 🟢 SQLite
**Pros**:
- Lightweight and fast
- Zero setup (just a file)
- Perfect for prototyping, mobile, or embedded

**Cons**:
- Not suited for multi-user concurrency
- Not scalable
- Limited to local storage

---

### 🟢 AWS DynamoDB
**Pros**:
- Fully managed, scalable
- High throughput and low latency
- Serverless-friendly (with AWS ecosystem)

**Cons**:
- Cost can be unpredictable
- Limited query capabilities
- Tied to AWS ecosystem

---

## 🧭 8. When to Choose What?

| Scenario                               | Best Choice         |
|----------------------------------------|---------------------|
| Building a mobile/desktop app          | SQLite              |
| Scalable web app with flexible schema  | MongoDB             |
| Serverless app with AWS integration    | DynamoDB            |
| Rapid prototyping (no backend setup)   | SQLite              |
| Real-time analytics with auto scaling  | DynamoDB            |
| Agile product with evolving schema     | MongoDB             |

---
