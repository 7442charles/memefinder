const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const { spawn } = require('child_process');

app.use(bodyParser.json());

// Define the "searchmeme" endpoint
app.post('/searchmeme', (req, res) => {
  try {
    const inputData = req.body.data; // Assuming data is sent as JSON with a "data" field

    // Run the Python script as a child process
    const pythonProcess = spawn('/usr/bin/python3', ['./processing.py', inputData]);

    let pythonResponse = '';

    pythonProcess.stdout.on('data', (data) => {
      // Collect output from the Python script
      pythonResponse += data.toString();
    });

    pythonProcess.on('close', (code) => {
      if (code === 0) {
        // Success: Send the Python script's response to the client
        res.json({ result: pythonResponse });
      } else {
        // Error: Handle the error response
        res.status(500).json({ error: 'An error occurred while processing the data.' });
      }
    });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

const port = 3000;
app.listen(port, () => {
  console.log(`Express.js server is running on port ${port}`);
});
