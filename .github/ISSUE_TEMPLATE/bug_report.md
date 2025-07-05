name: Bug Report
description: Report a problem or unexpected behavior
title: "[BUG] "
labels: [bug]
assignees: []

body:
  - type: markdown
    attributes:
      value: |
        Please describe the issue clearly and concisely.
  - type: input
    id: version
    attributes:
      label: Software Version
      placeholder: e.g., 2.2.1
    validations:
      required: true
  - type: textarea
    id: what-happened
    attributes:
      label: What happened?
      placeholder: Describe the issue.
    validations:
      required: true
  - type: textarea
    id: steps
    attributes:
      label: Steps to Reproduce
      placeholder: |
        1. Go to '...'
        2. Click on '...'
        3. Observe the behavior
