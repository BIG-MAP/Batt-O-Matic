import streamlit as st
import custom_cell_annotation_utils as ut

def custom_cell_annotator():
    loaded_dict = ut.load_from_file()
    if not bool(loaded_dict):
        input_dict = default_dict
        default_format = default_dict["@type"].replace("Cell", "")
        if default_format != "Battery":
            init_cell_format = {"format": default_format}
        else:
            init_cell_format = {"format": "Pouch"}
    else:
        input_dict = loaded_dict
        loaded_format = loaded_dict["@type"].replace("Cell", "")
        if loaded_format != "Battery":
            init_cell_format = {"format": loaded_format}
        else:
            init_cell_format = {"format": "Pouch"}

    format_data = set_cell_formats(init_cell_format)
    input_dict["@type"] = str(format_data["cell_format"]["value"]) + "Cell"
    #st.write(input_dict["@type"])

    (cell_format, cell_production_default_values, cell_properties_default_values, 
    pe_am_default_values, pe_binder_default_values, pe_additive_default_values, pe_coating_default_values, pe_current_collector_default_values, pe_dimensions_default_values,
    ne_am_default_values, ne_binder_default_values, ne_additive_default_values, ne_coating_default_values, ne_current_collector_default_values, ne_dimensions_default_values,
    sep_default_values) = load_default_values(input_dict)


    with st.form(key='my_form'):
        with st.expander("Production Details"):
            production_properties = cell_production_metadata(cell_production_default_values)

        with st.expander("Cell Properties"):
            tab1, tab2 = st.tabs(["Physical Dimensions", "Electrical Properties"])
            with tab1:
                if format_data["cell_format"]["value"] == "Coin" or format_data["cell_format"]["value"] == "Cylindrical":
                    physical_properties = round_cell_properties(cell_properties_default_values)
                else:
                    physical_properties = rectangular_cell_properties(cell_properties_default_values)
                
            with tab2:
                electrical_properties = cell_nominal_electrical_properties()
            
        with st.expander("Positive Electrode Properties"):
            if format_data["cell_format"]["value"] != "Coin":
                pe_properties = rectangular_electrode("pe", pe_am_default_values, pe_binder_default_values, pe_additive_default_values, pe_coating_default_values, pe_current_collector_default_values, pe_dimensions_default_values)
            else:
                pe_properties = circular_electrode("pe", pe_am_default_values, pe_binder_default_values, pe_additive_default_values, pe_coating_default_values, pe_current_collector_default_values, pe_dimensions_default_values)

        with st.expander("Negative Electrode Properties"):
            if format_data["cell_format"]["value"] != "Coin":
                ne_properties = rectangular_electrode("ne", ne_am_default_values, ne_binder_default_values, ne_additive_default_values, ne_coating_default_values, ne_current_collector_default_values, ne_dimensions_default_values)
            else:
                ne_properties = circular_electrode("ne", ne_am_default_values, ne_binder_default_values, ne_additive_default_values, ne_coating_default_values, ne_current_collector_default_values, ne_dimensions_default_values)
        
        with st.expander("Separator Properties"):
            if format_data["cell_format"]["value"] == "Coin":
                separator_properties = set_circular_separator_properties(sep_default_values)
            else:
                separator_properties = set_rectangular_separator_properties(sep_default_values)

        with st.expander("Electroylte Properties"):
            electrolyte_properties = electrolyte()
            
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        # Do something with the form data
        jsonld_data = disperse_fields_to_json(format_data, 
                                            production_properties, 
                                            physical_properties, 
                                            electrical_properties,
                                            pe_properties,
                                            ne_properties,
                                            separator_properties,
                                            electrolyte_properties)
        
        #st.write(jsonld_data)
        # Define a filename for the downloaded file
        filename = "scientific_metadata.json"
        json_data = json.dumps(jsonld_data, indent=4)

        # Write the JSON string to a file
        with open(filename, "w") as f:
            f.write(json_data)
        # Send the file to the user for download
        st.download_button(label="Download", data=json_data, file_name=filename, mime="application/ld+json")