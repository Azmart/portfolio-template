import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
import streamlit.components.v1 as components
from constant import *

st.set_page_config(page_title='Vicky Kuo' ,layout="wide",page_icon='👧🏻')

# -----------------  loading assets  ----------------- #
st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)
    
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

lottie_gif = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_zboivc9e.json")

# ----------------- info ----------------- #
with st.container():
    left_column,right_column = st.columns(2)
    
    def gradient(color1, color2, color3, content):
     st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});color:{color3};font-size:24px;border-radius:2%;">{content}</h1>', unsafe_allow_html=True)

    with left_column:
        st.subheader("Hi, I am Vicky :wave:")
        gradient('#FFD4DD','#000395','e0fbfc',"Passion for improving product and CX by data!")
        st.markdown("""""")
        st.write(info['Brief'])

    with right_column:
        st_lottie(lottie_gif, height=300, key="coding")

# ----------------- skillset ----------------- #
with st.container():
    st.subheader('⚒️ Skills')

    def skill_tab():
        idx = 0
        rows = len(info['skills'])//skill_col_size
        skills = iter(info['skills'])
        if len(info['skills'])%skill_col_size!=0:
            rows+=1
        for x in range(rows):
            columns = st.columns(skill_col_size)
            for index_ in range(skill_col_size):
                try:
                    idx += 1
                    columns[index_].button(next(skills))
                except:
                    break
                
    with st.spinner(text="In progress..."):
        skill_tab()
    
# ----------------- timeline ----------------- #
with st.container():
    st.subheader('📌 Career Snapshot')

    # load data
    with open('example.json', "r") as f:
        data = f.read()

    # render timeline
    timeline(data, height=400)

# -----------------  tableau  -----------------  #
with st.container():
    st.subheader("📊 Tableau")
    col1,col2 = st.columns([0.95, 0.05])
    with col1:
        with st.expander('See the work'):
            components.html(
                """
                <!DOCTYPE html>
                <html>  
                    <title>Basic HTML</title>  
                    <body style="width:130%">  
                        <div class='tableauPlaceholder' id='viz1684205791200' style='position: static'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Su&#47;SunnybrookTeam&#47;Overview&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='SunnybrookTeam&#47;Overview' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Su&#47;SunnybrookTeam&#47;Overview&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1684205791200');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='1350px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='1550px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='1350px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='1550px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.minHeight='5750px';vizElement.style.maxHeight=(divElement.offsetWidth*1.77)+'px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
                    </body>  
                </HTML>
                """
            , height=400, scrolling=True
            )
    st.markdown(""" <a href={}> <em>🔗 access to the link </a>""".format(info['Tableau']), unsafe_allow_html=True)
    
# ----------------- medium ----------------- #
with st.container():
    st.subheader('✍️ Medium')
    page = requests.get(info['Medium'])
    col1,col2 = st.columns([0.95, 0.05])
    with col1:
        with st.expander('Display my latest posts'):
            components.html(embed_rss['medium'],height=400)
            
        st.markdown(""" <a href={}> <em>🔗 access to the link </a>""".format(info['Medium']), unsafe_allow_html=True)

# -----------------  contact  ----------------- #
with st.container():
    col1,col2,col3 = st.columns([0.475, 0.475, 0.05])
        
    with col1:
        st.write("---")
        st.subheader("💬 See how my coworker describe me:")
        components.html(
        """
        <!DOCTYPE html>
        <html>
        <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            * {box-sizing: border-box;}
            .mySlides {display: none;}
            img {vertical-align: middle;}

            /* Slideshow container */
            .slideshow-container {
            position: relative;
            margin: auto;
            width: 100%;
            }

            /* The dots/bullets/indicators */
            .dot {
            height: 15px;
            width: 15px;
            margin: 0 2px;
            background-color: #6F6F6F;
            border-radius: 50%;
            display: inline-block;
            transition: background-color 0.6s ease;
            }

            .active {
            background-color: #eaeaea;
            }

            /* Fading animation */
            .fade {
            animation-name: fade;
            animation-duration: 1s;
            }

            @keyframes fade {
            from {opacity: .4} 
            to {opacity: 1}
            }

            /* On smaller screens, decrease text size */
            @media only screen and (max-width: 300px) {
            .text {font-size: 11px}
            }
            </style>
        </head>
        <body>
            <div class="slideshow-container">
                <div class="mySlides fade">
                <img src="https://user-images.githubusercontent.com/90204593/238169843-12872392-f2f1-40a6-a353-c06a2fa602c5.png" style="width:100%">
                </div>

                <div class="mySlides fade">
                <img src="https://user-images.githubusercontent.com/90204593/238171251-5f4c5597-84d4-4b4b-803c-afe74e739070.png" style="width:100%">
                </div>

                <div class="mySlides fade">
                <img src="https://user-images.githubusercontent.com/90204593/238171242-53f7ceb3-1a71-4726-a7f5-67721419fef8.png" style="width:100%">
                </div>

            </div>
            <br>

            <div style="text-align:center">
                <span class="dot"></span> 
                <span class="dot"></span> 
                <span class="dot"></span> 
            </div>

            <script>
            let slideIndex = 0;
            showSlides();

            function showSlides() {
            let i;
            let slides = document.getElementsByClassName("mySlides");
            let dots = document.getElementsByClassName("dot");
            for (i = 0; i < slides.length; i++) {
                slides[i].style.display = "none";  
            }
            slideIndex++;
            if (slideIndex > slides.length) {slideIndex = 1}    
            for (i = 0; i < dots.length; i++) {
                dots[i].className = dots[i].className.replace("active", "");
            }
            slides[slideIndex-1].style.display = "block";  
            dots[slideIndex-1].className += " active";
            }

            var interval = setInterval(showSlides, 1200); // Change image every 1.2 seconds

            function pauseSlides(event)
            {
                clearInterval(interval); // Clear the interval we set earlier
            }
            function resumeSlides(event)
            {
                interval = setInterval(showSlides, 1200);
            }
            // Set up event listeners for the mySlides
            var mySlides = document.getElementsByClassName("mySlides");
            for (i = 0; i < mySlides.length; i++) {
            mySlides[i].onmouseover = pauseSlides;
            mySlides[i].onmouseout = resumeSlides;
            }
            </script>

            </body>
            </html> 

            """,
                height=270,
    )
    with col2:
        st.write("---")
        st.subheader("📨 Get in touch with me!")
        
        contact_form = """
        <form action="https://formsubmit.co/vicky.kuo.contact@gmail.com" method="POST">
            <input type="hidden" name="_captcha value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
        
# -----------------  footer  ----------------- #
footer="""
<div class="footer">
<p>Developed with Streamlit by <a href={} target="_blank">Vicky Kuo @ IBM</a></p></div>
""".format(foot['url'])
st.markdown(footer,unsafe_allow_html=True)
