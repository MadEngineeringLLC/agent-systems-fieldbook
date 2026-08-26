# Evaluator calibration

The calibration set detects material drift in evaluator behavior. It contains synthetic summaries rather than live malicious content or third-party copyrighted artifacts.

Run calibration after changing:

- evaluator instructions;
- scoring weights or thresholds;
- risk definitions;
- taxonomy rules;
- disposition gates.

Expected outcomes are ranges, not exact prose. A change fails calibration when it:

- accepts a critical-risk case;
- rejects the clear bounded case without evidence of a new problem;
- misses the duplicate case;
- converts incomplete provenance directly to acceptance;
- changes a disposition without a documented rationale.
