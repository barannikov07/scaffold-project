#!/usr/bin/env python3
"""Stamp the project scaffold templates into a target folder.

Usage:
  python3 scaffold.py --target /path/to/project \
      --set PROJECT_NAME="Orbit" --set PURPOSE="..." --set OWNER="..." \
      --set FRAMEWORK="Next.js" --set DATABASE="Postgres (Supabase)" \
      --set AUTH="Supabase Auth" --set HOSTING="Vercel" \
      --set FIRST_FEATURE_NAME="Rent tracking" --set FIRST_FEATURE_SLUG="rent-tracking"

What it does:
  * copies every file under assets/templates/ into the target, keeping paths
  * replaces {{KEY}} placeholders with the values given via --set
  * DATE is filled automatically (today, ISO)
  * unknown placeholders become "TBD(owner): <key>" and are listed at the end
  * files under docs/products/_template/ are copied verbatim (they stay templates)
  * the product template is also copied to docs/products/<FIRST_FEATURE_SLUG>/
    with FEATURE_NAME / FEATURE_SLUG filled in
  * never overwrites an existing file unless --force is given
"""
import argparse
import datetime as dt
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATES = os.path.join(os.path.dirname(HERE), "assets", "templates")
PLACEHOLDER = re.compile(r"\{\{([A-Z0-9_]+)\}\}")
PRODUCT_TEMPLATE_REL = os.path.join("docs", "products", "_template")


def humanize(key: str) -> str:
    return key.replace("_", " ").lower()


def stamp(text: str, values: dict, unknown: set) -> str:
    def repl(m):
        key = m.group(1)
        if key in values:
            return values[key]
        unknown.add(key)
        return f"TBD(owner): {humanize(key)}"
    return PLACEHOLDER.sub(repl, text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", required=True)
    ap.add_argument("--set", action="append", default=[], metavar="KEY=VALUE")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    values = {
        "DATE": dt.date.today().isoformat(),
        "TRIPWIRES": "- None yet. Add the first line when the first hard invariant exists.",
        "TECH_LEVEL": "understands, doesn't code",
        "PRODUCT_LEVEL": "worked with PMs",
    }
    for item in args.set:
        if "=" not in item:
            sys.exit(f"bad --set value (expected KEY=VALUE): {item}")
        k, v = item.split("=", 1)
        values[k.strip()] = v.strip()

    target = os.path.abspath(args.target)
    os.makedirs(target, exist_ok=True)

    written, skipped, unknown = [], [], set()

    for root, _dirs, files in os.walk(TEMPLATES):
        for name in files:
            src = os.path.join(root, name)
            rel = os.path.relpath(src, TEMPLATES)
            dst = os.path.join(target, rel)
            if os.path.exists(dst) and not args.force:
                skipped.append(rel)
                continue
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            if rel.startswith(PRODUCT_TEMPLATE_REL + os.sep):
                shutil.copyfile(src, dst)
            else:
                with open(src, encoding="utf-8") as f:
                    content = f.read()
                with open(dst, "w", encoding="utf-8") as f:
                    f.write(stamp(content, values, unknown))
            written.append(rel)

    slug = values.get("FIRST_FEATURE_SLUG")
    if slug:
        feature_values = dict(values)
        feature_values["FEATURE_NAME"] = values.get("FIRST_FEATURE_NAME", slug)
        feature_values["FEATURE_SLUG"] = slug
        src_dir = os.path.join(TEMPLATES, PRODUCT_TEMPLATE_REL)
        dst_dir = os.path.join(target, "docs", "products", slug)
        os.makedirs(dst_dir, exist_ok=True)
        for name in sorted(os.listdir(src_dir)):
            src = os.path.join(src_dir, name)
            dst = os.path.join(dst_dir, name)
            rel = os.path.relpath(dst, target)
            if os.path.exists(dst) and not args.force:
                skipped.append(rel)
                continue
            with open(src, encoding="utf-8") as f:
                content = f.read()
            with open(dst, "w", encoding="utf-8") as f:
                f.write(stamp(content, feature_values, unknown))
            written.append(rel)

    print(f"Target: {target}")
    print(f"Written ({len(written)}):")
    for rel in sorted(written):
        print(f"  {rel}")
    if skipped:
        print(f"Skipped, already exist ({len(skipped)}):")
        for rel in sorted(skipped):
            print(f"  {rel}")
    if unknown:
        print("Placeholders with no value, now marked TBD(owner):")
        for key in sorted(unknown):
            print(f"  {key}")


if __name__ == "__main__":
    main()
