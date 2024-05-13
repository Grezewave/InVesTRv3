from pandas import DataFrame
import textwrap
from IPython.display import display
from IPython.display import Markdown


def restructure_dataframe(df: DataFrame):
    """
    Restructures a DataFrame with repeated columns into a dictionary.

    Args:
      df: The input DataFrame.

    Returns:
      A list of dictionaries, where each dictionary represents a row in the restructured format.
    """

    result = []
    for _, row in df.iterrows():
        id = row['investment_name'] 
        cycles = []

        # Iterate over value/date pairs
        for i in range(1, len(df.columns), 2):
            value_col = df.iloc[:, i].values[0]
            date_col = df.iloc[:, i + 1].values[0]

            if value_col is None:
                continue

            cycles.append({
                'value': value_col,
                'date': date_col
            })

        result.append({'id': id, 'cycles': cycles})
    return result

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))