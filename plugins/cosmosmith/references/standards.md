# Cosmosmith Standards References

Use this file as a routing map, not as a full standards dump.

## Research

Use web research when information may be current, competitive, regulatory, ecosystem-dependent, tool-version dependent, or platform-specific.

Research output must separate:

- Source links.
- Facts.
- Inferences.
- Product, design, architecture, QA, or release implications.

## Engineering

Follow the target repository's existing standards first.

When no local standard exists, use conservative defaults:

- Small, reviewable changes.
- Explicit contracts and schemas.
- Tests proportional to risk.
- No secrets in code or generated docs.
- Verification evidence before completion.

## Java / Backend Discipline

For Java or enterprise backend stacks, use Alibaba Java Coding Guidelines / P3C as a style and discipline reference where applicable.

Apply the spirit even outside Java:

- Clear naming.
- Explicit error handling.
- Safe collection and null handling.
- Consistent logging.
- Database and transaction caution.
- Security-aware input handling.

## Security

Use OWASP-style thinking for web/API surfaces:

- Authentication and authorization.
- Input validation.
- Injection risks.
- Secret handling.
- Error disclosure.
- Dependency and supply-chain risks.

## DevOps

Use Twelve-Factor-style configuration principles:

- Environment-specific config belongs in environment variables or managed config.
- Build, release, and run should be separable.
- Logs should be observable.
- Services should be reproducible.

## UI / Accessibility

Use platform accessibility expectations and current browser behavior:

- Keyboard access.
- Focus visibility.
- Color contrast.
- Text that does not overlap or overflow.
- Loading, empty, error, and disabled states.

