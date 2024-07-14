let express = require('express');
let fs = require('fs');

const data = fs.readFileSync('../sender_receiver_motortest/data.json', 'utf-8');
const jsonData = JSON.parse(data);

/*

{
  "gyroscope": {
    "x": 0.25,
    "y": -0.1,
    "z": 0.05
  },
  "range_sensor": {
    "sensor1": 10.5,
    "sensor2": 8.2,
    "sensor3": 12.7,
    "sensor4": 6.8,
    "sensor5": 9.3,
    "sensor6": 11.1,
    "sensor7": 7.6,
    "sensor8": 10.9
  }
}



*/

const app = express();
const port = 3000;

let html_send_to_user = '';

// create a function that auto update the webiste wenn jsonData is updated
const updateWebsite = () => {
	html_send_to_user = `
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Website</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
            }
            h1 {
                color: #333;
                text-align: center;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }
            th, td {
                padding: 10px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }
        </style>
    </head>
    <body>
        <h1>My Website</h1>
        <table>
            <tr>
                <th>Gyroscope</th>
                <th>Range Sensor</th>
            </tr>
            <tr>
                <td>
                    <ul>
                        <li>X: ${jsonData.gyroscope.x}</li>
                        <li>Y: ${jsonData.gyroscope.y}</li>
                        <li>Z: ${jsonData.gyroscope.z}</li>
                    </ul>
                </td>
                <td>
                    <ul>
                        <li>Sensor 1: ${jsonData.range_sensor.sensor1}</li>
                        <li>Sensor 2: ${jsonData.range_sensor.sensor2}</li>
                        <li>Sensor 3: ${jsonData.range_sensor.sensor3}</li>
                        <li>Sensor 4: ${jsonData.range_sensor.sensor4}</li>
                        <li>Sensor 5: ${jsonData.range_sensor.sensor5}</li>
                        <li>Sensor 6: ${jsonData.range_sensor.sensor6}</li>
                        <li>Sensor 7: ${jsonData.range_sensor.sensor7}</li>
                        <li>Sensor 8: ${jsonData.range_sensor.sensor8}</li>
                    </ul>
                </td>
            </tr>
        </table>
    </body>
    </html>
    `;
};

fs.watchFile('../sender_receiver_motortest/data.json', (curr, prev) => {
	if (curr.mtime > prev.mtime) {
		updateWebsite();
	}
});

app.get('/', (req, res) => {
	res.send(html_send_to_user);
});

app.listen(port, () => {
	console.log(`Server is running on port ${port}`);
});
