const express = require("express");
const app = express();
const cors = require("cors");
const singleFilename = require("./mocks/getFilename.json");
const allFilenames = require("./mocks/getFilenames.json");

app.use(cors());
app.use(express.json());

app.get("/filepaths", (req, res) => {
  res.json(allFilenames);
});

app.get("/filepaths/:id", (req, res) => {
  const targetFilename = allFilenames.find(file => {
    return file.id == req.params.id;
  });
  console.log(req.params.id);
  res.json(targetFilename);
});

app.post("/filepaths", (req, res) => {
  const newFilename = Object.assign({ id: allFilenames.length + 1 }, req.body);
  allFilenames.push(newFilename);
});

app.put("/filepaths/:id", (req, res) => {
  const targetFilename = allFilenames.find(file => {
    return file.id == req.params.id;
  });
  const updatedFilename = Object.assign(req.body, { id: req.params.id });
  allFilenames.splice(allFilenames.indexOf(targetFilename), 1, updatedFilename);
  res.send(allFilenames);
});

app.delete("/filepaths/:id", (req, res) => {
  console.log(req);
  const targetFilename = allFilenames.find(file => {
    return file.id == req.params.id;
  });
  allFilenames.splice(allFilenames.indexOf(targetFilename), 1);
  res.sendStatus(200);
});

app.listen(3000, () => console.log("Example app listening on port 3000!"));
