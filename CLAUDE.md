# CLAUDE.md

This file provides guidance for AI assistants working with this repository.

## Repository Status

This is a newly initialized repository. No application code, build configuration, or tests exist yet.

## Development Guidelines

When contributing to this repository, follow these conventions:

### Git Workflow

- Use feature branches with descriptive names
- Write clear, concise commit messages that explain the "why" behind changes
- Keep commits focused on a single logical change

### Code Quality

- Prefer simple, readable code over clever abstractions
- Add tests for new functionality
- Do not introduce known security vulnerabilities (OWASP top 10)

### File Organization

- Keep the project root clean; place source code in dedicated directories
- Store configuration files at the project root
- Place documentation in a `docs/` directory or as markdown files at the root

## Getting Started

This repository needs to be populated with project files. When setting up:

1. Choose a language/framework and add the appropriate project manifest (e.g., `package.json`, `Cargo.toml`, `pyproject.toml`)
2. Add a `.gitignore` appropriate for the chosen stack
3. Set up linting and formatting tools
4. Configure a test framework
5. Add CI/CD workflows
6. Update this file with project-specific details
