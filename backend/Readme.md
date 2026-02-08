
# Install Test Dependencies for testing
```
pip install -r requirements-test.txt
```


# stage:1 - Dev Stage [in Dev Env]

### Step-1 - Run the Test cases

we run Unut Test in Dev Environment servers
### Run the Unit test Cases
```
pytest tests/unit/test_unit.py
```


#### Step:2 - Run Sonar Scan [sonarQube]

Without Unit Test Coverage
```
sonar-scanner \
  -Dsonar.projectKey=employee-backend \
  -Dsonar.sources=app \
  -Dsonar.host.url=http://sonar.mycompany.local:9000 \
  -Dsonar.login=SONAR_TOKEN

```

With Unit Test Coverage
```
sonar-scanner \
  -Dsonar.projectKey=employee-backend \
  -Dsonar.sources=. \
  -Dsonar.tests=tests \
  -Dsonar.test.inclusions=tests/unit/** \
  -Dsonar.python.coverage.reportPaths=coverage.xml

```
Generate the Test Coverage XML Report 
```
pytest tests/unit --cov=app --cov-report=xml
```

#### Step:3 - Create Release Artifact [Nexus]

Create release Artifact 
```
VERSION=1.0.3
tar -czf backend-${VERSION}.tar.gz app requirements.txt initdb.js
```

upload to Nexus
```
curl -u nexususer:nexuspass \
  --upload-file backend-1.0.3.tar.gz \
  http://nexus.mycompany.local:8081/repository/backend-releases/backend-1.0.3.tar.gz
```

# stage:2 - QA Stage [in QA Env]

#### Step-1 - Download Artifact from Nexus

```
cd /opt/backend/releases
curl -u nexususer:nexuspass -O \
  http://nexus.mycompany.local:8081/repository/backend-releases/backend-1.0.3.tar.gz
```

#### Step-2 - Deploy to QA 

```
cd /opt/backend
tar -xzf releases/backend-1.0.3.tar.gz -C app
source venv/bin/activate
pip install -r app/requirements.txt
sudo systemctl restart backend
```

#### Step 3 – Run Test Cases (QA Manual + Automated)

we run Integration Test in QA Environment servers
### Run the Integration test Cases
```
pytest tests/integration/test_integration.py
```

### Run the e2e test Cases
```
These are like catchpoint testcases ==> it will open the browser and click button and validate
That test cases not Included HERE
```

## NOTE
```
QA team also executes:

API tests (Postman)

Regression test cases

Performance sanity tests

✔ QA sign-off document
✔ Defects logged & fixed before promotion
```


# stage:3 - UAT Stage [in UAT Env]

HERE Business Validation from Client side or some Bussiness people will Validate the thing from UI or using Postman 
```
Business validates:

Add employee

Update employee

Delete employee

Salary validation

UAT sign-off
```

# stage:4 - PROD Stage

## NOTE ==> before Deploy we need these following Change Approvals then only we proceed with Prod Deploy
```
CAB approval

Maintenance window

Rollback plan documented
```

#### Step-1 - Deploy to Prod 
```
cd /opt/backend/releases
curl -u nexususer:nexuspass -O \
  http://nexus.mycompany.local:8081/repository/backend-releases/backend-1.0.3.tar.gz


// create the folder for the Current Version

cd /opt/backend
ln -sfn releases/backend-1.0.3 current

source venv/bin/activate
pip install -r current/requirements.txt

sudo systemctl restart backend
sudo systemctl status backend
```

#### Step-2 - Smoke Test in Production
```
curl http://prod-server:5000/health
curl http://prod-server:5000/api/employees
```
HERE we test the Deployment is Succes or Not working fine or Not

```
✔ Monitoring confirms healthy
✔ Business confirms application working
```

# If Fail ==> need to Rollback 

```
ln -sfn releases/backend-1.0.2 current
sudo systemctl restart backend
```
