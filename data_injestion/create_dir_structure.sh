#!/bin/bash

# Create directory structure
mkdir -p kafka/configs
mkdir -p kafka/src
mkdir -p batch-processing/src
mkdir -p batch-processing/configs
mkdir -p schema-registry/configs
mkdir -p schema-registry/schemas

# Create placeholder files (optional)
touch kafka/configs/kafka-config.properties
touch kafka/src/kafkaProducerJSON.py
touch kafka/src/kafkaConsumerAvro.py
touch kafka/docker-compose.yml
touch batch-processing/src/csvProcessor.py
touch batch-processing/src/avroProcessor.py
touch batch-processing/configs/batch-config.properties
touch schema-registry/configs/schema-registry.properties
touch schema-registry/schemas/bidRequest.avsc
touch schema-registry/schemas/clickConversion.avsc

echo "Directory structure and placeholder files created."
