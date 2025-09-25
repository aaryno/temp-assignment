# M3A2 Sample Grading - References parent Docker image
DOCKER_IMAGE = m3a2-pandas-grader:latest
SAMPLE_DIR = $(shell pwd)

.PHONY: grade-sample check-docker-image

grade-sample: check-docker-image
	@echo "🧪 Grading $(shell basename $(SAMPLE_DIR)) sample..."
	docker run --rm \
		-v "$(SAMPLE_DIR)":/workspace \
		-w /workspace \
		$(DOCKER_IMAGE) \
		python /usr/local/bin/calculate_grade.py --verbose

check-docker-image:
	@if ! docker image inspect $(DOCKER_IMAGE) >/dev/null 2>&1; then \
		echo "❌ Docker image '$(DOCKER_IMAGE)' not found"; \
		echo "💡 Run 'make build' in the parent assignment directory first"; \
		exit 1; \
	fi
	@echo "✅ Docker image '$(DOCKER_IMAGE)' found"
