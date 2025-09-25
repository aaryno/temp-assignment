# M3A2: Pandas Environmental Analysis - Makefile
# GIST 604B - Module 3: Python GIS Containerization
#
# Standard Makefile for pandas data analysis assignment with Docker grading support.
# Provides consistent interface for building, testing, and grading.

# Configuration
DOCKER_IMAGE = m3a2-pandas-grader:latest
ASSIGNMENT_DIR = $(shell pwd)

# Colors for output
GREEN = \033[0;32m
YELLOW = \033[1;33m
RED = \033[0;31m
NC = \033[0m # No Color

.PHONY: help build grade grade-local grade-docker check-docker-image setup test clean

# Default target
help: ## Show this help message
	@echo "$(GREEN)M3A2: Pandas Environmental Analysis - Available Commands$(NC)"
	@echo ""
	@echo "$(YELLOW)Building:$(NC)"
	@echo "  build              Build Docker grading container"
	@echo "  check-docker-image Check if Docker image exists"
	@echo ""
	@echo "$(YELLOW)Grading:$(NC)"
	@echo "  grade              Grade assignment (Docker-based, recommended)"
	@echo "  grade-local        Grade assignment (local Python, for development)"
	@echo "  grade-docker       Grade assignment (explicit Docker call)"
	@echo ""
	@echo "$(YELLOW)Development:$(NC)"
	@echo "  setup              Install local development dependencies"
	@echo "  test               Run unit tests locally"
	@echo "  clean              Clean up generated files and containers"
	@echo ""
	@echo "$(YELLOW)Usage Examples:$(NC)"
	@echo "  make build         # Build grading container"
	@echo "  make grade         # Grade assignment"
	@echo "  make test          # Run tests locally"

# Build Docker grading container
build: ## Build the grading Docker container
	@echo "$(GREEN)Building pandas analysis grading container...$(NC)"
	docker build -f Dockerfile.grading -t $(DOCKER_IMAGE) .
	@echo "$(GREEN)✅ Container built successfully as '$(DOCKER_IMAGE)'$(NC)"

# Grade assignment using Docker (recommended)
grade: check-docker-image ## Grade assignment using Docker container
	@echo "$(GREEN)Grading M3A2 Pandas Environmental Analysis...$(NC)"
	docker run --rm \
		-v "$(ASSIGNMENT_DIR)":/workspace \
		-w /workspace \
		$(DOCKER_IMAGE) \
		python /usr/local/bin/calculate_grade.py --verbose

# Grade assignment locally (for development)
grade-local: ## Grade assignment using local Python
	@echo "$(GREEN)Grading M3A2 locally...$(NC)"
	python scripts/calculate_grade.py --verbose

# Grade assignment using Docker (explicit)
grade-docker: check-docker-image ## Grade assignment using Docker (explicit)
	@echo "$(GREEN)Grading M3A2 using Docker...$(NC)"
	docker run --rm \
		-v "$(ASSIGNMENT_DIR)":/workspace \
		-w /workspace \
		$(DOCKER_IMAGE) \
		python /usr/local/bin/calculate_grade.py --verbose

# Check if Docker image exists
check-docker-image: ## Check if the Docker grading image exists
	@if ! docker image inspect $(DOCKER_IMAGE) >/dev/null 2>&1; then \
		echo "$(RED)❌ Docker image '$(DOCKER_IMAGE)' not found$(NC)"; \
		echo "$(YELLOW)💡 Run 'make build' to create the grading container$(NC)"; \
		exit 1; \
	fi
	@echo "$(GREEN)✅ Docker image '$(DOCKER_IMAGE)' found$(NC)"

# Setup local development environment
setup: ## Install local development dependencies
	@echo "$(GREEN)Setting up local development environment...$(NC)"
	pip install -r requirements.txt
	pip install pytest pytest-json-report
	@echo "$(GREEN)✅ Development environment ready$(NC)"

# Run unit tests locally
test: ## Run unit tests locally
	@echo "$(GREEN)Running pandas analysis tests...$(NC)"
	python -m pytest tests/ -v
	@echo "$(GREEN)✅ Tests completed$(NC)"

# Clean up generated files and containers
clean: ## Clean up generated files and Docker containers
	@echo "$(GREEN)Cleaning up...$(NC)"
	# Remove Python cache
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
	# Remove test artifacts
	rm -f grade-report.json
	rm -rf .pytest_cache
	# Remove output files
	rm -rf output/*.csv 2>/dev/null || true
	# Clean Docker (optional - commented out to preserve image)
	# docker rmi $(DOCKER_IMAGE) 2>/dev/null || true
	@echo "$(GREEN)✅ Cleanup completed$(NC)"

# Sample grading target (for samples directory)
grade-sample: check-docker-image ## Grade sample submission (for samples directory)
	@echo "$(GREEN)Grading sample submission...$(NC)"
	docker run --rm \
		-v "$(ASSIGNMENT_DIR)":/workspace \
		-w /workspace \
		$(DOCKER_IMAGE) \
		python /usr/local/bin/calculate_grade.py --verbose
