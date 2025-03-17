
import pandas as pd
import streamlit as st
import plotly.express as px

# ✅ st.set_page_config() must be the first Streamlit command
st.set_page_config(
    
    layout='wide', page_title='IT Salary', page_icon="logo.png"
)

@st.cache_data
def load_data():
    return pd.read_csv("data/cleaned_data.csv")

df = load_data()
st.markdown("""
    <h1 style='text-align: center; color: #17202A;'>IT Salary Report 2020</h1>
    """, unsafe_allow_html=True)
st.markdown("""
    <p style='text-align: center; color: #414e66;'>Designed to guide fresh graduates in making informed decisions for a successful programming career.</p>
    """, unsafe_allow_html=True)

# Custom CSS for the sidebar
sidebar_style = """
<style>
/* Sidebar background and title color */
[data-testid="stSidebar"] {
    background-color: #414E66;
    border-radius: 7px;
    border-left: 5px solid #D0D3D9;
    color: #FFFFFF; /* Title color */
}

/* Selectbox label (title) color */
[data-testid="stSidebar"] label {
    color: #FFFFFF; /* White label */
}

/* All input widgets inside the sidebar (e.g., selectbox, slider, text input) */
[data-testid="stSidebar"] select,
[data-testid="stSidebar"] input,
[data-testid="stSidebar"] textarea {
    color: #000000; /* Black text */
    background-color: #D0D3D9; /* White background */
}

/* Button styling in sidebar */
[data-testid="stSidebar"] button {
    color: #000000; /* Black text */
    background-color: #D0D3D9; /* Yellow background */
    border-radius: 10px; /* Rounded corners */
}

/* Hover effect for buttons and selectbox */
[data-testid="stSidebar"] button:hover,
[data-testid="stSidebar"] select:hover {
    background-color: #ffffff; /* Golden Yellow hover */
}

/* Slider text and handle color */
[data-testid="stSidebar"] .stSlider {
    color: #000000 !important; /* Black slider text */
}

/* Hover effect for slider */
[data-testid="stSidebar"] .stSlider:hover {
    color: #FFD700 !important; /* Golden hover */
}


</style>
"""

# Injecting the custom style into your app
st.markdown(sidebar_style, unsafe_allow_html=True)



page_bg_color = """
<style>
/* Background for the main page */
.stApp {
    background-color: #ffffff; /* Light gray */
}
</style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)


# Sidebar content
st.sidebar.image("logo3.png", width=250)
st.sidebar.write("")


# Custom CSS for enhancements
st.markdown("""
    <style>
        .body {
            background-color: #ffffff !important;
        }
        .stApp {
            background-color: #ffffff !important;
            padding-top: 10px;
        }
        .title {
            background-color: #ffffff;
            color: #616f89;
            padding: 10px;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            border: 4px solid #000083;
            border-radius: 10px;
            box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2);
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
            margin-bottom: 20px;
        }
        .metric {
            background-color: #FFAF8A;
            border:none ;
            border-radius: 7px;
            padding: 15px;
            box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.1);
            text-align: center;
            margin-bottom: 25px;
            transition: transform 0.2s ease-in-out;
        }
        .metric:hover {
            box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.3);
            transform: scale(1.05);
        }
        .metric p {
            color: #f5f7fb;
            font-size: 26px;
            font-weight: 600;
            
            text-shadow: 1px 1px 2px #000083;
        }
        .metric h3 {
            margin-bottom: 5px;
            font-size: 20px;
            font-weight: 500;
            color: #ffaf8a;
        }
        @media (max-width: 768px) {
            .metric {
                padding: 10px;
            }
            .title {
                font-size: 30px;
            }
            .metric p {
                font-size: 20px;
            }
            .metric h3 {
                font-size: 16px;
            }
        }
    </style>
""", unsafe_allow_html=True)

with st.container(): # Metrics
    st.write()
    #metrics
    avg_age = int(round(df["age"].mean(),0))
    perc_age = round(df["age_range"].value_counts()/len(df)*100,1).tolist()[0]
    total_people  =df["timestamp"].count()
    avg_yearly_salary = int(round(df["yearly_salary_eur"].mean(),0))
    avg_yearly_bonus = int(round(df["yearly_bonus_stocks_eur"].mean(),0))
    common_company_size = df["company_size"].mode()
    common_age_range = df["age_range"].sort_index(ascending =False)[0]
    city_counts = df["city"].value_counts().reset_index()
    city_counts.columns = ['City', 'Count']  
    top_city = city_counts.iloc[0]['City']  
    perc_city = round(df["city"].value_counts()/len(df)*100,1).tolist()[0]
    
    perc_g_male = round(df["gender"].value_counts()/len(df)*100,1)[0]
    perc_g_female = round(df["gender"].value_counts()/len(df)*100,1)[1]
    
    
    
# Custom CSS for the KPI card with split background and top-left alignment
st.markdown(
    """
        <style>
    /* Main KPI Container */
    .split-kpi {
        border-radius: 7px; /* Rounded corners */
        overflow: hidden; /* Ensures no content spills out */
        padding: 0; /* Remove padding */
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1); /* Shadow effect */
        margin: 5px; /* Reduced margin for less spacing */
        transition: transform 0.2s ease-in-out; /* Hover animation */
        width: 250px; /* Adjust width for KPI size */
        height: 100px; /* Adjust height for KPI size */
        box-sizing: border-box; /* Ensures padding is included in total size */
    }
    

    /* Top section of the KPI */
    .split-top {
        background-color: white; 
        padding: 5px 10px; /* Reduced padding to control top space */
        height: 80%; /* Occupies 80% of the card */
        display: flex; 
        flex-direction: column; 
        justify-content: center; /* Center content vertically */
        align-items: center; /* Center content horizontally */
        text-align: center; /* Ensure text is centered */
        gap: 3px; /* Controls space between lines */
        font-family: 'Calibri';
        font-weight: bold;
        font-size: 18px; /* Font size for the main metric */
        line-height: 1.2; /* Reduce line height to remove extra space */
}

    /* Bottom section of the KPI */
    .split-bottom {
        background-color: #FF9800; /* Orange section */
        padding: 5px 10px; /* Consistent padding */
        height: 20%; /* Occupies 20% of the card */
        display: flex;
        justify-content: flex-start; /* Align to the left */
        align-items: center; /* Center vertically */
        font-weight: bold;
        font-family: 'Calibri';
        font-size: 12px; /* Smaller font for the label */
    }

    .split-bottomDblue {
        background-color: #FF9800; /* Orange section */
        padding: 5px 10px; /* Consistent padding */
        height: 20%; /* Occupies 20% of the card */
        display: flex;
        justify-content: flex-start; /* Align to the left */
        align-items: center; /* Center vertically */
        font-weight: bold;
        font-family: 'Calibri';
        font-size: 12px; /* Smaller font for the label */
        color: white
    }
    /* Hover effect */
    .split-kpi:hover {
        transform: translateY(-5px); /* Float up slightly */
    }

    .icon_green {
        color: #4CAF50; /* Green color */
        font-size: 16px; /* Icon size */
        margin-right: 8px; /* Space between icon and text */
        vertical-align: middle; /* Align icon with text */
        justify-content: center;
        align-items: center;
        text-align: center;
    }
    .icon_orange {
        font-size: 16px; /* Icon size */
        margin-right: 8px; /* Space between icon and text */
        vertical-align: middle; /* Align icon with text */
        justify-content: center;
        align-items: center;
        text-align: center;
        color: #FF9800; /* Green color */
    }
    .icon_blue {
       font-size: 16px; /* Icon size */
        margin-right: 8px; /* Space between icon and text */
        vertical-align: middle; /* Align icon with text */
        justify-content: center;
        align-items: center;
        text-align: center;
        color: #2196F3; /* Green color */
    }
    .icon_red {
        font-size: 16px; /* Icon size */
        margin-right: 8px; /* Space between icon and text */
        vertical-align: middle; /* Align icon with text */
        justify-content: center;
        align-items: center;
        text-align: center;
        color: #7b9acc; /* Green color */
    }
    .icon_Dblue {
       font-size: 16px; /* Icon size */
        margin-right: 8px; /* Space between icon and text */
        vertical-align: middle; /* Align icon with text */
        justify-content: center;
        align-items: center;
        text-align: center;
        color:#414e66 ; /* Green color */
    }
     .kpi-number {
        ; /* Reduce top and bottom margins */
        font-size: 35px; /* Number size */
         /* Bold number */
        display: flex;            /* Use Flexbox */
        justify-content: center;  /* Horizontal centering */
        align-items: center;      /* Vertical centering */
        height: 80%;             /* Ensure full height for vertical alignment */
        margin: 0; 
        margin-left: 10px/* Reset margins */ 
    }
    </style>
    """,    unsafe_allow_html=True
)
st.markdown(
    """
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    """,
    unsafe_allow_html=True,
)


st.markdown("""
    <style>
        .stTabs [data-baseweb="tab-list"] {
            gap: 24px; 
            justify-content: center; 
            border-bottom: 3px solid #ddd;
        }
        .stTabs [data-baseweb="tab"] {
            font-size: 18px;
            padding: 12px 24px;
            border-radius: 12px 12px 0 0;
            background: #f7f7f7;
            color: #2E3A59;
            transition: background 0.3s, color 0.3s;
        }
        .stTabs [aria-selected="true"] {
            background: linear-gradient(90deg, #414e66, #8f94fb);
            color: white;
        }
        .stApp {
            background: #414e66;
        }
    </style>
""", unsafe_allow_html=True)
st.markdown(
    """
    <style>
        div[data-testid="stTabs"] { padding-top: 0rem; }
         h1, .stApp { margin-top: 0rem; margin-bottom: 0rem; }
        </style>
    """,
    unsafe_allow_html=True
)
age_range = st.sidebar.multiselect("Select Age Range", options=df['age_range'].unique())
if age_range:  # Ensure the list is not empty
    filtered_df = df[df['age_range'].isin(age_range)]
else:
    filtered_df = df
st.sidebar.write("")
st.sidebar.write("")
seniority_levels = df['seniority_level'].unique()
selected_level = st.sidebar.selectbox("Select Seniority Level", options=seniority_levels)
st.sidebar.markdown(
    """
    <style>
        .sidebar-space {
            margin-bottom: 160px; /* Adjust space as needed */
        }
    </style>
    <div class="sidebar-space">
    </div>
    """,
    unsafe_allow_html=True
)
st.sidebar.markdown(
    """
    <style>
        .custom-line {
            border: none;
            height: 2px; /* Line thickness */
            background-color: #D0D3D9; /* Change this to any color */
            margin: 10px 0; /* Adjust spacing above & below */
        }
    </style>
    <hr class="custom-line">
    """,
    unsafe_allow_html=True
)
st.sidebar.title("ℹ️ About")
st.sidebar.markdown(
    """
    <style>
        .sidebar-links {
            font-size: 20px;
            font-weight: normal;
            color: #ffffff;
            text-align: left;
            padding: 10px;
        }
        .sidebar-links a {
            text-decoration: none;
            color: #D0D3D9; /* Google Yellow */
            font-weight: normal;
        }
        .sidebar-links a:hover {
            color: #ffffff; /* Hover Color */
        }
        .sidebar-links p {
            margin-bottom: 20px; /* Adds space between links */
        }
    </style>
    <div class="sidebar-links">
        <p>🔗 <a href="https://www.kaggle.com/datasets/parulpandey/2020-it-salary-survey-for-eu-region" target="_blank">Data Source</a></p>
        <p>🛠️ <a href="https://github.com/Yousef-Elattar/IT-Salary-2020/edit/main/Dashboard/salary.py>GitHub Repo</a></p>
        <p>📬 <a href="https://www.linkedin.com/in/yusuf-elattar-43159021b" target="_blank">Contact Me</a></p>
    </div>
    """,
    unsafe_allow_html=True
)

# Create Tabs in Streamlit
tab1, tab2 = st.tabs(["📈 Charts", "📄 Conclusion"])
with tab1:

    # KPI layout with split background
    col1, col2, col3, col4,col5 = st.columns(5)
    
    # KPI with split background
    with col1:
        st.markdown(
            f"""
            <div class="split-kpi">
               <div class="split-top">
                    <span style="margin-top: 15px; display: inline-block"><span class="icon_orange"><i class="fa-solid fa-calendar"></i></span>Average Age</span</span>
                    <h3 class= "kpi-number">{avg_age}</h3>
                </div>
                <div class="split-bottom">
                   between 25-34 Age Range
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Another KPI (for demonstration)
    with col2:
        st.markdown(
     f"""
            <div class="split-kpi">
                <div class="split-top">
                    <span style="margin-top: 15px; display: inline-block"><span class="icon_green"><i class="fas fa-users"></i></span>Total People</span</span>
                    <h3 class= "kpi-number">{total_people}</h3>
                </div>
                <div class="split-bottom" style="background-color: #4CAF50;">
                    with {perc_g_male}% for Male & {perc_g_female}% for Female
                </div>
            </div>
            """ ,
            unsafe_allow_html=True
        )
    
    # Another KPI (with a different bottom color)
    with col3:
        st.markdown(
            f"""
            <div class="split-kpi">
                <div class="split-top">
                    <span style="margin-top: 15px; display: inline-block"><span class="icon_blue"><i class="fas fa-users"></i></span>Average Yearly Salary</span</span>
                    <h3 class= "kpi-number">€ {avg_yearly_salary}</h3>
                </div>
                <div class="split-bottom" style="background-color: #2196F3;">
                    with Average annual bonus hits € {avg_yearly_bonus}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col4:
        st.markdown(
            f"""
            <div class="split-kpi">
                <div class="split-top">
                    <span style="margin-top: 15px; display: inline-block"><span class="icon_red"><i class="fas fa-users"></i></span>Common Age Range</span</span>
                    <h3 class= "kpi-number">{common_age_range}</h3>
                </div>
                <div class="split-bottom" style="background-color: #7b9acc;">
                   with rate {perc_age}%
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col5:
        st.markdown(
            f"""
            <div class="split-kpi">
               <div class="split-top">
                    <span style="margin-top: 15px; display: inline-block"><span class="icon_Dblue"><i class="fa-solid fa-city"></i></span>Top city</span</span>
                    <h3 class= "kpi-number">{top_city}</h3>
                </div>
                <div class="split-bottomDblue" style="background-color: #414e66;color: white !important;">
                   with rate {perc_city}%
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    #my_selection = st.radio("",["Charts","Statistics"],horizontal = True)
    #if my_selection =="Charts":
    
    #emp_status = st.sidebar.selectbox("Select Employment Status", options=df['employment_status'].unique())
    
        
    
    #post_df=df.groupby(['position', 'main_technology']).size().nlargest(8).reset_index(name='count')
    custom_colors = ["#414e66", "#7b9acc", "#ff9800", "#4caf50", "#2196f3"]
    # Ensure post_df is correctly calculated
    post_df = df.groupby(['position', 'main_technology']).size().reset_index(name='count')
    
    # Get the top 9 rows by 'count'
    post_df = post_df.nlargest(9, 'count').sort_values(by='main_technology', ascending=False)
    
    # Create a text label combining position, count, and position percentage
    post_df['text_label'] = (
        post_df['position'] + 
        " (" + post_df['count'].astype(str) + 
        ")"
    )
    # Create bar chart
    fig = px.bar(
        post_df,
        x='main_technology',
        y='count',
        color="position",
        title="Popular Technologies and Their Positions",
        text=post_df["text_label"],  # Show combined position and count
        template="presentation",
        color_discrete_sequence=custom_colors
    )
    
    # Ensure the text appears inside the bars
    fig.update_traces(
        textposition='inside',     # Forces text inside the bar
        insidetextanchor='middle', # Centers the text
        textfont=dict(size=12, color='white')  # Adjust font size and color
    )
    
    # Customize layout
    fig.update_layout(
        barmode="stack",  # Stacked bar chart
        xaxis=dict(title="Technology Usage"),
        yaxis=dict(title="",showgrid=False,visible = False),
        showlegend =False
    )
    
    # Display the chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("<hr style='border: 2px solid #414E66;'>", unsafe_allow_html=True)
    
    col1,col2,col3=st.columns([6,0.2,3])
    
    top_positions = filtered_df["position"].value_counts().nlargest(8).reset_index()
    top_positions.columns = ["position", "Count"]
    
    with col1:
    # Create a bar chart using the correct data
        fig = px.bar(top_positions, x='position', y='Count', 
                 template='presentation', text_auto=True, 
                 title='Top Position filtered by Age Range: ',
                    color_discrete_sequence=["#414e66"])
        fig.update_layout(yaxis=dict(visible=False),xaxis=dict(title=""))
    
    # Display the chart in Streamlit
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("""
            <div style="
                border-left: 2px solid #414E66; 
                height: 400px; 
                display: inline-block;">
            </div>
            """, unsafe_allow_html=True)
    
    
    with col3:
        counts = filtered_df["gender"].value_counts().reset_index()
        counts.columns = ["gender", 'count']
        fig =px.pie(
            counts,
            values="count",
            names="gender"
            ,template = "presentation"
            ,title = "Distribution of Gender filtered by Age Range: ",
            color_discrete_sequence=["#414e66", "#7b9acc"])
        
        fig.update_traces(textinfo='label+percent')
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    st.markdown("<hr style='border: 2px solid #414E66;'>", unsafe_allow_html=True)
    avg_experience = df.groupby("seniority_level")["total_experience_years"].mean().sort_values(ascending =False).reset_index()
    fig = px.bar(
        avg_experience,
        x="seniority_level",
        y="total_experience_years",
        text="total_experience_years",
        title="Average Years of Experience Required for Each Seniority Level: ",
        template="presentation",
        color_discrete_sequence=["#414e66"]
    )
    
    # Customize chart appearance
    fig.update_traces(texttemplate='%{text:.1f} years', textposition="auto")
    fig.update_layout(
        xaxis_title="",
        yaxis_title="",
        showlegend=False,
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False,visible =False)
    )
    st.plotly_chart(fig, use_container_width=True)
    
    
    
    st.markdown("<hr style='border: 2px solid #414E66;'>", unsafe_allow_html=True)
    
    
    col1,col2,col3 = st.columns([6,0.2,3])
    with col1:
            counts_age = df["age_range"].value_counts(ascending = True).reset_index()
            counts_age.columns = ["age_range", 'count']
    
            fig = px.bar(
                counts_age,
                x="count",  # Horizontal bar: x-axis for the count
                y="age_range",  # y-axis for the age range
                orientation='h',  # Horizontal bar chart
                template="presentation",
                text="count",
                title="Distribution of Age Range: ",
                color_discrete_sequence=["#414e66"]
            )
            
            # Optional: Customize layout
            fig.update_layout(yaxis=dict(title=""), xaxis=dict(title="",visible = False))
            
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("""
            <div style="
                border-left: 2px solid #414E66; 
                height: 400px; 
                display: inline-block;">
            </div>
            """, unsafe_allow_html=True)
    
    with col3:
        contract_ct = df["contract_duration"].value_counts().reset_index()
        contract_ct.columns = ["contract_duration", 'count']
        fig =px.pie(
            contract_ct,
            values="count",
            names="contract_duration"
            ,template = "presentation"
            ,title = "Distribution of Contract Duration: ",
            color_discrete_sequence=["#414e66", "#7b9acc"],
        hole = 0.3)
        
        fig.update_traces(textinfo='label+percent')
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    st.markdown("<hr style='border: 2px solid #414E66;'>", unsafe_allow_html=True)
    
    st.write("## Experience vs Salary Analysis by Seniority Level")
    
    # Filter by seniority level
    
    # Filtered DataFrame
    filtered_df = df[df['seniority_level'] == selected_level]
    
    # Scatter Plot: Years of Experience vs Yearly Salary
    st.subheader("Years of Experience vs Yearly Salary")
    fig_scatter = px.scatter(
        filtered_df, 
        x='total_experience_years', 
        y='yearly_salary_eur', 
        color='seniority_level',
        color_discrete_sequence=["#414e66"],
        title=f"Experience vs Salary for {selected_level}",
        size_max=15, 
        template='presentation'
    )
    fig_scatter.update_traces(marker=dict(size=10, opacity=0.8))
    fig_scatter.update_layout(
        xaxis_title="Years of Experience",
        yaxis_title="Yearly Salary (EUR)",
        showlegend=False,
        xaxis=dict(showgrid=False),  
        yaxis=dict(showgrid=False)
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    # Box Plot: Distribution of Yearly Salary by Experience Range
    st.subheader("Salary Distribution by Experience")
    
    # Create experience bins
    bins = [0, 2, 5, 10, 15, 20, 30]
    labels = ['0-2 years', '3-5 years', '6-10 years', '11-15 years', '16-20 years', '20+ years']
    df['experience_range'] = pd.cut(df['total_experience_years'], bins=bins, labels=labels)
    
    # Filtered DataFrame with experience bins
    filtered_df = df[df['seniority_level'] == selected_level]
    
    fig_box = px.box(
        filtered_df, 
        x='experience_range', 
        y='yearly_salary_eur',
        title=f"Salary Distribution by Experience for {selected_level}",
        color='experience_range',
        color_discrete_sequence=custom_colors,
        template='presentation'
    )
    fig_box.update_layout(
        xaxis_title="Experience Range",
        yaxis_title="Yearly Salary (EUR)",
        showlegend=False,
        xaxis=dict(showgrid=False),  
        yaxis=dict(showgrid=False) 
    )
    st.plotly_chart(fig_box, use_container_width=True)
    
    st.markdown("<hr style='border: 2px solid #414E66;'>", unsafe_allow_html=True)



    
    st.write("## 🏦 Company Types & Sizes Overview")
    col1,col2,col3=st.columns([4,1,4])
    with col1:
        type_counts = df['company_type'].value_counts().nlargest(6).reset_index()
        type_counts.columns = ['company_type', 'Count']
        fig1 = px.bar(
            type_counts, x='company_type', y='Count',
            title='Distribution of Company Type(Top 6)',
            text='Count', color_discrete_sequence=['#414e66']
        )
        fig1.update_layout(
        xaxis_title="",
        yaxis_title="",
        showlegend=False,
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False,visible =False)
    )
        st.plotly_chart(fig1, use_container_width=True)
        
    with col3:
    # Aggregate data for Company Size
        size_counts = df['company_size'].value_counts().reset_index()
        size_counts.columns = ['company_size', 'Count']
        
        # Create separate bar charts
        
        fig2 = px.bar(
            size_counts, x='company_size', y='Count',
            title='Distribution of Company Size',
            text='Count', color_discrete_sequence=['#414e66']
    
        )
        fig2.update_layout(
        xaxis_title="",
        yaxis_title="",
        showlegend=False,
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False,visible =False)
    )
        st.plotly_chart(fig2, use_container_width=True)





with tab2:
    # Custom CSS for design
    st.markdown("""
    <style>
        .stApp {
            background-color: #F8F9F9;
        }
        
        /* Title Styling */
        .title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #2C3E50;
        }
        
        /* Section Headers */
        .section-header {
            font-size: 24px;
            font-weight: bold;
            color: #2471A3;
            margin-top: 30px;
        }

        /* Subsection Headers */
        .sub-header {
            font-size: 20px;
            font-weight: bold;
            color: #1A5276;
        }

        /* Content Text */
        .content {
            font-size: 16px;
            color: #17202A;
        }

        /* Divider Line */
        hr {
            border: none;
            height: 2px;
            background-color: #2C3E50;
            margin: 20px 0;
        }

        /* Highlight Box */
        .highlight {
            padding: 10px;
            background-color: #D5DBDB;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            color: #17202A;
            text-align: center;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Title
    st.markdown("<h1 class='title'>📄 Conclusion</h1>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)  # Divider line
    
    # ---- Section 1: Yearly Salary ----
    st.markdown("<h2 class='section-header'>💰 Yearly Salary Insights</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    - **Salary Range:** *30,000 to 120,000 Euros/year.*
    - **Central Tendency:**
      - Mean: **70,370.07 Euros** (higher than median & mode)
      - Median: **70,000 Euros**
      - Mode: **70,000 Euros** (most common salary)
    - **Distribution Shape:** Right-skewed due to high salaries pulling the mean upwards.
    - **Salary Groups:**  
      - Lower 25%: **≤ 60,000 Euros**
      - Middle 50%: **60,000 – 80,000 Euros** *(most employees)*
      - Upper 25%: **> 80,000 Euros**
    """)
    
    st.markdown("<div class='highlight'>👉 Insight: Salaries are right-skewed, with most employees earning 60,000–80,000 Euros/year.</div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # ---- Section 2: Gender, Age, and City Insights ----
    st.markdown("<h2 class='section-header'>👥 Gender, Age, and City Insights</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    - **Gender Distribution:**  
      - The workforce is **84.6% male**, reflecting a stereotype favoring men in logical fields.
    
    - **Age Distribution:**  
      - Majority aged **25-34 (64.4%)** and **35-40 (22.2%)**.
      - Only **0.91%** of employees are over **50 years old**.
    
    - **City Distribution:**  
      - **Germany-focused** survey.
      - Majority from **Berlin (55.2%)** and **Munich (19.5%)**.
    """)
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # ---- Section 3: Job Insights ----
    st.markdown("<h2 class='section-header'>💼 Job Insights</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    - **Most Common Positions:**  
      - Software Engineer **(31.97%)** 🖥️
      - Backend Developer **(14.25%)** 🔗
      - Data Scientist **(8.6%)** 📊
      - Frontend Developer **(7.3%)** 🎨
    
    - **Seniority Levels:**  
      - Senior **(46.05%)**  
      - Middle **(29.28%)**  
      - Lead **(13.47%)**  
    
    - **Top Programming Languages:**  
      - Python **(21.29%)** 🐍  
      - Java **(18.16%)** ☕  
      - JavaScript **(11.29%)**  
    
    - **Employment Status:**  
      - **97.05%** Full-time  
      - **95.31%** Unlimited contracts  
    """)
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # ---- Section 4: Company Insights ----
    st.markdown("<h2 class='section-header'>🏢 Company Insights</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    - **Company Types:**  
      - Product Companies **(62.47%)**  
      - Startups **(20.16%)**  
      - Consulting Firms **(11.09%)**  
    
    - **Company Size:**  
      - **1000+ employees (36.06%)**  
      - **101-1000 employees (33.01%)**  
      - **11-50 employees (14.16%)**  
    
    - **Work Languages:**  
      - English **(82.97%)** 🌍  
      - German **(14.68%)** 🇩🇪  
    
    - **Vacation Days:**  
      - Most employees receive **30 days off (40.66%)** ☀️  
    
    - **COVID-19 Impact:**  
      - **Only 4.78%** lost jobs due to the pandemic.  
    """)
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # ---- Section 5: Final Takeaways ----
    st.markdown("<h2 class='section-header'>🔮 Final Takeaways</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    - **No significant correlation** between Yearly Salary and factors like Age, Years of Experience, or Yearly Bonus.
    - **Salary levels are determined by skills & talent,** not just experience or age.
    """)
    
    st.markdown("<div class='highlight'>🎯 Conclusion: IT salaries depend more on skills and talent than traditional factors like age or experience.</div>", unsafe_allow_html=True)
    
    # ---- Footer ----
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 14px;'>📊 Powered by Data | Created with ❤️ using Streamlit</p>", unsafe_allow_html=True)
    
            
        
            
