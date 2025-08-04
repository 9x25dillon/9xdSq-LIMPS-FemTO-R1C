FROM julia:1.8

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    nvidia-cuda-toolkit \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy Julia dependencies
COPY limps_core/julia/ ./limps_core/julia/
COPY polynomial_system/ ./polynomial_system/

# Install Julia packages
RUN julia -e 'using Pkg; Pkg.add(["DynamicPolynomials", "MultivariatePolynomials", "LinearAlgebra", "JSON", "HTTP", "Statistics"])'

# Copy Python dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy application code
COPY . .

# Expose ports
EXPOSE 8000 9090 3000

# Start command
CMD ["julia", "limps_core/julia/LIMPS.jl"]
