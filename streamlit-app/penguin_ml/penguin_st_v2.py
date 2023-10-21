import pickle
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st.title("Penguin Classifier")
st.write(
    """This app uses 6 inputs to predict the species of penguin using
 a model built on the Palmer's Penguins dataset. Use the form below
 to get started!"""
)

penguin_file = st.file_uploader("Upload your own penguin data")

if penguin_file is None:
    with open("/workspaces/ughhhh/streamlit-app/penguin_ml/random_forest_penguin.pickle", "rb") as rf_pickle:
        rfc = pickle.load(rf_pickle)
    with open("/workspaces/ughhhh/streamlit-app/penguin_ml/output_penguin.pickle", "rb") as map_pickle:
        unique_penguin_mapping = pickle.load(map_pickle)
else:
    penguin_file = pd.read_csv(r"/workspaces/ughhhh/streamlit-app/penguin_ml/penguins.csv")
    penguin_file.dropna(inplace=True)
    output = penguin_file["species"]
    features = penguin_file[
        [
            "island",
            "bill_length_mm",
            "bill_depth_mm",
            "flipper_length_mm",
            "body_mass_g",
            "sex",
        ]
    ]
    features = pd.get_dummies(features)
    output, uniques = pd.factorize(output)
    x_train, x_test, y_train, y_test = train_test_split(features, output, test_size=0.8)
    rfc = RandomForestClassifier(random_state=15)
    rfc.fit(x_train.values, y_train)
    y_pred = rfc.predict(x_test.values)
    score = round(accuracy_score(y_pred, y_test), 2)
    st.write(
        f"""We trained a Random Forest model on these
    data, it has a score of {score}! Use the
    inputs below to try out the model"""
    )

with st.form("user_inputs"):
    island = st.selectbox("Penguin Island", options=["Biscoe", "Dream", "Torgerson"])
    sex = st.selectbox("Sex", options=["male", "Female"])
    bill_length = st.number_input("Bill Length (mm)", min_value=0)
    bill_depth = st.number_input("Bill Depth (mm)", min_value=0)
    flipper_length = st.number_input("Flipper Length (mm)", min_value=0)
    body_mass = st.number_input("Body Mass (g)", min_value=0)
    ISLAND_BISCOE, ISLAND_DREAM, ISLAND_TORGERSON = 0, 0, 0
    if island == "Biscoe":
        ISLAND_BISCOE = 1
    elif island == "Dream":
        ISLAND_DREAM = 1
    elif island == "Torgerson":
        ISLAND_TORGERSON = 1
    SEX_FEMALE, SEX_MALE = 0, 0
    if sex == "Female":
        SEX_FEMALE = 1
    elif sex == "Male":
        SEX_MALE = 1
    new_prediction = rfc.predict(
        [
            [
                bill_length,
                bill_depth,
                flipper_length,
                body_mass,
                ISLAND_BISCOE,
                ISLAND_DREAM,
                ISLAND_TORGERSON,
                SEX_FEMALE,
                SEX_MALE,
            ]
        ]
    )
    if penguin_file is None:
        unique_penguin_mapping = None
    else:
        output, unique_penguin_mapping = pd.factorize(penguin_file["species"])

    prediction_species = unique_penguin_mapping[new_prediction[0]]

    st.subheader("Predicting Penguin Species")
    st.form_submit_button()

    st.write(f"We predict your penguin is of the {prediction_species} species")

    st.write("""We used a machine learning (Random Forest)
    model to predict the species, the features
    used in this prediction are ranked by
    relative importance below.""")

    if penguin_file is not None:
        st.write(penguin_file.head())

    st.subheader("Feature Importance")
    st.write("""Below are the histograms for each
    continuous variable separated by penguin
    species. The vertical line represents
    your the inputted value.""")

    fig = sns.FacetGrid(data=penguin_file, hue="species", height=5)
    fig.map(sns.histplot, "bill_length_mm", kde=True)
    fig.axvline(bill_length)
    plt.title("Bill Length by Species")
    st.pyplot(fig.fig)

    fig = sns.FacetGrid(data=penguin_file, hue="species", height=5)
    fig.map(sns.histplot, "bill_depth_mm", kde=True)
    fig.axvline(bill_depth)
    plt.title("Bill Depth by Species")
    st.pyplot(fig.fig)

    fig = sns.FacetGrid(data=penguin_file, hue="species", height=5)
    fig.map(sns.histplot, "flipper_length_mm", kde=True)
    fig.axvline(flipper_length)
    plt.title("Flipper Length by Species")
    st.pyplot(fig.fig)

fig = sns.FacetGrid(data=penguin_file, hue="species", height=5)
fig.map(sns.histplot, "bill_length_mm", kde=True)
plt.axvline(bill_length)
plt.title("Bill Length by Species")
st.pyplot(fig)

fig = sns.FacetGrid(data=penguin_file, hue="species", height=5)
fig.map(sns.histplot, "bill_depth_mm", kde=True)
plt.axvline(bill_depth)
plt.title("Bill Depth by Species")
st.pyplot(fig)

fig = sns.FacetGrid(data=penguin_file, hue="species", height=5)
fig.map(sns.histplot, "flipper_length_mm", kde=True)
plt.axvline(flipper_length)
plt.title("Flipper Length by Species")
st.pyplot(fig)

fig, ax = plt.subplots()
sns.histplot(data=penguin_file, x="flipper_length_mm", hue="species", kde=True, ax=ax)
plt.axvline(flipper_length)
plt.title("Flipper Length by Species")
st.pyplot(fig)

fig, ax = plt.subplots()
sns.distplot(x=penguin_file["flipper_length_mm"], kde=True, ax=ax)
plt.axvline(flipper_length)
plt.title("Flipper Length by Species")
st.pyplot(fig)
