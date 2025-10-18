import streamlit as st
from efgs import get_dec_fgs
from rdkit import Chem

from PIL import Image
from io import BytesIO

from collections import Counter


st.set_page_config(page_title="Smiles to Ertl Functional Groups",
                   page_icon="⌬",
                   layout="centered")
st.title("⌬ Smiles to Ertl Functional Groups", width='content')

prompt = st.text_input("Enter a SMILES string:", value="CC34CC(O)C1(F)C(CCC2=CC(=O)C=CC12C)C3CC(O)C4(O)C(=O)CO")

if st.button("Get EFGs"):
    try:
        img_text, fgs, psmis, fg_mols = get_dec_fgs(Chem.MolFromSmiles(prompt))
        image = Image.open(BytesIO(img_text))


        counts = Counter(psmis)

        st.image(image)
        st.json(counts)

    except Exception as e:
        st.error(f"Error: {e}")
