# Copyright 2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+


from wazo_calld.auth import required_acl
from wazo_calld.http import AuthResource


class AgentTestResource(AuthResource):

    def __init__(self, test_service):
        self._test_service = test_service

    @required_acl('agentd.test.read')
    def get(self):
        test_list = self._agent_service.list()

        return test_list, 200
