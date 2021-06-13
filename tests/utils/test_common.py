import os
from datetime import datetime
from unittest.mock import Mock, patch
from messageboard.utils.common import get_table, to_isoformat


@patch("messageboard.utils.common.get_table")
def test_get_table(mock_resp):
    mock_table = Mock()
    mock_table.name = os.environ["ITEMS_TABLE"]

    mock_resp.return_value = mock_table
    assert get_table().name == os.environ["ITEMS_TABLE"]


@patch("messageboard.utils.common.datetime")
def test_to_isoformat(mock_datetime):
    mock_datetime.utcnow.return_value = datetime(year=2021, month=6, day=13)

    assert to_isoformat() == "2021-06-13T00:00:00.000Z"
