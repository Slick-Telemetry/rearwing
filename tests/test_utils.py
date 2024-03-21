# Built-in
from datetime import datetime
from unittest import TestCase, mock

# External
import pandas as pd

# Project
from app.utils import get_default_year


class TestUtilDefaultYear(TestCase):

    def setUp(self) -> None:
        self.fake_event_schedule = pd.DataFrame.from_records([{"RoundNumber": 1}])

    def test_success(self):
        current_year = datetime.today().year
        mock_call_get_session_load = mock.MagicMock()
        with (
            mock.patch(
                "app.utils.fastf1.get_event_schedule", return_value=self.fake_event_schedule
            ) as _mock_get_event_schedule,
            mock.patch("app.utils.fastf1.get_session", return_value=mock_call_get_session_load) as _mock_get_session,
        ):
            self.assertEqual(get_default_year(), current_year)
            _mock_get_event_schedule.assert_called_once_with(current_year, include_testing=False)
            _mock_get_session.assert_called_once_with(current_year, 1, "Race")
