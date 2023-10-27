import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
st.markdown(
    f"""
    <style>
    .sidebar {{
        background-image: url("http://s1.picswalls.com/wallpapers/2017/12/10/4k-photos_110628610_312.jpg");
        background-attachment: fixed;
        background-size: cover;
        padding: 20px;  /* Add some padding to make content readable */
    }}
    </style>
    """,
    unsafe_allow_html=True
) 
st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("http://s1.picswalls.com/wallpapers/2017/12/10/4k-photos_110628610_312.jpg");
            background-attachment: fixed;
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    ) 
def load_lottie(url):
    r = requests.get(url)
    if (r.status_code != 200):
        return None
    return r.json()


def main():
    pass
# if __name__ == "main":
st.sidebar.title("AYUSH NAUTIYAL :smile:")
# st.sidebar.image("https://purepng.com/public/uploads/large/purepng.com-phone-iconsymbolsiconsapple-iosiosios-8-iconsios-8-721522596098aomr5.png",width=30)

st.sidebar.subheader(":phone: +919993583625")
# st.sidebar.image("https://pngimg.com/uploads/email/email_PNG11.png",width=30)
st.sidebar.subheader("ayushnautiyal1110@gmail.com")
# st.sidebar.subheader(":e-mail: ayushnautiyal1110@gmail.com")

github_url = "https://github.com/ayushnautiyal1110"
github_image = "https://c0.klipartz.com/pngpicture/800/1000/gratis-png-github-computer-icons-jupyter-repositorio-github.png"
st.sidebar.markdown(
    f'<a href="{github_url}" target=" _blank"><img src="{github_image}" alt="LinkedIn Profile" width="60"></a>',
    unsafe_allow_html=True
)
linkedin_url = "https://www.linkedin.com/in/ayush-nautiyal-27a025202"
# Replace with your image's file path
linkedin_image = "https://www.effa.nl/wp-content/uploads/2018/01/linkedin-logo.png"
st.sidebar.markdown(
    f'<a href="{linkedin_url}" target="_blank"><img src="{linkedin_image}" alt="LinkedIn Profile" width="30"></a>',
    unsafe_allow_html=True
)
# st.sidebar.subheader("[img](https://www.linkedin.com/in/ayush-nautiyal-27a025202)")

# st.write("[Content Gen App](https://content-generation-tool-6wi6ez9xgewdmbqqipqgyg.streamlit.app/)")
with st.container():
    selected = option_menu(
        menu_title=None,
        options=['Home', 'Experience','Projects', 'Coding', 'Skills', 'Certifications'],
        icons=['person', 'file-txt','file-txt', 'code-slash', 'file-txt', 'file-txt'],
        orientation='horizontal'
    )
if selected == "Home":
    st.title("I am Python Devloper")
    st.title("Competitive Programmer")
    lottie = load_lottie(
        "https://lottie.host/d9811d92-20d1-4444-8c20-8d8b5d98fb52/61mZLs7Bix.json")

    st_lottie(lottie, width=200)
elif selected == "Experience":
    st.title("Intern at Persistent Systems                    Jun23-Aug23")
elif selected == "Projects":
    st.title("MY PROJECT SECTION")
    st.header(" ")
    # lottie="https://lottie.host/593cf4f9-e78c-4f76-a0c1-769c839ef8cc/55bSmjVGFB.json"
    # st_lottie(lottie,width=500)
    col1,col2,col3=st.columns(3)
    
    with col1:
        p1="https://classintercom.com/wp-content/uploads/2018/07/theContentGen16x9-1.png"
        st.write("AI Content Genration Tool")
        p2="https://content-generation-tool-6wi6ez9xgewdmbqqipqgyg.streamlit.app/"
        st.markdown(
                f'<a href="{p2}" target=" _blank"><img src="{p1}" alt="LeetCode Profile" width="200"></a>',
                unsafe_allow_html=True
            )
    with col2:
        p1="https://techvidvan.com/tutorials/wp-content/uploads/sites/2/2021/06/driver-drowsiness-detection-python-opencv-ml.jpg"
        st.write("Drowsiness Detection")
        p2="https://github.com/ayushnautiyal1110/DrowsinessDetection"
        st.markdown(
                f'<a href="{p2}" target=" _blank"><img src="{p1}" alt="LeetCode Profile" width="200"></a>',
                unsafe_allow_html=True
        )
    with col3:
        p1="https://www.starlinkindia.com/blog/wp-content/uploads/2019/05/Biometrics-Face-Recognition-How-Does-it-work.jpg"
        st.write("FACE RECONGNITION")
        p2="https://github.com/ayushnautiyal1110/FACE-RECONGNITION"
        st.markdown(
                f'<a href="{p2}" target=" _blank"><img src="{p1}" alt="LeetCode Profile" width="200"></a>',
                unsafe_allow_html=True
        )    
elif selected == "Coding":
    # lottie=load_lottie("https://lottie.host/7a3086a0-9ec4-47bd-b731-0dd2d0039376/kUe7hZV9Bg.json")
    # st_lottie(lottie,width=100)
    col1, col2, col3 = st.columns(3)
    with col1:
        leetcode_url = "https://leetcode.com/ayushnautiyal1110"
        leetcode_img = "https://cdn.jsdelivr.net/gh/TaroPie0224/blogImage@main/img/LeetCode.jpg"
        st.header("LeetCode Profile")
        st.markdown(
            f'<a href="{leetcode_url}" target=" _blank"><img src="{leetcode_img}" alt="LeetCode Profile" width="200"></a>',
            unsafe_allow_html=True
        )
        st.subheader("--- MAX RATING :- 1787 (Top 7.87 % Globally)")
        st.subheader("--- Solved 800+ Problems ")
    with col2:    
        codeforce_url = "https://codeforces.com/profile/ayush_n"
        codeforce_img = "https://yxxshin.github.io/images/CodeForces_Cover.jpg"
        st.header("CodeForces Profile")
        st.markdown(
            f'<a href="{codeforce_url}" target=" _blank"><img src="{codeforce_img}" alt="LeetCode Profile" width="200"></a>',
            unsafe_allow_html=True
        )
        st.subheader("--- MAX RATING :- 1376 (Pupil)")
        st.subheader("--- Solved 1200+ Problems ")
    with col3:
        codechef_url = "https://www.codechef.com/users/ayushnautiyal"
        codechef_img = "https://www.mycplus.com/mycplus/wp-content/uploads/2018/03/codechef-1536x750.jpg"
        st.header("CodeChef Profile")
        st.markdown(

            f'<a href="{codechef_url}" target=" _blank"><img src="{codechef_img}" alt="LeetCode Profile" width="200" ></a>',
            unsafe_allow_html=True
        )
        st.subheader("--- MAX RATING :- 1809 (Pupil)")
        st.subheader("--- Solved 300+ Problems ")
elif selected=="Skills":
    col1,col2,col3=st.columns(3)
    with col1:
        st.image("https://cdn.hackr.io/uploads/posts/attachments/1570190908UfTQzF19EE.jpg",width=200) 
        st.image("https://wallpapercave.com/wp/wp2742472.jpg")
        st.image("https://media.istockphoto.com/vectors/blue-round-dbms-concept-vector-id954537764?k=6&m=954537764&s=170667a&w=0&h=-fcviToOX5KS5bsdfY_GGZyKh5UjS132KNwapqRLaGE=",width=200)
       
    with col2:
        st.image("https://i.ytimg.com/vi/Qmt0QwzEmh0/maxresdefault.jpg",width=200)
        st.image("https://i.ytimg.com/vi/6N1A15CG2bQ/maxresdefault.jpg",width=250)
        st.image("https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png",width=200)
    with col3:
        st.image("https://media.gettyimages.com/vectors/artificial-intelligence-banner-vector-id691178076",width=250)
        st.image("https://24x7servermanagement.com/wp-content/uploads/2016/09/mysql-logo.jpg",100)
        st.image("https://1.bp.blogspot.com/-NGHwBncyA68/UiMm_8b2ZUI/AAAAAAAAAnA/17OGXCKI4zE/s1600/Logo+HTML5.JPG")
        

elif selected=="Certifications":
    geek_img="https://noticedash.com/wp-content/uploads/2021/06/GeeksforGeeks.svg_.png"
    geek_url="https://media.geeksforgeeks.org/courses/certificates/537d80e0c606ef52a350f55adbecc024.pdf"
    
    
    st.markdown(

        f'<a href="{geek_url}" target=" _blank"><img src="{geek_img}" alt="LeetCode Profile" width="150" ></a>',
        unsafe_allow_html=True
    )
    st.subheader("DSA Self Paced Course")
    h1_img="https://images.yourstory.com/cs/1/6fe21cf0425e11ea943f1fd65c7bf912/hackerranklogo-1607404272375.png?fm=png&auto=format"
    h1_url="https://www.hackerrank.com/certificates/56bbbd727715?utm_medium=email&utm_source=mail_template_1393&utm_campaign=hrc_skills_certificate"
    st.markdown(

        f'<a href="{h1_url}" target=" _blank"><img src="{h1_img}" alt="LeetCode Profile" width="150" ></a>',
        unsafe_allow_html=True
    )
    st.subheader("Problem Solving (Intermediate) Certificate")
    h2_img="https://ugc.production.linktr.ee/d8B3KXoPSHinSb62Ysrv_648efede33f77_SEO-Image-_1_.jpg"
    h2_url="https://unstop.com/certificate-preview/adc8ac0a-597f-4c11-8b60-5fbc4e913b39?utm_campaign"
    st.markdown(

        f'<a href="{h2_url}" target=" _blank"><img src="{h2_img}" alt="LeetCode Profile" width="150" ></a>',
        unsafe_allow_html=True
    )
    st.subheader("Techsurf Certificate")
    h3_img="https://cdn.neow.in/news/images/uploaded/2021/03/1615067291_freecodecamp_story.jpg"
    h3_url="https://www.freecodecamp.org/certification/ayush_n/responsive-web-design"
    st.markdown(

        f'<a href="{h3_url}" target=" _blank"><img src="{h3_img}" alt="LeetCode Profile" width="150" ></a>',
        unsafe_allow_html=True
    )
    st.subheader("Responsive Web Design Certificate")
    h4_img="https://learnerbits.com/wp-content/uploads/2023/06/Flipkart-Grid-5.0.png"
    h4_url="https://unstop.com/certificate-preview/c3d03890-cf32-4050-bfb5-9b9b838919d7"
    st.markdown(

        f'<a href="{h4_url}" target=" _blank"><img src="{h4_img}" alt="LeetCode Profile" width="150" ></a>',
        unsafe_allow_html=True
    )
    st.subheader("Flipkart Grid 5.0 Certificate")
    h4_img="https://tse3.mm.bing.net/th?id=OIP.smhrpP2hxx2R6KJc8z8oeQHaEK&pid=Api&P=0&h=180"
    h4_url="https://www.credly.com/badges/c34f8964-83ac-4b05-8489-20bbe26afb4a/linked_in_profile"
    st.markdown(

        f'<a href="{h4_url}" target=" _blank"><img src="{h4_img}" alt="LeetCode Profile" width="150" ></a>',
        unsafe_allow_html=True
    )
    st.subheader("Cisco Cyber Ops")
    h4_img="https://images.credly.com/size/340x340/images/a4dd891f-7bf5-4938-8241-50dc81e8cc00/image.png"
    h4_url="https://www.credly.com/badges/0dda5ba3-c804-4c01-a997-60d438623c17/linked_in_profile"
    st.markdown(

        f'<a href="{h4_url}" target=" _blank"><img src="{h4_img}" alt="LeetCode Profile" width="150" ></a>',
        unsafe_allow_html=True
    )
    st.subheader("Cisco Networking and s")
    