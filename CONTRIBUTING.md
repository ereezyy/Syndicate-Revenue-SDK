# Contributing to Syndicate Agent SDK

First off, thank you for considering contributing to the Syndicate Agent SDK! It's people like you that make the open-source community such an amazing place to learn, inspire, and create.

## 🤝 Open-Source Contribution Policy

We welcome community pull requests and actively encourage contributions that improve the SDK, add new heuristics, or optimize the bidding logic. By participating in this project, you agree to abide by our Code of Conduct and the core principles outlined in `SOUL.md`.

## 🛠️ How Can I Contribute?

### 1. Reporting Bugs
- **Check the existing issues** to see if the bug has already been reported.
- **Open a new issue** if the bug is not yet reported, providing a clear and descriptive title.
- Include detailed steps to reproduce the bug, your environment details, and expected vs. actual behavior.

### 2. Suggesting Enhancements
- Have an idea for a new feature or optimization? Open an issue with the label `enhancement`.
- Describe the feature clearly and explain why it would be beneficial to the swarm.

### 3. Pull Requests
- **Fork** the repository and create your branch from `main`.
- If you've added code that should be tested, add tests!
- Ensure your code follows the existing style and passes all linting/formatting checks.
- Issue that PR! A maintainer will review it and provide feedback.

## ✅ Development Setup

1. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Syndicate-Revenue-SDK.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up pre-commit hooks to ensure CI/CD standards:
   ```bash
   pip install pre-commit
   pre-commit install
   ```

## 🔐 Security

If you discover a security vulnerability, please refer to our `SECURITY.md` for responsible disclosure guidelines. Do not open public issues for security vulnerabilities.

Let's build the swarm together! 🚀
Thank you for your interest in contributing to the Syndicate Agent SDK! We welcome pull requests from the community to help make this project better. By contributing, you're helping us build a robust ecosystem for AI agents.

## Getting Started

1. **Fork the Repository**: Start by forking the repository to your own GitHub account.
2. **Clone the Repo**: Clone your fork locally to begin development.
3. **Install Dependencies**: Set up a virtual environment and install the required dependencies (e.g., `pip install -r requirements.txt`).

## Open Source Contribution Policy

We encourage community PRs for bug fixes, new features, and documentation improvements. Here are some guidelines:

- **Create an Issue**: Before starting work on a major feature, please create an issue to discuss it with the maintainers.
- **Branching**: Create a feature branch for your work (e.g., `feature/my-new-feature` or `bugfix/issue-description`).
- **Coding Standards**: Ensure your code follows the existing style. We use auto-formatting and linting checks.
- **Testing**: Add tests for your changes. We require test coverage for all new features and bug fixes.
- **Commit Messages**: Write clear, descriptive commit messages.

## Submitting a Pull Request

1. **Push Changes**: Push your changes to your fork.
2. **Open PR**: Open a pull request against the `main` branch of the original repository.
3. **CI Checks**: Ensure all continuous integration (CI) checks pass. This includes auto-formatting, linting, tests, and lock file checks.
4. **Review**: A maintainer will review your PR. Be prepared to make requested changes.

## Setting Up Pre-Commit Hooks

We use `pre-commit` to enforce standards before code is even committed. Please run the following command after cloning the repo to set up the hooks:

```bash
pip install pre-commit
pre-commit install
```

This will automatically check for things like formatting, linting, and preventing lock files from being omitted.

Thank you for your contributions!
