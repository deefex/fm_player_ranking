import pandas as pd
from role_scoring_functions.apply_selected_scores import apply_selected_scores


def parse_and_calculate(file, selected_roles):
    print('parse_and_calculate')
    print(selected_roles)
    # This reads as a list, not a dataframe
    squad_rawdata_list = pd.read_html(file, header=0, encoding="utf-8", keep_default_na=False)

    # Turn the list into a dataframe
    squad_rawdata = squad_rawdata_list[0]

    # Calculate speed, work rate amd set pieces scores
    squad_rawdata['Spd'] = (squad_rawdata['Pac'] + squad_rawdata['Acc']) / 2
    squad_rawdata['Work'] = (squad_rawdata['Wor'] + squad_rawdata['Sta']) / 2
    squad_rawdata['SetP'] = (squad_rawdata['Jum'] + squad_rawdata['Bra']) / 2

    # Original Headers
    # squad = squad_rawdata[
    #     ['Inf', 'Name', 'Age', 'Club', 'Transfer Value', 'Wage', 'Nat', 'Position', 'Personality', 'Media Handling',
    #      'Left Foot', 'Right Foot', 'Spd', 'Jum', 'Str', 'Work', 'Height']]

    squad_rawdata = apply_selected_scores(squad_rawdata, selected_roles)

    mandatory_headers = ['Name', 'Age', 'Club', 'Transfer Value', 'Position', 'Spd', 'Work', 'SetP']
    optional_headers = selected_roles

    squad = squad_rawdata[mandatory_headers + optional_headers]

    table_html = squad.to_html(
        table_id="table",
        index=False,
        classes="table table-success table-striped table-bordered"
    )

    html = f"""
        <link rel="stylesheet" type="text/css" href="static/custom/css/styles.css">
        <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.25/css/dataTables.bootstrap5.min.css">
        <script type="text/javascript" charset="utf8" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.10.25/js/jquery.dataTables.min.js"></script>
        <script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.10.25/js/dataTables.bootstrap5.min.js"></script>
        
        {table_html}
        <script>
            $(document).ready( function () {{
                $('#table').DataTable();
            }});
        </script>
    """

    return html

