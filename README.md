# Python Pandas for GIS Data Analysis

**GIST 604B - Open Source GIS Programming**  
**Module 3: Python GIS Containerization**  
**Points: 15 | Due: One week from assignment date**

---

## 🎯 Assignment Overview

Learn the **essential pandas skills** you need for GIS data analysis! This assignment teaches you how to work with tabular data (like CSV files) using Python's most popular data analysis library.

**What you'll learn:**
- **Core Pandas Skills**: Load, explore, filter, and analyze CSV data for GIS applications
- **Advanced Data Operations**: Multi-condition filtering, data validation, time series analysis
- **Professional Python Concepts**: List comprehensions, boolean indexing, lambda functions
- **AI-Assisted Programming**: Using GitHub Copilot's ask, agent, and edit modes effectively
- **Library Understanding**: How to use AI to understand pandas documentation and methods
- **Quality Assurance**: Data validation, error handling, and professional testing with pytest
- **Reflection Practice**: Critical evaluation of AI assistance and learning outcomes

**🎓 AI-Enhanced Learning Approach:**
This assignment uses **interactive Jupyter notebooks** to teach you each function step-by-step, then you implement the actual code in Python files for grading. **GitHub Copilot Pro** is integrated to help with syntax and implementation, while you focus on mastering GIS concepts and analysis decisions. This mirrors real-world professional workflows where developers use AI assistance for efficient coding while applying domain expertise.

**Time commitment:** About 4-5 hours total (includes AI learning, notebook work, implementation, and reflection)

---

## 📋 Prerequisites and Verification

### Module Prerequisites ✅
**Before starting this pandas programming assignment, you must have:**
- [ ] **Completed Foundation Modules:**
  - [ ] **Module 1**: Open Source Discovery and Git Workflows (understanding of version control and open source philosophy)
  - [ ] **Module 2**: QGIS Desktop GIS (M2A1 & M2A2 - spatial data concepts, desktop GIS workflows)
  - [ ] **Module 3, Assignment 1**: Jupyter Primer (M3A1 - containerization and development environment setup)
- [ ] **Module 3 Learning Notes (minimum):**
  - [ ] Python GIS Ecosystem Overview (context for pandas in spatial workflows)
  - [ ] Python Package Managers and Environment Management (uv, pip, dependencies)
  - [ ] Python Pandas for Data Science (essential conceptual foundation)

### Programming Prerequisites ✅
**Python Foundation (First Programming Assignment):**
- [ ] **No prior Python experience required** - this is your programming introduction
- [ ] **Logical thinking** - ability to break problems into sequential steps
- [ ] **Basic computer skills** - file management, text editing, command line comfort
- [ ] **Mathematical concepts** - basic statistics, filtering, and data relationships

### Knowledge Prerequisites ✅
**Data Analysis Concepts:**
- [ ] **Tabular data understanding** - rows, columns, relationships (from spreadsheets/QGIS)
- [ ] **Data types** - numbers, text, dates, and missing data concepts
- [ ] **Filtering and selection** - logical conditions and data subsetting
- [ ] **Statistical thinking** - means, counts, grouping, and summary statistics
- [ ] **File formats** - CSV, Excel, and data interchange formats

### Technical Prerequisites ✅
**Development Environment:**
- [ ] **GitHub Codespaces** (strongly recommended) - Python environment pre-configured
  - [ ] OR **Local Python setup** - Python 3.8+, pandas, jupyter installed and working
- [ ] **Jupyter Notebooks** - comfortable with notebook interface and cell execution
- [ ] **Command line basics** - can navigate directories and run Python commands
- [ ] **Text editor proficiency** - can edit Python files (.py) effectively

### Data Prerequisites ✅
**GIS Data Experience (from previous modules):**
- [ ] **Attribute tables** - experience with tabular data from QGIS
- [ ] **Spatial concepts** - coordinates, projections, and spatial relationships
- [ ] **Data quality** - understanding of missing data, errors, and validation
- [ ] **Export/import workflows** - saving data from GIS software for analysis

### ⚠️ Critical Learning Foundation
**Why this assignment is foundational for Module 3 and beyond:**
- **Data manipulation skills** - essential for all subsequent Python GIS assignments (M3A3, M3A4)
- **Python syntax introduction** - establishes programming concepts for GeoPandas and Rasterio
- **Testing methodology** - introduces pytest for professional development practices  
- **Development workflow** - establishes notebook → code → testing pattern used throughout Module 3
- **AI-assisted learning** - develops skills for strategic AI usage in complex spatial programming

**Sequential dependency for later assignments:**
- **GeoPandas assignment** - builds directly on pandas data manipulation skills
- **Rasterio assignment** - uses pandas for attribute data associated with raster analysis
- **Spatial analysis workflows** - combines pandas with spatial libraries for complex analysis

---

## 🚀 Getting Started

### Step 1: Accept Assignment via GitHub Classroom
🎯 **IMPORTANT:** This assignment begins with accepting it through GitHub Classroom, which creates your personal GitHub repository.

1. **Accept the Assignment**
   - Click the GitHub Classroom link provided by your instructor
   - This creates your personal repository: `ua-gist604b-f25/{your-username}/2-pandas`

2. **Open in GitHub Codespaces**
   - Click the green "Code" button in your repository
   - Select "Codespaces" → "Create codespace on main"
   - Wait for the development environment to load
   - **🤖 GitHub Copilot Pro** will be automatically available for assistance

### Step 2: Verify Your Development Environment

**🪟 Windows Users: Use GitHub Codespaces (STRONGLY Recommended)**
- ✅ **No setup required** - everything works immediately
- ✅ **No Windows compatibility issues** - Unix environment provided
- ✅ **No conda/pip problems** - pre-configured pandas environment
- ✅ **Focus on learning** - not troubleshooting installation issues
- ✅ **Same environment as instructor** - guaranteed compatibility

```bash
# For Windows users (and everyone else):
# 1. Go to your assignment repository on GitHub
# 2. Click "Code" → "Create codespace on main"  
# 3. Wait 2-3 minutes for automatic setup
# 4. Start coding immediately!
```

**🐧🍎 Mac/Linux Users: Choose Your Preference**

**Option A: GitHub Codespaces (Recommended for All)**
```bash
# Click "Code" → "Create codespace on main"
# Pandas environment will be pre-configured and ready!
```

**Option B: Local Development (Mac/Linux Only - Windows at your own risk)**
```bash
# Clone your repository
git clone https://github.com/your-org/your-assignment-repo.git
cd your-assignment-repo

# Install uv (modern Python package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Sync dependencies (this creates a virtual environment automatically)
uv sync --group test --group dev

# Activate the virtual environment (optional - uv run handles this automatically)
source .venv/bin/activate
```

### Step 3: Verify Your Environment

**In Codespaces or Local Setup:**
```bash
# Test that pandas and pytest are working with uv
uv run python -c "import pandas as pd; print(f'Pandas {pd.__version__} ready!')"
uv run python -c "import pytest; print(f'pytest {pytest.__version__} ready!')"

# You should see both libraries working!
# Note: uv automatically manages the virtual environment
```

---

## 📁 Understanding Your Assignment Files

```
python-pandas/
├── README.md                     # This file - your instructions
├── src/
│   └── pandas_basics.py          # 👈 YOUR CODE GOES HERE (5 functions to complete)
├── tests/
│   └── test_pandas_basics.py     # 🧪 Unit tests - learn professional testing!
├── data/
│   ├── weather_stations.csv      # Station location data
│   ├── temperature_readings.csv  # Daily temperature measurements
│   └── data_dictionary.md        # Explains what each column means
├── pytest.ini                    # Test configuration  
├── pyproject.toml                # Modern Python project configuration (replaces requirements.txt)
├── uv.lock                       # Locked dependency versions for reproducible builds
├── requirements.txt              # Legacy dependency file (kept for compatibility)
└── .github/workflows/            # 🤖 Automated grading (CI/CD)
```

---

## 🤖 AI-Enhanced Learning with GitHub Copilot

### **Core Learning Objectives: Understanding Python & Pandas Through AI**

This assignment focuses on using GitHub Copilot as a **learning tool** to understand:
- **Python fundamentals**: List comprehensions, boolean indexing, lambda functions
- **Pandas library**: DataFrames, filtering methods, aggregation functions, joins
- **Professional programming**: Error handling, testing, code organization
- **GIS data patterns**: Spatial data structures, coordinate validation, quality assessment

### **GitHub Copilot Modes: Three Ways to Learn**

#### **🎯 Mode 1: ASK Mode (Copilot Chat)**
**Purpose**: Understanding concepts and getting explanations  
**How to Use**: Press `Ctrl+Shift+I` (or `Cmd+Shift+I`) to open Copilot Chat

**Practice Questions:**
- "Explain how pandas DataFrame.groupby() works with examples"
- "What's the difference between .loc and .iloc in pandas?"
- "Show me different ways to filter a DataFrame with multiple conditions"
- "How does boolean indexing work in pandas?"

#### **🔧 Mode 2: AGENT Mode (Inline Suggestions)**  
**Purpose**: Code completion and implementation assistance  
**How to Use**: Type comments or start code, accept/reject suggestions with Tab/Esc

**Practice Patterns:**
```python
# filter dataframe where temperature > 20 and quality == 'good'
# → Let Copilot suggest implementation

# group by station and calculate mean temperature  
# → See multiple implementation options

# create list comprehension to extract station IDs
# → Learn list comprehension syntax
```

#### **✏️ Mode 3: EDIT Mode (Code Modification)**
**Purpose**: Refactoring and improving existing code  
**How to Use**: Select code, right-click → "Copilot" → "Start Inline Chat" or use `Ctrl+I`

**Practice Scenarios:**
- Select a basic loop → Ask "Convert this to a list comprehension"
- Select filtering code → Ask "Make this more efficient using pandas methods"
- Select error-prone code → Ask "Add error handling and validation"

### **Learning Requirements (Not Just Coding!)**

**✅ For Each Function You Must:**
1. **Use all three Copilot modes** (ask, agent, edit) and document which you used
2. **Understand the underlying concepts** - explain what pandas methods do and why
3. **Learn Python patterns** - identify list comprehensions, boolean indexing, lambda functions
4. **Apply GIS reasoning** - make decisions about thresholds, data quality, and analysis approach

**🧠 Critical Thinking Required:**
- **AI can suggest syntax** → YOU decide the analysis approach  
- **AI can explain methods** → YOU choose which methods fit your GIS problem
- **AI can generate code** → YOU validate results and understand the logic
- **AI can fix errors** → YOU learn from the fixes for future problems

### **📝 Reflection Component (Required Deliverable)**
You must complete a **written reflection** (500+ words, written by YOU, not AI) addressing:

1. **AI Mode Usage**: How did ask, agent, and edit modes help you learn differently?
2. **Concept Learning**: What Python/pandas concepts did you learn through AI assistance?
3. **Problem Solving**: How did AI help you understand GIS data analysis challenges?
4. **Code Quality**: How did AI suggestions improve your code structure and efficiency?
5. **Learning Process**: What surprised you about learning programming with AI assistance?

**📎 Reflection File**: Create `AI_LEARNING_REFLECTION.md` in your repository root.

---

## 📝 Your Assignment Tasks

You need to implement **8 functions** in the file `src/pandas_basics.py`. Each function has a corresponding Jupyter notebook in the `notebooks/` directory that teaches you how to build it step by step.

**📊 Point Distribution (15 total points):**
- **Core Functions** (10 points): Essential pandas operations and GIS data handling
- **Advanced Functions** (3 points): Complex analysis, validation, and multi-dataset operations  
- **AI Learning Reflection** (2 points): Written reflection on AI-assisted learning process

**📚 Learning Process:**
1. **Learn**: Open the notebook for each function to understand how it works
2. **Practice AI Modes**: Use Copilot's ask, agent, and edit modes during implementation
3. **Implement**: Write your code in `src/pandas_basics.py` (replace the TODO comments)
4. **Test**: Run pytest to verify your implementation works correctly
5. **Reflect**: Complete the AI learning reflection (500+ words)
6. **Submit**: Push your completed assignment to GitHub

---

## 🎯 Function Implementation Tasks

### **Core Functions (10 points total)**

#### **1. `load_and_explore_gis_data()` (2 points)**
- Load CSV files and explore dataset structure
- Practice basic pandas DataFrames and exploration methods
- **AI Learning**: Use agent mode for basic pandas syntax

#### **2. `filter_environmental_data()` (2 points)**  
- Filter data based on temperature and quality criteria
- Learn boolean indexing in pandas
- **AI Learning**: Ask mode to understand filtering concepts

#### **3. `calculate_station_statistics()` (2 points)**
- Calculate aggregated statistics using groupby
- Practice pandas aggregation functions
- **AI Learning**: Edit mode to optimize statistical calculations

#### **4. `join_station_data()` (2 points)**
- Merge station locations with measurement data
- Understand pandas join operations
- **AI Learning**: Agent mode for join syntax, ask mode for join concepts

#### **5. `save_processed_data()` (2 points)**
- Export processed data to CSV format
- Handle file I/O and data export
- **AI Learning**: Edit mode to add error handling

### **Advanced Functions (3 points total)**

#### **6. `validate_coordinate_data()` (1 point)**
- Comprehensive coordinate validation and quality assessment
- Advanced boolean indexing and data quality techniques
- **AI Learning**: All three modes for complex validation logic

#### **7. `multi_condition_filtering()` (1 point)**
- Complex filtering with multiple criteria and logical operations
- Advanced pandas query methods and lambda functions  
- **AI Learning**: Edit mode to optimize filtering performance

#### **8. `analyze_temporal_patterns()` (1 point)**
- Time series analysis with pandas datetime functionality
- Rolling averages, resampling, and temporal aggregation
- **AI Learning**: Ask mode for time series concepts

### **Learning Reflection (2 points)**
- Complete `AI_LEARNING_REFLECTION.md` with 500+ words
- Reflect on using ask, agent, and edit modes
- Document learning outcomes and surprises
- **Must be written by you, not AI**

**🎯 Implementation Strategy:** Each function has a corresponding Jupyter notebook to teach concepts step-by-step. You implement working code in `src/pandas_basics.py` for automated grading. Use AI strategically to understand difficult concepts while ensuring you can explain every line of your code.

## 🧠 **CORE FUNCTIONS (10 points)**

### **1. `load_and_explore_gis_data()` (2 points)**
📚 **Learning Notebook:** `notebooks/01_function_load_and_explore_gis_data.ipynb`  
🤖 **AI Usage**: Use agent mode for pandas syntax assistance

**Core Requirements:**
- Load CSV files with comprehensive error handling and validation
- Display dataset structure, shape, data types, and basic statistics
- Perform initial data quality assessment with missing value analysis
- Return loaded DataFrame for further processing

**Test Command:**
```bash
uv run pytest tests/test_pandas_basics.py::test_load_and_explore_gis_data -v
```

### **2. `filter_environmental_data()` (2 points)**
📚 **Learning Notebook:** `notebooks/02_function_filter_environmental_data.ipynb`  
🤖 **AI Usage**: Ask mode to understand filtering concepts

**Core Requirements:**
- Filter data using boolean indexing with temperature and quality criteria
- Handle multiple filtering conditions with performance optimization
- Provide comprehensive filtering statistics and data loss analysis
- Return filtered DataFrame with detailed validation and reporting

**Test Command:**
```bash
uv run pytest tests/test_pandas_basics.py::test_filter_environmental_data -v
```

### **3. `calculate_station_statistics()` (2 points)**
📚 **Learning Notebook:** `notebooks/03_function_calculate_station_statistics.ipynb`  
🤖 **AI Usage**: Edit mode for statistical calculation optimization

**Core Requirements:**
- Group data by station using sophisticated `.groupby()` operations
- Calculate comprehensive station-level statistics with outlier detection
- Identify statistical outliers, extreme values, and data quality patterns
- Return formatted statistics DataFrame with professional-grade analysis

**Test Command:**
```bash
uv run pytest tests/test_pandas_basics.py::test_calculate_station_statistics -v
```

### **4. `join_station_data()` (2 points)**
📚 **Learning Notebook:** `notebooks/04_function_join_station_data.ipynb`  
🤖 **AI Usage**: Agent mode for join syntax, ask mode for join strategy concepts

**Core Requirements:**
- Perform sophisticated spatial joins using advanced `pd.merge()` techniques
- Handle multiple join scenarios, edge cases, and data validation
- Implement join result validation with comprehensive error checking
- Return enriched dataset with spatial attributes and join quality metrics

**Test Command:**
```bash
uv run pytest tests/test_pandas_basics.py::test_join_station_data -v
```

### **5. `save_processed_data()` (2 points)**
📚 **Learning Notebook:** `notebooks/05_function_save_processed_data.ipynb`  
🤖 **AI Usage**: Edit mode for error handling and optimization

**Core Requirements:**
- Export processed data with multiple format options and validation
- Handle file path validation, error recovery, and data integrity checks
- Generate export summaries, metadata, and data quality reports
- Ensure robust error handling with comprehensive user feedback

**Test Command:**
```bash
uv run pytest tests/test_pandas_basics.py::test_save_processed_data -v
```

## 🚀 **ADVANCED FUNCTIONS (3 points)**

### **6. `validate_coordinate_data()` (1 point)**  
📚 **Learning Notebook:** `notebooks/06_function_validate_coordinate_data.ipynb`  
🤖 **AI Usage**: Ask mode to understand coordinate validation concepts, agent mode for boolean operations

**Advanced Requirements:**
- Comprehensive coordinate validation for latitude/longitude data
- Check for missing values, invalid ranges, and precision issues  
- Generate quality scores and specific improvement recommendations
- Return detailed validation results dictionary with actionable insights

**Test Command:**
```bash
uv run pytest tests/test_pandas_basics.py::test_validate_coordinate_data -v
```

### **7. `multi_condition_filtering()` (1 point)**
📚 **Learning Notebook:** `notebooks/07_function_multi_condition_filtering.ipynb`  
🤖 **AI Usage**: Agent mode for complex filtering logic, edit mode for optimization

**Advanced Requirements:**
- Apply sophisticated filtering with multiple criteria and logical operations
- Support distance-based, attribute-based, and temporal filtering
- Use pandas `.query()` method and advanced boolean indexing techniques
- Return filtered DataFrame with comprehensive filtering statistics

**Test Command:**
```bash
uv run pytest tests/test_pandas_basics.py::test_multi_condition_filtering -v
```

### **8. `analyze_temporal_patterns()` (1 point)**
📚 **Learning Notebook:** `notebooks/08_function_analyze_temporal_patterns.ipynb`  
🤖 **AI Usage**: Ask mode for time series concepts, agent mode for datetime operations

**Advanced Requirements:**
- Comprehensive temporal pattern analysis in environmental data
- Calculate rolling averages, seasonal trends, and data completeness metrics
- Identify temporal gaps, irregular intervals, and trend analysis
- Return detailed temporal analysis results with forecasting insights

**Test Command:**
```bash
uv run pytest tests/test_pandas_basics.py::test_analyze_temporal_patterns -v
```

## 📝 **AI LEARNING REFLECTION (2 points)**

### **9. AI Learning Reflection Document (2 points)**
📎 **Template:** Use `AI_LEARNING_REFLECTION_TEMPLATE.md`  
🤖 **AI Usage**: Written entirely by you, NO AI assistance allowed

**Critical Requirements:**
- **Minimum 500 words** written independently by you (not AI-generated)
- Comprehensive reflection on ask, agent, and edit mode usage effectiveness
- Document specific Python/pandas concepts mastered through AI assistance
- Analyze how AI improved your problem-solving approach and learning efficiency
- Provide critical evaluation of AI assistance benefits and limitations

**Key Reflection Topics:**
1. **AI Mode Comparison**: How ask, agent, and edit modes helped you learn differently
2. **Concept Mastery**: Python/pandas techniques you learned through AI explanations  
3. **Problem-Solving Evolution**: How AI changed your approach to complex data problems
4. **Code Quality Improvements**: Ways AI suggestions enhanced your implementation
5. **Learning Surprises**: Unexpected benefits or limitations in AI-assisted learning

**Deliverable:** Create `AI_LEARNING_REFLECTION.md` in your repository root directory.

---

## 🧪 Professional Development Workflow

**Important Learning Objective**: This assignment teaches you professional development practices including unit testing and the notebook-to-code workflow used in industry.

### Step 1: Learning with Notebooks

```bash
# Navigate to the notebooks directory
cd notebooks/

# Open Jupyter in your browser (if using local setup)
uv run jupyter notebook

# In Codespaces, notebooks open directly in VS Code
```

**Work through notebooks in order:**
1. `01_function_load_and_explore_gis_data.ipynb`
2. `02_function_validate_coordinate_data.ipynb`  
3. `03_function_multi_condition_filtering.ipynb`
4. `04_function_analyze_temporal_patterns.ipynb`
5. `05_function_filter_environmental_data.ipynb`
6. `06_function_calculate_station_statistics.ipynb`
7. `07_function_join_station_data.ipynb`
8. `08_function_save_processed_data.ipynb`

### Step 2: Implement Functions

After learning from each notebook:
1. Open `src/pandas_basics.py`
2. Find the corresponding function
3. Replace TODO comments with your implementation
4. Test immediately (see Step 3)

### Step 3: Test-Driven Development

**Professional developers test as they code!** Test each function individually:

```bash
# Test a specific function
uv run pytest tests/test_pandas_basics.py::test_load_and_explore_gis_data -v

# Test all functions
uv run pytest tests/ -v

# Get detailed output when tests fail
uv run pytest tests/ -v -s
```

### Step 4: Debug and Iterate

When tests fail, the error messages tell you exactly what's wrong:

```bash
# Example of what you might see:
FAILED tests/test_pandas_basics.py::test_filter_environmental_data 
AssertionError: Expected DataFrame with 45 rows, got 0 rows
```

This tells you your filtering isn't working correctly - go back to the notebook to review!

### Step 5: Final Validation

When all functions work:

```bash
# Verify everything passes
uv run pytest tests/ -v

# You should see all PASSED
# Then commit and push your code
git add .
git commit -m "Complete pandas assignment - all functions implemented"
git push origin main
```

**🤖 Automated Grading:** GitHub Actions runs the same tests automatically and calculates your grade!

---

## 📊 Sample Data Provided

### `weather_stations.csv`
Information about 15 environmental monitoring stations in New York City:
- `station_id` - Unique identifier (STN_001, STN_002, etc.)
- `station_name` - Human-readable name
- `latitude`, `longitude` - Location coordinates  
- `elevation_m` - Height above sea level
- `station_type` - Type of monitoring equipment

### `temperature_readings.csv`
95 daily temperature measurements from the stations:
- `station_id` - Links to station information
- `date` - When measurement was taken (Jan 15-21, 2023)
- `temperature_c` - Air temperature in Celsius
- `humidity_percent` - Relative humidity
- `data_quality` - Quality flag ("good", "fair", "poor")

**💡 Tip:** Read `data/data_dictionary.md` for detailed information about the datasets!

---

## 📚 Learning Resources

### Pandas Basics
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html) - Quick tutorial
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf) - Reference guide

### Key Functions You'll Use
```python
# Load data
df = pd.read_csv('filename.csv')

# Explore data
df.head()        # Show first 5 rows
df.info()        # Show column info
df.describe()    # Summary statistics

# Filter rows
filtered = df[df['column'] > value]
filtered = df[(df['temp'] > 15) & (df['quality'] == 'good')]

# Group and calculate
stats = df.groupby('station_id')['temperature'].mean()

# Join dataframes  
combined = pd.merge(df1, df2, on='common_column')

# Save results
df.to_csv('output.csv', index=False)
```

---

## 🛠️ Troubleshooting

### Common Issues and Solutions

**"FileNotFoundError: No such file or directory"**
- Make sure you're in the assignment directory
- Check that data files are in the `data/` folder
- Use `pwd` to see your current location

**"KeyError: 'column_name'"**  
- Check column names using `df.columns`
- Column names are case-sensitive
- Look for extra spaces in column names

**"Tests are failing but my code looks right"**
- Read the error messages carefully
- Print intermediate results to debug: `print(df.head())`
- Make sure your function returns the right data type
- Check that your filtering conditions are correct

**"Grade script shows 0 points"**
- Run `python test_my_functions.py` first
- Fix any failing tests before running `grade.py`
- Make sure all 5 functions are implemented
- Check that function names are spelled correctly

---

## 📤 Submission Requirements

### What to Submit
1. **Completed code**: All 5 functions working in `src/pandas_basics.py`
2. **Passing tests**: `grade.py` shows 10/10 points
3. **Git commit**: Push your final code to your repository

### Grading Breakdown (10 points total)
- **Function 1** (2 pts): Load and explore data correctly
- **Function 2** (2 pts): Filter data with proper conditions  
- **Function 3** (2 pts): Calculate statistics by group
- **Function 4** (2 pts): Join datasets successfully
- **Function 5** (1 pt): Save data correctly
- **Code Quality** (1 pt): Clean, readable code with comments

### Success Checklist
- [ ] All functions implemented in `src/pandas_basics.py`
- [ ] `pytest tests/` shows all tests passing locally
- [ ] GitHub Actions shows green checkmark (automated tests pass)
- [ ] Code is clean and well-commented
- [ ] You understand how unit testing works
- [ ] Final commit pushed to GitHub

---

## 🎓 Why This Matters for GIS

**Real-world applications:**

🌡️ **Environmental Monitoring:** Process sensor data, filter for quality, calculate station averages

🏙️ **Urban Planning:** Combine census data with boundaries, analyze demographics by region

🌊 **Hydrology:** Join stream gauge data with station locations, identify flow patterns

🌱 **Agriculture:** Process crop yield data, correlate with weather and soil conditions

📊 **Data Preparation:** Clean and prepare tabular data before importing into QGIS

**Next steps:** These pandas skills will be essential for upcoming **GeoPandas** assignments where you'll work with spatial data directly!

---

## 🆘 Getting Help

1. **Read pytest error messages** - they show exactly which assertions failed
2. **Run individual tests** - `pytest tests/test_pandas_basics.py::test_function_name -v`
3. **Use print statements** - debug your code by printing intermediate results  
4. **Check the test file** - understand what the tests expect your functions to do
5. **Run tests frequently** - catch errors early with `pytest tests/`
6. **Use pytest debugging** - `pytest tests/ --pdb` drops you into Python debugger
7. **Ask on the course forum** - post specific test failure messages for help
8. **Attend office hours** - get help understanding unit testing concepts

---

**Remember:** Take your time to understand each function before moving to the next one. The step-by-step approach will make you successful! 🚀

**Good luck!**