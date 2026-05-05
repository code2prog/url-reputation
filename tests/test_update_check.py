from __future__ import annotations

import unittest
from unittest.mock import patch

from url_reputation.update_check import (
    check_for_update,
    format_update_result,
    normalize_release_version,
)


class FakeResponse:
    def __init__(self, payload, *, error: Exception | None = None):
        self.payload = payload
        self.error = error

    def raise_for_status(self):
        if self.error:
            raise self.error

    def json(self):
        return self.payload


class TestUpdateCheck(unittest.TestCase):
    def test_normalize_release_version(self):
        self.assertEqual(normalize_release_version("v1.11.1"), "1.11.1")
        self.assertEqual(normalize_release_version("1.11.1"), "1.11.1")

    @patch("url_reputation.update_check.requests.get")
    def test_check_for_update_detects_current_version(self, mock_get):
        mock_get.return_value = FakeResponse(
            {
                "tag_name": "v1.11.1",
                "html_url": "https://github.com/newuni/url-reputation/releases/tag/v1.11.1",
            }
        )

        result = check_for_update("1.11.1")

        self.assertFalse(result.update_available)
        self.assertIsNone(result.error)
        self.assertIn("up to date", format_update_result(result))

    @patch("url_reputation.update_check.requests.get")
    def test_check_for_update_detects_newer_release(self, mock_get):
        mock_get.return_value = FakeResponse(
            {
                "tag_name": "v1.12.0",
                "html_url": "https://github.com/newuni/url-reputation/releases/tag/v1.12.0",
            }
        )

        result = check_for_update("1.11.1")

        self.assertTrue(result.update_available)
        self.assertIsNone(result.error)
        self.assertIn("Update available", format_update_result(result))

    @patch("url_reputation.update_check.requests.get")
    def test_check_for_update_handles_request_errors(self, mock_get):
        mock_get.side_effect = RuntimeError("network down")

        result = check_for_update("1.11.1")

        self.assertFalse(result.update_available)
        self.assertEqual(result.error, "network down")
        self.assertIn("Could not check", format_update_result(result))


if __name__ == "__main__":
    unittest.main()
