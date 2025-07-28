# selfctl

`selfctl` is a personal MCP server that exposes your digital self — identity, memory, focus, and tool access — through programmable APIs. Built with FastAPI and powered by Pydantic, it lets tools and agents interact with you like a structured service.

## Features

- Command-style API interface (`/command`)
- Static profile, manifest, and preferences (JSON-based)
- Working memory and focus control
- OpenAPI schema support
- Ready to deploy on Fly.io, Render, etc.

## Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/selfctl.git
cd selfctl
```

### 2. Install Python 3.11 (with pyenv)

```bash
brew install pyenv
pyenv install 3.11.9
pyenv virtualenv 3.11.9 selfctl-env
pyenv local selfctl-env
```

Update your ~/.zshrc (if using zsh):

```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Then reload:

```bash
exec zsh
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the Server

```bash
uvicorn main:app --reload
```
Visit http://127.0.0.1:8000/docs for the Swagger UI.

## Testing the API

### Who Am I?

```bash
curl -X POST http://127.0.0.1:8000/command \
  -H "Content-Type: application/json" \
  -d '{"id": "test1", "command": "whoami"}'
````

Command Manifest

```bash
curl http://127.0.0.1:8000/manifest
```

## Docker (optional)

To run with Docker:

```bash
docker build -t selfctl .
docker run -p 8000:8000 selfctl
```

## Project Structure

selfctl/
├── main.py                  # FastAPI app
├── requirements.txt         # Dependencies
├── Dockerfile               # Container setup
├── README.md                # You are here
├── .python-version          # Pyenv local version
├── data/                    # Externalized profile data
│   ├── profile.json
│   ├── manifest.json
│   └── preferences.json