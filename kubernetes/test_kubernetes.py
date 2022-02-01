def test(kubernetes_test_client):
    _, client = kubernetes_test_client
    deployments_list = client.list_deployment_for_all_namespaces()

    deployment = deployments_list.items[0]
    deployment_replicas = deployment.spec.replicas

    assert deployment_replicas


def test2(kubernetes_test_client):
    klient, _ = kubernetes_test_client
    node_list = klient.list_node()
    print("%s\t\t%s" % ("NAME", "LABELS"))
    # Patching the node labels
    for node in node_list.items:
        #api_response = klient.patch_node(node.metadata.name, body)
        print("%s\t%s" % (node.metadata.name, node.metadata.labels))
        print(node.spec.taints)

