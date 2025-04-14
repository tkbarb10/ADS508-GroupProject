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
        'max_prob', 'norad_cat_id_1', 'norad_cat_id_2', 'object_name_1',
        'object_name_2', 'owner_1', 'object_type_1', 'launch_date_1',
        'launch_site_1', 'period_1', 'inclination_1', 'apogee_1', 'perigee_1',
        'orbit_type_1', 'owner_2', 'object_type_2', 'launch_date_2',
        'launch_site_2', 'period_2', 'inclination_2', 'apogee_2', 'perigee_2',
        'orbit_type_2'
    ],
    target_column_name='max_prob'
)


def build_feature_transform():
    """ Returns the model definition representing feature processing."""

    # These features can be parsed as numeric.

    numeric = HEADER.as_feature_indices(
        [
            'norad_cat_id_1', 'norad_cat_id_2', 'period_1', 'inclination_1',
            'apogee_1', 'perigee_1', 'period_2', 'inclination_2', 'apogee_2',
            'perigee_2'
        ]
    )

    # These features contain a relatively small number of unique items.

    categorical = HEADER.as_feature_indices(
        [
            'norad_cat_id_1', 'object_name_1', 'object_name_2', 'owner_1',
            'launch_site_1', 'period_1', 'inclination_1', 'apogee_1',
            'perigee_1', 'owner_2', 'object_type_2', 'launch_site_2',
            'period_2', 'inclination_2', 'apogee_2', 'perigee_2'
        ]
    )

    # These features can be parsed as natural language.

    text = HEADER.as_feature_indices(['object_name_1', 'object_name_2'])

    # These features can be parsed as date or time.

    datetime = HEADER.as_feature_indices(['launch_date_1', 'launch_date_2'])

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
            ('thresholdonehotencoder', ThresholdOneHotEncoder(threshold=19))
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
