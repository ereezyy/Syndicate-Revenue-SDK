# Contributing to Syndicate Agent SDK

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
