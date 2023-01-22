# -*- coding: utf-8 -*-

from datetime import datetime

from typing import Optional

from macrobond_data_api.common.enums import (
    SeriesMissingValueMethod,
    SeriesToLowerFrequencyMethod,
    SeriesToHigherFrequencyMethod,
    SeriesPartialPeriodsMethod,
)


class SeriesEntry:
    """
    Properties of a series in a call to `macrobond_data_api.common.api.Api.get_unified_series`.
    """

    __slots__ = (
        "name",
        "vintage",
        "missing_value_method",
        "to_lowerfrequency_method",
        "to_higherfrequency_method",
        "partial_periods_method",
    )

# pylint: disable=line-too-long
    def __init__(
        self,
        name: str,
        vintage: Optional[datetime] = None,
        missing_value_method: SeriesMissingValueMethod = SeriesMissingValueMethod.NONE,
        to_lowerfrequency_method: SeriesToLowerFrequencyMethod = SeriesToLowerFrequencyMethod.AUTO,
        to_higherfrequency_method: SeriesToHigherFrequencyMethod = SeriesToHigherFrequencyMethod.AUTO,
        partial_periods_method: SeriesPartialPeriodsMethod = SeriesPartialPeriodsMethod.NONE,
    ) -> None:
        self.name = name
        """The name of the series."""

        self.vintage = vintage
        """Optional vintage of the series."""

        self.missing_value_method = missing_value_method
        """
        Method to use to fill in missing values.
        Should be a value of
        `macrobond_data_api.common.enums.series_missing_value_method.SeriesMissingValueMethod`
        """
        self.to_lowerfrequency_method = to_lowerfrequency_method
        """
        Method to use when converting to a lower frequency.
        Should be a value of
        `macrobond_data_api.common.enums.series_to_lower_frequency_method.SeriesToLowerFrequencyMethod`
        """

        self.to_higherfrequency_method = to_higherfrequency_method
        """
        Method to use when converting to a higher frequency.
        Should be a value of
        `macrobond_data_api.common.enums.series_to_higher_frequency_method.SeriesToHigherFrequencyMethod`
        """

        self.partial_periods_method = partial_periods_method
        """
        Method to use when converting partial periods to a lower frequency.
        Should be a value of
        `macrobond_data_api.common.enums.series_partial_periods_method.SeriesPartialPeriodsMethod`
        """
# pylint: enable=line-too-long
