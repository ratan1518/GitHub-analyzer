"""
analysis/repo_health.py
Compute per-repo and aggregate health scores from already-fetched repo data.
"""

def _to_int(value, default=0):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


HEALTH_MAX = 100

# Weight for each signal (must sum to 100)
WEIGHTS = {
    "has_readme":       15,
    "has_ci":           20,
    "has_tests":        20,
    "has_license":      15,
    "recently_active":  20,
    "low_open_issues":  10,
}


def calculate_grade(score: float) -> str:
    """Map numeric score (0-100) to a letter grade."""
    if not isinstance(score, (int, float)) or score < 0:
        return "N/A"
    if score >= 90: return "A+"
    if score >= 75: return "A"
    if score >= 60: return "B"
    if score >= 40: return "C"
    if score >= 20: return "D"
    return "F"


def score_repo(repo: dict) -> dict:
    """
    Score a single repo dict (as returned by fetcher).
    """
    signals = {
        "has_readme":      bool(repo.get("has_readme", False)),
        "has_ci":          bool(repo.get("has_ci", False)),
        "has_tests":       bool(repo.get("has_tests", False)),
        "has_license":     bool(repo.get("has_license", False)),
        "recently_active": bool(repo.get("recently_active", False)),
        "low_open_issues": bool(repo.get("low_open_issues", True)),
    }

    total = sum(WEIGHTS[k] for k, v in signals.items() if v)
    grade = calculate_grade(total)

    if total >= 80:
        emoji, label = "🟢", "Healthy"
    elif total >= 50:
        emoji, label = "🟡", "Needs Work"
    else:
        emoji, label = "🔴", "Abandoned"

    return {
        "name": repo.get("name", ""),
        "score": total,
        "grade": grade,
        "emoji": emoji,
        "label": label,
        "signals": signals,
        "stars": _to_int(repo.get("stars", 0)),
        "forks": _to_int(repo.get("forks", 0)),
        "language": repo.get("language", "Unknown"),
        "commit_count": _to_int(repo.get("commit_count", 0)),
        "has_readme": signals["has_readme"],
    }


def aggregate_health(repo_scores: list[dict]) -> dict:
    """Compute an overall maintainer health score across all repos."""
    if not repo_scores:
        return {"maintainer_score": 0, "label": "No repos", "emoji": "❓", "grade": "N/A"}

    avg = sum(_to_int(r.get("score", 0)) for r in repo_scores) / len(repo_scores)
    grade = calculate_grade(avg)

    if avg >= 75:
        label, emoji = "Excellent Maintainer", "🏆"
    elif avg >= 55:
        label, emoji = "Good Maintainer", "✅"
    elif avg >= 35:
        label, emoji = "Average Maintainer", "📋"
    else:
        label, emoji = "Needs Improvement", "⚠️"

    healthy   = sum(1 for r in repo_scores if _to_int(r.get("score", 0)) >= 80)
    needs_work = sum(1 for r in repo_scores if 50 <= _to_int(r.get("score", 0)) < 80)
    abandoned  = sum(1 for r in repo_scores if _to_int(r.get("score", 0)) < 50)

    return {
        "maintainer_score": round(avg),
        "grade": grade,
        "label": label,
        "emoji": emoji,
        "healthy_count": healthy,
        "needs_work_count": needs_work,
        "abandoned_count": abandoned,
    }
