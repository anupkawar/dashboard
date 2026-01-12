"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                           PROJECT IOCL                                       ║
║              HR Analytics Dashboard - IOCL ERPL HQ Guwahati                  ║
║                     Professional HR Management System                        ║
╚══════════════════════════════════════════════════════════════════════════════╝

Developer: Apprentice
Technology Stack: Streamlit, Pandas, Plotly
Version: 1.0.1
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, date
import warnings
warnings.filterwarnings('ignore')
from PIL import Image
from io import BytesIO

# ═══════════════════════════════════════════════════════════════════════════
# PAGE CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="HR Analytics Dashboard",
    page_icon="⛽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ═══════════════════════════════════════════════════════════════════════════
# CUSTOM CSS STYLING - Professional IOCL Theme
# ═══════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    * {
        font-family: 'Inter', 'Segoe UI', sans-serif;
    }

    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #eef2f7 100%);
        padding: 0.5rem;
    }

    .header-container {
        background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 50%, #2563eb 100%);
        padding: 1.5rem 2rem;
        border-radius: 15px;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        border-left: 8px solid #f97316;
    }

    .header-title {
        color: #ffffff;
        font-size: 2.2rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.5px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }

    .header-subtitle {
        color: #fde68a;
        font-size: 1.1rem;
        font-weight: 500;
        margin: 0.3rem 0 0 0;
    }

    [data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 700;
        color: #1e40af;
    }

    [data-testid="stMetricLabel"] {
        font-size: 0.95rem;
        font-weight: 600;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    div[data-testid="metric-container"] {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        padding: 1.2rem 1.5rem;
        border-radius: 12px;
        border-left: 5px solid #f97316;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    div[data-testid="metric-container"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.12);
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e3a8a 0%, #1e40af 100%);
        padding: 1rem 0.5rem;
    }

    [data-testid="stSidebar"] .stMarkdown {
        color: #ffffff;
    }

    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3 {
        color: #fde68a;
        font-weight: 700;
    }

    .stButton>button {
        background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);
        color: white;
        font-weight: 600;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 2rem;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(249, 115, 22, 0.3);
    }

    .stButton>button:hover {
        background: linear-gradient(135deg, #ea580c 0%, #c2410c 100%);
        box-shadow: 0 6px 20px rgba(249, 115, 22, 0.4);
        transform: translateY(-2px);
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #f1f5f9;
        padding: 0.5rem;
        border-radius: 10px;
    }

    .stTabs [data-baseweb="tab"] {
        background-color: #ffffff;
        color: #334155;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.7rem 1.5rem;
        font-size: 0.95rem;
        border: 2px solid transparent;
        transition: all 0.3s ease;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);
        color: white;
        border-color: #f97316;
    }

    .dataframe {
        font-size: 0.9rem;
        border-radius: 10px;
        overflow: hidden;
    }

    .dataframe thead tr th {
        background: linear-gradient(135deg, #1e40af 0%, #2563eb 100%);
        color: white;
        font-weight: 700;
        padding: 12px;
        text-align: left;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .dataframe tbody tr:hover {
        background-color: #fef3c7;
        transition: background-color 0.2s ease;
    }

    .streamlit-expanderHeader {
        background-color: #f1f5f9;
        color: #1e40af;
        font-weight: 600;
        border-radius: 8px;
        border-left: 4px solid #f97316;
    }

    .stDownloadButton>button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.6rem 1.5rem;
        border: none;
        transition: all 0.3s ease;
    }

    .stDownloadButton>button:hover {
        background: linear-gradient(135deg, #059669 0%, #047857 100%);
        box-shadow: 0 6px 20px rgba(16, 185, 129, 0.3);
    }

    .js-plotly-plot {
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    }

    hr {
        margin: 2rem 0;
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #f97316, transparent);
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
# DATA LOADING AND PREPROCESSING
# ═══════════════════════════════════════════════════════════════════════════

@st.cache_data(show_spinner=False)
def load_data():
    """Load and preprocess employee data with error handling"""
    try:
        df = pd.read_excel('emp_data.xlsx')

        # Data Cleaning and Preprocessing
        df['Employee No.'] = df['Employee No.'].astype(str)
        df['Full Name'] = df['First Name'] + ' ' + df['Last Name']

        # Date Conversions
        date_columns = ['Date of Joining Corporation', 'Birth Date', 'Date of Marriage', 
                       'Date in Current Position', 'Date in Current Grade as per Seniority']

        for col in date_columns:
            df[col] = pd.to_datetime(df[col], format='%d.%m.%Y', errors='coerce')

        # Calculate Age
        current_date = datetime.now()
        df['Age'] = ((current_date - df['Birth Date']).dt.days / 365.25).round(0).astype('Int64')

        # Calculate Experience
        df['Experience (Years)'] = ((current_date - df['Date of Joining Corporation']).dt.days / 365.25).round(1)

        # Calculate Tenure in Current Position
        df['Tenure in Position (Years)'] = ((current_date - df['Date in Current Position']).dt.days / 365.25).round(1)

        # Age Groups
        def categorize_age(age):
            if pd.isna(age):
                return 'Unknown'
            elif age < 30:
                return '<30'
            elif age < 40:
                return '30-39'
            elif age < 50:
                return '40-49'
            elif age < 60:
                return '50-59'
            else:
                return '60+'

        df['Age Group'] = df['Age'].apply(categorize_age)

        # Experience Groups
        def categorize_experience(exp):
            if pd.isna(exp):
                return 'Unknown'
            elif exp < 5:
                return '0-5 years'
            elif exp < 10:
                return '5-10 years'
            elif exp < 15:
                return '10-15 years'
            elif exp < 20:
                return '15-20 years'
            else:
                return '20+ years'

        df['Experience Group'] = df['Experience (Years)'].apply(categorize_experience)

        # Clean Location Names
        df['Location'] = df['Personnel Area'].str.replace('ERPL, ', '', regex=False)

        # Fill missing values
        df['Minority'] = df['Minority'].fillna('NO')
        df['Whether Physically Handicap'] = df['Whether Physically Handicap'].fillna('NO')

        return df

    except Exception as e:
        st.error(f"❌ Error loading data: {str(e)}")
        return None

# ═══════════════════════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

def create_chart_title(text):
    """Create standardized chart title - NO WEIGHT PROPERTY"""
    return dict(
        text=text,
        font=dict(size=18, color='#1e40af', family='Inter'),
        x=0.5,
        xanchor='center'
    )

def display_employee_list(df, category, value):
    """Display list of employees for a specific category"""
    with st.expander(f"👥 View Employees: {value} ({len(df)} employees)", expanded=False):
        display_df = df[['Employee No.', 'Full Name', 'Designation', 'Location', 
                        'Personnel Sub Area', 'Email Id']].copy()
        display_df.columns = ['Employee ID', 'Name', 'Designation', 'Location', 
                             'Department', 'Email']

        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True,
            height=min(400, len(display_df) * 35 + 38)
        )

        csv = display_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label=f"📥 Download {value} Employee List",
            data=csv,
            file_name=f"IOCL_{value}_employees_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv",
            key=f"download_{category}_{value}"
        )

# ═══════════════════════════════════════════════════════════════════════════
# MAIN APPLICATION
# ═══════════════════════════════════════════════════════════════════════════

def main():
    # Load Data
    with st.spinner('🔄 Loading HR Data...'):
        df = load_data()

    if df is None:
        st.stop()

    # ═══════════════════════════════════════════════════════════════════════
    # SIDEBAR - AND FILTERS
    # ═══════════════════════════════════════════════════════════════════════

    with st.sidebar:

        st.markdown("### 🔍 Global Filters")

        # Location Filter
        locations = ['All Locations'] + sorted(df['Location'].unique().tolist())
        selected_location = st.selectbox(
            "📍 Select Location",
            locations,
            key='location_filter'
        )

        # Department Filter
        departments = ['All Departments'] + sorted(df['Personnel Sub Area'].unique().tolist())
        selected_department = st.selectbox(
            "🏢 Select Department",
            departments,
            key='dept_filter'
        )

        # Gender Filter
        genders = ['All'] + sorted(df['Gender'].unique().tolist())
        selected_gender = st.selectbox(
            "👤 Select Gender",
            genders,
            key='gender_filter'
        )

        # Cadre Filter
        cadres = ['All Cadres'] + sorted(df['Cadre'].unique().tolist())
        selected_cadre = st.selectbox(
            "🎓 Select Cadre",
            cadres,
            key='cadre_filter'
        )

        # Age Range Filter
        st.markdown("**Age Range**")
        min_age = int(df['Age'].min()) if not df['Age'].isna().all() else 20
        max_age = int(df['Age'].max()) if not df['Age'].isna().all() else 70
        age_range = st.slider(
            "Select Age Range",
            min_value=min_age,
            max_value=max_age,
            value=(min_age, max_age),
            key='age_filter'
        )

        st.markdown("---")

        # CORRECTED RESET LOGIC TO PREVENT INFINITE LOOP
        if st.button("🔄 RESET ALL FILTERS", use_container_width=True, type="primary"):
            # Clear all keys in session state to force widgets back to defaults
            for key in st.session_state.keys():
                del st.session_state[key]
            # Trigger a single clean rerun
            st.rerun()

        st.markdown("---")

    # Apply filters to data
    filtered_df = df.copy()

    if selected_location != 'All Locations':
        filtered_df = filtered_df[filtered_df['Location'] == selected_location]

    if selected_department != 'All Departments':
        filtered_df = filtered_df[filtered_df['Personnel Sub Area'] == selected_department]

    if selected_gender != 'All':
        filtered_df = filtered_df[filtered_df['Gender'] == selected_gender]

    if selected_cadre != 'All Cadres':
        filtered_df = filtered_df[filtered_df['Cadre'] == selected_cadre]

    filtered_df = filtered_df[
        (filtered_df['Age'] >= age_range[0]) & 
        (filtered_df['Age'] <= age_range[1])]
    
    # ← ADD THIS BLOCK HERE ←
    if len(filtered_df) == 0:
        st.warning("⚠️ No data matches the selected filters. Please adjust your criteria.")
        st.info("💡 Try resetting filters using the 'Reset All Filters' button in the sidebar.")
        st.stop()  # Stops execution, prevents all errors
    
    # HEADER SECTION
    # Using 3 columns: [Logo Area, Main Header Area, Spacer for Symmetry]
    head_col1, head_col2, head_col3 = st.columns([1, 4, 1])
    
    with head_col1:
        try:
            logo_img = Image.open('Logo.png')
            st.image(logo_img, width=120) # Adjusted size for better fit
        except:
            st.markdown("### 🛢️")
    
    with head_col2:
        st.markdown("""
        <div class='header-container' style='text-align: center;'>
            <h1 class='header-title'>HR Analytics Dashboard</h1>
            <p class='header-subtitle'>
                GSPL HQ Guwahati | Indian Oil Corporation Ltd.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with head_col3:
        # Empty column to push the blue box into the center
        pass

    st.markdown("<br>", unsafe_allow_html=True)

    # KEY METRICS SECTION
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            label="👥 Total Employees",
            value=f"{len(filtered_df):,}",
            delta=f"{len(filtered_df)/len(df)*100:.1f}% of total"
        )

    with col2:
        avg_age = filtered_df['Age'].mean()
        st.metric(
            label="📅 Average Age",
            value=f"{avg_age:.1f} years" if not pd.isna(avg_age) else "N/A"
        )

    with col3:
        avg_exp = filtered_df['Experience (Years)'].mean()
        st.metric(
            label="⏱️ Avg Experience",
            value=f"{avg_exp:.1f} years" if not pd.isna(avg_exp) else "N/A"
        )

    with col4:
        male_count = len(filtered_df[filtered_df['Gender'] == 'Male'])
        st.metric(
            label="👨 Male Employees",
            value=f"{male_count:,}",
            delta=f"{male_count/len(filtered_df)*100:.1f}%" if len(filtered_df) > 0 else "0%"
        )

    with col5:
        female_count = len(filtered_df[filtered_df['Gender'] == 'Female'])
        st.metric(
            label="👩 Female Employees",
            value=f"{female_count:,}",
            delta=f"{female_count/len(filtered_df)*100:.1f}%" if len(filtered_df) > 0 else "0%"
        )

    st.markdown("---")

    # TABS NAVIGATION
    tab1, tab2, tab3, tab4, tab5, tab8, tab6 = st.tabs([
        "🏠 Overview",
        "📍 Location Analysis",
        "🏢 Department Analysis",
        "🎓 Education & Skills",
        "👥 Demographics",
        "📋 Employee Directory",
        "🎂 Events & Milestones"
    ])


    # ═══════════════════════════════════════════════════════════════════════
    # TAB 1: OVERVIEW
    # ═══════════════════════════════════════════════════════════════════════

    with tab1:
        st.markdown(" ")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 📊 Workforce Distribution by Location")

            location_data = filtered_df['Location'].value_counts().reset_index()
            location_data.columns = ['Location', 'Count']

            fig_location = px.pie(
                location_data,
                values='Count',
                names='Location',
                color_discrete_sequence=px.colors.sequential.Oranges_r,
                hole=0.4
            )

            fig_location.update_layout(
                title=create_chart_title('🌍 Employee Distribution by Location'),
                height=450,
                showlegend=True,
                paper_bgcolor='rgba(255,255,255,0.95)'
            )

            st.plotly_chart(fig_location, use_container_width=True)

            selected_loc = st.selectbox(
                "Select location to view employees:",
                location_data['Location'].tolist(),
                key='overview_loc'
            )

            if selected_loc:
                loc_df = filtered_df[filtered_df['Location'] == selected_loc]
                display_employee_list(loc_df, 'Location', selected_loc)

        with col2:
            st.markdown("### 🏢 Department Wise Distribution")

            dept_data = filtered_df['Personnel Sub Area'].value_counts().head(10).reset_index()
            dept_data.columns = ['Department', 'Count']

            fig_dept = go.Figure(data=[
                go.Bar(
                    x=dept_data['Count'],
                    y=dept_data['Department'],
                    orientation='h',
                    marker=dict(
                        color=dept_data['Count'],
                        colorscale='Blues',
                        line=dict(color='#ffffff', width=1)
                    ),
                    text=dept_data['Count'],
                    textposition='auto',
                    hovertemplate='<b>%{y}</b><br>Employees: %{x}<extra></extra>'
                )
            ])

            fig_dept.update_layout(
                title=create_chart_title('🏢 Top 10 Departments by Headcount'),
                xaxis_title="Number of Employees",
                yaxis_title="",
                height=450,
                paper_bgcolor='rgba(255,255,255,0.95)',
                plot_bgcolor='rgba(255,255,255,0.95)',
                margin=dict(l=20, r=20, t=60, b=20),
                yaxis=dict(autorange="reversed")
            )

            st.plotly_chart(fig_dept, use_container_width=True)

            selected_dept = st.selectbox(
                "Select department to view employees:",
                dept_data['Department'].tolist(),
                key='overview_dept'
            )

            if selected_dept:
                dept_df = filtered_df[filtered_df['Personnel Sub Area'] == selected_dept]
                display_employee_list(dept_df, 'Department', selected_dept)

        st.markdown("---")

        col3, col4 = st.columns(2)

        with col3:
            st.markdown("### 👥 Gender Distribution")

            gender_data = filtered_df['Gender'].value_counts().reset_index()
            gender_data.columns = ['Gender', 'Count']

            colors = {'Male': '#2563eb', 'Female': '#ec4899'}

            fig_gender = go.Figure(data=[
                go.Pie(
                    labels=gender_data['Gender'],
                    values=gender_data['Count'],
                    marker=dict(
                        colors=[colors.get(g, '#94a3b8') for g in gender_data['Gender']],
                        line=dict(color='#ffffff', width=3)
                    ),
                    textinfo='label+percent+value',
                    textfont=dict(size=14, family='Inter', color='white'),
                    hole=0.5,
                    hovertemplate='<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent}<extra></extra>'
                )
            ])

            fig_gender.update_layout(
                title=create_chart_title('👥 Gender Distribution Analysis'),
                height=400,
                showlegend=True,
                legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
                paper_bgcolor='rgba(255,255,255,0.95)',
                annotations=[dict(text='Gender<br>Split', x=0.5, y=0.5, font_size=16, showarrow=False)]
            )

            st.plotly_chart(fig_gender, use_container_width=True)

            # NEW INTERACTIVE SECTION FOR GENDER
            gender_list = gender_data['Gender'].tolist()
            
            selected_gen = st.selectbox(
                "Select gender to view employees:",
                options=gender_list,
                key='gender_view_selector' # Unique key for this tab
            )

            if selected_gen:
                gen_df = filtered_df[filtered_df['Gender'] == selected_gen]
                display_employee_list(gen_df, 'Gender', selected_gen)

        with col4:
            st.markdown("### 📅 Age Group Distribution")

            age_group_data = filtered_df['Age Group'].value_counts().reset_index()
            age_group_data.columns = ['Age Group', 'Count']

            age_order = ['<30', '30-39', '40-49', '50-59', '60+', 'Unknown']
            age_group_data['Age Group'] = pd.Categorical(
                age_group_data['Age Group'],
                categories=age_order,
                ordered=True
            )
            age_group_data = age_group_data.sort_values('Age Group')

            fig_age = go.Figure(data=[
                go.Bar(
                    x=age_group_data['Age Group'],
                    y=age_group_data['Count'],
                    marker=dict(
                        color=age_group_data['Count'],
                        colorscale='Oranges',
                        line=dict(color='#ffffff', width=2)
                    ),
                    text=age_group_data['Count'],
                    textposition='outside',
                    hovertemplate='<b>Age: %{x}</b><br>Employees: %{y}<extra></extra>'
                )
            ])

            fig_age.update_layout(
                title=create_chart_title('📅 Employee Age Distribution'),
                xaxis_title="Age Group",
                yaxis_title="Number of Employees",
                height=400,
                paper_bgcolor='rgba(255,255,255,0.95)',
                plot_bgcolor='rgba(255,255,255,0.95)',
                margin=dict(l=20, r=20, t=60, b=20)
            )

            st.plotly_chart(fig_age, use_container_width=True)

    # ═══════════════════════════════════════════════════════════════════════
    # TAB 2: LOCATION ANALYSIS
    # ═══════════════════════════════════════════════════════════════════════

    with tab2:
        st.markdown(" ")

        location_summary = filtered_df.groupby('Location').agg({
            'Employee No.': 'count',
            'Age': 'mean',
            'Experience (Years)': 'mean'
        }).reset_index()
        location_summary.columns = ['Location', 'Total Employees', 'Avg Age', 'Avg Experience']
        location_summary = location_summary.sort_values('Total Employees', ascending=False)

        st.markdown("### 📊 Location Summary Statistics")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("🌍 Total Locations", len(location_summary))
        with col2:
            st.metric("👥 Largest Location", location_summary.iloc[0]['Location'])
        with col3:
            st.metric("📊 Headcount", int(location_summary.iloc[0]['Total Employees']))
        with col4:
            avg_per_loc = location_summary['Total Employees'].mean()
            st.metric("📈 Avg per Location", f"{avg_per_loc:.0f}")

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            fig_loc_bar = go.Figure(data=[
                go.Bar(
                    x=location_summary['Location'],
                    y=location_summary['Total Employees'],
                    marker=dict(
                        color=location_summary['Total Employees'],
                        colorscale='RdYlGn',
                        line=dict(color='#ffffff', width=2)
                    ),
                    text=location_summary['Total Employees'],
                    textposition='outside',
                    hovertemplate='<b>%{x}</b><br>Employees: %{y}<extra></extra>'
                )
            ])

            fig_loc_bar.update_layout(
                title=create_chart_title('📍 Headcount by Location'),
                xaxis_title="Location",
                yaxis_title="Number of Employees",
                height=450,
                paper_bgcolor='rgba(255,255,255,0.95)',
                plot_bgcolor='rgba(255,255,255,0.95)'
            )

            st.plotly_chart(fig_loc_bar, use_container_width=True)

            # NEW INTERACTIVE SECTION FOR LOCATION TAB
            loc_list_tab2 = sorted(location_summary['Location'].tolist())
            
            # Defaulting to Guwahati if it exists in the filtered list
            default_ix_loc = loc_list_tab2.index("Guwahati") if "Guwahati" in loc_list_tab2 else 0

            selected_loc_tab2 = st.selectbox(
                "Select Location to view employees:",
                options=loc_list_tab2,
                index=default_ix_loc,
                key='location_tab_selector'
            )

            if selected_loc_tab2:
                loc_tab_df = filtered_df[filtered_df['Location'] == selected_loc_tab2]
                display_employee_list(loc_tab_df, 'Location_Tab', selected_loc_tab2)

        with col2:
            loc_dept = filtered_df.groupby(['Location', 'Personnel Sub Area']).size().reset_index(name='Count')
            top_loc_dept = loc_dept.nlargest(15, 'Count')

            fig_sunburst = px.sunburst(
                top_loc_dept,
                path=['Location', 'Personnel Sub Area'],
                values='Count',
                color='Count',
                color_continuous_scale='Oranges'
            )

            fig_sunburst.update_layout(
                title=create_chart_title('🌐 Location-Department Hierarchy'),
                height=450,
                paper_bgcolor='rgba(255,255,255,0.95)'
            )

            st.plotly_chart(fig_sunburst, use_container_width=True)

            # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        # TREEMAP: FADING DECREASING ORDER (Deep Navy -> Soft Grey)
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        st.markdown("### 🗺️ Organizational Structure Treemap")
        if not filtered_df.empty:
            tm_data = filtered_df.groupby(["Location", "Personnel Sub Area"]).size().reset_index(name="Headcount")
            
            # Professional Fading Scale: Darker colors for higher headcount, lighter for lower
            fading_eye_safe_scale = ["#cbd5e1", "#94a3b8", "#475569", "#1e3a8a"] # Reversed for visual hierarchy
            
            fig_tm = px.treemap(
                tm_data,
                path=["Location", "Personnel Sub Area"],
                values="Headcount",
                color="Headcount",
                color_continuous_scale=fading_eye_safe_scale,
                hover_data={"Headcount": ":,"},
            )
            
            fig_tm.update_traces(
                textinfo="label+value",
                textfont=dict(size=14, family="Inter", color="white"),
                marker=dict(line=dict(width=1.5, color="#f8fafc")), # Subtle separation
                hovertemplate='<b>%{label}</b><br>Employees: %{value}<extra></extra>'
            )
            
            fig_tm.update_layout(
                margin=dict(l=0, r=0, t=30, b=0),
                height=550,
                coloraxis_colorbar=dict(title="Headcount", thickness=15)
            )
            
            st.plotly_chart(fig_tm, use_container_width=True, key="tm_location_fading", config={'displayModeBar': False})

            # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            # SUBSET INSPECTOR (Click-Alternative for Drilldown)
            # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            st.markdown(" ")
            st.caption("Drill down into any block above to view the specific list of employees.")
            
            ins1, ins2 = st.columns(2)
            with ins1:
                inspect_loc = st.selectbox(
                    "1. Select Location (Outer Box)", 
                    options=sorted(filtered_df['Location'].unique()),
                    key="tm_insp_loc_final"
                )
            with ins2:
                available_subs = sorted(filtered_df[filtered_df['Location'] == inspect_loc]['Personnel Sub Area'].unique())
                inspect_sub = st.selectbox(
                    f"2. Select Subset in {inspect_loc} (Inner Box)", 
                    options=["All Subsets"] + available_subs,
                    key="tm_insp_sub_final"
                )

            # Filter data for display
            final_subset_df = filtered_df[filtered_df['Location'] == inspect_loc]
            if inspect_sub != "All Subsets":
                final_subset_df = final_subset_df[final_subset_df['Personnel Sub Area'] == inspect_sub]
            
            # Use professional helper function from iocl_dashboardf.py
            display_employee_list(final_subset_df, "Treemap_Drilldown", f"{inspect_loc} - {inspect_sub}")
            
        else:
            st.warning("⚠️ No data available for the Treemap with current filters.")

        st.markdown("---")

            
            

    # ═══════════════════════════════════════════════════════════════════════
    # TAB 3: DEPARTMENT ANALYSIS
    # ═══════════════════════════════════════════════════════════════════════

    with tab3:
        st.markdown("### 🏢 Department-wise Comprehensive Analysis")

        dept_summary = filtered_df.groupby('Personnel Sub Area').agg({
            'Employee No.': 'count',
            'Age': 'mean',
            'Experience (Years)': 'mean'
        }).reset_index()
        dept_summary.columns = ['Department', 'Total Employees', 'Avg Age', 'Avg Experience']
        dept_summary = dept_summary.sort_values('Total Employees', ascending=False)

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("🏢 Total Departments", len(dept_summary))
        with col2:
            st.metric("👥 Largest Department", dept_summary.iloc[0]['Department'])
        with col3:
            st.metric("📊 Size", int(dept_summary.iloc[0]['Total Employees']))
        with col4:
            st.metric("📈 Avg per Dept", f"{dept_summary['Total Employees'].mean():.0f}")

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            top_depts = dept_summary.head(10)

            fig_dept_top = go.Figure(data=[
                go.Bar(
                    y=top_depts['Department'],
                    x=top_depts['Total Employees'],
                    orientation='h',
                    marker=dict(
                        color=top_depts['Total Employees'],
                        colorscale='Teal',
                        line=dict(color='#ffffff', width=2)
                    ),
                    text=top_depts['Total Employees'],
                    textposition='auto',
                    hovertemplate='<b>%{y}</b><br>Employees: %{x}<extra></extra>'
                )
            ])

            fig_dept_top.update_layout(
                title=create_chart_title('🏆 Top 10 Departments by Headcount'),
                xaxis_title="Number of Employees",
                yaxis_title="",
                height=500,
                yaxis=dict(autorange="reversed"),
                paper_bgcolor='rgba(255,255,255,0.95)',
                plot_bgcolor='rgba(255,255,255,0.95)'
            )

            st.plotly_chart(fig_dept_top, use_container_width=True)

        with col2:
            fig_treemap = px.treemap(
                dept_summary,
                path=['Department'],
                values='Total Employees',
                color='Avg Age',
                color_continuous_scale='RdYlGn_r',
                hover_data={'Avg Experience': ':.1f'}
            )

            fig_treemap.update_layout(
                title=create_chart_title('🗺️ Department Size Treemap'),
                height=500,
                paper_bgcolor='rgba(255,255,255,0.95)'
            )

            st.plotly_chart(fig_treemap, use_container_width=True)

        st.markdown("---")

        st.markdown("### 👥 Gender Distribution Across Departments")

        dept_gender = filtered_df.groupby(['Personnel Sub Area', 'Gender']).size().reset_index(name='Count')
        top_depts_list = dept_summary.head(10)['Department'].tolist()
        dept_gender_filtered = dept_gender[dept_gender['Personnel Sub Area'].isin(top_depts_list)]

        fig_gender_dept = px.bar(
            dept_gender_filtered,
            x='Personnel Sub Area',
            y='Count',
            color='Gender',
            barmode='group',
            color_discrete_map={'Male': '#2563eb', 'Female': '#ec4899'},
            text='Count'
        )

        fig_gender_dept.update_traces(textposition='outside')

        fig_gender_dept.update_layout(
            title=create_chart_title('👥 Gender Distribution in Top Departments'),
            xaxis_title="Department",
            yaxis_title="Number of Employees",
            height=450,
            xaxis={'tickangle': -45},
            paper_bgcolor='rgba(255,255,255,0.95)',
            plot_bgcolor='rgba(255,255,255,0.95)',
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )

        st.plotly_chart(fig_gender_dept, use_container_width=True)

    # ═══════════════════════════════════════════════════════════════════════
    # TAB 4: EDUCATION & SKILLS
    # ═══════════════════════════════════════════════════════════════════════

    with tab4:
        st.markdown("### 🎓 Education & Skill Analysis")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            unique_quals = filtered_df['Prescribed Induction Level Qualification'].nunique()
            st.metric("📚 Qualification Types", unique_quals)
        with col2:
            unique_cadres = filtered_df['Cadre'].nunique()
            st.metric("🎓 Cadre Types", unique_cadres)
        with col3:
            unique_edu = filtered_df['Education Profile'].nunique()
            st.metric("📖 Education Profiles", unique_edu)
        with col4:
            engineers = len(filtered_df[filtered_df['Education Profile'].str.contains('Engineer', case=False, na=False)])
            st.metric("👨‍🔧 Engineers", engineers)

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🎓 Cadre Distribution")

            cadre_data = filtered_df['Cadre'].value_counts().reset_index()
            cadre_data.columns = ['Cadre', 'Count']

            fig_cadre = px.pie(
                cadre_data,
                values='Count',
                names='Cadre',
                color_discrete_sequence=px.colors.sequential.Plasma_r,
                hole=0.35
            )

            fig_cadre.update_layout(
                title=create_chart_title('🎓 Employee Distribution by Cadre'),
                height=450,
                showlegend=True,
                paper_bgcolor='rgba(255,255,255,0.95)'
            )

            st.plotly_chart(fig_cadre, use_container_width=True)

        with col2:
            st.markdown("### 📖 Education Profile Distribution")

            edu_data = filtered_df['Education Profile'].value_counts().head(10).reset_index()
            edu_data.columns = ['Education', 'Count']

            fig_edu = go.Figure(data=[
                go.Bar(
                    y=edu_data['Education'],
                    x=edu_data['Count'],
                    orientation='h',
                    marker=dict(
                        color=edu_data['Count'],
                        colorscale='Viridis',
                        line=dict(color='#ffffff', width=2)
                    ),
                    text=edu_data['Count'],
                    textposition='auto',
                    hovertemplate='<b>%{y}</b><br>Count: %{x}<extra></extra>'
                )
            ])

            fig_edu.update_layout(
                title=create_chart_title('📖 Top 10 Education Profiles'),
                xaxis_title="Number of Employees",
                yaxis_title="",
                height=450,
                yaxis=dict(autorange="reversed"),
                paper_bgcolor='rgba(255,255,255,0.95)',
                plot_bgcolor='rgba(255,255,255,0.95)'
            )

            st.plotly_chart(fig_edu, use_container_width=True)

    # ═══════════════════════════════════════════════════════════════════════
    # TAB 5: DEMOGRAPHICS
    # ═══════════════════════════════════════════════════════════════════════

    with tab5:
        st.markdown("### 👥 Workforce Demographics Analysis")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            minority_count = len(filtered_df[filtered_df['Minority'] == 'YES'])
            st.metric("🌍 Minority Employees", minority_count, 
                     delta=f"{minority_count/len(filtered_df)*100:.1f}%" if len(filtered_df) > 0 else "0%")

        with col2:
            avg_age = filtered_df['Age'].mean()
            st.metric("📅 Average Age", f"{avg_age:.1f} years" if not pd.isna(avg_age) else "N/A")

        with col3:
            languages = filtered_df['Mother Tongue'].nunique()
            st.metric("🗣️ Languages", languages)

        with col4:
            married = len(filtered_df[filtered_df['Date of Marriage'].notna()])
            st.metric("💍 Married Employees", married,
                     delta=f"{married/len(filtered_df)*100:.1f}%" if len(filtered_df) > 0 else "0%")

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 📊 Age Distribution Histogram")

            fig_age_hist = go.Figure()

            fig_age_hist.add_trace(go.Histogram(
                x=filtered_df['Age'].dropna(),
                nbinsx=20,
                marker=dict(
                    color='#f97316',
                    line=dict(color='#ffffff', width=1.5)
                ),
                hovertemplate='Age Range: %{x}<br>Count: %{y}<extra></extra>',
                name='Age Distribution'
            ))

            fig_age_hist.update_layout(
                title=create_chart_title('📊 Employee Age Distribution'),
                xaxis_title="Age (Years)",
                yaxis_title="Number of Employees",
                height=400,
                showlegend=False,
                paper_bgcolor='rgba(255,255,255,0.95)',
                plot_bgcolor='rgba(255,255,255,0.95)'
            )

            st.plotly_chart(fig_age_hist, use_container_width=True)

            # To make it interactive like your other charts:
            age_list_hist = sorted(filtered_df['Age'].unique().tolist())
            selected_age = st.selectbox("Select Age to view employees:", options=age_list_hist, key='age_hist_selector')
            if selected_age:
                display_employee_list(filtered_df[filtered_df['Age'] == selected_age], 'Age_Distribution', f"Age {selected_age}")

        with col2:
            st.markdown("### 🗣️ Language Diversity")

            lang_data = filtered_df['Mother Tongue'].value_counts().head(10).reset_index()
            lang_data.columns = ['Language', 'Count']

            fig_lang = px.bar(
                lang_data,
                x='Language',
                y='Count',
                color='Count',
                color_continuous_scale='Viridis',
                text='Count'
            )

            fig_lang.update_traces(textposition='outside')

            fig_lang.update_layout(
                title=create_chart_title('🗣️ Top Languages Spoken'),
                xaxis_title="Mother Tongue",
                yaxis_title="Number of Employees",
                height=400,
                xaxis={'tickangle': -45},
                paper_bgcolor='rgba(255,255,255,0.95)',
                plot_bgcolor='rgba(255,255,255,0.95)'
            )

            st.plotly_chart(fig_lang, use_container_width=True)

            # NEW INTERACTIVE SECTION FOR LANGUAGE DIVERSITY
            lang_list = lang_data['Language'].tolist()
            
            selected_lang = st.selectbox(
                "Select Mother Tongue to view employees:",
                options=lang_list,
                key='language_tab_selector'
            )

            if selected_lang:
                lang_df = filtered_df[filtered_df['Mother Tongue'] == selected_lang]
                display_employee_list(lang_df, 'Language_Tab', selected_lang)

        st.markdown("---")

        st.markdown("### 📈 Age vs Experience Analysis")

        fig_scatter = px.scatter(
            filtered_df,
            x='Age',
            y='Experience (Years)',
            color='Gender',
            size='Experience (Years)',
            hover_data=['Full Name', 'Designation', 'Location'],
            color_discrete_map={'Male': '#2563eb', 'Female': '#ec4899'},
            size_max=20
        )

        fig_scatter.update_layout(
            title=create_chart_title('📈 Age vs Experience Correlation'),
            xaxis_title="Age (Years)",
            yaxis_title="Experience (Years)",
            height=500,
            paper_bgcolor='rgba(255,255,255,0.95)',
            plot_bgcolor='rgba(255,255,255,0.95)',
            legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
        )

        st.plotly_chart(fig_scatter, use_container_width=True)


    # ═══════════════════════════════════════════════════════════════════════
    # TAB 6: EMPLOYEE DIRECTORY
    # ═══════════════════════════════════════════════════════════════════════
    with tab8:
        st.markdown("### 📋 Complete Employee Directory")

        # Top Metric and Search Controls
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("📊 Total Headcount", len(filtered_df))
        with col2:
            search_name = st.text_input("🔍 Search Name", placeholder="Type name...", key="dir_search_name")
        with col3:
            search_empid = st.text_input("🔍 Search Emp ID", placeholder="Type ID...", key="dir_search_id")

        st.markdown("---")
       
        # Create a Copy for the Directory Table
        display_df = filtered_df.copy()

        # Apply Search Logic
        if search_name:
            display_df = display_df[display_df['Full Name'].str.contains(search_name, case=False, na=False)]
        if search_empid:
            display_df = display_df[display_df['Employee No.'].astype(str).str.contains(search_empid, na=False)]

        # Explicit Mapping for Table Columns (Ordered as requested)
        requested_cols = {
            'Employee No.': 'Emp ID',
            'Full Name': 'Name',
            'Gender': 'Gender',
            'Personnel Area': 'Area',
            'Personnel Sub Area': 'Sub Area',
            'Designation': 'Designation',
            'Cadre': 'Cadre',
            'Minority': 'Minority',
            'Whether Physically Handicap': 'Handicap',
            'Mother Tongue': 'Mother Tongue',
            'Email Id': 'Email ID',
            'Age': 'Age',
            'Experience (Years)': 'Total Service',
            'Service GSPL': 'Service in GSPL',
            'Tenure in Position (Years)': 'Current Position',
            'Years in Grade': 'Years in Grade',
            'Birthday': 'Birthday',
            'Anniversary': 'Anniversary',
            'Year of Retirement': 'Year of Retirement'
        }

        # Filter available columns and display
        available = [c for c in requested_cols.keys() if c in display_df.columns]
        final_table = display_df[available].rename(columns=requested_cols)

        # Apply standard numeric formatting
        num_cfg = {col: st.column_config.NumberColumn(col, format="%.1f") for col in 
                  ['Age', 'Total Service', 'Service in GSPL', 'Current Position', 'Years in Grade']}

        # Display High-Contrast Table (Sort/Order UI removed)
        st.dataframe(
            final_table, 
            use_container_width=True, 
            hide_index=True, 
            height=550, 
            column_config=num_cfg
        )

        # Synced Export Section
        st.markdown("---")
        exp1, exp2 = st.columns(2)
        with exp1:
            st.download_button("📥 Download CSV", final_table.to_csv(index=False).encode('utf-8'), 
                               "IOCL_Directory.csv", "text/csv", use_container_width=True)
        with exp2:
            from io import BytesIO
            output = BytesIO()
            final_table.to_excel(output, index=False)
            st.download_button("📥 Download Excel", output.getvalue(), 
                               "IOCL_Directory.xlsx", "application/vnd.ms-excel", use_container_width=True)

########################################
# Milistone section
#########################################
    with tab6:
        st.markdown("### 🎂 Events & Milestones Dashboard")
        st.markdown("---")
        
        # Key Metrics
        col1, col2, col3, col4 = st.columns(4)
        
        # Calculate upcoming birthdays and anniversaries
        from datetime import timedelta
        today = datetime.now()
        
        # Birthday calculations
        filtered_df['Birth Month'] = filtered_df['Birth Date'].dt.month
        filtered_df['Birth Day'] = filtered_df['Birth Date'].dt.day
        current_month = today.month
        current_day = today.day
        
        # Marriage Anniversary calculations
        filtered_df['Marriage Month'] = filtered_df['Date of Marriage'].dt.month
        filtered_df['Marriage Day'] = filtered_df['Date of Marriage'].dt.day
        
        # Count events (this month)
        upcoming_birthdays = len(filtered_df[filtered_df['Birth Month'] == current_month])
        upcoming_anniversaries = len(
            filtered_df[
                (filtered_df['Marriage Month'] == current_month)
                & (filtered_df['Date of Marriage'].notna())
            ]
        )
        
        with col1:
            st.metric("Total Employees", f"{len(filtered_df):,}")
        
        with col2:
            st.metric("Birthdays This Month", upcoming_birthdays)
        
        with col3:
            married_employees = len(filtered_df[filtered_df['Date of Marriage'].notna()])
            st.metric("Married Employees", f"{married_employees:,}")
        
        with col4:
            st.metric("Anniversaries This Month", upcoming_anniversaries)
        
        st.markdown("---")
        
        # Two columns for charts
        col1, col2 = st.columns(2)
        
        # CHART 1: Monthly Birthday Distribution
        with col1:
            st.markdown("#### 🎂 Monthly Birthday Distribution")
            
            birthday_counts = filtered_df.groupby('Birth Month').size().reset_index(name='Count')
            month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            
            all_months = pd.DataFrame({'Birth Month': range(1, 13)})
            birthday_counts = all_months.merge(birthday_counts, on='Birth Month', how='left').fillna(0)
            birthday_counts['Month Name'] = [month_names[i-1] for i in birthday_counts['Birth Month']]
            birthday_counts['Count'] = birthday_counts['Count'].astype(int)
            
            fig_birthday = px.bar(
                birthday_counts,
                x='Month Name',
                y='Count',
                title='Employee Birthdays by Month',
                color='Count',
                color_continuous_scale='Blues',
                text='Count'
            )
            fig_birthday.update_traces(
                textposition='outside',
                marker_line_color='#1e40af',
                marker_line_width=1.5
            )
            fig_birthday.update_layout(
                title=create_chart_title('Employee Birthdays by Month'),
                xaxis_title='Month',
                yaxis_title='Number of Birthdays',
                showlegend=False,
                hovermode='x unified',
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family='Inter', size=12),
                height=400
            )
            fig_birthday.update_xaxes(showgrid=False)
            fig_birthday.update_yaxes(showgrid=True, gridcolor='rgba(0,0,0,0.1)')
            
            st.plotly_chart(fig_birthday, use_container_width=True, key='birthday_monthly_chart')
            
            # Employees with birthdays this month
            this_month_birthdays = filtered_df[
                filtered_df['Birth Month'] == current_month
            ].sort_values('Birth Day')
            
            if len(this_month_birthdays) > 0:
                with st.expander(
                    f"👥 View Birthdays This Month ({len(this_month_birthdays)} employees)",
                    expanded=False
                ):
                    display_df = this_month_birthdays[
                        ['Employee No.', 'Full Name', 'Designation', 'Location', 'Birth Date']
                    ].copy()
                    display_df['Birth Date'] = display_df['Birth Date'].dt.strftime('%d %B %Y')
                    display_df.columns = ['Employee ID', 'Name', 'Designation', 'Location', 'Birthday']
                    st.dataframe(
                        display_df,
                        use_container_width=True,
                        hide_index=True,
                        height=min(400, len(display_df) * 35 + 38)
                    )
        
        # CHART 2: Monthly Anniversary Distribution
        with col2:
            st.markdown("#### 💑 Monthly Anniversary Distribution")
            
            df_married = filtered_df[filtered_df['Date of Marriage'].notna()].copy()
            
            if len(df_married) > 0:
                anniversary_counts = df_married.groupby('Marriage Month').size().reset_index(name='Count')
                all_months = pd.DataFrame({'Marriage Month': range(1, 13)})
                anniversary_counts = all_months.merge(anniversary_counts, on='Marriage Month', how='left').fillna(0)
                anniversary_counts['Month Name'] = [
                    month_names[i-1] for i in anniversary_counts['Marriage Month']
                ]
                anniversary_counts['Count'] = anniversary_counts['Count'].astype(int)
                
                fig_anniversary = px.bar(
                    anniversary_counts,
                    x='Month Name',
                    y='Count',
                    title='Employee Anniversaries by Month',
                    color='Count',
                    color_continuous_scale='Greens',
                    text='Count'
                )
                fig_anniversary.update_traces(
                    textposition='outside',
                    marker_line_color='#15803d',
                    marker_line_width=1.5
                )
                fig_anniversary.update_layout(
                    title=create_chart_title('Employee Wedding Anniversaries by Month'),
                    xaxis_title='Month',
                    yaxis_title='Number of Anniversaries',
                    showlegend=False,
                    hovermode='x unified',
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(family='Inter', size=12),
                    height=400
                )
                fig_anniversary.update_xaxes(showgrid=False)
                fig_anniversary.update_yaxes(showgrid=True, gridcolor='rgba(0,0,0,0.1)')
                
                st.plotly_chart(fig_anniversary, use_container_width=True, key='anniversary_monthly_chart')
                
                # Employees with anniversaries this month
                this_month_anniversaries = df_married[
                    df_married['Marriage Month'] == current_month
                ].sort_values('Marriage Day')
                
                if len(this_month_anniversaries) > 0:
                    with st.expander(
                        f"👥 View Anniversaries This Month ({len(this_month_anniversaries)} employees)",
                        expanded=False
                    ):
                        display_df = this_month_anniversaries[
                            ['Employee No.', 'Full Name', 'Designation', 'Location', 'Date of Marriage']
                        ].copy()
                        display_df['Date of Marriage'] = display_df['Date of Marriage'].dt.strftime('%d %B %Y')
                        display_df.columns = ['Employee ID', 'Name', 'Designation', 'Location', 'Anniversary Date']
                        st.dataframe(
                            display_df,
                            use_container_width=True,
                            hide_index=True,
                            height=min(400, len(display_df) * 35 + 38)
                        )
            else:
                st.info("No marriage anniversary data available")
        
        st.markdown("---")
        
        # Additional insights
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 📊 Age-wise Birthday Distribution")
            age_birthday = filtered_df.groupby('Age Group').size().reset_index(name='Count')
            age_birthday = age_birthday.sort_values('Age Group')
            
            fig_age = px.pie(
                age_birthday,
                values='Count',
                names='Age Group',
                title='Employees by Age Group',
                color_discrete_sequence=px.colors.sequential.Blues_r
            )
            fig_age.update_traces(
                textposition='inside',
                textinfo='percent+label',
                hovertemplate='<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent}<extra></extra>'
            )
            fig_age.update_layout(
                title=create_chart_title('Employee Distribution by Age Group'),
                showlegend=True,
                height=350,
                font=dict(family='Inter', size=12)
            )
            
            st.plotly_chart(fig_age, use_container_width=True, key='age_distribution_pie')
        
        with col2:
            st.markdown("#### 📊 Marital Status Overview")
            marital_status = pd.DataFrame({
                'Status': ['Married', 'Not Married'],
                'Count': [
                    len(filtered_df[filtered_df['Date of Marriage'].notna()]),
                    len(filtered_df[filtered_df['Date of Marriage'].isna()])
                ]
            })
            
            fig_marital = px.pie(
                marital_status,
                values='Count',
                names='Status',
                title='Marital Status Distribution',
                color='Status',
                color_discrete_map={'Married': '#15803d', 'Not Married': '#94a3b8'}
            )
            fig_marital.update_traces(
                textposition='inside',
                textinfo='percent+label+value',
                hovertemplate='<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent}<extra></extra>'
            )
            fig_marital.update_layout(
                title=create_chart_title('Marital Status Distribution'),
                showlegend=True,
                height=350,
                font=dict(family='Inter', size=12)
            )
            
            st.plotly_chart(fig_marital, use_container_width=True, key='marital_status_pie')

    # FOOTER
    st.markdown("---")

        # ═══════════════════════════════════════════════════════════════════════
    # FOOTER – DEVELOPER CREDIT (DO NOT MODIFY OTHER PARTS)
    # ═══════════════════════════════════════════════════════════════════════
    st.markdown(
        """
        <hr style="margin-top:3rem;margin-bottom:1rem;border:0;border-top:1px solid #e5e7eb;" />
        <div style="text-align:center;font-size:0.9rem;color:#4b5563;">
            <div style="font-weight:600;color:#111827;">
                Developed by: IOCL Apprentice
            </div>
            <div>
                GSPL HQ Guwahati | Indian Oil Corporation Ltd. (IOCL)
            </div>
            <div style="margin-top:0.25rem;color:#6b7280;">
                Built with using Streamlit, Pandas & Plotly | Version 1.0.1 | ©2026
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
