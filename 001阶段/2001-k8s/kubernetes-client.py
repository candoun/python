from kubernetes import client, config
from os import path
from pprint import pprint
import yaml

""" 
https://github.com/kubernetes-client/python/tree/master/kubernetes
"""
#############################################
# CoreV1Api

# config.load_kube_config()
config.load_kube_config('179config')
v1 = client.CoreV1Api()


# 获取所有namespace
def list_namespace():
    print("\nListing All namespace :")
    for ns in v1.list_namespace().items:
        print(ns.metadata.name)


# 获取所有service
def list_service():
    print("\nListing All services with their info:")
    ret = v1.list_service_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s \t%s \t%s \t%s \t" % (
        i.kind, i.metadata.namespace, i.metadata.name, i.spec.cluster_ip))


# 获取所有pod
def list_pod():
    print("Listing pods with their IPs:\n")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


# 获取node
def list_node():
    print("\nListing Nodes:")
    ret = v1.list_node()
    for i in ret.items:
        print(i.status.addresses[0].address)


#############################################
# AppsV1Api
api_instance = client.AppsV1Api()
api_response = api_instance.list_replica_set_for_all_namespaces()


# 获取所有RC
def list_rc():
    print("Listing RC with their name:\n")
    for i in api_response.items:
        print("%s\t%s\t%s/%s" % (i.metadata.name, i.metadata.namespace, i.status.available_replicas, i.status.replicas))

#############################################
# ExtensionsV1beta1Api


# 创建 deployment
def create_namespace():
    with open(path.join(path.dirname(__file__), "prism-redis-deployment.yaml")) as f:
        dep = yaml.load(f)
        k8s_beta = client.ExtensionsV1beta1Api()
        resp = k8s_beta.create_namespaced_deployment(
            body=dep, namespace="default")
    print("Deployment created. status='%s'" % str(resp.status))


# 删除deployment
def delete_namespace():
    with open(path.join(path.dirname(__file__), "prism-redis-deployment.yaml")) as f:
        dep = yaml.load(f)
        k8s_beta = client.ExtensionsV1beta1Api()
        resp = k8s_beta.delete_namespaced_deployment(name="prism-redis",
            body= client.V1DeleteOptions(), namespace="default")
    print("Deployment delete. status='%s'" % str(resp.status))


# 删除deployment方法2
def delete_namespace_req():
    import requests
    requests.delete('http://10.25.175.179:8086/apis/extensions/v1beta1/namespaces/default/deployments/prism-redis')


if __name__ == "__main__":
    list_namespace()
    # list_service()
    # list_pod()
    # list_node()
    # list_rc()
    # create_namespace()
    # delete_namespace()
    # delete_namespace_req()
