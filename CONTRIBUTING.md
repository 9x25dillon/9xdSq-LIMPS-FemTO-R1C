# Contributing to Unified LIMPS

Thank you for your interest in contributing to the Unified Language-Integrated Matrix Processing System (LIMPS)! This document provides guidelines for contributing to this comprehensive framework.

## Table of Contents

- [Getting Started](#getting-started)
- [Development Environment](#development-environment)
- [Code Organization](#code-organization)
- [Contributing Guidelines](#contributing-guidelines)
- [Testing](#testing)
- [Pull Request Process](#pull-request-process)
- [Code Style](#code-style)

## Getting Started

### Prerequisites

- Python 3.8+
- Julia 1.6+
- CUDA toolkit (optional, for GPU acceleration)
- Git

### Development Environment Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/9x25dillon/unified-limps.git
   cd unified-limps
   ```

2. **Set up environment**:
   ```bash
   source config/environments/limps.env
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Install Julia dependencies**:
   ```bash
   julia -e 'using Pkg; Pkg.instantiate()'
   ```

4. **Verify installation**:
   ```bash
   python main.py --mode test
   ```

## Code Organization

The repository is organized into logical modules:

```
unified-limps/
├── limps_core/           # Core LIMPS system
│   ├── julia/           # Julia modules and API
│   └── python/          # Python workflow integration
├── matrix_ops/          # Matrix processing and optimization
├── polynomial_system/   # Polynomial operations and analysis
├── entropy_analysis/    # Entropy processing engines
├── models/              # AI/ML model integration
├── interfaces/          # Client interfaces
├── data/                # Data processing utilities
├── utils/               # Monitoring, testing, benchmarking
├── tests/               # Comprehensive test suite
├── config/              # Configuration management
└── deployment/          # Deployment configurations
```

## Contributing Guidelines

### Types of Contributions

1. **Bug Fixes**: Fix identified issues in existing functionality
2. **Feature Enhancements**: Improve existing features
3. **New Features**: Add new capabilities to the system
4. **Documentation**: Improve or add documentation
5. **Performance Optimizations**: Enhance system performance
6. **Tests**: Add or improve test coverage

### Development Workflow

1. **Fork the repository** and create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the code style guidelines

3. **Add tests** for your changes:
   - Unit tests in `tests/unit/`
   - Integration tests in `tests/integration/`
   - Performance tests in `tests/performance/`

4. **Run the test suite**:
   ```bash
   python -m pytest tests/ -v
   ```

5. **Update documentation** as needed

6. **Commit your changes** with descriptive messages:
   ```bash
   git commit -m "feat: add matrix sparse optimization algorithm"
   ```

### Commit Message Convention

Use conventional commit format:
- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation changes
- `style:` - Code style changes
- `refactor:` - Code refactoring
- `test:` - Test additions/modifications
- `perf:` - Performance improvements

## Testing

### Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test categories
python -m pytest tests/unit/ -v
python -m pytest tests/integration/ -v
python -m pytest tests/performance/ -v

# Run with coverage
python -m pytest tests/ --cov=limps_core --cov-report=html
```

### Writing Tests

#### Python Tests
```python
import pytest
import torch
from matrix_ops.processors.matrix_processor import MatrixProcessor

class TestMatrixProcessor:
    def setup_method(self):
        self.processor = MatrixProcessor(use_gpu=False)
    
    def test_matrix_optimization(self):
        matrix = torch.randn(10, 10)
        result = self.processor.optimize_matrix(matrix, "sparsity")
        assert "compression_ratio" in result
        assert result["compression_ratio"] >= 0
```

#### Julia Tests
```julia
using Test
using LIMPS

@testset "LIMPS Tests" begin
    @test create_polynomials([1.0 2.0; 3.0 4.0], ["x", "y"]) isa Dict
    @test analyze_polynomials(Dict("P1" => Dict("degree" => 2))) isa Dict
end
```

## Pull Request Process

1. **Ensure your PR addresses an issue** or implements a planned feature

2. **Update documentation** including:
   - Code comments
   - API documentation
   - README if applicable
   - Examples in `docs/examples/`

3. **Ensure tests pass** and add new tests for your changes

4. **Request review** from maintainers

5. **Address feedback** and make necessary changes

6. **Squash commits** if requested before merging

### PR Checklist

- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Tests added/updated and passing
- [ ] Documentation updated
- [ ] No merge conflicts
- [ ] Changelog updated (for significant changes)

## Code Style

### Python Style

- Follow [PEP 8](https://pep8.org/)
- Use type hints where applicable
- Maximum line length: 88 characters
- Use descriptive variable and function names

```python
def optimize_matrix(matrix: torch.Tensor, 
                   method: str = "sparsity") -> Dict[str, Any]:
    """
    Optimize matrix using specified method.
    
    Args:
        matrix: Input tensor to optimize
        method: Optimization method to use
        
    Returns:
        Dictionary containing optimization results
    """
    # Implementation here
    pass
```

### Julia Style

- Follow [Julia Style Guide](https://docs.julialang.org/en/v1/manual/style-guide/)
- Use descriptive function and variable names
- Add docstrings for exported functions

```julia
"""
    create_polynomials(data::Matrix{Float64}, variables::Vector{String})

Create polynomial representation from numerical data.

# Arguments
- `data::Matrix{Float64}`: Input data matrix
- `variables::Vector{String}`: Variable names

# Returns
- `Dict{String, Any}`: Polynomial representation
"""
function create_polynomials(data::Matrix{Float64}, variables::Vector{String})
    # Implementation here
end
```

### Documentation Style

- Use clear, concise language
- Include code examples where appropriate
- Document all public APIs
- Keep documentation up-to-date with code changes

## Performance Considerations

### Optimization Guidelines

1. **GPU Acceleration**: Utilize GPU when available for matrix operations
2. **Memory Management**: Be mindful of memory usage, especially with large matrices
3. **Caching**: Implement caching for expensive computations
4. **Profiling**: Profile code to identify bottlenecks

### Benchmarking

```python
# Example benchmarking code
import time
from utils.benchmarking import benchmark_function

@benchmark_function
def matrix_operation(matrix):
    # Your operation here
    pass
```

## Getting Help

- **Issues**: Open an issue for bugs or feature requests
- **Discussions**: Use GitHub Discussions for questions
- **Discord**: Join our Discord server for real-time chat
- **Email**: Contact maintainers directly for sensitive issues

## Recognition

Contributors will be recognized in:
- `CONTRIBUTORS.md` file
- Release notes for significant contributions
- Annual contributor acknowledgments

Thank you for contributing to Unified LIMPS!