## This is privet project of address booking application

### Setup address booking the application
(make sure you dont have conflicts on port 1337 and 5434 running on your local machine or local docker image)

Step 1. Fetch source code from github

Step 2. Build docker image and start `docker-compose up --build` <br />
#### You can check the code coverage in the console log, which can be further integrated into the CI pipeline <br />

----------- coverage: platform linux, python 3.6.9-final-0 ----------- <br />
australia-addressbook-api       | Name                                    Stmts   Miss  Cover <br />
australia-addressbook-api       | ----------------------------------------------------------- <br />
australia-addressbook-api       | apps/__init__.py                            0      0   100% <br />
australia-addressbook-api       | apps/common/__init__.py                     1      0   100% <br />
australia-addressbook-api       | apps/common/helpers.py                      8      0   100% <br />
australia-addressbook-api       | apps/models/__init__.py                     1      0   100% <br />
australia-addressbook-api       | apps/models/addressmodel.py                12      0   100% <br />
australia-addressbook-api       | apps/serializers/__init__.py                1      0   100% <br />
australia-addressbook-api       | apps/serializers/addressserializer.py      23      0   100% <br />
australia-addressbook-api       | apps/views/__init__.py                      5      0   100% <br />
australia-addressbook-api       | apps/views/addressview.py                  28      0   100% <br />
australia-addressbook-api       | apps/views/main.py                         12      0   100% <br />
australia-addressbook-api       | ----------------------------------------------------------- <br />
australia-addressbook-api       | TOTAL                                      91      0   100% <br />

#### You can check the locust load test result of get and post address endpoints (default is 30 seconds, after that locust container will be killed, you can rerun load test by enter `docker-compose restart australia-addressbook-locust`)<br />
#### reference https://docs.locust.io/en/stable/quickstart.html
australia-addressbook-locust    |  Name                  # reqs      # fails     Avg     Min     Max  |  Median   reqs <br />
---------------------------------------------------------------------------------------------------------------------- <br />
australia-addressbook-locust    |  GET /api/v1/address/  284     0(0.00%)    1479      42    9860  |     570  13.30 <br />
australia-addressbook-locust    |  POST /api/v1/address/ 13     0(0.00%)     684      18    3088  |     220   0.50 <br />
australia-addressbook-locust    | ---------------------------------------------------------------------------------------- <br />
australia-addressbook-locust    |  Aggregated            297     0(0.00%)                                     13.80 <br />

Step 3. Check couple of links:<br />
`localhost:1337/api/v1` (check success of api root page)<br />
`localhost:1337/api/v1/healthz` (check success of healthz page for k8 livness and readiness)<br />
`localhost:1337/api/v1/docz` (check swagger for the address booking api)<br />

Step 4. Use `localhost:1337/api/v1/docz` to run through get/post/delete request follow the swagger instructions<br />

At moment this api does not have token authorization, you can turn it on by uncomment the code below:<br />
`#url(r'^api-token-verify/', verify_jwt_token)` in urls.py <br /><br /> and
`#'DEFAULT_PERMISSION_CLASSES': (` <br />
`#'rest_framework.permissions.IsAuthenticated',` <br />
`#),`  in settings.py <br />