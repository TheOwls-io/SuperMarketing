"""
SuperMarketing Commands
Marketing automation commands for Claude Code
"""

# Campaign & Strategy Commands
CAMPAIGN_COMMANDS = [
    "campaign",
    "strategy", 
    "research",
]

# Content & Creative Commands
CONTENT_COMMANDS = [
    "create",
    "optimize",
    "personalize",
]

# Analytics & Performance Commands
ANALYTICS_COMMANDS = [
    "analyze",
    "measure",
    "report",
    "forecast",
]

# Testing & Workflow Commands
WORKFLOW_COMMANDS = [
    "test",
    "workflow",
    "calendar",
    "brief",
    "collaborate",
    "launch",
    "audit",
]

ALL_COMMANDS = (
    CAMPAIGN_COMMANDS + 
    CONTENT_COMMANDS + 
    ANALYTICS_COMMANDS + 
    WORKFLOW_COMMANDS
)

__all__ = ["ALL_COMMANDS"]