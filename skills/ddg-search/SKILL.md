---
name: ddg-search
description: Search the web with DuckDuckGo as a no-API-key fallback or second source. Use when the normal web_search tool or primary search provider is rate-limited, failing, unavailable, not delivering enough useful results, or producing weak/inaccurate results, and you want quick text, news, image, or video search results without browser automation.
---

# ddg-search

Use the installed `ddg-search` CLI for lightweight DuckDuckGo search.

This skill exists to make fallback web search simple and low-noise instead of rebuilding ad hoc search helpers each time.

## Quick rules

- Prefer your normal primary search tool when it is healthy.
- Use this skill when you need a fallback or a second source.
- Keep searches narrow and intentional.
- Prefer JSON output by default.
- Use `--text` only when human-readable terminal output is actually more useful.
- Use `references/notes.md` for quick guidance on when this tool fits.

## Installation preference

Prefer an installed CLI over hardcoded script paths.

Preferred install:

```bash
pipx install git+https://github.com/ropl-btc/ddg-search-cli.git
```

Fallback inside a repo checkout:

```bash
pip install .
```

After install, use:

`ddg-search`

## Commands

### Show built-in help

```bash
ddg-search help
```

### Text search

```bash
ddg-search search 'openclaw github'
```

### News search

```bash
ddg-search search 'bitcoin etf' --type news --timelimit d --max-results 10
```

### Image search

```bash
ddg-search search 'bitcoin logo' --type images --max-results 10
```

### Video search

```bash
ddg-search search 'openai launch' --type videos --timelimit w --max-results 10
```

### Human-readable output

```bash
ddg-search search 'site:docs.openclaw.ai browser' --text
```

## Workflow

1. Read `references/notes.md` if you want quick selection guidance.
2. Ensure the `ddg-search` CLI is installed.
3. Run `search` with the narrowest useful query.
4. Parse JSON output by default.
5. Cross-check with another source when the question is important.

## Expected outputs

The CLI returns JSON by default. Parse it instead of scraping text.

Use `--text` when you want a readable terminal view.

## Files

- Package repo: `https://github.com/ropl-btc/ddg-search-cli`
- Compatibility wrapper: `scripts/ddg_search.py`
- Notes: `references/notes.md`

## When to stop and ask

Stop and ask before:
- turning this into browser automation
- adding scraping-heavy flows
- adding provider-specific hacks that make the wrapper fragile
- changing default behavior from lightweight fallback search to something much broader
