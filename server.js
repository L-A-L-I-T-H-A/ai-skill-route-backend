const express = require("express");
const axios = require("axios");
const cors = require("cors");
const mongoose = require("mongoose");

const app = express();

app.use(cors());
app.use(express.json());
// connecting the Nodejs to Local Mongodb
mongoose.connect("mongodb://127.0.0.1:27017/careerguidance")
.then(() => console.log("MongoDB Connected"))
.catch((err) => console.log(err));

// create the schema 
const studentSchema = new mongoose.Schema({
    name: String,
    attendance: Number,
    coding: Number,
    aptitude: Number,
    communication: Number,
    projects: Number,
    certifications: Number,

    performance_score: Number,
    placement_eligible: Number,
    career_domain: String,
    skill_category: String
});

// create model ( save the data into mongodb)
const Student = mongoose.model("Student", studentSchema);

app.post("/student",async (req, res) => {
    try{
        const response = await axios.post(
            "http://127.0.0.1:5000/predict",
            req.body
        );

        const prediction = response.data;
        // create mongodb document
        const studentData = new Student({
            name: req.body.name,
            attendance: req.body.attendance,
            coding: req.body.coding,
            aptitude: req.body.aptitude,
            communication: req.body.communication,
            projects: req.body.projects,
            certifications: req.body.certifications,
            performance_score: prediction.performance_score,
            placement_eligible: prediction.placement_eligible,
            career_domain: prediction.career_domain,
            skill_category: prediction.skill_category
        });
            await studentData.save();
            res.json(prediction);

    } catch(error) {
    console.log("Node Error:");
    console.log(error.message);

    if(error.response){
        console.log("Flask Response Error:");
        console.log(error.response.data);
    }

    res.status(500).json({
        message: "Error connecting Flask API"
    });
}
});
app.listen(3000, () => {
            console.log("Node server running on port 3000")
        });
