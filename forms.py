import logging
import os

import openai
import repo
import streamlit as st
from streamlit_tree_select import tree_select
from utils import EXTENSION_TO_LANGUAGE_MAP, ANALYSIS_TYPE


class RepoForm:
    """A class to encapsulate the repository form and its operations."""

    options = EXTENSION_TO_LANGUAGE_MAP.keys()
    a_option = ANALYSIS_TYPE.keys()

    def __init__(self, default_repo_url: str):
        self.default_repo_url = default_repo_url
        self.repo_url = ""
        self.api_key = ""
        self.extensions = []
        self.analyze = ""
        self.additional_extensions = ""

    def display_form(self):
        """Displays the repository form and its elements."""
        self.repo_url = st.text_input(
            "GitHub Repository URL:", self.default_repo_url
        )

        env_api_key = os.getenv("OPENAI_API_KEY", "test")
        self.api_key = env_api_key
        openai.api_key = self.api_key

        ANALYSIS_TYPE

        self.analyze = st.selectbox(
            "Type of analyze",
            (self.a_option)
        )

        self.extensions = st.multiselect(
            "File extensions to analyze",
            options=self.options,
            default=self.options,
        )
        self.additional_extensions = st.text_input(
            "Additional file extensions to analyze (comma-separated):"
        )
        if self.additional_extensions:
            self.extensions.extend(
                [ext.strip() for ext in self.additional_extensions.split(",")]
            )

        self.clone_repo_button = st.form_submit_button("Clone Repository")

    def get_form_data(self):
        """Returns the data captured by the repository form."""
        return (
            self.repo_url,
            self.extensions,
        )

    def is_api_key_valid(self):
        """Checks if the OpenAI API key is valid and returns a boolean value."""
        if not self.api_key:
            st.error("OpenAI API key is not available.")
            return False
        return True


class AnalyzeFilesForm:
    """A class to encapsulate the analyze files form and its operations."""

    def __init__(self, session_state):
        self.session_state = session_state

    def display_form(self):
        """Displays the analyze files form and its elements."""
        st.write("Select files to analyze:")
        file_tree = repo.create_file_tree(self.session_state.code_files)
        self.session_state.selected_files = tree_select(
            file_tree,
            show_expand_all=True,
            check_model="leaf",
            checked=self.session_state.get("selected_files"),
        )["checked"]
        logging.info("Selected files: %s", self.session_state.selected_files)
        self.session_state.analyze_files = st.form_submit_button(
            "Analyze Files"
        ) or self.session_state.get("analyze_files")
