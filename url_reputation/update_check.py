"""Check the installed version against the latest GitHub release."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import requests
from packaging.version import InvalidVersion, Version

LATEST_RELEASE_URL = "https://api.github.com/repos/newuni/url-reputation/releases/latest"


@dataclass(frozen=True)
class UpdateCheckResult:
    current_version: str
    latest_version: str | None
    latest_url: str | None
    update_available: bool
    error: str | None = None


def normalize_release_version(value: str) -> str:
    """Normalize GitHub tags such as v1.11.1 to package versions such as 1.11.1."""

    return value.strip().lstrip("vV")


def check_for_update(current_version: str, *, timeout: int = 5) -> UpdateCheckResult:
    """Fetch the latest GitHub release and compare it to the installed version."""

    try:
        response = requests.get(
            LATEST_RELEASE_URL,
            headers={
                "Accept": "application/vnd.github+json",
                "User-Agent": "url-reputation",
            },
            timeout=timeout,
        )
        response.raise_for_status()
        payload = response.json()
    except Exception as exc:
        return UpdateCheckResult(
            current_version=current_version,
            latest_version=None,
            latest_url=None,
            update_available=False,
            error=str(exc),
        )

    if not isinstance(payload, dict):
        return UpdateCheckResult(
            current_version=current_version,
            latest_version=None,
            latest_url=None,
            update_available=False,
            error="unexpected GitHub response",
        )

    tag_name = _string_field(payload, "tag_name")
    if not tag_name:
        return UpdateCheckResult(
            current_version=current_version,
            latest_version=None,
            latest_url=None,
            update_available=False,
            error="latest release has no tag_name",
        )

    latest_version = normalize_release_version(tag_name)
    try:
        update_available = Version(latest_version) > Version(
            normalize_release_version(current_version)
        )
    except InvalidVersion as exc:
        return UpdateCheckResult(
            current_version=current_version,
            latest_version=latest_version,
            latest_url=_string_field(payload, "html_url"),
            update_available=False,
            error=str(exc),
        )

    return UpdateCheckResult(
        current_version=current_version,
        latest_version=latest_version,
        latest_url=_string_field(payload, "html_url"),
        update_available=update_available,
    )


def format_update_result(result: UpdateCheckResult) -> str:
    if result.error:
        return f"Could not check for updates: {result.error}"

    if result.latest_version is None:
        return "Could not check for updates: latest version unavailable"

    if result.update_available:
        suffix = f"\n{result.latest_url}" if result.latest_url else ""
        return f"Update available: {result.current_version} -> {result.latest_version}{suffix}"

    return f"url-reputation {result.current_version} is up to date"


def _string_field(payload: dict[str, Any], key: str) -> str | None:
    value = payload.get(key)
    return value if isinstance(value, str) else None
