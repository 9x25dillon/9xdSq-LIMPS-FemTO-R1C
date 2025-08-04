# Unified LIMPS - Language-Integrated Matrix Processing System

A comprehensive, integrated system combining polynomial operations, matrix processing, entropy analysis, and AI model integration.

## Architecture Overview

The Unified LIMPS system is organized into the following modules:

### Core Components

- **limps_core/**: Core LIMPS system with Julia and Python integration
- **matrix_ops/**: Matrix processing and optimization engines  
- **polynomial_system/**: Polynomial operations and analysis
- **entropy_analysis/**: Entropy processing and analysis engines
- **models/**: AI/ML model integration (DeepSeek, transformers)

### Interfaces & APIs

- **interfaces/**: Client interfaces for Julia and Python integration
- **data/**: Data processing and validation utilities
- **utils/**: Monitoring, testing, and benchmarking tools

## Quick Start

1. **Setup Environment**:
   ```bash
   source config/environments/limps.env
   pip install -r requirements.txt
   ```

2. **Start Julia Server**:
   ```bash
   julia limps_core/julia/LIMPS.jl
   ```

3. **Run Integrated Workflow**:
   ```bash
   python main.py --mode workflow --gpu
   ```

## Workflow Integration

The system provides a cohesive workflow through the `LIMPSWorkflow` class:

```python
from limps_core.python.limps_workflow import LIMPSWorkflow

# Initialize integrated workflow
workflow = LIMPSWorkflow(use_gpu=True)

# Run comprehensive demonstration
workflow.run_comprehensive_demo()
```

## Features

- **GPU-Accelerated Matrix Operations**: CUDA-optimized matrix processing
- **Polynomial Analysis**: Symbolic polynomial operations via Julia
- **Entropy Processing**: Advanced entropy analysis and optimization
- **AI Model Integration**: DeepSeek and transformer model support
- **Cross-Language Interop**: Seamless Python-Julia integration
- **Comprehensive Testing**: Unit, integration, and performance tests

## Configuration

Configuration is managed through:
- `config/project.toml`: Main project configuration
- `config/environments/limps.env`: Environment variables
- Component-specific configs in respective modules

## Directory Structure

```
unified-limps/
├── limps_core/           # Core LIMPS system
│   ├── julia/           # Julia modules and API
│   └── python/          # Python workflow integration
├── matrix_ops/          # Matrix processing
├── polynomial_system/   # Polynomial operations  
├── entropy_analysis/    # Entropy processing
├── models/              # AI/ML models
├── interfaces/          # Client interfaces
├── data/                # Data processing
├── utils/               # Utilities and tools
├── tests/               # Comprehensive tests
├── config/              # Configuration files
└── deployment/          # Deployment configs
```

## Contributing

See `CONTRIBUTING.md` for development guidelines.

## License

Apache 2.0 License - see `LICENSE` file.
