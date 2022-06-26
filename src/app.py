from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Dummy Ambari'

    # @app.route('/clusters/:clusterName/hosts/:hostName')
    @app.route('/api/v1/clusters/<cluster>/hosts/<host>')
    def host_info(cluster, host):

        res = {
            "href": f"http://your.ambari.server/api/v1/clusters/{cluster}/hosts/{host}",
            "metrics": {
                "process": {
                },
                "rpc": {
                },
                "ugi": {
                },
                "disk": {
                },
                "cpu": {
                },
                "rpcdetailed": {
                },
                "jvm": {
                },
                "load": {
                },
                "memory": {
                },
                "network": {
                },
            },
            "Hosts": {
                "cluster_name": f"{cluster}",
                "host_name": f"{host}",
                "host_state": "HEALTHY",
                "public_host_name": f"{host}.yourDomain.com",
                "cpu_count": 1,
                "rack_info": "rack-name",
                "os_arch": "x86_64",
                "disk_info": [
                    {
                        "available": "41497444",
                        "used": "9584560",
                        "percent": "19%",
                        "size": "51606140",
                        "type": "ext4",
                        "mountpoint": "/"
                    }
                ],
                "ip": "10.0.2.15",
                "os_type": "rhel6",
                "total_mem": 2055208,
            },
            "host_components": [
                {
                    "href": f"http://your.ambari.server/api/v1/clusters/{cluster}/hosts/{host}/host_components/DATANODE",
                    "HostRoles": {
                        "cluster_name": f"{cluster}",
                        "component_name": "DATANODE",
                        "host_name": f"{host}"
                    }
                }
            ]
        }

        return res

    return app


if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=5222)
