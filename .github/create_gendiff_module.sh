#!/bin/bash
# Этот скрипт создаст модуль gendiff для совместимости с тестами Хекслета

mkdir -p gendiff
cat > gendiff/__init__.py << 'EOS'
from hexlet_code import generate_diff
__all__ = ['generate_diff']
EOS

echo "Created gendiff module for Hexlet tests compatibility"
