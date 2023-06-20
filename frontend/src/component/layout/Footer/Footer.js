import React from "react";
import "./Footer.css";

const Footer = () => {
  return (
    <footer id="footer">
      <div className="leftFooter">
        <h4>SUBSCRIBE OUR YOUTUBE CHANNEL</h4>
        <p>VISIT OUR INSTAGRAM PAGE </p>
       
      </div>

      <div className="midFooter">
        <h1>SmartElectronicStore</h1>
        <p>High Quality is our first priority</p>

        <p>Copyrights 2021 &copy; SmartElectronicStore</p>
      </div>

      <div className="rightFooter">
        <h4>Follow Us</h4>
        <a href="https://www.instagram.com/kaustubshetty123/">Instagram</a>
        <a href="https://www.linkedin.com/in/kaustub-shetty-508964220/">LinkedIn</a>
        <a href="https://www.facebook.com/kaustub.shetty.37">Facebook</a>
      </div>
    </footer>
  );
};

export default Footer;
