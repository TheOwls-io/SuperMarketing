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

# Framework components
from . import Core
from . import Commands
from . import Templates

__all__ = [
    "Core",
    "Commands", 
    "Templates",
    "__version__",
    "FRAMEWORK_NAME",
    "COMMAND_PREFIX",
]