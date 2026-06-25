"""scaffolder — `product init`: copy the command pack into a target project and write the
chosen harness's command files (via integrations).

Resolves the payload from the **repo root** when running from a source checkout (dev). A bundled
mode (shipping the pack inside the wheel) is the optional next step; for now `product init`
requires a source checkout / editable install.
"""

import shutil
from pathlib import Path

from . import integrations

N_COMMANDS = 5  # .product/commands/*.md


def sources() -> dict:
    """Locate the payload source. Keys: product, commands, agents, skills, mode."""
    here = Path(__file__).resolve()
    root = here.parents[1]
    if (root / ".product").is_dir() and (root / "agents").is_dir():
        return {"product": root / ".product", "commands": root / ".product" / "commands",
                "agents": root / "agents", "skills": root / "skills", "mode": "source"}
    p = here.parent / "payload"
    if (p / "product").is_dir():
        return {"product": p / "product", "commands": p / "product" / "commands",
                "agents": p / "agents", "skills": p / "skills", "mode": "bundled"}
    raise RuntimeError("Product-Kit payload not found — run from a source checkout / editable install.")


def init(target: str, agent: str = "claude") -> dict:
    """Scaffold .product/ + missions/ into `target` and install the harness command pack."""
    src = sources()
    target = Path(target).resolve()
    target.mkdir(parents=True, exist_ok=True)

    # 1) the .product/ payload (the command pack)
    shutil.copytree(src["product"], target / ".product", dirs_exist_ok=True)

    # 2) missions/ output dir
    (target / "missions").mkdir(exist_ok=True)

    # 3) harness integration (commands + engine for claude)
    summary = integrations.install(agent, src, target)
    summary["target"] = str(target)
    summary["payload_mode"] = src["mode"]
    return summary


def check(target: str = ".") -> list:
    """Lightweight prerequisite/health check. Returns (label, ok, detail) tuples."""
    checks = []
    try:
        src = sources()
        checks.append((f"payload found ({src['mode']})", True, str(src["product"].parent)))
        checks.append(("constitution present", (src["product"] / "memory" / "constitution.md").is_file(), ""))
        n_soldiers = len(list(src["agents"].glob("soldier-*.md")))
        checks.append(("all 30 soldiers wired", n_soldiers == 30, f"found {n_soldiers}"))
    except RuntimeError as e:
        checks.append(("payload found", False, str(e)))
    try:
        from product_kit import commander  # noqa: F401
        importable = True
    except ImportError:
        importable = False
    checks.append(("commander importable", importable, "check product_kit install"))
    try:
        import agents  # noqa: F401  (the Agents SDK)
        sdk = True
    except ImportError:
        sdk = False
    checks.append(("Agents SDK installed (needed for `product run`)", sdk, "pip install openai-agents"))
    return checks
