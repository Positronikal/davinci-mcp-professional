#!/usr/bin/env python3
"""
Security audit script for DaVinci MCP Professional.

This script runs a comprehensive security audit including:
- Dependency vulnerability scanning
- Static application security testing (SAST)
- License compliance checking
- Code quality analysis
- Security test execution
"""

import subprocess
import sys
import json
import os
from pathlib import Path
from typing import Dict, List, Tuple, Optional


class SecurityAuditor:
    """Comprehensive security auditing tool."""
    
    def __init__(self, project_root: Optional[Path] = None):
        self.project_root = project_root or Path(__file__).parent
        self.results = {}
        self.errors = []
    
    def run_command(self, cmd: List[str], description: str) -> Tuple[bool, str, str]:
        """Run a command and capture output."""
        try:
            result = subprocess.run(
                cmd, capture_output=True, text=True, cwd=self.project_root
            )
            return (
                result.returncode == 0,
                result.stdout,
                result.stderr
            )
        except FileNotFoundError:
            return False, "", f"Command not found: {cmd[0]}"
        except Exception as e:
            return False, "", str(e)
    
    def check_dependencies_safety(self) -> Dict:
        """Check dependencies for known vulnerabilities using Safety."""
        print("🔍 Checking dependencies with Safety...")
        
        success, stdout, stderr = self.run_command(
            ["safety", "check", "--json"], 
            "Safety vulnerability scan"
        )
        
        if success:
            try:
                vulnerabilities = json.loads(stdout) if stdout.strip() else []
                return {
                    "status": "success",
                    "vulnerabilities": vulnerabilities,
                    "count": len(vulnerabilities)
                }
            except json.JSONDecodeError:
                return {
                    "status": "error",
                    "error": "Failed to parse Safety output"
                }
        else:
            return {
                "status": "error", 
                "error": stderr or "Safety check failed"
            }
    
    def run_bandit_sast(self) -> Dict:
        """Run Bandit static application security testing."""
        print("🔍 Running Bandit SAST analysis...")
        
        success, stdout, stderr = self.run_command(
            ["bandit", "-r", "src/", "-f", "json", "-o", "bandit-report.json"],
            "Bandit SAST scan"
        )
        
        # Bandit returns non-zero when issues are found, so check the output file
        report_file = self.project_root / "bandit-report.json"
        if report_file.exists():
            try:
                with open(report_file, 'r') as f:
                    report = json.load(f)
                
                return {
                    "status": "success",
                    "results": report.get("results", []),
                    "metrics": report.get("metrics", {}),
                    "count": len(report.get("results", []))
                }
            except Exception as e:
                return {
                    "status": "error",
                    "error": f"Failed to read Bandit report: {e}"
                }
        else:
            return {
                "status": "error",
                "error": "Bandit report not generated"
            }
    
    def check_license_compliance(self) -> Dict:
        """Check license compliance."""
        print("📄 Checking license compliance...")
        
        success, stdout, stderr = self.run_command(
            ["pip-licenses", "--format=json"],
            "License compliance check"
        )
        
        if success:
            try:
                licenses = json.loads(stdout)
                
                # Check for problematic licenses
                problematic_licenses = [
                    "GPL", "AGPL", "LGPL", "CDDL", "EPL", "MPL"
                ]
                
                issues = []
                for package in licenses:
                    license_name = package.get("License", "").upper()
                    if any(prob in license_name for prob in problematic_licenses):
                        issues.append({
                            "package": package.get("Name"),
                            "license": package.get("License"),
                            "version": package.get("Version")
                        })
                
                return {
                    "status": "success",
                    "licenses": licenses,
                    "total_packages": len(licenses),
                    "problematic_licenses": issues,
                    "issues_count": len(issues)
                }
            except json.JSONDecodeError:
                return {
                    "status": "error",
                    "error": "Failed to parse license data"
                }
        else:
            return {
                "status": "error",
                "error": stderr or "License check failed"
            }
    
    def run_security_tests(self) -> Dict:
        """Run security-focused tests."""
        print("🧪 Running security tests...")
        
        success, stdout, stderr = self.run_command(
            ["python", "-m", "pytest", "tests/test_security.py", "-v", "--tb=short"],
            "Security tests"
        )
        
        return {
            "status": "success" if success else "failed",
            "output": stdout,
            "error": stderr if not success else None
        }
    
    def run_code_quality_checks(self) -> Dict:
        """Run code quality and style checks."""
        print("✨ Running code quality checks...")
        
        results = {}
        
        # Run Black formatter check
        success, stdout, stderr = self.run_command(
            ["black", "--check", "--diff", "src/"],
            "Black formatter check"
        )
        results["black"] = {
            "passed": success,
            "output": stdout,
            "error": stderr if not success else None
        }
        
        # Run isort import sorting check
        success, stdout, stderr = self.run_command(
            ["isort", "--check-only", "--diff", "src/"],
            "isort import check"
        )
        results["isort"] = {
            "passed": success,
            "output": stdout,
            "error": stderr if not success else None
        }
        
        # Run Ruff linting
        success, stdout, stderr = self.run_command(
            ["ruff", "check", "src/"],
            "Ruff linting"
        )
        results["ruff"] = {
            "passed": success,
            "output": stdout,
            "error": stderr if not success else None
        }
        
        return results
    
    def generate_report(self) -> str:
        """Generate a comprehensive security report."""
        report_lines = [
            "=" * 80,
            "🛡️  DAVINCI MCP PROFESSIONAL SECURITY AUDIT REPORT",
            "=" * 80,
            ""
        ]
        
        # Safety results
        if "safety" in self.results:
            safety = self.results["safety"]
            report_lines.append("📦 DEPENDENCY SECURITY (Safety)")
            report_lines.append("-" * 40)
            if safety["status"] == "success":
                vuln_count = safety["count"]
                if vuln_count == 0:
                    report_lines.append("✅ No known vulnerabilities found")
                else:
                    report_lines.append(f"⚠️  {vuln_count} vulnerabilities found:")
                    for vuln in safety["vulnerabilities"][:5]:  # Show first 5
                        pkg = vuln.get("package", "Unknown")
                        ver = vuln.get("installed_version", "Unknown")
                        vuln_id = vuln.get("vulnerability_id", "Unknown")
                        report_lines.append(f"   • {pkg} {ver} - {vuln_id}")
            else:
                report_lines.append(f"❌ Error: {safety['error']}")
            report_lines.append("")
        
        # Bandit results
        if "bandit" in self.results:
            bandit = self.results["bandit"]
            report_lines.append("🔍 STATIC APPLICATION SECURITY TESTING (Bandit)")
            report_lines.append("-" * 50)
            if bandit["status"] == "success":
                issue_count = bandit["count"]
                if issue_count == 0:
                    report_lines.append("✅ No security issues found")
                else:
                    report_lines.append(f"⚠️  {issue_count} security issues found:")
                    for issue in bandit["results"][:5]:  # Show first 5
                        test_id = issue.get("test_id", "Unknown")
                        severity = issue.get("issue_severity", "Unknown")
                        confidence = issue.get("issue_confidence", "Unknown")
                        text = issue.get("issue_text", "Unknown")
                        report_lines.append(f"   • {test_id} ({severity}/{confidence}): {text}")
            else:
                report_lines.append(f"❌ Error: {bandit['error']}")
            report_lines.append("")
        
        # License compliance
        if "licenses" in self.results:
            licenses = self.results["licenses"]
            report_lines.append("📄 LICENSE COMPLIANCE")
            report_lines.append("-" * 20)
            if licenses["status"] == "success":
                total = licenses["total_packages"]
                issues = licenses["issues_count"]
                report_lines.append(f"📊 Total packages: {total}")
                if issues == 0:
                    report_lines.append("✅ No problematic licenses found")
                else:
                    report_lines.append(f"⚠️  {issues} potentially problematic licenses:")
                    for issue in licenses["problematic_licenses"]:
                        pkg = issue["package"]
                        lic = issue["license"]
                        report_lines.append(f"   • {pkg}: {lic}")
            else:
                report_lines.append(f"❌ Error: {licenses['error']}")
            report_lines.append("")
        
        # Security tests
        if "security_tests" in self.results:
            tests = self.results["security_tests"]
            report_lines.append("🧪 SECURITY TESTS")
            report_lines.append("-" * 15)
            if tests["status"] == "success":
                report_lines.append("✅ All security tests passed")
            else:
                report_lines.append("❌ Some security tests failed")
                if tests.get("error"):
                    report_lines.append(f"Error: {tests['error']}")
            report_lines.append("")
        
        # Code quality
        if "code_quality" in self.results:
            quality = self.results["code_quality"]
            report_lines.append("✨ CODE QUALITY")
            report_lines.append("-" * 13)
            for tool, result in quality.items():
                status = "✅" if result["passed"] else "❌"
                report_lines.append(f"{status} {tool.capitalize()}")
            report_lines.append("")
        
        # Summary
        report_lines.extend([
            "📊 SECURITY AUDIT SUMMARY",
            "-" * 25,
            f"🗓️  Audit Date: {os.environ.get('DATE', 'Unknown')}",
            f"👤 Auditor: Security Automation Script",
            f"📁 Project: DaVinci MCP Professional v2.2.1",
            "",
            "🔗 Next Steps:",
            "1. Review and address any security vulnerabilities",
            "2. Update dependencies with known issues", 
            "3. Fix code quality issues",
            "4. Re-run audit after fixes",
            "",
            "=" * 80
        ])
        
        return "\n".join(report_lines)
    
    def run_full_audit(self) -> None:
        """Run the complete security audit."""
        print("🚀 Starting comprehensive security audit...")
        print()
        
        # Run all security checks
        self.results["safety"] = self.check_dependencies_safety()
        self.results["bandit"] = self.run_bandit_sast()
        self.results["licenses"] = self.check_license_compliance()
        self.results["security_tests"] = self.run_security_tests()
        self.results["code_quality"] = self.run_code_quality_checks()
        
        # Generate and save report
        report = self.generate_report()
        print(report)
        
        # Save report to file
        report_file = self.project_root / "security-audit-report.txt"
        with open(report_file, 'w') as f:
            f.write(report)
        
        print(f"\n📄 Full report saved to: {report_file}")
        
        # Save JSON results for CI/CD
        json_file = self.project_root / "security-audit-results.json"
        with open(json_file, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        print(f"📊 JSON results saved to: {json_file}")


def main():
    """Main entry point."""
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        print("""
DaVinci MCP Professional Security Auditor

Usage: python security_audit.py [options]

Options:
  --help     Show this help message
  
This script performs a comprehensive security audit including:
- Dependency vulnerability scanning (Safety)
- Static application security testing (Bandit)
- License compliance checking
- Security test execution
- Code quality analysis

Results are saved to security-audit-report.txt and security-audit-results.json
        """)
        return
    
    auditor = SecurityAuditor()
    auditor.run_full_audit()


if __name__ == "__main__":
    main()
