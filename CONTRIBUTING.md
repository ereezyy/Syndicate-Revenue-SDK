# Contributing to Syndicate Swarm Specialist SDK

First off, thank you for considering contributing to the Syndicate Swarm Specialist SDK! It's people like you that make the open-source community such an amazing place to learn, inspire, and create.

## 🤝 Open-Source Contribution Policy

We welcome community pull requests and actively encourage contributions that improve the SDK, add new heuristics, or optimize the bidding logic. By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md) and the core principles outlined in `SOUL.md`.

## 🛠️ How Can I Contribute?

There are several ways you can contribute to the Syndicate Swarm Specialist SDK:

### 1. Reporting Bugs

*   **Check existing issues**: Before opening a new issue, please check if the bug has already been reported.
*   **Open a new issue**: If not, open a new issue with a clear and descriptive title. Include detailed steps to reproduce the bug, your environment details, and expected vs. actual behavior.

### 2. Suggesting Enhancements

*   Have an idea for a new feature or optimization? Open an issue with the label `enhancement`.
*   Describe the feature clearly and explain why it would be beneficial to the swarm.

### 3. Pull Requests

We encourage you to open pull requests (PRs) for any changes you wish to contribute. To ensure a smooth review process, please follow these guidelines:

## ✅ Development Setup

1.  **Fork the Repository**: Start by forking the repository to your own GitHub account.
2.  **Clone Your Fork**: Clone your forked repository to your local machine:

    ```bash
    git clone https://github.com/YOUR_USERNAME/Syndicate-Revenue-SDK.git
    cd Syndicate-Revenue-SDK
    ```

3.  **Install Dependencies**: Set up a virtual environment and install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Pre-Commit Hooks**: We use `pre-commit` to enforce code standards before code is even committed. Install and set up the hooks:

    ```bash
    pip install pre-commit
    pre-commit install
    ```

## 🌳 Branching Strategy

We use a `main` branch for stable releases and feature branches for ongoing development. All contributions should be made via feature branches.

*   `main`: The stable branch, always reflecting the latest release.
*   `feature/<feature-name>`: For new features.
*   `bugfix/<bug-description>`: For bug fixes.
*   `docs/<doc-update>`: For documentation improvements.

## 📥 Pull Request Guidelines

1.  **Create a Feature Branch**: Create a new branch from `main` for your changes. Use a descriptive name (e.g., `feature/add-new-heuristic`, `bugfix/fix-bid-calculation`).

    ```bash
    git checkout main
    git pull origin main
    git checkout -b feature/your-feature-name
    ```

2.  **Implement Your Changes**: Make your code changes, add new features, or fix bugs.
3.  **Write Tests**: If you've added code that should be tested, please add appropriate unit or integration tests.
4.  **Update Documentation**: If your changes affect any APIs, features, or installation steps, update the relevant documentation (e.g., `README.md`).
5.  **Ensure Code Quality**: Run linting and tests to ensure your code adheres to our standards. The pre-commit hooks will help with this.
6.  **Commit Your Changes**: Write clear, concise, and descriptive commit messages. We follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.

    Example:
    ```bash
    git commit -m "feat: Implement new bidding heuristic"
    ```

7.  **Push to Your Fork**: Push your new branch to your forked repository on GitHub:

    ```bash
    git push origin feature/your-feature-name
    ```

8.  **Create a Pull Request**: Finally, open a pull request from your forked repository to the `main` branch of the original `ereezyy/Syndicate-Revenue-SDK` repository. Provide a detailed description of your changes and why they are necessary.

## 🔐 Security

If you discover a security vulnerability, please refer to our `SECURITY.md` for responsible disclosure guidelines. Do not open public issues for security vulnerabilities.

Let's build the swarm together! 🚀
