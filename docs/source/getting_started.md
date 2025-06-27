# Getting Started with MarketMind

## Overview

This guide provides step-by-step instructions to set up and run **MarketMind** on your system.

## Prerequisites

- **Java**: Version 21 LTS
- **Python**: Version 3.12.9+ or higher
- **C++**: Compiler supporting C++20 (e.g., GCC, MSVC)
- **Maven**: For building the Java and C++ components
- **Dependencies**: Listed in `srcPy/requirements.txt` and `pom.xml`

## Installation

1. **Clone the Repository**:
   ```bash
   git clone [repository-url]
   cd MarketMind
   ```

2. **Set Up Python Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r srcPy/requirements.txt
   ```

3. **Build the Project**:
   ```bash
   mvn clean install
   ```

4. **Configure InfluxDB**:
   - Edit `deployment/influxdb_config.yaml` with your settings.
   - Start InfluxDB using `docker-compose.yml`.

5. **Run the Application**:
   ```bash
   mvn javafx:run
   ```

## Next Steps

- Explore the [Usage Guide](./usage_guide.md) for detailed instructions.
- Try the [Basic Prediction Tutorial](./tutorials/basic_prediction.ipynb).