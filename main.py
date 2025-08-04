#!/usr/bin/env python3
"""
Unified LIMPS Main Entry Point
Provides a comprehensive workflow interface for the integrated system.
"""

import argparse
import sys
import logging
from pathlib import Path

# Add local modules to path
sys.path.insert(0, str(Path(__file__).parent))

from limps_core.python.limps_workflow import LIMPSWorkflow
from interfaces.julia_client.julia_client import JuliaClient
from matrix_ops.processors.matrix_processor import MatrixProcessor

def setup_logging(level='INFO'):
    """Setup logging configuration"""
    logging.basicConfig(
        level=getattr(logging, level),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def main():
    """Main entry point for unified LIMPS system"""
    parser = argparse.ArgumentParser(description="Unified LIMPS System")
    parser.add_argument('--mode', choices=['server', 'client', 'workflow', 'test'], 
                       default='workflow', help='Operation mode')
    parser.add_argument('--config', default='config/project.toml', 
                       help='Configuration file path')
    parser.add_argument('--gpu', action='store_true', 
                       help='Enable GPU acceleration')
    parser.add_argument('--julia-port', type=int, default=8000,
                       help='Julia server port')
    parser.add_argument('--log-level', default='INFO',
                       choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'])
    
    args = parser.parse_args()
    setup_logging(args.log_level)
    
    logger = logging.getLogger(__name__)
    logger.info(f"Starting Unified LIMPS System in {args.mode} mode")
    
    if args.mode == 'server':
        start_julia_server(args.julia_port)
    elif args.mode == 'client':
        run_client_demo(args.julia_port, args.gpu)
    elif args.mode == 'workflow':
        run_integrated_workflow(args.config, args.gpu)
    elif args.mode == 'test':
        run_comprehensive_tests()

def start_julia_server(port):
    """Start Julia LIMPS server"""
    import subprocess
    cmd = ["julia", "-e", f"include('limps_core/julia/LIMPS.jl'); start_limps_server({port})"]
    subprocess.run(cmd)

def run_client_demo(julia_port, use_gpu):
    """Run client demonstration"""
    # Initialize components
    client = JuliaClient(f"http://localhost:{julia_port}")
    processor = MatrixProcessor(use_gpu=use_gpu)
    
    # Demo workflow
    print("Testing integrated LIMPS workflow...")
    
    # Test matrix processing
    import torch
    matrix = torch.randn(10, 10)
    result = processor.optimize_matrix(matrix, method="sparsity")
    print(f"Matrix optimization completed: compression ratio = {result['compression_ratio']:.3f}")
    
    # Test Julia integration
    if client.test_connection():
        julia_result = client.optimize_matrix(matrix.numpy(), "sparsity")
        print(f"Julia integration successful")

def run_integrated_workflow(config_path, use_gpu):
    """Run integrated workflow demonstration"""
    workflow = LIMPSWorkflow(config_path=config_path, use_gpu=use_gpu)
    workflow.run_comprehensive_demo()

def run_comprehensive_tests():
    """Run comprehensive system tests"""
    import subprocess
    subprocess.run(["python", "-m", "pytest", "tests/", "-v"])

if __name__ == "__main__":
    main()
