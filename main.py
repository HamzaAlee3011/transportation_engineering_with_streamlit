import streamlit as st


# PAGE SETUP
st.set_page_config(layout='wide')

RPD_equation_solver_page = st.Page(
    page="views/AASHTO_RPD_equation_solver.py",
    title="Rigid Pavement Design Eq. Solver",
    # icon=":material/bid_landscape:",
)

FPD_equation_solver_page = st.Page(
    page="views/AASHTO_FPD_equation_solver.py",
    title="Flexible Pavement Design Eq. Solver",
    # icon=":material/bid_landscape:",
)
# about_me = st.Page(
#     page="views/about_me.py",
#     title="About Me",
#     icon=":material/account_circle:",
# )


about_app = st.Page(
    page="views/about_app.py",
    title="About Application",
    icon=":material/info:",
)

# NAVIGATION SETUP (WITHOUT SECTIONS)
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# NAVIGATION SETUP (WITH SECTIONS)
pg = st.navigation({
    'Applications': [RPD_equation_solver_page, FPD_equation_solver_page],
    # 'Usage': [instructions],
    'Info': [about_app]
})

#RUN NAVIGATION
pg.run()
