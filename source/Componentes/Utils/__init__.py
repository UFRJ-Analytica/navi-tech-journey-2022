
# Global Variable to Hold Anything
global_state = {}

# Colors
purple_black = "rgb(29, 31, 28)" #1d1f1c
mustard_yellow = "rgb(250, 173, 45)" #faad2d
white = "rgb(255,255,255)" #ffffff
green = "rgb(27, 196, 100)" #1bc464

dark_blue = "rgb(49,51,102)"
pink = "rgb(223,104,95)"

tooltip_style = """
    <style>
        div[data-testid=stExpander] * {
            color: #faad2d;
            font-size: 16px;
            background-color: #333333
        }

        div[data-testid=stHorizontalBlock] div[data-testid=column]:first-child button:first-of-type {
            display:none !important;
        }

        div[data-testid=column] div[data-testid=stForm] {
            background-color: #333333;
            border-radius: 10px;
        }

        label {
            color: #faad2d !important;
        }

        button {
            color: #ffffff !important;
        }

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