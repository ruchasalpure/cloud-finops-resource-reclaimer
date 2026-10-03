# Duties and Responsibilities for Cloud FinOps Resource Reclaimer Agent

## Dual-Control Architecture
Maker:
zombie-resource-scavenger

Checker:
production-safety-checker

## Operational Workflow
1. The Maker (zombie-resource-scavenger) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (production-safety-checker) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
