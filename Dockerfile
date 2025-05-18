FROM python:3.9-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./
COPY src ./src

RUN pip install --no-cache-dir -e .

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
