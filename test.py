
# Set up Dash layout
app.layout = html.Div(children=[
        html.H1('Handwritten Digit Classifier'),

        html.Div(id='reset-page', key='page', children=[

        html.Div([
            html.Div([
                html.H3('Draw & Submit'),
                html.Br(),
                html.Br(),
                html.Br(),
                DashCanvas(
                    id='canvas',
                    lineWidth=5,
                    lineColor='rgba(255, 0, 0, 0.5)',
                    width=canvas_size,
                    height=canvas_size,
                    hide_buttons=["zoom", "pan", "line", "pencil",
                                  "rectangle", "undo", "select"],
                    goButtonTitle='Submit',
                ),
                html.A(html.Button('Reset'), href='/'),
            ], style={"padding-left": "20px", "align": "left"},
                className="three columns"),

            html.Div([
                html.H3('Image converted to Dataframe', style={
                    "padding-left": "65px", "align": "left"}),
                dcc.Graph(id='output-figure', figure=blank_fig,
                style={'width': '100%', 'height': '100%', "padding-left":
                    "1px", "align": "left"}
                ),
            ], style={"padding-left": "0px", "align":"left"},
                className='six columns'),

            html.Div([
                html.H3('Predicted Digit'),
                html.Br(),
                html.H4('Random Forest Model:'),
                html.H6(id='rf-prediction', children='...'),
                html.H6(id='rf-probability', children='waiting for inputs'),
                html.Br(),
                html.H4('XGBoost Model:'),
                html.H6(id='xgb-prediction', children='...'),
                html.H6(id='xgb-probability', children='waiting for inputs'),
            ], className='three columns'),
        ], className="twelve columns"),]),
        html.Div(children=[
            html.Div('Updated'),
            html.Div(children=[
                html.Li('Added Reset button'),
                html.Li('Decreased drawing line width.'),
                html.Li('Adjusted test_size=0.1'),
                html.Li('Augmented X_train from 7000 to 315000 using 1up, '
                        '1down, 1right, 1left'),
                html.Li('Tried to use GridSearchCV, RandomizedSearchCV but '
                        'didn\'t complete within 8 hours with augmented data.'),
                html.Li('Therefore used static params with GridSearchCV.'),
                html.Li('Accuracy: 0.9851428571428571 '
                        'Precision: 0.9849865193732226 '
                        'Recall: 0.9852401268810149 '
                        'F1 Score: 0.9850931222167884'),
            ],),
        ],),
        html.Br(),
        html.A('Code on Github', href=githublink),
        html.Br(),
        html.A("Data Source", href=sourceurl),
], className="twelve columns")
