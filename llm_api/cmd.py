import argparse
from argparse import ArgumentParser
from llm_api.config.config import Config
from llm_api.config.reader import read
from llm_api.config import settings
from llm_api.server import rest_server


# read commandline args to initiate server
def main():
    parser = ArgumentParser(
        prog=settings.PROJECT_PROG,
        description=settings.PROJECT_DESCRIPTION,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    subcommands = parser.add_subparsers(
        title='subcommands',
        description='valid subcommands',
        help='additional help',
        dest='subcommand',
    )
    run_parser = subcommands.add_parser(
        'run',
        help='Run the llm rest server',
    )
    run_parser.add_argument(
        '-t', '--hostname',
        default="info",
        help='Api hostname serve',
    )
    run_parser.add_argument(
        '-c', '--config',
        help='Path to the config yaml file',
    )
    run_parser.add_argument(
        '-p', '--port',
        type=int,
        default=5566,
        help='Port to listen on',
    )
    run_parser.add_argument(
        '-w', '--num-workers',
        type=int,
        default=4,
        help='Number of workers',
    )
    run_parser.add_argument(
        '-v', '--version',
        default=1,
        help='Api Version',
    )
    run_parser.add_argument(
        '-l', '--loglevel',
        default="info",
        help='Api logging level',
    )
    args = parser.parse_args()
    if args.subcommand == 'run':
        config = Config(config_file=args.config)
        if config.config_file is not None:
            config = read(config)
            print(f"read config file as {config}")
        else:
            config.api_metrics.port = args.port
            config.api_metrics.num_workers = args.num_workers
            config.api_metrics.version = "v1"
            config.api_metrics.host = "0.0.0.0"
            config.api_metrics.loglevel = args.loglevel
        rest_server(config.api_metrics)
    else:
        parser.print_help()
    return None

if __name__ == "__main__":
    main()



