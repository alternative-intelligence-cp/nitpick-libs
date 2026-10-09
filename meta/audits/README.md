# `meta/audits/`

Audit reports, filed by the orchestrator from the auditor's final message,
named `<repo>-<cycle>-<date>.md` (or `ecosystem-<date>.md`). *(Corrected 2026-10-09, E2-12: the files here also take `<repo>-pin-<commit>-<date>.md`, `<repo>-docs-<commit>-<date>.md`, `currency-<date>.md` and `ecosystem-early-<date>.md`, and an ordinal suffix for a repeat audit, `…-<date>-second.md` and on.)* The auditor
writes nothing (A-1); the close worker of the audited repository reads the
report from here and triages every finding in its execution record.
