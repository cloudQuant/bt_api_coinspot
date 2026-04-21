from __future__ import annotations

from typing import Any

from bt_api_base.error import ErrorCategory, ErrorTranslator, UnifiedError, UnifiedErrorCode


class CoinSpotErrorTranslator(ErrorTranslator):
    @classmethod
    def translate(cls, raw_error: dict[str, Any], venue: str) -> UnifiedError | None:
        message = str(raw_error.get("message", raw_error.get("error", "")))
        lower = message.lower()

        if "signature" in lower or "auth" in lower or "api key" in lower:
            code = UnifiedErrorCode.INVALID_SIGNATURE
            category = ErrorCategory.AUTH
        elif "balance" in lower or "insufficient" in lower:
            code = UnifiedErrorCode.INSUFFICIENT_BALANCE
            category = ErrorCategory.BUSINESS
        elif "rate" in lower or "limit" in lower or "too many requests" in lower:
            code = UnifiedErrorCode.RATE_LIMIT_EXCEEDED
            category = ErrorCategory.RATE_LIMIT
        elif "not found" in lower or "does not exist" in lower:
            code = UnifiedErrorCode.ORDER_NOT_FOUND
            category = ErrorCategory.BUSINESS
        elif "market" in lower and "closed" in lower:
            code = UnifiedErrorCode.MARKET_CLOSED
            category = ErrorCategory.BUSINESS
        else:
            code = UnifiedErrorCode.INTERNAL_ERROR
            category = ErrorCategory.SYSTEM

        return UnifiedError(
            code=code,
            category=category,
            venue=venue,
            message=message or "Unknown error",
            original_error=str(raw_error),
            context={"raw_response": raw_error},
        )
