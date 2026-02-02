import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="Professional Biolography", layout="wide")

# Sidebar Menu
st.sidebar.title("Dr MJ Phiri Profile")
menu = st.sidebar.radio(
    "Links to:",
    ["Personal Details", "Academic Qualifications", "Work Experience", "Student Supervision", "Research Outputs", "Contact"],
)

# Dummy STEM data
honours_data = pd.DataFrame({
    "Student Name": ["Lakheni Tshutshane", "Akhona Mqushulu", "Jabulani Gumede", "Sisonke Kotelo"],
    "Project Role": ["Supervisor", "Supervisor", "Co-supervisor", "Supervisor"],
    "Institution":["Vaal University of Technology", "Vaal University of Technology", "Nelson Mandela University", "Nelson Mandela University"],
    "Graduation Date": [2024, 2024, 2017, 2016],
})

masters_data = pd.DataFrame({
    "Student Name": ["Akhona Mqushulu", "Phindile Vester", "Matshediso Makhelema", "Lefika Mosia", "Phuti Tsipa"],
    "Project Role": ["Supervisor", "Co-supervisor", "Co-supervisor", "Co-supervisor","Co-supervisor"],
    "Institution":["Vaal University of Technology", "Vaal University of Technology", "Nelson Mandela University", "Nelson Mandela University", "Nelson Mandela University"],
    "Graduation Date": [2025, 2025, 2021, 2020, 2018],
})


# Sections based on menu selection
if menu == "Personal Details":
    st.title("Personal Details")

    # Collect basic information
    name = "Dr. Mohau Justice Phiri, (PhD)"
    field = " Sustainable Polymer Composites"
    institution = "Vaal University of Technology"
    department  = "Natural Sciences (Chemistry)"
    group = "Organic, Polymer Technologies and Environmental"

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")
    st.write(f"**Department:** {department}")
    st.write(f"**Research Group:** {group}")
    
    st.image("https://media.licdn.com/dms/image/v2/D4D03AQE5vNWJbizq2g/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1694308384827?e=1771459200&v=beta&t=zwHgxZ3x2DTe-4m0PCFNBX5zOg6VhunrxgylFsf5MUw",
    )
 
elif menu == "Academic Qualifications":
    st.title("Academic Qualifications")
    
    #Collect the Doctoral qualification information
    name1 = "Doctor of Philosophy, (PhD)"
    field1 = "Polymer Sciences, (Analytical Chemistry)"
    institution1 = "Stellenbosch University"
    
 # Display basic Qualification information
    st.header("PhD Degree")
    st.write(f"**Name of Qualification:** {name1}")
    st.write(f"**Field of Study:** {field1}")
    st.write(f"**Institution of Study:** {institution1}")
    
    #Collect the Masters qualification information
    name2 = "Masters of Science in Engineering, (MSc.Eng)"
    field2 = "Chemical Engineering, (Mineral Processing)"
    institution2 = "Stellenbosch University"
    
 # Display basic Qualification information
    st.header("MSc Degree")
    st.write(f"**Name of Qualification:** {name2}")
    st.write(f"**Field of Study:** {field2}")
    st.write(f"**Institution of Study:** {institution2}")
    
    #Collect the qualification information
    name3 = "Bachelor of Science, (BSc.)"
    field3 = "Chemical Technology"
    institution3 = "National University of Lesotho"
    
 # Display basic Qualification information
    st.header("BSc Degree")
    st.write(f"**Name of Qualification:** {name3}")
    st.write(f"**Field of Study:** {field3}")
    st.write(f"**Institution of Study:** {institution3}")
  
elif menu == "Work Experience":
    st.title("Academic Work Expreience")
    
    #Collect the work experience information
    name4 = "1 March 2023 - up-to-date"
    field4 = "Physical Chemistry & Engineering Chemistry"
    institution4 = "Vaal University of University"
    
 # Display basic Qualification information
    st.header("Senior Lecturer & Researcher")
    st.write(f"**Duration:** {name4}")
    st.write(f"**Areas of Teaching:** {field4}")
    st.write(f"**Institution:** {institution4}")
    
    #Collect the Masters qualification information
    name5 = "1 September 2022 - 28 February 2023"
    field5 = "Polymer Chemistry, Biomass Processsing & Waster Tyre Recycling"
    institution5 = "Nelson Mandela University"
    
 # Display basic Qualification information
    st.header("Researcher")
    st.write(f"**Duration:** {name5}")
    st.write(f"**Areas of Research:** {field5}")
    st.write(f"**Institution:** {institution5}")
    
    #Collect the Masters qualification information
    name6 = "1 July 2016 - 31 December 2020"
    field6 = "Physical Chemistry, Polymer Technology & Chemical Process Technology"
    institution6 = "Nelson Mandela University"
    
 # Display basic Qualification information
    st.header("Lecturer & Researcher")
    st.write(f"**Duration:** {name6}")
    st.write(f"**Areas of Teaching:** {field6}")
    st.write(f"**Institution:** {institution6}")
        
      
elif menu == "Student Supervision":
    st.title("Postgraduate Supervision")
        
    # Tabbed view for STEM data
    data_option = st.sidebar.selectbox(
        "Select a category", 
        ["Honours Students", "Masters Students"]
    )

    if data_option == "Honours Students":
        st.write("### Honours Students")
        st.dataframe(honours_data)
        

    elif data_option == "Masters Students":
        st.write("### Masters Students")
        st.dataframe(masters_data)        

elif menu == "Research Outputs":
    st.title("Publications")
    
    #Collect the work experience information
    publi1 = "Phiri, M.J., Mofokeng, J.P, Phiri, M.M., Mngomezulu, M., Tywabi-Ngeva, Z., Chemical, thermal and morphological properties of polybutylene succinate-waste pineapple leaf fibres composites. Heliyon. 2024, 9. https://doi.org/10.1016/j.heliyon.2023.e21238 "
    publi2 = "Tsipa, P.C., Phiri, M.M., Iwarere, S.A., Mkhize, N.M., Phiri, M.J. and Hlangothi, S.P., The effect of pre-pyrolysis chemical treatment of waste tyre rubber crumbs: comparison between pre-treated and conventional waste tyre-derived oil. Journal Chemical Technology and Biotechnology. 2023. https://doi.org/10.1002/jctb.7346."
    publi3 = "Phiri, M.M; Phiri, M.J; Formela, K.; Hlangothi, S.P., Chemical Surface Etching Methods for Ground Tire Rubber as Sustainable Approach for Environmentally-Friendly Composites Development– A Review. Composites Part B: Engineering, 2020. 108429. https://doi.org/10.1016/j.compositesb.2020.108429."
    publi4 = "Liu, Y; Phiri, M.J, Ndiripo, A; Pasch, H., Chemical Composition Separation of a Propylene-Ethylene Random Copolymer by High Temperature Solvent Gradient Interaction Chromatography, Journal of chromatography A, 2017, 1522: 23-29. https://doi.org/10.1016/j.chroma.2017.09.042."
    publi5 = "Phiri, M.J.; Cheruthazhekatt, S.; Dimeska, A.; Pasch, H., Molecular Heterogeneity of Ethylene-Propylene Rubbers: New Insights through Advanced Crystallization-based and Chromatographic Techniques. Journal of Polymer Science Part A: Polymer Chemistry 2015, 53, 863-874. https://doi.org/10.1002/pola.27512."
    
 # Display basic Qualification information
    st.header("Selected Peer-reviewd Articles")
    st.write(f"{publi1}")
    st.write(f"{publi2}")
    st.write(f"{publi3}")
    st.write(f"{publi4}")
    st.write(f"{publi5}")

elif menu == "Contact":
    # Add a contact section
    st.header("Contact Information")
    
    email = "mohaup@vut.ac.za"
    phonenumber = "+27 78 347 8074"
    scopuslink = "https://orcid.org/0000-0002-0545-9289"
    
    st.write(f"Email: {email}")
    st.write(f"Cellphone: {phonenumber}")
    st.write(f"Research scholar profile: {scopuslink}")