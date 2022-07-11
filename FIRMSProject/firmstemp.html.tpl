<!doctype html>
<html lang="en">
<head>
<link rel="stylesheet" href={css_tar}>
<title>
HOTSPOTS - NASA
</title>
</head>
<h1>
FIRMS ANALYSIS RESULTS
</h1>
<hr class="divider">
<h3>
PARAMETER RESULTS
</h3>
<body>
    <div class= "grid-container">
        <div class="grid-item">
            <table>
                <thead>
                    <tr>
                        <th>{one_name}</th>
                        <th>CRITICAL THRESHOLDS</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="border-left">MAXIMUM</td>
                        <td>{max_one_data}</td>
                    </tr>
                    <tr>
                        <td class="border-left">MINIMUM</td>
                        <td>{min_one_data}</td>
                    </tr>
                    <tr>
                        <td class="border-left">MEAN</td>
                        <td>{mean_one_data}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="grid-item">
            <table>
                <thead>
                    <tr>
                        <th>{two_name}</th>
                        <th>CRITICAL THRESHOLDS</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="border-left">MAXIMUM</td>
                        <td>{max_two_data}</td>
                    </tr>
                    <tr>
                        <td class="border-left">MINIMUM</td>
                        <td>{min_two_data}</td>
                    </tr>
                    <tr>
                        <td class="border-left">MEAN</td>
                        <td>{mean_two_data}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="grid-item">
            <table>
                <thead>
                    <tr>
                        <th>{three_name}</th>
                        <th>CRITICAL THRESHOLDS</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="border-left">MAXIMUM</td>
                        <td>{max_three_data}</td>
                    </tr>
                    <tr>
                        <td class="border-left">MINIMUM</td>
                        <td>{min_three_data}</td>
                    </tr>
                    <tr>
                        <td class="border-left">MEAN</td>
                        <td>{mean_three_data}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    <hr class="divider">
    <h3>
    INTERACTIVE MAP
    </h3>
    <iframe src= "www/resultMAP.html" height=550 width=1220 title="INTERACTIVE RESULT"></iframe>
    <hr class="divider">
    <h3>
    LINE PLOT
    </h3>
    <iframe src= "www/lineplot.html" height=550 width=1220 title="LINE PLOT"></iframe>
    <hr class="divider">
    <h3>
    GEO PLOT
    </h3>
    <iframe src= "www/geoplot.html" height=550 width=1220 title="GEO PLOT"></iframe>
    <hr class="divider">
    <h3>
    HEAT PLOT
    </h3>
    <iframe src= "www/heat.html" height=550 width=1220 title="LINE PLOT"></iframe>
    <hr class="divider">
    <h3>
    BAR PLOT
    </h3>
    <iframe src= "www/barplot.html" height=550 width=1220 title="BAR PLOT"></iframe>
    <hr class="divider">
    <h3>
    MULTI - LINE
    </h3>
    <iframe src= "www/multiline.html" height=550 width=1220 title="MULTI-LINE PLOT"></iframe>
    <hr class="divider">
    <h3>
    MULTI - MAP
    </h3>
    <iframe src= "www/multimap.html" height=550 width=1220 title="MULTI-MAP PLOT"></iframe>
    <hr class="divider">
    <a href=https://firms.modaps.eosdis.nasa.gov>
    NASA - FIRMS
    </a>
</body>
</html>