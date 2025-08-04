"""
Unified LIMPS Workflow
Integrates all components into a cohesive comprehensive workflow
"""

import logging
import numpy as np
import torch
from pathlib import Path
import json
import time

from interfaces.julia_client.julia_client import JuliaClient, LIMPSJuliaIntegration
from matrix_ops.processors.matrix_processor import MatrixProcessor
from entropy_analysis.engines.entropy_engine import EntropyEngine

logger = logging.getLogger(__name__)

class LIMPSWorkflow:
    """Unified workflow for LIMPS system integration"""
    
    def __init__(self, config_path=None, use_gpu=False, julia_port=8000):
        """Initialize the unified workflow"""
        self.config_path = config_path
        self.use_gpu = use_gpu
        self.julia_port = julia_port
        
        # Initialize components
        self.julia_client = None
        self.matrix_processor = None
        self.entropy_engine = None
        self.limps_integration = None
        
        self._initialize_components()
    
    def _initialize_components(self):
        """Initialize all workflow components"""
        logger.info("Initializing workflow components...")
        
        # Initialize matrix processor
        self.matrix_processor = MatrixProcessor(
            use_gpu=self.use_gpu,
            precision="float32",
            debug=True
        )
        
        # Initialize Julia client
        self.julia_client = JuliaClient(f"http://localhost:{self.julia_port}")
        
        # Initialize LIMPS integration
        self.limps_integration = LIMPSJuliaIntegration(self.julia_client)
        
        # Initialize entropy engine
        self.entropy_engine = EntropyEngine()
        
        logger.info("All components initialized successfully")
    
    def run_comprehensive_demo(self):
        """Run a comprehensive demonstration of the integrated workflow"""
        logger.info("Starting comprehensive workflow demonstration...")
        
        # Test matrix processing workflow
        self.test_matrix_workflow()
        
        # Test polynomial analysis workflow  
        self.test_polynomial_workflow()
        
        # Test entropy analysis workflow
        self.test_entropy_workflow()
        
        # Test natural language processing workflow
        self.test_nlp_workflow()
        
        # Test integrated optimization workflow
        self.test_integrated_optimization()
        
        logger.info("Comprehensive workflow demonstration completed")
    
    def test_matrix_workflow(self):
        """Test matrix processing workflow"""
        logger.info("Testing matrix processing workflow...")
        
        # Create test matrices
        matrices = [
            torch.randn(20, 20),
            torch.randn(50, 30), 
            torch.randn(15, 15)
        ]
        
        methods = ["sparsity", "rank", "structure", "polynomial"]
        
        for i, matrix in enumerate(matrices):
            logger.info(f"Processing matrix {i+1} with shape {matrix.shape}")
            
            for method in methods:
                try:
                    result = self.matrix_processor.optimize_matrix(matrix, method)
                    logger.info(f"  {method}: compression ratio = {result['compression_ratio']:.3f}")
                except Exception as e:
                    logger.error(f"  {method}: failed with error {e}")
    
    def test_polynomial_workflow(self):
        """Test polynomial analysis workflow"""
        logger.info("Testing polynomial analysis workflow...")
        
        if not self.julia_client.test_connection():
            logger.warning("Julia server not available, skipping polynomial tests")
            return
        
        # Create test data
        data = np.random.rand(5, 3)
        variables = ["x", "y", "z"]
        
        try:
            # Create polynomials
            polys = self.julia_client.create_polynomials(data, variables)
            logger.info(f"Created {len(polys)} polynomials")
            
            # Analyze polynomials
            analysis = self.julia_client.analyze_polynomials(polys)
            logger.info(f"Polynomial analysis: complexity = {analysis.get('complexity_score', 'N/A')}")
            
        except Exception as e:
            logger.error(f"Polynomial workflow failed: {e}")
    
    def test_entropy_workflow(self):
        """Test entropy analysis workflow"""
        logger.info("Testing entropy analysis workflow...")
        
        # Create test entropy matrix
        entropy_matrix = np.random.rand(20, 20)
        
        try:
            if self.julia_client.test_connection():
                result = self.limps_integration.process_entropy_matrix(entropy_matrix)
                logger.info(f"Entropy processing: complexity = {result.get('complexity_score', 'N/A')}")
            else:
                logger.warning("Julia server not available for entropy processing")
        except Exception as e:
            logger.error(f"Entropy workflow failed: {e}")
    
    def test_nlp_workflow(self):
        """Test natural language processing workflow"""
        logger.info("Testing natural language processing workflow...")
        
        test_texts = [
            "Show monthly sales totals for electronics category",
            "Analyze customer behavior patterns in Q4 data",
            "Optimize inventory management for retail stores"
        ]
        
        for text in test_texts:
            try:
                if self.julia_client.test_connection():
                    analysis = self.limps_integration.analyze_natural_language(text)
                    logger.info(f"NLP analysis: '{text[:30]}...' -> entropy = {analysis.get('text_entropy', 'N/A')}")
                else:
                    logger.warning("Julia server not available for NLP processing")
                    break
            except Exception as e:
                logger.error(f"NLP workflow failed for '{text}': {e}")
    
    def test_integrated_optimization(self):
        """Test integrated optimization workflow"""
        logger.info("Testing integrated optimization workflow...")
        
        # Create complex test matrix
        matrix = torch.randn(30, 30)
        
        try:
            # Python optimization
            python_result = self.matrix_processor.optimize_matrix(matrix, "sparsity")
            
            # Julia optimization (if available)
            if self.julia_client.test_connection():
                julia_result = self.julia_client.optimize_matrix(matrix.numpy(), "sparsity")
                
                # Compare results
                py_compression = python_result['compression_ratio']
                jl_compression = julia_result.get('compression_ratio', 0)
                
                logger.info(f"Optimization comparison:")
                logger.info(f"  Python: {py_compression:.3f}")
                logger.info(f"  Julia:  {jl_compression:.3f}")
            else:
                logger.info(f"Python optimization: {python_result['compression_ratio']:.3f}")
                
        except Exception as e:
            logger.error(f"Integrated optimization failed: {e}")
    
    def save_workflow_results(self, output_path="workflow_results.json"):
        """Save workflow results to file"""
        results = {
            "timestamp": time.time(),
            "components_initialized": {
                "matrix_processor": self.matrix_processor is not None,
                "julia_client": self.julia_client is not None,
                "entropy_engine": self.entropy_engine is not None,
                "limps_integration": self.limps_integration is not None
            },
            "julia_connection": self.julia_client.test_connection() if self.julia_client else False
        }
        
        with open(output_path, 'w') as f:
            json.dump(results, f, indent=2)
        
        logger.info(f"Workflow results saved to {output_path}")
