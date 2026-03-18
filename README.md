# ddg-search-cli

Small DuckDuckGo search CLI for **OpenClaw**, **Claude Code**, and other AI agents that need a simple fallback web search tool without an API key.

This repo gives you two things:
- a small installable CLI: `ddg-search`
- a matching OpenClaw skill in `skills/ddg-search`

## What this is

- a small **DuckDuckGo search CLI** built on `ddgs`
- intentionally minimal and easy to use in scripts, shells, and agent workflows
- a matching **OpenClaw skill** under `skills/ddg-search`
- opinionated defaults for quick fallback web search
- designed to be easy for humans and AI agents to use repeatedly

## What this is not

- not a browser automation tool
- not a scraping framework
- not a full wrapper for every `ddgs` capability
- not meant to replace your primary search provider when that provider is healthy

## Features

- install a real shell command: `ddg-search`
- run text, news, image, and video search
- return JSON by default for agent-friendly parsing
- switch to readable text output with `--text`
- adjust result count, region, safesearch, and time filtering
- work as a no-API-key fallback when another search provider is rate-limited or failing

## Commands

- `help`
- `search`

Run built-in help:

```bash
ddg-search help
```

## Requirements

- Python 3.10+

## Install

### Preferred: pipx

```bash
pipx install git+https://github.com/ropl-btc/ddg-search-cli.git
```

Then run:

```bash
ddg-search help
```

### Fallback: local venv

```bash
git clone https://github.com/ropl-btc/ddg-search-cli.git
cd ddg-search-cli
python3 -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install .
```

Then run:

```bash
ddg-search help
```

### Developer mode

```bash
pip install -e .
```

## Usage examples

### Show help

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

### Set region and safesearch

```bash
ddg-search search 'liquid staking' --region us-en --safesearch off
```

## Output

Default output is JSON.

That is intentional: AI agents should parse structured output instead of scraping plain text.

Use `--text` when you want a readable terminal view.

## OpenClaw / AI-agent usage

This repo includes an OpenClaw skill under:

- `skills/ddg-search/SKILL.md`
- `skills/ddg-search/scripts/ddg_search.py`
- `skills/ddg-search/references/notes.md`

That subfolder is the one to use for skill-specific packaging and publishing.

The main intended interface for end users and agents is still the installed `ddg-search` command.

## Why this exists

Many agent setups already have a primary search provider.

This wrapper exists for the annoying cases where:
- the primary provider is rate-limited
- the primary provider is temporarily failing
- you want a second source to cross-check results
- you want a fast no-key search command inside scripts and agent workflows

## License

MIT
