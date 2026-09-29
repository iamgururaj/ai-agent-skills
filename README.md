# Agent skills

Reusable skills maintained by Gururaj.

| Skill | Purpose |
| --- | --- |
| [focused](skills/focused/SKILL.md) | Actionable, calm responses with small steps and visible progress. |

## Install

After these files are published to the public GitHub repository:

```sh
npx skills add iamgururaj/ai-agent-skills --skill focused
```

To try the local checkout first, run from this repository:

```sh
npx skills add . --skill focused
```

Ask your agent: `Use focused for this session. Help me work through this task.`
Say `stop focused mode` or `normal mode` to stop. Selection and session retention
depend on the host; the skill does not install persistence hooks.

## Validate and publish

1. Add or edit `skills/<name>/SKILL.md`, with YAML `name` and `description` fields.
2. Run the checks below and review realistic behavior using the [evaluation guide](evals/focused.md).
3. Commit and push the reviewed changes to the public repository's default branch. GitHub Actions validates pushes and pull requests; configure branch protection to require the `validate` job if desired.
4. Verify remote discovery with `npx skills add iamgururaj/ai-agent-skills --list`, then install using the command above.
5. Share the install command. [skills.sh documents automatic listing through CLI installation telemetry](https://skills.sh/docs/faq); listing timing and ranking are not guaranteed.

Run validation from the repository folder. If you have `uv`, this is the recommended
option; it supplies PyYAML in an isolated environment without a separate install
or environment activation step:

```sh
uv run --with "PyYAML>=6.0.2,<7" scripts/validate_skills.py
```

Alternatively, use Python and pip:

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate_skills.py
```

The validator checks skill metadata, required content, and local documentation
links. It does not test model behavior. Python is only needed for this optional
check, not to install or use the skill. GitHub Actions runs the same validator
with pip regardless of which option you use locally.

No separate package upload or skills.sh submission is required. Repeat the review,
validation, and push process for updates. Users can run `npx skills update` to
retrieve updates. See the [official CLI documentation](https://github.com/vercel-labs/skills).

## License

See the [skill license](skills/focused/LICENSE) and the repository's
[MIT license](LICENSE).
