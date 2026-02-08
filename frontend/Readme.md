#### Install Test Dependencies for testing
```
npm install --save-dev \
@testing-library/react \
@testing-library/jest-dom \
@testing-library/user-event \
jest-environment-jsdom
```


# stage:1 - Dev Stage [in Dev Env]

### Step-1 - Run the Test cases


we Run the Unit test Cases in dev environment Servers
```
npm run test:unit
```

Unit test Coverage only 
```
npm run test:unit -- --coverage
```


#### Step:2 - Run Sonar Scan [sonarQube]
```
sonar-scanner \
  -Dsonar.projectKey=employee-frontend \
  -Dsonar.sources=src \
  -Dsonar.tests=src \
  -Dsonar.test.inclusions=**/*.unit.test.js \
  -Dsonar.javascript.lcov.reportPaths=coverage/lcov.info

```

#### Step:3 - Create Release Artifact [Nexus]

Build the Artifact
```
npm run build
```

Create release Artifact 
```
zip -r frontend-1.0.0.zip build/
```

upload to Nexus
```
curl -u nexususer:nexuspass \
  --upload-file frontend-1.0.0.zip \
  http://nexus.mycompany.local:8081/repository/frontend-releases/frontend-1.0.0.zip
```

# stage:2 - QA Stage [in QA Env]

#### Step-1 - Download Artifact from Nexus

Downlod the Artifact from Repo
```
cd /opt/frontend/releases
curl -u nexususer:nexuspass -O \
  http://nexus.mycompany.local:8081/repository/frontend-releases/frontend-1.0.0.zip
```


#### Step-2 - Deploy to QA 

Unzip the Repo
```
unzip frontend-1.0.0.zip
```

Switch Release
```
ln -sfn /opt/apps/frontend/releases/build /opt/apps/frontend/current

```

Reload Nginx
```
systemctl reload nginx
```

#### Step 3 – Run Test Cases (QA Manual + Automated)

we Run the Integration test Cases in QA environment Servers
```
npm run test:integration
```

Integration test Coverage only 
```
npm run test:integration -- --coverage
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

#### Step-1 - Download Artifact from Nexus

Downlod the Artifact from Repo
```
cd /opt/frontend/releases
curl -u nexususer:nexuspass -O \
  http://nexus.mycompany.local:8081/repository/frontend-releases/frontend-1.0.0.zip
```


#### Step-2 - Deploy to Prod 

Unzip the Repo
```
unzip frontend-1.0.0.zip
```

Switch Release
```
ln -sfn /opt/apps/frontend/releases/build /opt/apps/frontend/current

```

Reload Nginx
```
systemctl reload nginx
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
ln -sfn releases/frontend-1.0.0 current
sudo systemctl restart backend
```
