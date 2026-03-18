#!/usr/bin/env python3
import argparse
import json
import sys
from typing import Any


def eprint(*args: Any, **kwargs: Any) -> None:
    print(*args, file=sys.stderr, **kwargs)


def run_search(args: argparse.Namespace) -> int:
    try:
        from ddgs import DDGS
    except Exception as exc:
        raise SystemExit(
            "ddgs is not installed. Install this package with: pip install ."
        ) from exc

    with DDGS() as ddgs:
        if args.type == "text":
            results = list(
                ddgs.text(
                    args.query,
                    region=args.region,
                    safesearch=args.safesearch,
                    timelimit=args.timelimit,
                    max_results=args.max_results,
                )
            )
        elif args.type == "news":
            results = list(
                ddgs.news(
                    args.query,
                    region=args.region,
                    safesearch=args.safesearch,
                    timelimit=args.timelimit,
                    max_results=args.max_results,
                )
            )
        elif args.type == "images":
            results = list(
                ddgs.images(
                    args.query,
                    region=args.region,
                    safesearch=args.safesearch,
                    max_results=args.max_results,
                )
            )
        elif args.type == "videos":
            results = list(
                ddgs.videos(
                    args.query,
                    region=args.region,
                    safesearch=args.safesearch,
                    timelimit=args.timelimit,
                    max_results=args.max_results,
                )
            )
        else:
            results = []

    if args.text:
        for i, row in enumerate(results, 1):
            title = row.get("title") or row.get("source") or "(no title)"
            url = row.get("href") or row.get("url") or row.get("content") or row.get("image") or ""
            body = row.get("body") or row.get("excerpt") or ""
            print(f"{i}. {title}")
            if url:
                print(f"   {url}")
            if body:
                print(f"   {body[:220]}")
            print()
        return 0

    print(json.dumps(results, indent=2, ensure_ascii=False))
    return 0


def cmd_help(args: argparse.Namespace) -> int:
    payload = {
        "tool": "ddg-search",
        "purpose": "DuckDuckGo search wrapper for fallback web search and secondary-source checking.",
        "defaults": {
            "type": "text",
            "max_results": 5,
            "region": "wt-wt",
            "safesearch": "moderate",
            "output": "json",
        },
        "notes": [
            "JSON is the default output so agents can parse results directly.",
            "Use --text when a readable terminal view is better than JSON.",
            "This wrapper is intentionally small and focused.",
            "Use it as a fallback or second search source, not as heavy browser automation.",
        ],
        "commands": {
            "search": "Run DuckDuckGo search. Supports text, news, images, and videos.",
            "help": "Show this command summary.",
        },
        "examples": [
            "ddg-search search 'openclaw github'",
            "ddg-search search 'bitcoin etf' --type news --timelimit d --max-results 10",
            "ddg-search search 'bitcoin logo' --type images --max-results 10",
            "ddg-search search 'openai launch' --type videos --timelimit w --max-results 10",
            "ddg-search search 'site:docs.openclaw.ai browser' --text",
        ],
    }
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Small DuckDuckGo search CLI with JSON output by default."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    search = sub.add_parser("search", help="Run DuckDuckGo search")
    search.add_argument("query", help="Search query")
    search.add_argument("--type", choices=["text", "news", "images", "videos"], default="text")
    search.add_argument("--max-results", type=int, default=5)
    search.add_argument("--region", default="wt-wt")
    search.add_argument("--safesearch", default="moderate")
    search.add_argument("--timelimit", default=None)
    search.add_argument("--text", action="store_true", help="Return readable text output instead of JSON")

    sub.add_parser("help", help="Show a descriptive summary of commands, defaults, and examples")

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        if args.command == "search":
            return run_search(args)
        if args.command == "help":
            return cmd_help(args)
        parser.error("unknown command")
        return 2
    except KeyboardInterrupt:
        eprint("Interrupted")
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
