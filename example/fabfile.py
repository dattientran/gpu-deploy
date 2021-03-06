from gpu_deploy import *



DOCKER_DIR = abspath('./docker')
SCRIPTS_DIR = abspath('./scripts')
ENV_PATH = abspath('.env')


d = Deploy(DOCKER_DIR, SCRIPTS_DIR, ENV_PATH)

def deploy_staticnet(script=None, n=10, gpus=1, token=None):
    d.deploy('staticnet', script, n, gpus, token)

def stop_staticnet(script=None):
    d.stop('staticnet', script)
