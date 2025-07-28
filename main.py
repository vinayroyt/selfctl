import json
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Dict, Any

app = FastAPI(title="My MCP Server")

# Load static data at startup
with open("data/profile.json") as f:
    PROFILE = json.load(f)

with open("data/manifest.json") as f:
    MANIFEST = json.load(f)

with open("data/preferences.json") as f:
    PREFERENCES = json.load(f)

# MCP API Schemas
class MCPCommand(BaseModel):
    id: str
    command: str
    params: Optional[Dict[str, Any]] = {}

class MCPResponse(BaseModel):
    id: str
    result: Optional[Any] = None
    error: Optional[str] = None
    meta: Optional[Dict[str, Any]] = {}

# State
current_focus = None
memory = []

@app.post("/command", response_model=MCPResponse)
async def handle_command(cmd: MCPCommand):
    global current_focus  # ⬅️ Move this to the top of the function
    try:
        if cmd.command == "whoami":
            return MCPResponse(id=cmd.id, result=PROFILE)

        elif cmd.command == "get_focus":
            return MCPResponse(id=cmd.id, result=current_focus)

        elif cmd.command == "set_focus":
            current_focus = cmd.params.get("topic")
            return MCPResponse(id=cmd.id, result="Focus set.")

        elif cmd.command == "remember":
            memory.append(cmd.params)
            return MCPResponse(id=cmd.id, result="Memory stored.")

        elif cmd.command == "recall":
            return MCPResponse(id=cmd.id, result=memory)

        else:
            return MCPResponse(id=cmd.id, error="Unknown command")

    except Exception as e:
        return MCPResponse(id=cmd.id, error=str(e))

@app.get("/manifest")
async def manifest():
    return MANIFEST

@app.get("/preferences")
async def preferences():
    return PREFERENCES