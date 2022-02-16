from typing import List

import pytest
import h2o_mlops_client as mlops
import faker


@pytest.fixture(scope="session")
def user1(authenticated_user, user, client):
    yield authenticated_user(user, client)


def test_user1(user1):
    assert user1.driverless
    assert user1.mlops
    assert user1.keycloak_id


def test_user_can_list_projects(user1):
    _mlops: mlops.Client = user1.mlops
    projects: List[mlops.StorageProject] = _mlops.storage.project.list_projects(
        mlops.StorageListProjectsRequest()
    ).project
    for project in projects:
        print(" Project Name: " + project.display_name)


def test_user_can_create_project(user1):
    _mlops: mlops.Client = user1.mlops
    project_name = faker.Faker().name()
    res: mlops.StorageCreateProjectResponse = _mlops.storage.project.create_project(
        mlops.StorageCreateProjectRequest(
            mlops.StorageProject(display_name=project_name)
        )
    )
    project: mlops.StorageProject = res.project
    assert project.display_name == project_name


def test_user_can_delete_project(user1):
    _mlops: mlops.Client = user1.mlops
    project_name = faker.Faker().name()
    res: mlops.StorageCreateProjectResponse = _mlops.storage.project.create_project(
        mlops.StorageCreateProjectRequest(
            mlops.StorageProject(display_name=project_name)
        )
    )
    project: mlops.StorageProject = res.project
    _mlops.storage.project.delete_project(
        mlops.StorageDeleteProjectRequest(project_id=project.id)
    )
