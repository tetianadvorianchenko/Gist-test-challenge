# Testing strategy and justification
Black box testing - as we don't have access to the code base 

Functional testing - as user should be able to perform user journey to achive the result.

Acceptance testing - as we have the documentation provided. Documentation is descriptive and based on user journey, can be used for the acceptance criteria validation.

Adhock testing - for evaluations and testing in case for documented scenarios

# List of features
- CRUD gists
- auth + gists
- gists access (secret/public) as owner/ as other user
- Different file types support for gists
- comments on gists

# Testing types
Boundaries testing:
- min data required to create gist
- max number of files in one gist
- max size of file content/file name/gist description
- bulk gists creation(if possible and needed)

Security:
- create gist as not authorised user
- access secret gists with search as not logged/not owner

# Tools and Framework
for UI test:
- different browsers for the cross browsing testing
- pytest + Selenium for the UI test automation

for API test:
- Postman
- pytest + request lib
