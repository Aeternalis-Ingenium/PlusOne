# Conventional Commit

The 5 most important commit types are

- feat $\rightarrow$ Writing a feature
- fix $\rightarrow$ Fixing code
- docs $\rightarrow$ Writing a documentation
- refactor $\rightarrow$ Refactor code
- test $\rightarrow$ Test code
- ci $\rightarrow$ Writing CI/CD

## Commit Title Convention

| Type | Convention  | Example |
| ---- | ----------- | ------- |
| Feature | feat(scope): SUMMARY OF NEW FEATURE | `feat(models): Create User Model` |
| Fix | fix(scope): SUMMARY OF FIXED CODE | `fix(main): Add missing CORS to app` |
| Docs | docs(scope): SUMMARY OF NEW DOCS | `docs(main): Write backend start up guide` |
| Refactor | refactor(scope): SUMMARY OF REFACTORED CODE | `refactor(user): Rewrite create user method` |
| Test | test(scope): SUMMARY OF TESTED CODE | `test(password): Ensure password can be verified` |
| CI | ci(scope): SUMMARY OF CI | `ci(test): Create test job pipeline with PyTest` |

## Commit Body Convention

| Type | Convention  | Example |
| ---- | ----------- | ------- |
| Feature | What's being added? Where? Purpose? | `Create Account class as superclass for Admin and User subclasses in src/models/db/account.py` |
| Fix | What was the error? How is it fixed? IS-Behaviour? Where? | `The registration endpoint localhost:8000/api/user-signup didn't redirect correctly and showed HTTP 404. Now, I added the id after the last path in the URL to redirect the page after a successful registration to the respective user. Code in src/api/routes/authentication.py` |
| Docs | Topic of documentation and where | `Write the start up guide for the backend app specifically the FastAPI using uvicorn. Docs in docs/BACKEND.md` |
| Refactor | Why? How? Where? | `Verifying user's password doesn't need a doubled is_verified() function. I merged the functions into 1 and moved it to src/security/hashing/password.py` |
| Test | What is being tested? What's the goal of the test? Where? | `Testing the Account class construction. The goal is to ensure that the Account class contains the correct attributes. Code found in tests/unit_tests/model_tests/test_account.py` |
| CI | What job + its goal? Which libraries? Where? | `Create build job to ensure the compatibility of the backend app using FastAPI. CI found in .github/workflows/CI-Backend.yaml` |
