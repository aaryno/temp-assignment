# 🤖 M3A2 Codespaces Setup & Testing Guide

## ⏱️ Expected Setup Time: **2-3 Minutes**

When you create a Codespace for this repository, the environment setup takes **2-3 minutes** to complete. This is normal and expected behavior.

### What happens during setup:
```bash
pip install uv && uv sync && echo '🤖 M3A2 AI-Enhanced Environment Ready!'
```

**🔧 Project Setup:** The repository includes a `pyproject.toml` with all required dependencies. The `uv sync` command installs everything automatically.

**✅ You'll see:**
- Package installation progress in the terminal
- "Finishing up..." message
- "Running postCreateCommand..." with spinning indicator
- Finally: "🤖 M3A2 AI-Enhanced Environment Ready!"

**⚠️ Important:** Wait for the setup to complete before running any Python commands!

---

## 🧪 Quick Environment Test Commands

### Test Python & Pandas Installation
```bash
# Test uv installation
uv --version

# Test pandas installation (uv is the primary method)
uv run python -c "import pandas as pd; print('Pandas version:', pd.__version__)"

# Test geopandas installation  
uv run python -c "import geopandas as gpd; print('GeoPandas version:', gpd.__version__)"

# Test all core libraries with uv
uv run python -c "
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
print('✅ All libraries loaded successfully!')
print(f'📊 Pandas: {pd.__version__}')
print(f'🔢 NumPy: {np.__version__}')
print('📈 Matplotlib: installed')"

# Test pytest for assignment grading
uv run pytest --version
```

### Test GitHub Copilot Integration
1. **Open any Python file** (e.g., `src/pandas_basics.py`)
2. **Type a comment:** `# Calculate the mean temperature for each station`
3. **Press Tab** to see Copilot suggestions
4. **Try Copilot Chat:** Use `Ctrl+I` (Windows/Linux) or `Cmd+I` (Mac)

---

## 📚 Recommended Testing Workflow

### 1. Start with Overview Notebook
```bash
# Open the main overview notebook
jupyter lab notebooks/00_start_here_overview.ipynb
```

### 2. Test Copilot Modes
- **ASK Mode:** Use Copilot Chat (`Ctrl+I` or `Cmd+I`) to ask questions
- **AGENT Mode:** Let Copilot generate code blocks
- **EDIT Mode:** Use Copilot to modify existing code

### 3. Try Sample Data Analysis
```bash
# Test with sample data using uv
uv run python -c "
import pandas as pd
import numpy as np

# Create sample environmental data
data = {
    'station_id': ['A01', 'A02', 'A03'],
    'temperature': [23.5, 18.2, 25.1],
    'humidity': [65, 72, 58]
}
df = pd.DataFrame(data)
print('Sample data loaded:')
print(df)
print('✅ Pandas working correctly with uv!')
"
```

---

## 🚨 Troubleshooting

### Command Line Issues
**❌ Avoid:** Commands with single quotes + exclamation marks
```bash
# This will fail in bash:
python -c 'print(f"Version {pd.__version__}!")'  # ❌ bash: !': event not found
```

**✅ Use instead:**
```bash
# Double quotes work fine:
python -c "print(f'Version {pd.__version__}!')"

# Or escape the exclamation:
python -c 'print(f"Version {pd.__version__}\!")'
```

### If Packages Aren't Found
```bash
# Install uv first if missing:
pip install uv

# Sync project dependencies (reads from pyproject.toml):
uv sync

# Or manually install if needed:
uv add pandas geopandas numpy matplotlib jupyter pytest

# Verify installation with uv (primary method):
uv run python -c "import pandas; print('✅ Pandas installed')"
```

### GitHub Copilot Not Working?
1. **Check extension is installed:** Look for Copilot icon in VS Code
2. **Sign in to GitHub:** Use Command Palette > "GitHub Copilot: Sign In"
3. **Check settings:** `github.copilot.enable` should be `true`

---

## 🎯 Success Indicators

**✅ Environment is ready when:**
- Python imports pandas, geopandas, numpy without errors
- Jupyter Lab launches successfully (`jupyter lab`)
- GitHub Copilot provides code suggestions when typing
- All 9 notebooks open without import errors

**🚀 You're ready to explore AI-enhanced pandas learning!**
