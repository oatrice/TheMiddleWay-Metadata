
import sys
import os
import json

# Add path to Luma
sys.path.insert(0, "/Users/oatrice/Software-projects/Luma")

# Mock simple-term-menu just in case actions.py uses it inside
# Wait, actions.py uses simple-term-menu inside interactive functions?
# action_guided_workflow calls interactive functions like action_refine_issue
from luma_core.state_manager import load_state, save_state
from luma_core.config import PROJECTS
import luma_core.actions as actions

def run_workflow():
    project_key = "6"
    project = PROJECTS[project_key]
    
    # Load state
    state_path = project["path"]
    state = load_state(state_path)
    state.project_key = project_key
    
    print(f"🚀 Starting Guided Workflow for Issue #{state.active_issue.number}")
    
    # Run the workflow action
    # This will still be interactive in terms of prompts, but bypasses the menu
    actions.action_guided_workflow(state, project)
    
    # Save state
    save_state(state, state_path)

if __name__ == "__main__":
    run_workflow()
