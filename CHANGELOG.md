# Changelog

All notable changes to this project are documented here.

## [v1.12.0] - 2026-05-05
### Added
- CLI version reporting with `url-reputation --version`.
- Live GitHub Releases update detection with `url-reputation --check-update`.
- Script-friendly update-check exit codes: `0` when up to date, `1` when an update is available, and `2` when the check fails.

### Changed
- Added `packaging` as a runtime dependency for PEP 440-safe version comparisons.
- README now documents version and update-check commands.

## [v1.11.1] - 2026-05-05
### Fixed
- Python 3.9 CI type-check compatibility for MX DNS records when `dnspython` resolves to older type metadata.
- Release state docs now point to `v1.11.1` as the latest patch release.

## [v1.11.0] - 2026-05-05
### Added
- Python 3.13 and 3.14 package classifiers.
- CI coverage for Python 3.9 through 3.14, with Python 3.14 as the primary coverage, release, benchmark, macOS, and Windows lane.

### Changed
- Docker and Docker development images now use `python:3.14-slim`.
- Release workflow now builds and validates on Python 3.14.
- README, contributor docs, issue template, and status docs now present Python 3.14 as the recommended runtime while keeping Python 3.9+ compatibility.
- CI Docker build detection now uses `web/Dockerfile`, matching the repository layout.
- Benchmarks now run on pushes to both `main` and `master`.

### Fixed
- Release workflow now checks Ruff formatting before publishing.
- Status and development docs no longer reference stale local paths or older release state.

## [v1.10.0] - 2026-02-24
### Added
- Stronger TLS posture analysis in `tls` enrichment:
  - Protocol probing (`TLSv1.0`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`)
  - Cipher classification and negotiated cipher capture
  - Posture grading (`A`-`F`) with assessment text
  - Legacy protocol and weak-cipher indicators
- Scoring contributions for weak TLS posture signals:
  - `enrichment.tls.posture_grade`
  - `enrichment.tls.legacy_protocols`
  - `enrichment.tls.weak_ciphers`
- Web UI support for TLS posture output (`grade`, protocols, legacy).

### Changed
- `--enrich tls` now surfaces protocol/cipher posture data in CLI and web output.
- Legacy `enrich()` compatibility path now supports `tls` and emits risk indicators for weak posture.
- Roadmap cleanup in README to keep only future-facing "Next ideas".

### Fixed
- Release docs consistency for `v1.10.0` (README + changelog alignment).

## [v1.9.0] - 2026-02-19
### Added
- HN-ready web UX improvements for screenshot enrichment:
  - Dedicated `/api/screenshot-capture` endpoint (decoupled from main check)
  - UI async screenshot fetch with loading state
  - Screenshot preview rendering through `/api/screenshot` file-serving endpoint
- Screenshot backend fallback now works in web deployments without Playwright (`thumio`).

### Fixed
- Geo enrichment compatibility fix for `ip-api` free-tier endpoint behavior.
- TLS web output reliability and hostname matching behavior.
- WHOIS empty-state clarity in web UI.
- CI stability: restored lint/type/test/coverage green after F-block additions.

### Security
- Repository scanned for leaked secrets before release (no real keys detected in tracked files).
- Kept keyless default path working (free sources + optional enrichers).

## [v1.8.0] - 2026-02-19
### Added
- F-block roadmap delivered end-to-end:
  - Rich-enhanced pretty output (with plain fallback)
  - Watch mode (`--watch`, `--watch-changes-only`)
  - Script-friendly flags (`--quiet`, `--alert-above`)
  - HTML reports (`--format html`, `--report-html`)
  - SSL/TLS enrichment (`ssl`, `tls`, `tls_cert`) with scoring hooks
  - Screenshot enrichment (`screenshot`, best-effort optional Playwright)
- New HTML report renderer module: `url_reputation/html_report.py`.
- Web UI parity updates: auto-refresh, export report action, TLS panel, screenshot section.

### Changed
- Web API enrichment path aligned with CLI enrichment engine and score recomputation.
- Version bump to 1.8.0 across package + web API.

## [v1.7.0] - 2026-02-18
### Changed
- Significant static-analysis hardening completed in staged blocks.
- mypy tightened (`no_implicit_optional`, `check_untyped_defs`, `warn_return_any`, `disallow_untyped_defs`, `strict_equality`).
- Ruff tightened and adopted additional rule families (`UP`, `SIM`) with deferred items fully resolved.
- Test and codebase cleanups to keep `ruff`, `mypy`, and full test suite green under stricter rules.

## [v1.6.0] - 2026-02-18
### Added
- Benchmark suite (`pytest-benchmark`) and performance docs.
- Test/documentation polish and release prep.

### Changed
- README and wiki updates for the release.

## [v1.5.0] - 2026-02-18
### Changed
- README updates and version bump.
- Static analysis cleanup (`ruff` + `mypy`).

## [v1.4.1] - 2026-02-17
### Added
- Docker healthcheck and improved dev workflow.

## [v1.4.0] - 2026-01-20
### Added
- DNS + Whois enrichment.

## [v1.3.0] - 2026-01-20
### Added
- Webhook notifications with HMAC verification.

## [v1.2.0] - 2026-01-20
### Added
- `.env` support for API keys.

## [v1.1.0] - 2026-01-20
### Added
- New data sources (including AlienVault OTX).

## [v1.0.0] - 2026-01-20
### Added
- Initial release.

[v1.12.0]: https://github.com/newuni/url-reputation/compare/v1.11.1...v1.12.0
[v1.11.1]: https://github.com/newuni/url-reputation/compare/v1.11.0...v1.11.1
[v1.11.0]: https://github.com/newuni/url-reputation/compare/v1.10.0...v1.11.0
[v1.10.0]: https://github.com/newuni/url-reputation/compare/v1.9.0...v1.10.0
[v1.9.0]: https://github.com/newuni/url-reputation/compare/v1.8.0...v1.9.0
[v1.8.0]: https://github.com/newuni/url-reputation/compare/v1.7.0...v1.8.0
[v1.7.0]: https://github.com/newuni/url-reputation/compare/v1.6.0...v1.7.0
[v1.6.0]: https://github.com/newuni/url-reputation/compare/v1.5.0...v1.6.0
[v1.5.0]: https://github.com/newuni/url-reputation/compare/v1.4.1...v1.5.0
[v1.4.1]: https://github.com/newuni/url-reputation/compare/v1.4.0...v1.4.1
[v1.4.0]: https://github.com/newuni/url-reputation/compare/v1.3.0...v1.4.0
[v1.3.0]: https://github.com/newuni/url-reputation/compare/v1.2.0...v1.3.0
[v1.2.0]: https://github.com/newuni/url-reputation/compare/v1.1.0...v1.2.0
[v1.1.0]: https://github.com/newuni/url-reputation/compare/v1.0.0...v1.1.0
[v1.0.0]: https://github.com/newuni/url-reputation/releases/tag/v1.0.0
