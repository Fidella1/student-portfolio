import streamlit as st
import pandas as pd
from datetime import datetime
import time

# Set page title and icon
st.set_page_config(page_title="Student Portfolio", page_icon="🎓", layout="wide")

# Add CSS for animations
st.markdown("""
<style>
    .fade-in {
        animation: fadeIn 1.5s;
    }
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    .project-card {
        transition: transform 0.3s ease;
        padding: 20px;
        border-radius: 10px;
        background-color: #f0f2f6;
        margin-bottom: 20px;
    }
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    .timeline-item {
        border-left: 2px solid #4682b4;
        padding-left: 20px;
        padding-bottom: 20px;
        margin-left: 20px;
    }
    .timeline-dot {
        width: 16px;
        height: 16px;
        background-color: #4682b4;
        border-radius: 50%;
        margin-left: -28px;
        margin-top: 3px;
        float: left;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for storing data
if 'projects' not in st.session_state:
    st.session_state.projects = [
        {
            "title": "Data Analysis Project", 
            "type": "Individual", 
            "year": "Year 2", 
            "description": "A project analyzing trends of Rwanda GDP accounts using Pandas and Matplotlib",
            "link": "https://github.com/username/data-analysis"
        },
        {
            "title": "AI Chatbot", 
            "type": "Group", 
            "year": "Year 3", 
            "description": "Developed an AI-Powered chatbot using Python and NLP Techniques",
            "link": "https://github.com/username/ai-chatbot"
        },
        {
            "title": "Caritas CDJP Gikongoro Website", 
            "type": "Internship", 
            "year": "Year 3", 
            "description": "Designed and developed a website for Caritas Gikongoro using WordPress CMS",
            "link": "https://github.com/username/caritas-website"
        },
        {
            "title": "AI-Based Student Attendance System", 
            "type": "Dissertation", 
            "year": "Final Year", 
            "description": "Working on a facial recognition system to automate student attendance tracking for INES-Ruhengeri",
            "link": "https://github.com/username/attendance-system"
        }
    ]

if 'testimonials' not in st.session_state:
    st.session_state.testimonials = [
        {"name": "Dr. Theodore", "role": "Professor, AI Department", "text": "Fidella is a brilliant problem solver! Her final year project was truly innovative."},
        {"name": "Diane K.", "role": "Classmate", "text": "Working with Fidella on group projects has been a great experience. She's dedicated and brings creative solutions to difficult problems."}
    ]

if 'timeline' not in st.session_state:
    st.session_state.timeline = [
        {"year": "2023", "event": "First Python project completed ✅", "description": "Created a simple data analysis tool"},
        {"year": "2023", "event": "Joined AI research club 🔍", "description": "Started working on NLP projects"},
        {"year": "2024", "event": "Hackathon participation 🏆", "description": "Won 2nd place in the university coding challenge"},
        {"year": "2024", "event": "Summer internship at a local tech company 💼", "description": "Worked on web development projects"},
        {"year": "2025", "event": "Dissertation underway 📖", "description": "Working on AI-Based Student Attendance System"}
    ]

# Sidebar navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go To:", ["Home", "Projects", "Skills", "Timeline", "Testimonials", "Settings", "Contact"])

# Home section
if page == "Home":
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.title("🎓 Student Portfolio")

    col1, col2 = st.columns([1, 2])

    with col1:
        # Profile image
        uploaded_image = st.file_uploader("Upload Profile Picture", type=["jpg", "png"])
        if uploaded_image is not None:
            st.image(uploaded_image, width=200, caption="Uploaded image")
        else:
            st.image("my_profile.jpg", width=200, caption="Default image")

    with col2:
        # Student details (Editable!)
        name = st.text_input("Name: ", "Fidella I.")
        location = st.text_input("Location: ", "Musanze, Rwanda")
        field_of_study = st.text_input("Field of Study: ", "BSc Computer Science, Year 3")
        university = st.text_input("University: ", "INES - Ruhengeri")

        st.write(f"📍 {location}")
        st.write(f"📚 {field_of_study}")
        st.write(f"🎓 {university}")

        # Resume download button
        try:
            with open("resume.pdf", "rb") as file:
                resume_bytes = file.read()
            st.download_button(
                label="📄 Download Resume",
                data=resume_bytes,
                file_name="resume.pdf",
                mime="application/pdf"
            )
        except FileNotFoundError:
            st.warning("Resume file not found. Please upload a resume.pdf file.")
            st.file_uploader("Upload your resume (PDF)", type=["pdf"])

    st.markdown("---")
    st.subheader("About Me")
    about_me = st.text_area(
        "Short introduction about myself:",
        "I am a passionate AI and software engineering student at INES-Ruhengeri. My interests span machine learning, web development, and data analysis. I enjoy solving complex problems and building applications that make a positive impact. Currently, I'm working on my dissertation focused on an AI-based student attendance system using facial recognition. I'm seeking opportunities to apply my skills in real-world scenarios through internships and collaborative projects."
    )
    st.write(about_me)
    st.markdown('</div>', unsafe_allow_html=True)

# Projects section
elif page == "Projects":    
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.title("💻 My Projects")
    
    # Project filtering system
    st.subheader("Filter Projects")
    filter_options = ["All"] + sorted(list(set([p["year"] for p in st.session_state.projects]))) + sorted(list(set([p["type"] for p in st.session_state.projects])))
    filter_selection = st.selectbox("Select Category:", filter_options)
    
    filtered_projects = st.session_state.projects
    if filter_selection != "All":
        filtered_projects = [p for p in st.session_state.projects 
                            if p["year"] == filter_selection or p["type"] == filter_selection]
    
    for project in filtered_projects:
        with st.container():
            st.markdown(f'<div class="project-card">', unsafe_allow_html=True)
            col1, col2 = st.columns([3, 1])
            with col1:
                st.subheader(f"{project['title']} ({project['year']})")
                st.caption(f"Type: {project['type']}")
                st.write(project['description'])
            with col2:
                st.markdown(f"[View Code]({project['link']})")
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Add new project form (only visible in Settings)
    st.markdown('</div>', unsafe_allow_html=True)

# Skills section
elif page == "Skills":
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.title("⚡ Skills and Achievements")

    st.subheader("Programming Skills")
    
    col1, col2 = st.columns(2)
    with col1:
        skill_python = st.slider("Python", 0, 100, 90)
        st.progress(skill_python)
        
        skill_js = st.slider("JavaScript", 0, 100, 75)
        st.progress(skill_js)
        
        skill_AI = st.slider("Artificial Intelligence", 0, 100, 65)
        st.progress(skill_AI)
    
    with col2:
        skill_html_css = st.slider("HTML & CSS", 0, 100, 85)
        st.progress(skill_html_css)
        
        skill_sql = st.slider("SQL", 0, 100, 70)
        st.progress(skill_sql)
        
        skill_data = st.slider("Data Analysis", 0, 100, 80)
        st.progress(skill_data)

    st.subheader("Certifications & Achievements")
    st.write("✔ Completed AI & ML in Business Certification")
    st.write("✔ Certified in AI for Research and Course Preparation for Education")
    st.write("✔ 2nd Place in University Coding Challenge 2024")
    st.write("✔ Contributing Member of INES AI Research Group")
    st.markdown('</div>', unsafe_allow_html=True)

# Timeline section (NEW)
elif page == "Timeline":
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.title("⏳ Academic & Project Timeline")
    
    for item in st.session_state.timeline:
        st.markdown(f"""
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <strong>{item["year"]}: {item["event"]}</strong>
            <p>{item["description"]}</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Testimonials section (NEW)
elif page == "Testimonials":
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.title("🗣️ Testimonials")
    
    for testimony in st.session_state.testimonials:
        with st.container():
            st.markdown("""
            <div style="padding: 20px; border-radius: 10px; background-color: #f0f2f6; margin-bottom: 20px;">
                <p style="font-style: italic;">"{}"</p>
                <p style="text-align: right; font-weight: bold;">{}</p>
                <p style="text-align: right;">{}</p>
            </div>
            """.format(testimony["text"], testimony["name"], testimony["role"]), unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Settings section
elif page == "Settings":
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.title("🎨 Customize your profile")

    tabs = st.tabs(["Profile", "Add Project", "Add Testimonial", "Add Timeline Event"])
    
    with tabs[0]:
        st.subheader("Upload a Profile Picture")
        uploaded_image = st.file_uploader("Choose a file", type=["jpg", "png"])
        if uploaded_image:
            st.image(uploaded_image, width=150)

        st.subheader("✍ Edit Personal Info")
        name = st.text_input("Update Name:", "Fidella I.")
        bio = st.text_area("Update Bio:", "I am a passionate AI and software engineering student...")
        if st.button("Save Profile Updates"):
            st.success("Profile updated successfully!")
    
    with tabs[1]:
        st.subheader("Add New Project")
        new_project_title = st.text_input("Project Title:")
        new_project_type = st.selectbox("Project Type:", ["Individual", "Group", "Internship", "Dissertation", "Class Assignment"])
        new_project_year = st.selectbox("Project Year:", ["Year 1", "Year 2", "Year 3", "Final Year"])
        new_project_desc = st.text_area("Project Description:")
        new_project_link = st.text_input("GitHub/Project Link:")
        
        if st.button("Add Project"):
            if new_project_title and new_project_desc:
                st.session_state.projects.append({
                    "title": new_project_title,
                    "type": new_project_type,
                    "year": new_project_year,
                    "description": new_project_desc,
                    "link": new_project_link
                })
                st.success("Project added successfully!")
            else:
                st.error("Please fill in all required fields.")
    
    with tabs[2]:
        st.subheader("Add New Testimonial")
        new_testimonial_name = st.text_input("Person's Name:")
        new_testimonial_role = st.text_input("Role/Relationship:")
        new_testimonial_text = st.text_area("Testimonial Text:")
        
        if st.button("Add Testimonial"):
            if new_testimonial_name and new_testimonial_text:
                st.session_state.testimonials.append({
                    "name": new_testimonial_name,
                    "role": new_testimonial_role,
                    "text": new_testimonial_text
                })
                st.success("Testimonial added successfully!")
            else:
                st.error("Please fill in all required fields.")
    
    with tabs[3]:
        st.subheader("Add Timeline Event")
        new_timeline_year = st.text_input("Year:")
        new_timeline_event = st.text_input("Event Title:")
        new_timeline_desc = st.text_area("Event Description:")
        
        if st.button("Add Timeline Event"):
            if new_timeline_year and new_timeline_event:
                st.session_state.timeline.append({
                    "year": new_timeline_year,
                    "event": new_timeline_event,
                    "description": new_timeline_desc
                })
                st.success("Timeline event added successfully!")
            else:
                st.error("Please fill in all required fields.")
    st.markdown('</div>', unsafe_allow_html=True)

# Contact section
elif page == "Contact":
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.title("📬 Contact Me")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")

        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success("✅ Message sent successfully")
    
    st.markdown("---")
    st.subheader("Connect with me")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("📧 Email: mclement@ines.ac.rw")
        st.write("[🔗 LinkedIn](https://linkedin.com/in/username)")
    
    with col2:
        st.write("[📂 GitHub](https://github.com/username)")
        st.write("[🌐 Personal Website](https://myportfolio.com)")
    st.markdown('</div>', unsafe_allow_html=True)

st.sidebar.write("---")
st.sidebar.write("🔹 Last updated: March 2025")
st.sidebar.write("🔹 Made with ❤️ at INES-Ruhengeri")

