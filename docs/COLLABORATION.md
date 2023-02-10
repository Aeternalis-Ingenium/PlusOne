# Collaboration

To ensure the best possible experience in this project, we need a unified workflow that applies for everyone.

## Workflow

There is a lot of workflows for collaboration in software development. In this project we are going to integrate the workflow called [Trunk-Based Development](https://trunkbaseddevelopment.com/) with its particular style "[Short-Lived Feature Branch](https://trunkbaseddevelopment.com/short-lived-feature-branches/)".

Why? Simply because this workflow is proven to be accurate and straight forward for a team that is small enough while still tackling quite complex tasks. This workflow relies heavily on CI pipeline 🚀

**P. S. The name of the main branch is now `trunk` and NOT `main` or `master`.**

## Working-Flow

Follow the below working-flow to avoid conflicts in your commits!

- Flow 1: First time in the morning is to `pull` and `rebase` from the `origin trunk`!

    ```shell
    git checkout trunk
    git pull --rebase origin trunk
    ```

<br>

- Flow 2: Go back to your working branch and `rebase`!

    ```shell
    git checkout YOU/WORKING/BRANCH
    git rebase trunk
    ```

<br>

- Flow 3: Commit atomically!

    ```shell
    git add .
    git commit
    ```

<br>

- Flow 4: Push to ONLY your newly "Short-Lived" remote branch!

    ```shell
    git push origin YOUR/WORKING/BRANCH
    ```

<br>

- Flow 5: Pull Request!

    Go to our repository and create a pull request (REMEMBER our conventional commit rules! See the template [here](./../.github/templates/COMMIT_TEMPLATE/README.md)). Plus point if you create a check list in the body of your commit!

<br>

- Flow 6 (Optional): Delete your remote branch once it's merged (Remember the word "Short-Lived")!

    The merge will only happen after your code passes the CI and reviewed by at least 1 of your team member!

<br>

- Optional Flow: You got a conflict?

    No biggie! Just do [cherry-picking](https://git-scm.com/docs/git-cherry-pick).

---
