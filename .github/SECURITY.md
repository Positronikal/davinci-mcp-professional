# Security Policy

## Supported Versions

We actively support the following versions with security updates:

| Version | Supported          | End of Support |
| ------- | ------------------ | -------------- |
| 2.2.x   | :white_check_mark: | TBD            |
| 2.1.x   | :white_check_mark: | 2025-12-31     |
| < 2.0   | :x:                | 2024-12-31     |

## Reporting a Vulnerability

### How to Report

**For security vulnerabilities, please do NOT create a public GitHub issue.**

Instead, please report security vulnerabilities through one of these methods:

1. **Private Security Advisory** (Preferred): Use GitHub's private vulnerability reporting feature
2. **Email**: Send details to `hoyt.harness@gmail.com` with subject line `[SECURITY] DaVinci MCP Professional`
3. **PGP Encrypted Email**: If you have sensitive information, request our PGP key first

### What to Include

Please provide as much information as possible:

- **Description**: Clear description of the vulnerability
- **Steps to Reproduce**: Detailed steps to reproduce the issue
- **Impact Assessment**: Your assessment of the potential impact
- **Affected Versions**: Which versions are affected
- **Proof of Concept**: Code or screenshots demonstrating the issue (if applicable)
- **Suggested Fix**: Any recommendations for fixing the vulnerability (optional)

### Response Timeline

We are committed to responding to security reports promptly:

- **Initial Response**: Within 48-72 hours
- **Triage Assessment**: Within 5 business days
- **Fix Development**: Varies by severity (see below)
- **Public Disclosure**: Coordinated with reporter, typically 30-90 days after fix

### Severity Levels

| Severity | Response Time | Examples |
|----------|---------------|----------|
| **Critical** | 24-48 hours | Remote code execution, authentication bypass |
| **High** | 3-5 days | Privilege escalation, significant data exposure |
| **Medium** | 7-14 days | Cross-site scripting, information disclosure |
| **Low** | 30 days | Minor information leaks, non-exploitable issues |

### Security Best Practices

When using DaVinci MCP Professional:

- **Keep Updated**: Always use the latest version
- **Secure Environment**: Run in isolated environments when possible
- **Access Control**: Limit access to DaVinci Resolve API credentials
- **Monitor Logs**: Regularly review application logs for anomalies
- **Network Security**: Use encrypted connections when available

### Security Features

Current security measures in place:

- **Dependency Scanning**: Automated dependency vulnerability scanning
- **Static Analysis**: Code quality and security analysis
- **Input Validation**: Comprehensive input sanitization
- **Error Handling**: Secure error messages that don't leak sensitive information
- **Audit Logging**: Activity logging for forensic analysis

### Hall of Fame

We appreciate security researchers who help make our project safer:

- [Your name could be here!]

### Legal

This security policy applies to the DaVinci MCP Professional project. By participating in our security program, you agree to:

- Make a good faith effort to avoid privacy violations and service disruption
- Only interact with systems you own or have explicit permission to test
- Not access or modify user data without explicit permission
- Follow responsible disclosure practices

We commit to:

- Respond to your report promptly and work with you to understand the issue
- Not pursue legal action against researchers who follow this policy
- Recognize your contribution publicly (if desired) after the issue is resolved

---

**Contact**: For questions about this security policy, contact hoyt.harness@gmail.com
