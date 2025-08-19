"""
SuperMarketing Framework
AI-powered marketing automation and optimization for Claude Code
"""

__version__ = "1.0.0"
__author__ = "SuperMarketing Team"
__email__ = "contact@supermarketing.ai"

# Framework components
from . import Core
from . import Commands
from . import Templates

__all__ = [
    "Core",
    "Commands", 
    "Templates",
    "__version__",
]