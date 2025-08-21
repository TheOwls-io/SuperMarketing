"""
SuperMarketing Framework
AI-powered marketing automation and optimization for Claude Code
"""

__version__ = "1.0.0"
__author__ = "The Owls"
__email__ = "contact@theowls.io"
__url__ = "https://github.com/TheOwls-io/SuperMarketing"

# Framework metadata
FRAMEWORK_NAME = "SuperMarketing"
FRAMEWORK_VERSION = __version__
COMMAND_PREFIX = "/sm:"
INSTALL_DIR = "~/.claude/SuperMarketing"

# Available components (as strings, not imports)
COMPONENTS = [
    'Core',
    'Commands',
    'BrandContext',
    'Templates'
]

# Marketing personas
PERSONAS = [
    'strategist',
    'copywriter',
    'creative',
    'content',
    'analyst',
    'growth',
    'seo',
    'social',
    'email',
    'paid',
    'brand'
]

# Marketing commands
COMMANDS = [
    'campaign',
    'strategy',
    'research',
    'create',
    'optimize',
    'personalize',
    'analyze',
    'measure',
    'report',
    'forecast',
    'test',
    'workflow',
    'calendar',
    'brief',
    'collaborate',
    'launch',
    'audit',
    'brand'
]

__all__ = [
    "__version__",
    "FRAMEWORK_NAME",
    "FRAMEWORK_VERSION",
    "COMMAND_PREFIX",
    "INSTALL_DIR",
    "COMPONENTS",
    "PERSONAS",
    "COMMANDS"
]