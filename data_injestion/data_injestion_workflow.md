data-ingestion/
│
├── kafka/
│   ├── configs/
│   │   └── kafka-config.properties
│   ├── src/
│   │   ├── kafkaProducerJSON.py
│   │   └── kafkaConsumerAvro.py
│   └── docker-compose.yml
│
├── batch-processing/
│   ├── src/
│   │   ├── csvProcessor.py
│   │   └── avroProcessor.py
│   └── configs/
│       └── batch-config.properties
│
└── schema-registry/
    ├── configs/
    │   └── schema-registry.properties
    └── schemas/
        ├── bidRequest.avsc
        └── clickConversion.avsc
