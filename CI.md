## GitHub actions best practices:

1. Avoid installing unnecessary dependencies. GitHub Actions virtual machines are limited to a hard cap of free minutes per month ~2,000 for the free plan, so each redundant second spent running on the VM might add up to thousands dollars wasted when scaling up.

2. Do not hardcode secrets. Use GitHub encrypted secret handling. The reasons are obvious, I guess.

3. Don’t use self-hosted runners in a public repository. If you’re working on a public Action, somebody could fork it and submit a pull request for a workflow containing malicious code. That malicious code will then be executed by the Action on your self-hosted machine, and could easily escape its sandbox, invade your network, and do all sorts of bad things.

4. Use layer caching for, again, avoiding redundant seconds running on the VM to save time -> money.

## Jenkins best practices:

1. Using Declarative syntax for the Jenkinsfile.

2. Don't use input within an agent.