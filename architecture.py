from diagrams import Cluster
from diagrams.k8s.compute import Deployment
from diagrams.programming.framework import React, FastAPI
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.database import PostgreSQL
# from diagrams.custom import Custom
# from diagrams.generic.blank import Blank
from diagrams.generic.storage import Storage
from sphinx_diagrams import SphinxDiagram


with SphinxDiagram(title=""):
    # github_repo = Custom("GitHub Repository", str(github_icon))
    github_repo = Storage("GitHub Repository")

    with Cluster("Science Platform Kubernetes Cluster"):
        with Cluster("times-square"):
            ui = React("times-square-ui")
            api = FastAPI("times-square-api")
            db = PostgreSQL("db")
            cache = Redis("cache")

        with Cluster("noteburst"):
            noteburst = Deployment("noteburst")

        with Cluster("nublado"):
            jupyterhub = Deployment("jupyterhub")
            labs = [Deployment(f"jupyterlab {i+1}") for i in range(3)]
            for lab in labs:
                jupyterhub >> lab

    ui >> api
    api >> db
    api >> cache
    api - github_repo

    api >> noteburst
    noteburst >> jupyterhub
