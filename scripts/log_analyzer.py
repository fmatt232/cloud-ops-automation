#!/usr/bin/env python3
import argparse
import re
from collections import Counter
from pathlib import Path

LEVEL = re.compile(r"\b(DEBUG|INFO|WARNING|WARN|ERROR|CRITICAL)\b", re.I)

def analyze(path: Path):
    counts = Counter()
    examples = []
    with path.open(encoding="utf-8", errors="replace") as handle:
        for number, line in enumerate(handle, 1):
            match = LEVEL.search(line)
            if not match:
                continue
            level = match.group(1).upper().replace("WARN", "WARNING")
            counts[level] += 1
            if level in {"ERROR", "CRITICAL"} and len(examples) < 10:
                examples.append((number, line.strip()))
    return counts, examples

def main():
    parser = argparse.ArgumentParser(description="Summarize application log severity.")
    parser.add_argument("logfile", type=Path)
    args = parser.parse_args()
    counts, examples = analyze(args.logfile)
    print("Log summary")
    for level in ("CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"):
        print(f"{level:8} {counts[level]}")
    if examples:
        print("\nFirst high-severity events:")
        for number, line in examples:
            print(f"Line {number}: {line}")

if __name__ == "__main__":
    main()
