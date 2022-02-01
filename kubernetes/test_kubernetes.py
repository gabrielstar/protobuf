import time


def test(kubernetes_test_client):
    _, client = kubernetes_test_client
    deployments_list = client.list_deployment_for_all_namespaces()

    deployment = deployments_list.items[0]
    deployment_replicas = deployment.spec.replicas

    assert deployment_replicas


def test_taint_untaint(kubernetes_test_client):
    #kubectl get nodes -o json | jq '.items[].spec.taints'
    taint = {"spec": {"taints": [
        {"effect": "NoSchedule", "key": "test", "value": "1", 'tolerationSeconds': '300'}]}}
    notaint = {"spec": {"taints": []}}
    klient, _ = kubernetes_test_client
    node_list = klient.list_node()
    print("%s\t\t%s" % ("NAME", "LABELS"))
    # Patching the node labels
    for node in node_list.items:
        klient.patch_node(node.metadata.name, taint)
        print("%s\t%s" % (node.metadata.name, node.metadata.labels))
        print(node.spec.taints)
        #untaint
        time.sleep(5)
        klient.patch_node(node.metadata.name, notaint)
