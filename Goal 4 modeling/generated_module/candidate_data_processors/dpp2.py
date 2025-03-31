from datetime import datetime as dt
from numpy import nan
from sagemaker_sklearn_extension.externals import Header
from sagemaker_sklearn_extension.feature_extraction.date_time import DateTimeVectorizer
from sagemaker_sklearn_extension.feature_extraction.text import MultiColumnTfidfVectorizer
from sagemaker_sklearn_extension.impute import RobustImputer
from sagemaker_sklearn_extension.preprocessing import NALabelEncoder
from sagemaker_sklearn_extension.preprocessing import RobustStandardScaler
from sagemaker_sklearn_extension.preprocessing import ThresholdOneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Given a list of column names and target column name, Header can return the index
# for given column name
HEADER = Header(
    column_names=[
        'MAX_PROB', 'NORAD_CAT_ID_1', 'DSE_1', 'NORAD_CAT_ID_2', 'DSE_2', 'TCA',
        'TCA_RANGE', 'TCA_RELATIVE_SPEED', 'DILUTION', 'OBJECT_NAME_1',
        'OBJECT_ID', 'OBJECT_TYPE', 'OWNER', 'LAUNCH_DATE', 'LAUNCH_SITE',
        'PERIOD', 'INCLINATION', 'APOGEE', 'PERIGEE', 'ORBIT_TYPE',
        'OBJECT_ID_2', 'OBJECT_TYPE_2', 'OWNER_2', 'LAUNCH_DATE_2',
        'LAUNCH_SITE_2', 'PERIOD_2', 'INCLINATION_2', 'APOGEE_2', 'PERIGEE_2',
        'ORBIT_TYPE_2', 'diameter', 'span', 'xSectAvg', 'cataloguedFragments',
        'onOrbitCataloguedFragments', 'diameter_2', 'span_2', 'xSectAvg_2',
        'cataloguedFragments_2', 'onOrbitCataloguedFragments_2'
    ],
    target_column_name='MAX_PROB'
)


def build_feature_transform():
    """ Returns the model definition representing feature processing."""

    # These features can be parsed as numeric.

    numeric = HEADER.as_feature_indices(
        [
            'NORAD_CAT_ID_1', 'DSE_1', 'NORAD_CAT_ID_2', 'DSE_2', 'TCA_RANGE',
            'TCA_RELATIVE_SPEED', 'DILUTION', 'PERIOD', 'INCLINATION', 'APOGEE',
            'PERIGEE', 'PERIOD_2', 'INCLINATION_2', 'APOGEE_2', 'PERIGEE_2',
            'diameter', 'span', 'xSectAvg', 'cataloguedFragments',
            'onOrbitCataloguedFragments', 'diameter_2', 'span_2', 'xSectAvg_2',
            'cataloguedFragments_2', 'onOrbitCataloguedFragments_2'
        ]
    )

    # These features contain a relatively small number of unique items.

    categorical = HEADER.as_feature_indices(
        [
            'NORAD_CAT_ID_1', 'DSE_1', 'DSE_2', 'TCA_RANGE', 'DILUTION',
            'OBJECT_NAME_1', 'OBJECT_ID', 'OWNER', 'LAUNCH_SITE', 'PERIOD',
            'INCLINATION', 'APOGEE', 'PERIGEE', 'OBJECT_TYPE_2', 'OWNER_2',
            'LAUNCH_SITE_2', 'PERIOD_2', 'INCLINATION_2', 'APOGEE_2',
            'PERIGEE_2', 'diameter', 'span', 'xSectAvg', 'cataloguedFragments',
            'onOrbitCataloguedFragments', 'diameter_2', 'span_2', 'xSectAvg_2',
            'cataloguedFragments_2', 'onOrbitCataloguedFragments_2'
        ]
    )

    # These features can be parsed as natural language.

    text = HEADER.as_feature_indices(
        ['OBJECT_NAME_1', 'OBJECT_ID', 'OBJECT_ID_2']
    )

    # These features can be parsed as date or time.

    datetime = HEADER.as_feature_indices(
        ['TCA', 'LAUNCH_DATE', 'LAUNCH_DATE_2']
    )

    numeric_processors = Pipeline(
        steps=[
            (
                'robustimputer',
                RobustImputer(strategy='constant', fill_values=nan)
            )
        ]
    )

    categorical_processors = Pipeline(
        steps=[
            ('thresholdonehotencoder', ThresholdOneHotEncoder(threshold=14))
        ]
    )

    text_processors = Pipeline(
        steps=[
            (
                'multicolumntfidfvectorizer',
                MultiColumnTfidfVectorizer(
                    max_df=0.9568,
                    min_df=0.0052,
                    analyzer='word',
                    max_features=10000
                )
            )
        ]
    )

    datetime_processors = Pipeline(
        steps=[
            (
                'datetimevectorizer',
                DateTimeVectorizer(
                    mode='ordinal',
                    default_datetime=dt(year=1970, month=1, day=1)
                )
            )
        ]
    )

    column_transformer = ColumnTransformer(
        transformers=[
            ('numeric_processing', numeric_processors, numeric
            ), ('categorical_processing', categorical_processors,
                categorical), ('text_processing', text_processors, text),
            ('datetime_processing', datetime_processors, datetime)
        ]
    )

    return Pipeline(
        steps=[
            ('column_transformer', column_transformer
            ), ('robuststandardscaler', RobustStandardScaler())
        ]
    )


def build_label_transform():
    """Returns the model definition representing feature processing."""

    return NALabelEncoder()
