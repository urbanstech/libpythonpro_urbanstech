from unittest.mock import Mock
from libpythonpro_urbanstech import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        "login":"urbanstech","id":35203750,
        "avatar_url":"https://avatars.githubusercontent.com/u/35203750?v=4"
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('urbanstech')
    assert 'https://avatars.githubusercontent.com/u/35203750?v=4' == url