import pkg_resources


PROJECT_PROG = pkg_resources.get_distribution('llm_api').project_name
PROJECT_VERSION = "1"
PROJECT_DESCRIPTION = 'rest-api LLM'

SERVICER_ADDER = "pb2_grpc.add_VectorizerServicer_to_server"
SERVICE = None
