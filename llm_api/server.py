from llm_api.config.config import Config
import uvicorn
from llm_api.util.logging import logger


# run rest api server with defined router
def rest_server(metrics:Config):
    logger.info(f'Starting server port={metrics.port}')
    uvicorn.run(f"llm_api.api.{metrics.version}:app",host=metrics.host, port=metrics.port, workers=metrics.num_workers,log_level=metrics.loglevel)
