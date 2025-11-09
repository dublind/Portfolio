# Data Engineering Learning Path
**A Complete Roadmap to Becoming a Data Engineer**

*By Ignacio Salinas*
*Last Updated: November 2025*

---

## Table of Contents
1. [Introduction](#introduction)
2. [Current Skills Assessment](#current-skills-assessment)
3. [Phase 1: Strengthen Foundations](#phase-1-strengthen-foundations-2-3-months)
4. [Phase 2: Core Data Engineering](#phase-2-core-data-engineering-3-4-months)
5. [Phase 3: Big Data & Cloud](#phase-3-big-data--cloud-3-4-months)
6. [Phase 4: Advanced Topics](#phase-4-advanced-topics-2-3-months)
7. [Project-Based Milestones](#project-based-milestones)
8. [Learning Resources](#learning-resources)
9. [Key Skills Employers Want](#key-skills-employers-want)
10. [Weekly Study Schedule](#weekly-study-schedule)

---

## Introduction

Data Engineering is one of the fastest-growing fields in tech. Data Engineers build and maintain the infrastructure that enables data scientists and analysts to do their work. This roadmap will take you from foundational skills to job-ready expertise in approximately 10-12 months.

### What Does a Data Engineer Do?

- Build and maintain data pipelines (ETL/ELT)
- Design and manage data warehouses and data lakes
- Ensure data quality and reliability
- Optimize data storage and retrieval
- Work with big data technologies and cloud platforms
- Collaborate with data scientists, analysts, and stakeholders

### Estimated Timeline
- **Total Duration**: 10-12 months of consistent study
- **Time Commitment**: 15-20 hours per week
- **Intensity**: Mix of theory (40%) and hands-on practice (60%)

---

## Current Skills Assessment

### ✅ Skills You Already Have
- **Python**: Programming fundamentals
- **SQL**: Database querying
- **HTML/CSS/JavaScript**: Web development basics
- **Git/GitHub**: Version control

### 🎯 Skills to Acquire
- Advanced SQL and database design
- ETL/ELT pipeline development
- Workflow orchestration (Apache Airflow)
- Cloud platforms (AWS/GCP/Azure)
- Big data processing (Apache Spark)
- Containerization (Docker)
- Data modeling and warehousing

---

## Phase 1: Strengthen Foundations (2-3 months)

### 1.1 Advanced SQL & Databases

**What to Learn:**
- **Window Functions**: ROW_NUMBER(), RANK(), LEAD(), LAG()
- **Common Table Expressions (CTEs)**: Recursive and non-recursive
- **Query Optimization**: EXPLAIN plans, indexing strategies
- **Advanced Joins**: Self-joins, cross joins, lateral joins
- **Stored Procedures & Functions**: PL/pgSQL
- **Transactions & ACID**: Isolation levels, locking
- **Database Design**: Normalization (1NF to BCNF), denormalization

**Hands-On Practice:**
- Solve SQL problems on LeetCode, HackerRank, SQLZoo
- Work with a real PostgreSQL database
- Optimize slow queries
- Design schemas for real-world scenarios

**Resources:**
- PostgreSQL Documentation
- "SQL Performance Explained" by Markus Winand
- Mode Analytics SQL Tutorial
- PostgreSQL Exercises (pgexercises.com)

**Time Estimate**: 4-5 weeks

---

### 1.2 Python for Data Engineering

**What to Learn:**
- **Pandas & NumPy**: DataFrames, Series, data manipulation
- **Data Validation**: Pydantic, Great Expectations
- **Working with APIs**: requests, authentication, pagination
- **File Formats**: CSV, JSON, XML, Parquet, Avro, ORC
- **Error Handling**: try/except, logging
- **Testing**: pytest, unittest
- **Virtual Environments**: venv, conda
- **Package Management**: pip, requirements.txt

**Hands-On Practice:**
- Read data from various file formats
- Clean and transform messy datasets
- Consume REST APIs and process responses
- Write unit tests for data transformation functions
- Build a data validation pipeline

**Resources:**
- "Python for Data Analysis" by Wes McKinney
- Real Python tutorials
- Pandas Documentation
- Kaggle Python courses

**Time Estimate**: 3-4 weeks

---

### 1.3 Linux & Command Line

**What to Learn:**
- **Basic Commands**: ls, cd, mkdir, cp, mv, rm
- **File Manipulation**: grep, awk, sed, cut, sort, uniq
- **Process Management**: ps, top, kill
- **Permissions**: chmod, chown
- **SSH**: Connecting to remote servers
- **Cron Jobs**: Scheduling tasks
- **Shell Scripting**: Bash basics, variables, loops

**Hands-On Practice:**
- Set up a Linux VM or WSL
- Write bash scripts for data processing
- Schedule automated tasks with cron
- Process log files with command-line tools

**Resources:**
- Linux Journey (linuxjourney.com)
- "The Linux Command Line" by William Shotts
- OverTheWire Bandit (wargames)

**Time Estimate**: 2-3 weeks

---

### 1.4 Introduction to NoSQL

**What to Learn:**
- NoSQL vs SQL databases
- Document stores: MongoDB
- Key-value stores: Redis
- Column-family stores: Cassandra (overview)
- When to use NoSQL vs SQL

**Hands-On Practice:**
- Install and use MongoDB
- Perform CRUD operations
- Understand document schema design
- Compare with relational databases

**Time Estimate**: 2 weeks

---

## Phase 2: Core Data Engineering (3-4 months)

### 2.1 ETL/ELT Fundamentals

**What to Learn:**
- **ETL vs ELT**: When to use each approach
- **Data Extraction**: From APIs, databases, files, web scraping
- **Data Transformation**: Cleaning, aggregation, enrichment
- **Data Loading**: Bulk loading, incremental loading, upserts
- **Idempotency**: Ensuring pipeline reruns are safe
- **Error Handling**: Retries, dead letter queues

**Hands-On Practice:**
- Build Python ETL scripts
- Extract data from multiple sources
- Transform and clean real-world messy data
- Load data into PostgreSQL
- Handle failures gracefully

**Project Ideas:**
- COVID-19 data tracker pipeline
- Stock market data aggregator
- E-commerce sales data pipeline
- Weather data collector

**Time Estimate**: 4-5 weeks

---

### 2.2 Workflow Orchestration with Apache Airflow

**What to Learn:**
- **DAGs (Directed Acyclic Graphs)**: Defining workflows
- **Operators**: PythonOperator, BashOperator, PostgresOperator
- **Task Dependencies**: set_upstream, set_downstream, >>
- **Scheduling**: Cron expressions, intervals
- **XComs**: Passing data between tasks
- **Sensors**: Waiting for conditions
- **Hooks**: Connecting to external systems
- **Monitoring**: UI, logs, alerts

**Hands-On Practice:**
- Install Airflow locally with Docker
- Create your first DAG
- Schedule ETL pipelines
- Set up task dependencies
- Monitor and debug failed tasks
- Implement retries and SLAs

**Resources:**
- Apache Airflow Documentation
- "Data Pipelines with Apache Airflow" by Bas Harenslak
- Astronomer Academy (free courses)
- Marc Lamberti's Airflow courses

**Time Estimate**: 5-6 weeks

---

### 2.3 Data Modeling

**What to Learn:**
- **Dimensional Modeling**: Star schema, snowflake schema
- **Fact Tables**: Additive, semi-additive, non-additive measures
- **Dimension Tables**: Slowly Changing Dimensions (SCD Type 1, 2, 3)
- **Normalization vs Denormalization**: Trade-offs
- **Surrogate Keys**: When and why to use them
- **Data Vault**: Advanced modeling technique

**Hands-On Practice:**
- Design a star schema for a business scenario
- Implement SCD Type 2 dimensions
- Build a small data warehouse
- Write queries against dimensional models

**Resources:**
- "The Data Warehouse Toolkit" by Ralph Kimball
- Kimball Group website
- Data modeling tutorials on YouTube

**Time Estimate**: 3-4 weeks

---

### 2.4 Docker & Containerization

**What to Learn:**
- **Docker Basics**: Images, containers, volumes
- **Dockerfile**: Creating custom images
- **Docker Compose**: Multi-container applications
- **Networking**: Container communication
- **Volumes**: Persistent data storage
- **Best Practices**: Small images, layer caching

**Hands-On Practice:**
- Install Docker Desktop
- Run PostgreSQL in a container
- Containerize a Python ETL script
- Use Docker Compose for Airflow
- Build and push images to Docker Hub

**Resources:**
- Docker Documentation
- Docker for Beginners (YouTube)
- Play with Docker (labs.play-with-docker.com)

**Time Estimate**: 3-4 weeks

---

## Phase 3: Big Data & Cloud (3-4 months)

### 3.1 Data Warehousing

**What to Learn:**
- **Data Warehouse Concepts**: OLAP vs OLTP
- **dbt (data build tool)**: Transformations as code
- **Partitioning**: Date-based, range, list partitioning
- **Clustering**: Optimizing query performance
- **Materialized Views**: Pre-computed results
- **Modern Data Stack**: ELT approach

**Cloud Data Warehouses:**
- **Snowflake**: Multi-cluster architecture
- **Google BigQuery**: Serverless, columnar storage
- **Amazon Redshift**: MPP architecture

**Hands-On Practice:**
- Set up dbt with PostgreSQL
- Write dbt models and tests
- Implement incremental models
- Create documentation with dbt docs
- Try BigQuery or Snowflake free tier

**Resources:**
- dbt Documentation and Courses
- Snowflake University (free)
- Google Cloud Skills Boost (BigQuery)
- "The Data Warehouse Toolkit" by Kimball

**Time Estimate**: 4-5 weeks

---

### 3.2 Big Data Processing with Apache Spark

**What to Learn:**
- **Distributed Computing**: Concepts and architecture
- **PySpark**: Python API for Spark
- **RDDs**: Resilient Distributed Datasets
- **DataFrames & Datasets**: Structured APIs
- **Transformations**: map, filter, groupBy, join
- **Actions**: collect, count, save
- **Lazy Evaluation**: Execution plans
- **Performance Optimization**: Partitioning, caching, broadcast joins

**Hands-On Practice:**
- Install Spark locally or use Databricks Community Edition
- Process large CSV/JSON files
- Perform aggregations and joins
- Read/write Parquet files
- Optimize Spark jobs

**Resources:**
- Apache Spark Documentation
- Databricks Academy (free courses)
- "Learning Spark" by Jules Damji et al.
- Spark tutorials on DataCamp

**Time Estimate**: 5-6 weeks

---

### 3.3 Cloud Platforms (Choose ONE to Start)

#### Option A: Amazon Web Services (AWS)

**Core Services to Learn:**
- **S3**: Object storage for data lakes
- **RDS**: Managed relational databases
- **Redshift**: Data warehouse
- **Glue**: ETL service and data catalog
- **Lambda**: Serverless functions
- **Kinesis**: Real-time data streaming
- **IAM**: Security and permissions
- **CloudWatch**: Monitoring and logging

**Hands-On Practice:**
- Create S3 buckets and upload data
- Set up RDS PostgreSQL instance
- Build ETL job with AWS Glue
- Create Lambda function for data processing
- Configure IAM roles and policies

**Certification**: AWS Certified Data Analytics - Specialty

---

#### Option B: Google Cloud Platform (GCP)

**Core Services to Learn:**
- **Cloud Storage**: Object storage
- **BigQuery**: Serverless data warehouse
- **Cloud SQL**: Managed databases
- **Dataflow**: Stream and batch processing
- **Pub/Sub**: Messaging service
- **Cloud Functions**: Serverless
- **IAM**: Access control
- **Cloud Logging**: Monitoring

**Hands-On Practice:**
- Upload data to Cloud Storage
- Query data in BigQuery
- Create Dataflow pipeline
- Set up Pub/Sub topics

**Certification**: Google Professional Data Engineer

---

#### Option C: Microsoft Azure

**Core Services to Learn:**
- **Blob Storage**: Object storage
- **Azure SQL Database**: Managed SQL
- **Synapse Analytics**: Data warehouse
- **Data Factory**: ETL/ELT service
- **Databricks**: Spark platform
- **Event Hubs**: Streaming
- **Azure Functions**: Serverless

**Time Estimate for Cloud**: 6-8 weeks

---

### 3.4 Data Streaming Basics

**What to Learn:**
- **Stream Processing Concepts**: Real-time vs batch
- **Apache Kafka**: Distributed event streaming
- **Topics & Partitions**: Data organization
- **Producers & Consumers**: Publishing and reading
- **Message Queues**: RabbitMQ, AWS SQS
- **Use Cases**: Real-time analytics, event-driven architecture

**Hands-On Practice:**
- Install Kafka with Docker
- Create topics and partitions
- Write producers and consumers in Python
- Process streaming data
- Integrate with databases

**Resources:**
- Kafka Documentation
- Confluent Developer courses
- "Kafka: The Definitive Guide" by Neha Narkhede

**Time Estimate**: 4-5 weeks

---

## Phase 4: Advanced Topics (2-3 months)

### 4.1 Data Quality & Testing

**What to Learn:**
- **Data Validation**: Schema validation, business rules
- **Great Expectations**: Data quality framework
- **Unit Testing**: Testing transformations
- **Integration Testing**: End-to-end pipeline tests
- **Data Lineage**: Tracking data flow
- **Monitoring**: Alerts for data issues
- **SLAs**: Service level agreements

**Tools:**
- Great Expectations
- dbt tests
- pytest
- Apache Griffin

**Time Estimate**: 3-4 weeks

---

### 4.2 Infrastructure as Code

**What to Learn:**
- **Terraform**: Provisioning cloud infrastructure
- **Resources**: Defining infrastructure components
- **State Management**: Tracking infrastructure
- **Modules**: Reusable components
- **Version Control**: Git for infrastructure

**Hands-On Practice:**
- Write Terraform for AWS/GCP resources
- Provision databases and storage
- Manage infrastructure changes
- Destroy and recreate environments

**Time Estimate**: 3-4 weeks

---

### 4.3 CI/CD for Data Pipelines

**What to Learn:**
- **Continuous Integration**: Automated testing
- **Continuous Deployment**: Automated deployment
- **GitHub Actions / GitLab CI**: Pipeline automation
- **Testing Strategies**: Unit, integration, smoke tests
- **Environment Management**: Dev, staging, production

**Hands-On Practice:**
- Set up GitHub Actions workflows
- Automate testing and deployment
- Implement blue-green deployments

**Time Estimate**: 2-3 weeks

---

### 4.4 Performance & Optimization

**What to Learn:**
- **Query Optimization**: Indexes, query plans
- **Pipeline Optimization**: Parallelization, incremental processing
- **Cost Optimization**: Cloud cost management
- **Caching**: Redis, in-memory caching
- **Compression**: Parquet, Snappy, Gzip

**Time Estimate**: 2-3 weeks

---

## Project-Based Milestones

Build these projects progressively to demonstrate your skills:

### Month 1-2: Basic ETL Project
**Project**: Web Scraper with Database Storage
- Scrape data from a website (e.g., news, weather, stocks)
- Clean and transform the data
- Store in PostgreSQL
- Automate with cron or Python schedule

**Skills Demonstrated**: Python, SQL, data extraction, automation

---

### Month 3-4: Orchestrated Pipeline
**Project**: Multi-Source ETL with Airflow
- Extract from 3+ sources (API, CSV, database)
- Transform and validate data
- Load to PostgreSQL
- Orchestrate with Airflow
- Monitor and log

**Skills Demonstrated**: ETL, Airflow, data validation, orchestration

---

### Month 5-6: Data Warehouse
**Project**: Analytics Data Warehouse with dbt
- Build star schema with fact and dimension tables
- Implement SCD Type 2
- Use dbt for transformations
- Create analytics queries
- Generate dbt documentation

**Skills Demonstrated**: Data modeling, dbt, dimensional modeling, analytics

---

### Month 7-8: Big Data Processing
**Project**: Large-Scale Data Processing with Spark
- Process millions of records
- Perform complex aggregations
- Join multiple large datasets
- Optimize performance
- Save results in Parquet format

**Skills Demonstrated**: PySpark, distributed computing, performance optimization

---

### Month 9-10: Cloud & Streaming
**Project**: Real-Time Data Pipeline in Cloud
- Ingest real-time data (Kafka or cloud streaming service)
- Process with Spark Streaming or cloud service
- Store in cloud data warehouse
- Build dashboard for real-time metrics

**Skills Demonstrated**: Streaming, cloud platforms, real-time processing

---

### Month 11-12: Production-Ready System
**Project**: End-to-End Production Pipeline
- Full ETL/ELT pipeline
- Infrastructure as code (Terraform)
- CI/CD with automated testing
- Monitoring and alerting
- Data quality checks
- Documentation

**Skills Demonstrated**: Everything! Production-ready, professional-grade system

---

## Learning Resources

### Online Courses

**Comprehensive Platforms:**
- **DataCamp**: Data Engineer with Python track
- **Udemy**:
  - "The Complete Apache Airflow Course"
  - "Apache Spark with Python"
  - "AWS Certified Data Analytics"
- **Coursera**:
  - Google Cloud Data Engineering
  - IBM Data Engineering Professional Certificate
- **LinkedIn Learning**: Various data engineering courses

**Specialized Learning:**
- **Astronomer Academy**: Airflow (free)
- **Databricks Academy**: Spark (free)
- **Snowflake University**: Data warehousing (free)
- **Google Cloud Skills Boost**: GCP services (free tier)
- **AWS Skill Builder**: AWS services (free tier)

---

### Books

**Essential Reading:**
1. **"Fundamentals of Data Engineering"** by Joe Reis & Matt Housley
   - Modern best practices and concepts

2. **"Designing Data-Intensive Applications"** by Martin Kleppmann
   - Deep dive into distributed systems

3. **"The Data Warehouse Toolkit"** by Ralph Kimball
   - Dimensional modeling bible

4. **"Data Pipelines with Apache Airflow"** by Bas Harenslak & Julian de Ruiter
   - Comprehensive Airflow guide

5. **"Learning Spark"** by Jules Damji et al.
   - Spark fundamentals and advanced topics

**Advanced Reading:**
6. "SQL Performance Explained" by Markus Winand
7. "Streaming Systems" by Tyler Akidau et al.
8. "Python for Data Analysis" by Wes McKinney

---

### YouTube Channels & Creators

- **Seattle Data Guy**: Data engineering career advice and tutorials
- **Data Engineering Zoomcamp** (DataTalks.Club): Free comprehensive course
- **Karolina Sowinska**: Data engineering projects
- **Andreas Kretz**: DE Academy channel
- **TechWorld with Nana**: DevOps and cloud
- **freeCodeCamp**: Various data engineering courses

---

### Practice Platforms

**Coding Practice:**
- **LeetCode**: SQL and algorithm problems
- **HackerRank**: SQL, Python challenges
- **SQLZoo**: Interactive SQL tutorials
- **Mode Analytics**: SQL practice with real datasets
- **Kaggle**: Datasets and competitions

**Cloud Practice:**
- **AWS Free Tier**: 12 months free
- **GCP Free Tier**: $300 credit
- **Azure Free Tier**: $200 credit
- **Databricks Community Edition**: Free Spark environment

---

### Communities & Forums

- **r/dataengineering** (Reddit): Active community
- **Data Engineering Discord servers**
- **Stack Overflow**: Q&A
- **LinkedIn Groups**: Data Engineering professionals
- **Local Meetups**: Check Meetup.com for data engineering groups

---

### Blogs & Websites

- **DataEngineeringWeekly.com**: Newsletter
- **Locally Optimistic**: Data blog
- **The Data Engineering Podcast**
- **dbt Blog**: Modern data stack insights
- **AWS Big Data Blog**
- **Google Cloud Blog**

---

## Key Skills Employers Want

### Must-Have Skills (Core)

**Programming & Databases:**
- ✅ SQL (Advanced) - **CRITICAL**
- ✅ Python - **CRITICAL**
- Version Control (Git) - **CRITICAL**

**Data Engineering Tools:**
- Apache Airflow or similar orchestration - **CRITICAL**
- ETL/ELT experience - **CRITICAL**
- Docker & containerization - **HIGHLY DESIRED**

**Cloud Platforms:**
- AWS, GCP, or Azure (at least one) - **CRITICAL**
- Understanding of cloud data services - **CRITICAL**

---

### Nice-to-Have Skills (Bonus)

**Big Data:**
- Apache Spark/PySpark
- Hadoop ecosystem (basic understanding)
- Distributed computing concepts

**Streaming:**
- Apache Kafka
- Real-time processing
- Event-driven architecture

**Modern Data Stack:**
- dbt (data build tool)
- Snowflake/BigQuery/Redshift
- Fivetran/Airbyte (ELT tools)

**DevOps:**
- Terraform or CloudFormation
- CI/CD pipelines
- Kubernetes (basic understanding)

**Data Quality:**
- Great Expectations
- Data validation frameworks
- Testing practices

---

### Soft Skills (Often Overlooked!)

- **Communication**: Explain technical concepts to non-technical stakeholders
- **Problem-Solving**: Debug complex data issues
- **Collaboration**: Work with data scientists, analysts, engineers
- **Documentation**: Write clear docs for pipelines and systems
- **Business Acumen**: Understand business requirements

---

## Weekly Study Schedule

### Template Schedule (15-20 hours/week)

**Monday (2-3 hours):**
- 🎓 Theory & Concepts
- Watch tutorials or read documentation
- Take notes, understand fundamentals

**Tuesday (2-3 hours):**
- 🎓 Theory & Concepts (continued)
- Deep dive into specific topics
- Complete online course modules

**Wednesday (2-3 hours):**
- 💻 Hands-On Practice
- Code along with tutorials
- Practice exercises on platforms (LeetCode, DataCamp)

**Thursday (2-3 hours):**
- 💻 Hands-On Practice
- Build small proof-of-concept projects
- Experiment with new tools

**Friday (2-3 hours):**
- 💻 Hands-On Practice
- Debug and troubleshoot
- Review week's learning

**Saturday (3-4 hours):**
- 🚀 Portfolio Project Work
- Apply week's learning to main project
- Build, test, iterate

**Sunday (2-3 hours):**
- 🚀 Portfolio Project Work (continued)
- Document your code
- Write README, add to GitHub
- **Optional**: Review and plan next week

---

### Study Tips for Success

**1. Build in Public:**
- Share your learning journey on LinkedIn
- Post projects on GitHub
- Write blog posts about what you're learning

**2. Follow the 80/20 Rule:**
- 20% theory, 80% hands-on practice
- Learning by doing is most effective

**3. Don't Get Stuck in Tutorial Hell:**
- After learning a concept, build something without following a tutorial
- Struggle is where learning happens

**4. Join Communities:**
- Ask questions on Stack Overflow, Reddit
- Attend virtual meetups
- Network with other learners and professionals

**5. Track Your Progress:**
- Keep a learning journal
- Celebrate small wins
- Review and reflect regularly

**6. Focus on Fundamentals First:**
- Master SQL and Python before moving to advanced tools
- Strong foundations make everything else easier

**7. Don't Learn Everything:**
- You don't need to know every tool
- Focus on core skills, specialize later

---

## Career Roadmap

### Entry-Level Roles to Target

**Junior Data Engineer:**
- Build and maintain ETL pipelines
- Write SQL queries
- Basic Python scripting
- Support senior engineers

**Data Analyst (Transition Role):**
- Strong SQL skills
- Data analysis and reporting
- Can transition to DE role

**ETL Developer:**
- Focus on data integration
- Transform and load data
- Pipeline development

**BI Developer (Transition Role):**
- Data warehousing
- Dimensional modeling
- Can pivot to data engineering

---

### Typical Salary Ranges (US, 2025)

- **Junior Data Engineer**: $70,000 - $95,000
- **Mid-Level Data Engineer**: $95,000 - $130,000
- **Senior Data Engineer**: $130,000 - $180,000
- **Staff/Principal Data Engineer**: $180,000 - $250,000+

*Note: Varies significantly by location, company, and experience*

---

### How to Get Your First Job

**1. Build a Strong Portfolio:**
- 3-5 projects showcasing different skills
- Clean, well-documented code on GitHub
- README files explaining projects
- Live demos or screenshots

**2. Create a Data Engineering Resume:**
- Highlight relevant projects
- List technical skills clearly
- Quantify achievements (e.g., "Built pipeline processing 1M+ records daily")
- Include links to GitHub and portfolio

**3. Network:**
- Connect with data engineers on LinkedIn
- Attend meetups and conferences
- Engage with the community online

**4. Apply Strategically:**
- Target junior/entry-level roles
- Consider startups (more willing to take juniors)
- Look for "Associate" or "Junior" positions
- Consider internships or contract roles

**5. Prepare for Interviews:**
- **SQL**: Practice complex queries
- **Python**: Data structures, algorithms
- **System Design**: Design a data pipeline
- **Behavioral**: STAR method responses
- **Projects**: Be ready to deep-dive into your work

---

## Conclusion

Becoming a data engineer is a rewarding journey that requires dedication and consistent practice. With your existing Python and SQL skills, you already have a strong foundation. Follow this roadmap, build projects, and stay curious.

**Remember:**
- Learning never stops in data engineering
- Technologies evolve rapidly
- Fundamentals remain constant
- Hands-on practice is key
- Community support accelerates learning

**Your Next Steps:**
1. Save this learning path
2. Choose Phase 1 topic to start with
3. Set up your learning environment
4. Build your first project
5. Share your progress

**Good luck on your data engineering journey!**

---

## Additional Resources

### GitHub Repositories to Study

- **Awesome Data Engineering**: Curated list of resources
- **Data Engineering Cookbook**: Recipes for common tasks
- **DataTalks.Club**: Data Engineering Zoomcamp materials

### Podcasts

- **Data Engineering Podcast** by Tobias Macey
- **The Data Stack Show**
- **Analytics Engineering Podcast**

### Newsletters

- **Data Engineering Weekly**
- **Seattle Data Guy Newsletter**
- **dbt Newsletter**

---

**Document Version**: 1.0
**Created**: November 2025
**For**: Ignacio Salinas Portfolio
**Contact**: isalinasg06@gmail.com
**GitHub**: github.com/dublind
