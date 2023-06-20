import React from "react";
import "./aboutSection.css";
import { Button, Typography, Avatar } from "@material-ui/core";
import InstagramIcon from "@material-ui/icons/Instagram";
import LinkedInIcon from "@material-ui/icons/LinkedIn"

const About = () => {
  const visitInstagram = () => {
    window.location = "";
  };
  return (
    <div className="aboutSection">
      <div></div>
      <div className="aboutSectionGradient"></div>
      <div className="aboutSectionContainer">
        <Typography component="h1">About Us</Typography>

        <div>
          <div>
            <Avatar
              style={{ width: "10vmax", height: "10vmax", margin: "2vmax 0" }}
              src="/KautubShetty_inft.jpeg"
              alt="Founder"
            />
            <Typography>Kaustub Sudhakar Shetty</Typography>
            <Typography><b>FOUNDER</b></Typography>
            <Button onClick={visitInstagram} color="primary">
              Visit Instagram
            </Button>
            <span>
             Lorem ipsum dolor sit, amet consectetur adipisicing elit. 
             Molestiae tenetur eveniet quaerat impedit accusantium reiciendis,
            </span>
          </div>
          <div className="aboutSectionContainer2">
            <Typography component="h2">More about us..</Typography>
            <a
              href="https://www.linkedin.com/in/kaustub-shetty-508964220/"
              target="blank"
            >
              <LinkedInIcon className="youtubeSvgIcon" />
            </a>

            <a href="https://www.instagram.com/kaustubshetty123/" target="blank">
              <InstagramIcon className="instagramSvgIcon" />
            </a>
          </div>
        </div>
      </div>
    </div>
  );
};

export default About;
