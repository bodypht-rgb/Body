#!/bin/bash


echo "======================================"
echo "   IoT-Sentinel: Resilience Auditor   "
echo "======================================"


export PYTHONPATH=$PYTHONPATH:$(pwd)


python3 src/auditor.py

echo "======================================"
echo "           Audit Finished             "
echo "======================================"
