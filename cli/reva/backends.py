"""Backend definitions: command templates and system-prompt filenames per backend."""

from dataclasses import dataclass

# Paper Lantern MCP server config, inlined into the claude-code command template.
# The JSON is wrapped in single quotes at the shell level so its internal double
# quotes pass through unchanged; `\'` escapes the single quotes inside the Python
# string. Braces are doubled ({{ / }}) so that reva's str.format() call in
# cli.py (which substitutes {prompt} for other backends) does not interpret them
# as format fields — the doubling collapses back to single braces at format time.
_PAPER_LANTERN_MCP_CONFIG = (
    '\'{{"mcpServers":{{"paperlantern":'
    '{{"type":"http","url":"https://mcp.paperlantern.ai/chat/mcp?key=pl_cd1099cd5b35f6c193f9"}}'
    '}}}}\''
)


@dataclass(frozen=True)
class Backend:
    name: str
    prompt_filename: str  # backend-specific system prompt file (e.g. CLAUDE.md)
    command_template: str  # shell command; {prompt} is replaced with initial prompt


BACKENDS: dict[str, Backend] = {
    "claude-code": Backend(
        name="claude-code",
        prompt_filename="CLAUDE.md",
        command_template=(
            'claude -p "$(cat initial_prompt.txt)"'
            " --dangerously-skip-permissions"
            " --output-format stream-json --verbose"
            f" --mcp-config {_PAPER_LANTERN_MCP_CONFIG}"
            " 2>&1 | tee -a agent.log"
        ),
    ),
    "gemini-cli": Backend(
        name="gemini-cli",
        prompt_filename="GEMINI.md",
        command_template='gemini --yolo --prompt "{prompt}"',
    ),
    "codex": Backend(
        name="codex",
        prompt_filename="AGENTS.md",
        command_template='codex --dangerously-bypass-approvals-and-sandbox "{prompt}"',
    ),
    "aider": Backend(
        name="aider",
        prompt_filename="AIDER.md",
        command_template='aider --yes --message "{prompt}"',
    ),
    "opencode": Backend(
        name="opencode",
        prompt_filename="OPENCODE.md",
        command_template='opencode run --dangerously-skip-permissions "{prompt}"',
    ),
}

BACKEND_CHOICES = list(BACKENDS.keys())


def get_backend(name: str) -> Backend:
    if name not in BACKENDS:
        raise ValueError(f"Unknown backend: {name!r}. Choose from: {BACKEND_CHOICES}")
    return BACKENDS[name]
