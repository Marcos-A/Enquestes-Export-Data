#!/usr/bin/env python
import sys

template = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dashboard</title>

        <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/v/dt/jq-3.3.1/jszip-2.5.0/dt-1.10.24/b-1.7.0/b-colvis-1.7.0/b-html5-1.7.0/b-print-1.7.0/cr-1.5.3/kt-2.6.1/r-2.2.7/sp-1.2.2/datatables.min.css"/>

        <style>
            body{
                background-color: whitesmoke;
                padding-bottom: 10px;
            }

            body, 
            h1{            
                margin: 0px;
                font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
            }

            header{
                background-color: #ad0050;
                color: white;
                padding: 10px;
            }

            h1{
                padding: 0px;
            }
        
            h2{
                font-weight: normal;
            }

            .canvas, 
            .table{
                position: relative; 
                width:100%;          
            }

            .canvas{
                padding-bottom: 20px;
                height:400px !important;
            }

            .box{            
                width: calc(50% - 36px);
                border: solid 1px grey;
                box-shadow: 1px 1px 10px #888888;
                border-radius: 5px;
                margin: 10px 10px 0px 10px;
                padding: 0px 10px 10px 10px;
                background-color: white;
            }

            .left{
                float: left;            
                margin-right: 5px;
            }

            .right{
                float: right;
                margin-left: 5px;
            }

            .full{
                width: calc(100% - 42px);
                padding: 0px 10px 10px 10px;
            }

            .clear{
                clear: both;
            }

            .content{
                width: 100%;
                display: flex;
            }

            .box h3{
                margin-top: 10px;
            }

            .box ol{
                padding-left: 20px;
                margin-left: 40px;
            }

            .box li{
                cursor: pointer;
            }

            .box li:hover{
                color: darkgray;
            }

            .box li.cross{
                text-decoration: line-through;
            }

            .box li .icon{
                width: 28px;
                height: 10px;
                background-color: red;
                position: relative;
                display: inline-block;
                margin-left: -60px;
                margin-right: 35px;
            }    

            .hide table,
            .hide #data_filter,
            .hide #data_info,
            .hide #data_paginate{
                display: none;
            }

            .hide .dt-buttons{
                margin-left: 10px;
            }   

            @media only screen and (max-width: 800px) {
                .content{
                    display: inline;
                }

                .left,
                .right {
                    float: none;
                    display: block;
                    margin:10px;
                    width: calc(100% - 42px);
                }
            }   
                    
        </style>

        <script src="https://cdn.jsdelivr.net/npm/chart.js@3.2.1/dist/chart.min.js"></script>    
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.36/pdfmake.min.js"></script>
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.36/vfs_fonts.js"></script>
        <script type="text/javascript" src="https://cdn.datatables.net/v/dt/jq-3.3.1/jszip-2.5.0/dt-1.10.24/af-2.3.6/b-1.7.0/b-colvis-1.7.0/b-html5-1.7.0/b-print-1.7.0/cr-1.5.3/kt-2.6.1/r-2.2.7/sp-1.2.2/datatables.min.js"></script>

        <script type="text/javascript">
            window.onload = function () {                       
                const globalData = {
                    labels:  [
                        "Pregunta 1", 
                        "Pregunta 2", 
                        "Pregunta 3", 
                        "Pregunta 4", 
                    ],
                    datasets: [
                        {
                            data:  [9.75, 8.25, 7, 9],
                            backgroundColor: [
                            'rgb(255, 99, 132, 0.25)',
                            'rgb(75, 192, 192, 0.25)',
                            'rgb(255, 205, 86, 0.25)',
                            'rgb(54, 162, 235, 0.25)'
                            ]
                        }
                    ]
                };

                const totalData = {
                    labels: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    datasets: [
                        {
                            label: "Pregunta 1",
                            data:  [0, 0, 0, 1, 0, 2, 7, 5, 3],
                            backgroundColor: 'rgb(255, 99, 132, 0.25)',
                            borderColor: 'rgb(255, 99, 132, 0.25)'
                        },
                        {
                            label: "Pregunta 2", 
                            data:  [0, 1, 0, 0, 0, 3, 6, 3, 4],
                            backgroundColor: 'rgb(75, 192, 192, 0.25)',
                            borderColor: 'rgb(75, 192, 192, 0.25)'
                        },
                        {
                            label: "Pregunta 3", 
                            data:  [0, 0, 0, 0, 0, 3, 4, 8, 1],
                            backgroundColor: 'rgb(255, 205, 86, 0.25)',
                            borderColor: 'rgb(255, 205, 86, 0.25)'
                        },
                        {
                            label: "Pregunta 4",
                            data:  [0, 1, 0,2, 0, 2, 2, 9, 1],
                            backgroundColor: 'rgb(54, 162, 235, 0.25)',
                            borderColor: 'rgb(54, 162, 235, 0.25)'
                        }
                    ]
                };

                var fullData = [            
                    {                
                        "degree": "This is a demo comment (1).",
                        "subject_code": "This is a demo comment (1).",
                        "subject_name": "This is a demo comment (1).",
                        "question_statement": "This is a demo comment (1).",
                        "value": "This is a demo comment (1).",
                    },
                    {                
                        "degree": "This is a demo comment (2).",
                        "subject_code": "This is a demo comment (2).",
                        "subject_name": "This is a demo comment (2).",
                        "question_statement": "This is a demo comment (2).",
                        "value": "This is a demo comment (2).",
                    },
                    {                
                        "degree": "This is a demo comment (3).",
                        "subject_code": "This is a demo comment (3).",
                        "subject_name": "This is a demo comment (3).",
                        "question_statement": "This is a demo comment (3).",
                        "value": "This is a demo comment (3).",
                    }
                ];

            
                var globalChart = new Chart(document.getElementById('globalChart'), {
                    type: 'polarArea',
                    data: globalData,                
                    options: {                    
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: {
                                //position: 'left'
                                display: false
                            }
                        }
                    },
                });

                var totalChart = new Chart(document.getElementById('totalChart'), {
                    type: 'line',
                    data: totalData,                
                    options: {                    
                        responsive: true,
                        maintainAspectRatio: false,
                        scales: {
                            x:{
                                title: {
                                    display: true,
                                    text: 'Puntuació'
                                }
                            },
                            y:{
                                title: {
                                    display: true,
                                    text: 'Quantitat de valoracions'
                                }
                            }
                        },
                        plugins: {
                            legend: {
                                //position: 'right'
                                display: false
                            }
                        }
                    },
                });

                $('#table').DataTable({
                    data: fullData,
                    columns: [                                     
                        {data: "value"}
                    ]          
                });

                var table = $('#data').DataTable({
                    data: fullData,
                    columns: [                                     
                        {data: "degree"},
                        {data: "subject_code"},
                        {data: "subject_name"},
                        {data: "question_statement"},
                        {data: "value"}
                    ],
                    "columnDefs": [
                        {
                            "targets": [ 1 ],
                            "visible": false,
                            "searchable": false
                        }
                    ],
                    dom: 'Bfrtip',
                    buttons: [
                        'copy', 'excel', 'pdf'
                    ],            
                });
                
                var legendItems = document.querySelector('#legend').getElementsByTagName('li');

                for (var i = 0; i < legendItems.length; i++) {
                    legendItems[i].addEventListener("click", legendClickCallback.bind(this,i), false);
                }

                function legendClickCallback(legendItemIndex){
                    var legendItem = document.querySelector('#legend').getElementsByTagName('li')[legendItemIndex];
                    legendItem.classList.toggle("cross");

                    document.querySelectorAll('canvas').forEach((chartItem,index)=>{
                        var chart = Chart.instances[index];
                        if(chart.config.type == "polarArea") chart.toggleDataVisibility(legendItemIndex);
                        else  chart.data.datasets[legendItemIndex].hidden = !(chart.data.datasets[legendItemIndex].hidden ?? false);                    
                        chart.update();                    
                    });  
                }
            };         
        </script>
    <head>
    
    <body>
        <header>
            <h1>DAM</h1>
            <h2>MP04: Llenguatges de marques i sistemes de gestió d'informació</h2>
        </header>

        <div class="box full">
            <h3>Preguntes</h3>
            <ol id="legend">
                <li><div class="icon" style="background-color: rgb(255, 99, 132, 0.25);"></div>Avalua la metodologia d'aprenentatge, l'organització de la classe i l'assistència rebuda.</li>
                <li><div class="icon" style="background-color: rgb(75, 192, 192, 0.25);"></div>Penses que la manera d'avaluar és l'adequada?</li>
                <li><div class="icon" style="background-color: rgb(255, 205, 86, 0.25);"></div>Penses que el que has après pot ser útil a la teva futura vida professional?</li>
                <li><div class="icon" style="background-color: rgb(54, 162, 235, 0.25);"></div>Penses que el material triat pel professor és l'adequat? (Llibre o apunts, Moodle, activitats, transparències, videotutorials, etc.)</li>
            </ol>
        </div>

        <div class="content">    
            <div class="box left">
                <h3>Valoracions totals</h3>
                <div class="canvas">
                    <canvas id="totalChart"></canvas>
                </div>
            </div>

            <div class="box right">
                <h3>Valoracions globals</h3>
                <div class="canvas">
                    <canvas id="globalChart"></canvas>
                </div>
            </div>
        </div>

        <div class="clear"></div>
    
        <div class="box full">
            <h3>Comentaris</h3>
            <div class="table">
                <table id="table" style="width:100%">   <!-- inline needed to allow responsive behaviour -->
                    <thead>
                        <tr>              
                            <th>Si us plau, fes una proposta per millorar el mòdul. (Opcional, però molt important si penses que hi ha coses per polir. Longitud màxima: 280 caràcters.)</th>                    
                        </tr>                    
                    </thead>            
                </table>
            </div>
        </div>  
        
        <div class="box hide full">
            <h3>Exportació de dades </h3>
            <table id="data">
                <thead>
                    <tr>              
                        <th>degree</th>
                        <th>subject_code</th>
                        <th>subject_name</th>
                        <th>question_statement</th>
                        <th>value</th>
                    </tr>                    
                </thead>            
            </table>
        </div>
        
    </body>
    
</html>
"""

original_stdout = sys.stdout

with open('dashboard.html', 'w') as f:
    sys.stdout = f
    print(template)
    sys.stdout = original_stdout
