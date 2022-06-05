
# Global Variable to Hold Anything
global_state = {}

# Colors
dark_blue = "rgb(49,51,102)"
pink = "rgb(223,104,95)"

tooltip_style = """
    <style>
        .tooltip {
            position:relative; 
            border-bottom:1px dashed #000;
        }

        .tooltip:before {
          content: attr(data-text); /* here's the magic */
          position:absolute;

          text-color: #ffffff;

          /* vertically center */
          top:50%;
          transform:translateY(-50%);

          /* move to right */
          left:100%;
          margin-left:15px; /* and add a small left margin */

          /* basic styles */
          width:200px;
          padding:10px;
          border-radius: 10px;
          background:#000;
          color: #fff;
          text-align:center;
          z-index: 2;

          display:none; /* hide by default */
        }

        .tooltip:hover:before {
          display:block;
        }

        .tooltip:after {
          content: "";
          position:absolute;
        
          /* position tooltip correctly */
          left:100%;
          margin-left:-5px;
        
          /* vertically center */
          top:50%;
          transform:translateY(-50%);
        
          /* the arrow */
          border:10px solid #000;
          border-color: transparent black transparent transparent;
        
          display:none;
        }
        .tooltip:hover:before, .tooltip:hover:after {
          display:block;
        }
    </style>
"""