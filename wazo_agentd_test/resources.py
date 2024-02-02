# Copyright 2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+


from xivo.auth_verifier import required_acl
from wazo_agentd.http import AuthResource


class AgentTestResource(AuthResource):

    def __init__(self, test_service):
        self._test_service = test_service

    @required_acl('agentd.test.read')
    def get(self):
        test_list = self._test_service.list()

        return test_list, 200
