from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent / "docs" / "source" / "reference" / "srcPy"


def fix_ib_api(p: Path) -> None:
    t = p.read_text(encoding="utf-8")
    t = t.replace(
        "   srcPy.data.ib_api.IBKRConnectionError\n   srcPy.data.ib_api.IBKRConnectionError\n",
        "   srcPy.data.ib_api.IBKRConnectionError\n",
    )
    t = re.sub(
        r"\n\.\. py:exception:: IBKRConnectionError\n\n   Bases: :py:obj:`Exception`\n\n\n   Common base class for all non-exit exceptions.\n\n\n",
        "\n",
        t,
        count=1,
    )
    t = re.sub(
        r"\n\.\. py:exception:: IBKRConnectionError\n\n   Bases: :py:obj:`RuntimeError`\n\n\n   Unspecified run-time error.\n\n\n",
        "\n",
        t,
        count=1,
    )
    p.write_text(t, encoding="utf-8")


def fix_ops(p: Path) -> None:
    t = p.read_text(encoding="utf-8")
    t = t.replace(
        "   srcPy.ops.configure_logger\n   srcPy.ops.multi_tier_cache\n   srcPy.ops.get_logger\n",
        "   srcPy.ops.configure_logger\n   srcPy.ops.get_logger\n",
    )
    needle = (
        ".. py:function:: multi_tier_cache(ttl = 60, version = 'v1', "
        "persist_large_objects = False, key_fn = None, redis_client=None, "
        "l2_type = 'memfd', check_l4_on_miss = False)\n"
    )
    if needle in t:
        after = t.split(needle, 1)[1]
        if not after.lstrip().startswith(":no-index:"):
            t = t.replace(needle, needle + "   :no-index:\n")
    p.write_text(t, encoding="utf-8")


def fix_pipeline_base(p: Path) -> None:
    t = p.read_text(encoding="utf-8")
    t = t.replace(
        "   srcPy.pipeline.core.pipeline_core_base.StepRegistry\n   srcPy.pipeline.core.pipeline_core_base.InT\n",
        "   srcPy.pipeline.core.pipeline_core_base.InT\n",
    )
    block = ".. py:data:: StepRegistry\n   :type:  Any\n   :value: Ellipsis\n\n\n"
    if block in t:
        t = t.replace(block, "")
    p.write_text(t, encoding="utf-8")


def fix_cleaning_base(p: Path) -> None:
    t = p.read_text(encoding="utf-8")
    attr = (
        "Attributes\n----------\n\n.. autoapisummary::\n\n"
        "   srcPy.pipeline.stages.cleaning.core.base.PolarsDataFrame\n\n\n"
    )
    if attr in t:
        t = t.replace(attr, "")
    block = ".. py:data:: PolarsDataFrame\n   :type:  Any\n   :value: Ellipsis\n\n\n"
    if block in t:
        t = t.replace(block, "")
    p.write_text(t, encoding="utf-8")


if __name__ == "__main__":
    fix_ib_api(ROOT / "data" / "ib_api" / "index.rst")
    fix_ops(ROOT / "ops" / "index.rst")
    fix_pipeline_base(ROOT / "pipeline" / "core" / "pipeline_core_base" / "index.rst")
    fix_cleaning_base(ROOT / "pipeline" / "stages" / "cleaning" / "core" / "base" / "index.rst")
    print("patched")
