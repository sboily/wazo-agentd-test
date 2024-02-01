# Copyright 2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+


from .resources import AgentTestResource
from .services import AgentTestService


class Plugin:

    def load(self, dependencies):
        api = dependencies['api']
        ami = dependencies['ami']

        agent_service = AgentTestService()

        api.add_resource(AgentTest, '/test', resource_class_args=[agent_service])
