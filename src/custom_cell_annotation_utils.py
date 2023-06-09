def load_from_file():
    agree = st.checkbox('Load from file')
    json_dict = {}
    if agree:
        uploaded_file = st.file_uploader("Upload a JSON-LD metadata profile", accept_multiple_files=False)
        if uploaded_file is not None:
            content = uploaded_file.read()
            json_dict = json.loads(content.decode('utf-8'))
    return json_dict

def load_default_values(input_dict):
    #st.write(input_dict)

    #cell_format = {"format": "Pouch"}
    loaded_format = input_dict["@type"].replace("Cell", "")
    if loaded_format != "Battery":
        cell_format = {"format": loaded_format}
    else:
        cell_format = {"format": "Pouch"}

    #st.write(cell_format)

    if cell_format["format"] == "Coin" or cell_format["format"] == "Cylindrical":
        cell_properties_default_values = {
        "mass": {
            "value": input_dict["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"],
            "unit": unit_abbreviations[uri_label_dict[input_dict["hasQuantitativeProperty"][0]["hasReferenceUnit"]]]
        },
        "diameter": {
            "value": input_dict["hasQuantitativeProperty"][1]["hasQuantityValue"]["hasNumericalData"],
            "unit": unit_abbreviations[uri_label_dict[input_dict["hasQuantitativeProperty"][1]["hasReferenceUnit"]]]
        },
        "height": {
            "value": input_dict["hasQuantitativeProperty"][1]["hasQuantityValue"]["hasNumericalData"],
            "unit": unit_abbreviations[uri_label_dict[input_dict["hasQuantitativeProperty"][2]["hasReferenceUnit"]]]
        }}
    else:
        cell_properties_default_values = {
            "mass": {
                "value": input_dict["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"],
                "unit": unit_abbreviations[uri_label_dict[input_dict["hasQuantitativeProperty"][0]["hasReferenceUnit"]]]
            },
            "width": {
                "value": input_dict["hasQuantitativeProperty"][1]["hasQuantityValue"]["hasNumericalData"],
                "unit": unit_abbreviations[uri_label_dict[input_dict["hasQuantitativeProperty"][1]["hasReferenceUnit"]]]
            },
            "height": {
                "value": input_dict["hasQuantitativeProperty"][2]["hasQuantityValue"]["hasNumericalData"],
                "unit": unit_abbreviations[uri_label_dict[input_dict["hasQuantitativeProperty"][2]["hasReferenceUnit"]]]
            },
            "thickness": {
                "value": input_dict["hasQuantitativeProperty"][3]["hasQuantityValue"]["hasNumericalData"],
                "unit": unit_abbreviations[uri_label_dict[input_dict["hasQuantitativeProperty"][3]["hasReferenceUnit"]]]
            }}

    cell_production_default_values = {
           "name": input_dict["schema:name"] , 
           "productionDate": input_dict["schema:productionDate"] ,
           "creator": input_dict["schema:creator"].replace("https://orcid.org/", ""), 
           "manufacturer": input_dict["schema:manufacturer"].replace("https://ror.org/", "") }
    
    # Positive Electrode Default Values
    pe_am_default_values = {
        "active_material": {"value": "NMC"}, 
        "specific_capacity": {
            "value": input_dict["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][2]["hasQuantityValue"]["hasNumericalData"], 
            "unit": unit_abbreviations[uri_label_dict[input_dict["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][2]["hasReferenceUnit"]]]}, 
        "am_density": {
            "value": input_dict["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][1]["hasQuantityValue"]["hasNumericalData"], 
            "unit": unit_abbreviations[uri_label_dict[input_dict["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][1]["hasReferenceUnit"]]]}}
    
    pe_binder_default_values = {
        "binder": {"value": "PVDF"}, 
        "binder_density": {
            "value": input_dict["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][1]["hasQuantitativeProperty"][1]["hasQuantityValue"]["hasNumericalData"], 
            "unit": unit_abbreviations[uri_label_dict[input_dict["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][1]["hasQuantitativeProperty"][1]["hasReferenceUnit"]]]}}
    
    pe_additive_default_values = {
        "additive": {"value": "Carbon Black"}, 
        "additive_density": {
            "value": input_dict["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][2]["hasQuantitativeProperty"][1]["hasQuantityValue"]["hasNumericalData"], 
            "unit": unit_abbreviations[uri_label_dict[input_dict["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][2]["hasQuantitativeProperty"][1]["hasReferenceUnit"]]]}}
    
    pe_coating_default_values = {
        "am_mass_fraction": {"value": input_dict["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"]}, 
        "binder_mass_fraction": {"value": input_dict["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][1]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"]}, 
        "additive_mass_fraction": {"value": input_dict["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][2]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"]}, 
        "coating_thickness": {
            "value": input_dict["hasPositiveElectrode"]["hasConstituent"][1]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"], 
            "unit": unit_abbreviations[uri_label_dict[input_dict["hasPositiveElectrode"]["hasConstituent"][1]["hasQuantitativeProperty"][0]["hasReferenceUnit"]]]}, 
        "mass_loading": {
            "value": input_dict["hasPositiveElectrode"]["hasQuantitativeProperty"][1]["hasQuantityValue"]["hasNumericalData"], 
            "unit": unit_abbreviations[uri_label_dict[input_dict["hasPositiveElectrode"]["hasQuantitativeProperty"][1]["hasReferenceUnit"]]]}}
    
    pe_current_collector_default_values = {
        "current_collector_thickness": {
            "value": input_dict["hasPositiveElectrode"]["hasConstituent"][0]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"], 
            "unit": unit_abbreviations[uri_label_dict[input_dict["hasPositiveElectrode"]["hasConstituent"][0]["hasQuantitativeProperty"][0]["hasReferenceUnit"]]]}}
    
    if cell_format["format"] == "Coin":
        pe_dimensions_default_values = {
        "electrode_layers": {"value":input_dict["hasPositiveElectrode"]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"]},
        "electrode_diameter": {
            "value": input_dict["hasPositiveElectrode"]["hasQuantitativeProperty"][2]["hasQuantityValue"]["hasNumericalData"] , 
            "unit": unit_abbreviations[uri_label_dict[input_dict["hasPositiveElectrode"]["hasQuantitativeProperty"][2]["hasReferenceUnit"]]]},
        "electrode_thickness": {
            "value": input_dict["hasPositiveElectrode"]["hasQuantitativeProperty"][3]["hasQuantityValue"]["hasNumericalData"], 
            "unit": unit_abbreviations[uri_label_dict[input_dict["hasPositiveElectrode"]["hasQuantitativeProperty"][3]["hasReferenceUnit"]]]}}
    else:
        pe_dimensions_default_values = {
            "electrode_layers": {"value":input_dict["hasPositiveElectrode"]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"]},
            "electrode_width": {
                "value": input_dict["hasPositiveElectrode"]["hasQuantitativeProperty"][2]["hasQuantityValue"]["hasNumericalData"], 
                "unit": unit_abbreviations[uri_label_dict[input_dict["hasPositiveElectrode"]["hasQuantitativeProperty"][2]["hasReferenceUnit"]]]},
            "electrode_height": {
                "value": input_dict["hasPositiveElectrode"]["hasQuantitativeProperty"][3]["hasQuantityValue"]["hasNumericalData"], 
                "unit": unit_abbreviations[uri_label_dict[input_dict["hasPositiveElectrode"]["hasQuantitativeProperty"][3]["hasReferenceUnit"]]]},
            "electrode_thickness": {
                "value": input_dict["hasPositiveElectrode"]["hasQuantitativeProperty"][4]["hasQuantityValue"]["hasNumericalData"], 
                "unit": unit_abbreviations[uri_label_dict[input_dict["hasPositiveElectrode"]["hasQuantitativeProperty"][4]["hasReferenceUnit"]]]}}
    
    # Negative Electrode Default Values
    ne_am_default_values = {
        "active_material": {"value": "NMC"}, 
        "specific_capacity": {
            "value": input_dict["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][2]["hasQuantityValue"]["hasNumericalData"], 
            "unit": unit_abbreviations[uri_label_dict[input_dict["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][2]["hasReferenceUnit"]]]}, 
        "am_density": {
            "value": input_dict["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][1]["hasQuantityValue"]["hasNumericalData"], 
            "unit": unit_abbreviations[uri_label_dict[input_dict["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][1]["hasReferenceUnit"]]]}}
    
    ne_binder_default_values = {
        "binder": {"value": "PVDF"}, 
        "binder_density": {
            "value": input_dict["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][1]["hasQuantitativeProperty"][1]["hasQuantityValue"]["hasNumericalData"], 
            "unit": unit_abbreviations[uri_label_dict[input_dict["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][1]["hasQuantitativeProperty"][1]["hasReferenceUnit"]]]}}
    
    ne_additive_default_values = {
        "additive": {"value": "Carbon Black"}, 
        "additive_density": {
            "value": input_dict["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][2]["hasQuantitativeProperty"][1]["hasQuantityValue"]["hasNumericalData"], 
            "unit": unit_abbreviations[uri_label_dict[input_dict["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][2]["hasQuantitativeProperty"][1]["hasReferenceUnit"]]]}}
    
    ne_coating_default_values = {
        "am_mass_fraction": {"value": input_dict["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"]}, 
        "binder_mass_fraction": {"value": input_dict["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][1]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"]}, 
        "additive_mass_fraction": {"value": input_dict["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][2]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"]}, 
        "coating_thickness": {
            "value": input_dict["hasNegativeElectrode"]["hasConstituent"][1]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"], 
            "unit": unit_abbreviations[uri_label_dict[input_dict["hasNegativeElectrode"]["hasConstituent"][1]["hasQuantitativeProperty"][0]["hasReferenceUnit"]]]}, 
        "mass_loading": {
            "value": input_dict["hasNegativeElectrode"]["hasQuantitativeProperty"][1]["hasQuantityValue"]["hasNumericalData"], 
            "unit": unit_abbreviations[uri_label_dict[input_dict["hasNegativeElectrode"]["hasQuantitativeProperty"][1]["hasReferenceUnit"]]]}}
    
    ne_current_collector_default_values = {
        "current_collector_thickness": {
            "value": input_dict["hasNegativeElectrode"]["hasConstituent"][0]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"], 
            "unit": unit_abbreviations[uri_label_dict[input_dict["hasNegativeElectrode"]["hasConstituent"][0]["hasQuantitativeProperty"][0]["hasReferenceUnit"]]]}}
    
    if cell_format["format"] == "Coin":
        ne_dimensions_default_values = {
        "electrode_layers": {"value":input_dict["hasNegativeElectrode"]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"]},
        "electrode_diameter": {
            "value": input_dict["hasNegativeElectrode"]["hasQuantitativeProperty"][2]["hasQuantityValue"]["hasNumericalData"] , 
            "unit": unit_abbreviations[uri_label_dict[input_dict["hasNegativeElectrode"]["hasQuantitativeProperty"][2]["hasReferenceUnit"]]]},
        "electrode_thickness": {
            "value": input_dict["hasNegativeElectrode"]["hasQuantitativeProperty"][3]["hasQuantityValue"]["hasNumericalData"], 
            "unit": unit_abbreviations[uri_label_dict[input_dict["hasNegativeElectrode"]["hasQuantitativeProperty"][3]["hasReferenceUnit"]]]}}
    else:
        ne_dimensions_default_values = {
            "electrode_layers": {"value":input_dict["hasNegativeElectrode"]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"]},
            "electrode_width": {
                "value": input_dict["hasNegativeElectrode"]["hasQuantitativeProperty"][2]["hasQuantityValue"]["hasNumericalData"], 
                "unit": unit_abbreviations[uri_label_dict[input_dict["hasNegativeElectrode"]["hasQuantitativeProperty"][2]["hasReferenceUnit"]]]},
            "electrode_height": {
                "value": input_dict["hasNegativeElectrode"]["hasQuantitativeProperty"][3]["hasQuantityValue"]["hasNumericalData"], 
                "unit": unit_abbreviations[uri_label_dict[input_dict["hasNegativeElectrode"]["hasQuantitativeProperty"][3]["hasReferenceUnit"]]]},
            "electrode_thickness": {
                "value": input_dict["hasNegativeElectrode"]["hasQuantitativeProperty"][4]["hasQuantityValue"]["hasNumericalData"], 
                "unit": unit_abbreviations[uri_label_dict[input_dict["hasNegativeElectrode"]["hasQuantitativeProperty"][4]["hasReferenceUnit"]]]}}
    
    # Separator Default Values 
    if cell_format["format"] == "Coin":
        sep_default_values = {
        "separator_mass": {
            "value": input_dict["hasSeparator"]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"], 
            "unit": unit_abbreviations[uri_label_dict[input_dict["hasSeparator"]["hasQuantitativeProperty"][0]["hasReferenceUnit"]]]},
        "separator_porosity": {
            "value": input_dict["hasSeparator"]["hasQuantitativeProperty"][3]["hasQuantityValue"]["hasNumericalData"]},
        "separator_diameter": {
            "value": input_dict["hasSeparator"]["hasQuantitativeProperty"][1]["hasQuantityValue"]["hasNumericalData"], 
            "unit": unit_abbreviations[uri_label_dict[input_dict["hasSeparator"]["hasQuantitativeProperty"][1]["hasReferenceUnit"]]]},
        "separator_thickness": {
            "value": input_dict["hasSeparator"]["hasQuantitativeProperty"][2]["hasQuantityValue"]["hasNumericalData"] , 
            "unit": unit_abbreviations[uri_label_dict[input_dict["hasSeparator"]["hasQuantitativeProperty"][2]["hasReferenceUnit"]]]}}
    else:
        sep_default_values = {
            "separator_mass": {
                "value": input_dict["hasSeparator"]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"], 
                "unit": unit_abbreviations[uri_label_dict[input_dict["hasSeparator"]["hasQuantitativeProperty"][0]["hasReferenceUnit"]]]},
            "separator_porosity": {
                "value": input_dict["hasSeparator"]["hasQuantitativeProperty"][4]["hasQuantityValue"]["hasNumericalData"]},
            "separator_width": {
                "value": input_dict["hasSeparator"]["hasQuantitativeProperty"][1]["hasQuantityValue"]["hasNumericalData"], 
                "unit": unit_abbreviations[uri_label_dict[input_dict["hasSeparator"]["hasQuantitativeProperty"][1]["hasReferenceUnit"]]]},
            "separator_height": {
                "value": input_dict["hasSeparator"]["hasQuantitativeProperty"][2]["hasQuantityValue"]["hasNumericalData"], 
                "unit": unit_abbreviations[uri_label_dict[input_dict["hasSeparator"]["hasQuantitativeProperty"][2]["hasReferenceUnit"]]]},
            "separator_thickness": {
                "value": input_dict["hasSeparator"]["hasQuantitativeProperty"][3]["hasQuantityValue"]["hasNumericalData"], 
                "unit": unit_abbreviations[uri_label_dict[input_dict["hasSeparator"]["hasQuantitativeProperty"][3]["hasReferenceUnit"]]]}}

    return (cell_format, cell_production_default_values, cell_properties_default_values, 
            pe_am_default_values, pe_binder_default_values, pe_additive_default_values, pe_coating_default_values, pe_current_collector_default_values, pe_dimensions_default_values,
            ne_am_default_values, ne_binder_default_values, ne_additive_default_values, ne_coating_default_values, ne_current_collector_default_values, ne_dimensions_default_values,
            sep_default_values)


def rectangular_cell_properties(default_values):
    cell_mass       = default_values["mass"]["value"]
    cell_width      = default_values["width"]["value"]
    cell_height     = default_values["height"]["value"]
    cell_thickness  = default_values["thickness"]["value"]

    cell_mass_unit          = default_values["mass"]["unit"]
    cell_width_unit         = default_values["width"]["unit"]
    cell_height_unit        = default_values["height"]["unit"]
    cell_thickness_unit     = default_values["thickness"]["unit"]

    length_units = ('mm', 'micron')
    mass_units = ('g', 'kg')
    col1, col2 = st.columns(2)
    with col1:
        cell_mass       = st.number_input(label='Cell Mass', step = 0.1, min_value=0.0, value=float(cell_mass))
        cell_width      = st.number_input(label='Cell Width', step = 0.1, min_value=0.0, value=float(cell_width))
        cell_height     = st.number_input(label='Cell Height', step = 0.1, min_value=0.0, value=float(cell_height))
        cell_thickness  = st.number_input(label='Cell Thickness', step = 0.1, min_value=0.0, value=float(cell_thickness))
    with col2:
        cell_mass_unit      = st.selectbox('',mass_units, key="selectbox_cell_mass_unit", index=mass_units.index(cell_mass_unit))
        cell_width_unit     = st.selectbox('',length_units, key="selectbox_cell_width_unit", index=length_units.index(cell_width_unit))
        cell_height_unit    = st.selectbox('',length_units, key="selectbox_cell_height_unit", index=length_units.index(cell_height_unit))
        cell_thickness_unit = st.selectbox('',length_units, key="selectbox_cell_thickness_unit", index=length_units.index(cell_thickness_unit))
    
    output_dict = {"mass": {
            "value": cell_mass,
            "unit": label_uri_dict[unit_prefLabel[cell_mass_unit]]
        },
        "width": {
            "value": cell_width,
            "unit": label_uri_dict[unit_prefLabel[cell_width_unit]]
        },
        "height": {
            "value": cell_height,
            "unit": label_uri_dict[unit_prefLabel[cell_height_unit]]
        },
        "thickness": {
            "value": cell_thickness,
            "unit": label_uri_dict[unit_prefLabel[cell_thickness_unit]]
        }}
    return output_dict

def round_cell_properties(default_values):
    st.write(default_values)
    length_units = ('mm', 'micron')
    mass_units = ('g', 'kg')
    col1, col2 = st.columns(2)
    with col1:
        cell_mass       = st.number_input(label='Cell Mass', step = 0.1, min_value=0.0, value=float(default_values["mass"]["value"]))
        cell_diameter   = st.number_input(label='Cell Width', step = 0.1, min_value=0.0, value=float(default_values["diameter"]["value"]))
        cell_height     = st.number_input(label='Cell Height', step = 0.1, min_value=0.0, value=float(default_values["height"]["value"]))
    with col2:
        cell_mass_unit      = st.selectbox('',mass_units, key="selectbox_cell_mass_unit", index=mass_units.index(default_values["mass"]["unit"]))
        cell_diameter_unit  = st.selectbox('',length_units, key="selectbox_cell_width_unit", index=length_units.index(default_values["diameter"]["unit"]))
        cell_height_unit    = st.selectbox('',length_units, key="selectbox_cell_height_unit", index=length_units.index(default_values["height"]["unit"]))
    
    output_dict = {"mass": {
            "value": cell_mass,
            "unit": label_uri_dict[unit_prefLabel[cell_mass_unit]]
        },
        "diameter": {
            "value": cell_diameter,
            "unit": label_uri_dict[unit_prefLabel[cell_diameter_unit]]
        },
        "height": {
            "value": cell_height,
            "unit": label_uri_dict[unit_prefLabel[cell_height_unit]]
        }}
    return output_dict


def set_cell_formats(default_values):
    formats = ['Coin', 'Cylindrical', 'Pouch', 'Prismatic']
    col1, col2 = st.columns(2)
    with col1:
        format_option = st.selectbox(
        'Battery Cell Format',
        formats, index=formats.index(default_values["format"]))

    with col2:
        if format_option == 'Coin':
            types = ['R2032', 'R2016', 'Other']
            type_option = st.selectbox('Standard Size',types)
        elif format_option == 'Cylindrical':
            types = ['1865', '2170', '4680']
            type_option = st.selectbox('Standard Size',types)
        else:
            type_option = 'Other'
    return{"cell_format": {"value": format_option}, 
        "cell_type": {"value": type_option}}

def cell_production_metadata(default_values):
    name = st.text_input(label='Cell Name', value=default_values["name"])
    production_date = st.date_input("Production Date", value=datetime.datetime.strptime(default_values["productionDate"], '%Y-%m-%d').date())
    creator = st.text_input(label='Creator ORCID (Person)', value=default_values["creator"])
    manufacturer = st.text_input(label='Manufacturer ROR ID (Organization)', value=default_values["manufacturer"])

    if len(creator) != 0:
        creator = orcid_namespace + creator
    
    if len(manufacturer) != 0:
        manufacturer = rorid_namespace + manufacturer

    output_dict = {
           "name": name, 
           "productionDate": str(production_date),
           "creator": creator, 
           "manufacturer": manufacturer}
    return output_dict

def cell_nominal_electrical_properties():
    capacity_units = ['mAh', 'Ah']
    energy_units = ['mWh', 'Wh']
    col1, col2 = st.columns(2)
    with col1:
        cell_capacity = st.number_input(label='Nominal Capacity', min_value=0.00, step = 0.01)
        cell_energy = st.number_input(label='Nominal Energy', min_value=0)
    with col2:
        cell_capacity_unit = st.selectbox('',capacity_units, key="selectbox_cell_capacity_unit")
        cell_energy_unit = st.selectbox('',energy_units, key="selectbox_cell_energy_unit")
    output_dict = {
        "cell_capacity": {
            "value": cell_capacity, 
            "unit": label_uri_dict[unit_prefLabel[cell_capacity_unit]]},
        "cell_energy": {
            "value": cell_energy,
            "unit": label_uri_dict[unit_prefLabel[cell_energy_unit]]}}
    return output_dict

def set_active_material(elde, am_default_values):
    specific_capacity_units = ['mAh/g', 'Ah/kg']
    density_units = ['g/cm3', 'kg/L', "kg/m3"]
    if elde =="pe":
        materials = ['LFP', 'NMC', 'NMC811', 'NMC622', 'NMC532', 'NMC111', 'LCO', 'LNMO', 'NCA']
    else:
        materials = ['Graphite', 'Si', 'Li']
    am = st.selectbox('Active Material',materials, key=elde+"_am")
    col1, col2 = st.columns(2)
    with col1:
        am_specific_capacity = st.number_input(label='Specific Capacity', step = 0.1, min_value=0.0, key=elde+"_am_specific_capacity", value = float(am_default_values["specific_capacity"]["value"]))
        am_density = st.number_input(label='AM Density', step = 0.1, min_value=0.0, key=elde+"_am_denisty", value = float(am_default_values["am_density"]["value"]))
    with col2:
        am_specific_capacity_unit = st.selectbox('',specific_capacity_units, key=elde + "_selectbox_am_specific_capacity_unit", index=specific_capacity_units.index(am_default_values["specific_capacity"]["unit"]))
        am_density_unit = st.selectbox('',density_units, key=elde+"_selectbox_am_density_unit", index=density_units.index(am_default_values["am_density"]["unit"]))
    return{"active_material": {"value": material_prefLabel[am]}, 
           "specific_capacity": {
               "value": am_specific_capacity, 
               "unit": label_uri_dict[unit_prefLabel[am_specific_capacity_unit]]}, 
           "am_density": {
               "value": am_density, 
               "unit": label_uri_dict[unit_prefLabel[am_density_unit]]}}

def set_binder_material(elde, binder_default_values):
    density_units = ['g/cm3', 'kg/L', "kg/m3"]
    binder = st.selectbox('Positive Electrode Binder',('PVDF', 'CMC'), key=elde+"_binder")
    col1, col2 = st.columns(2)
    with col1:
        binder_density = st.number_input(label='Binder Density', step = 0.1, min_value=0.0, key = elde+"_binder_density", value = float(binder_default_values["binder_density"]["value"]))
    with col2:
        binder_density_unit = st.selectbox('',density_units, key=elde+"_selectbox_binder_density_unit", index=density_units.index(binder_default_values["binder_density"]["unit"]))
    return{"binder": {"value": material_prefLabel[binder]}, 
           "binder_density": {
               "value": binder_density, 
               "unit": label_uri_dict[unit_prefLabel[binder_density_unit]]}}

def set_additive_material(elde, additive_default_values):
    density_units = ['g/cm3', 'kg/L', "kg/m3"]
    additive = st.selectbox('Positive Electrode Conductive Additive',('Carbon Black', 'Carbon Nanotubes'), key=elde+"_additive")
    col1, col2 = st.columns(2)
    with col1:
        additive_density = st.number_input(label='Additive Density', step = 0.1, min_value=0.0, key = elde+"_additive_density", value = float(additive_default_values["additive_density"]["value"]))
    with col2:
        additive_density_unit = st.selectbox('',density_units, key=elde+"_selectbox_additive_density_unit", index=density_units.index(additive_default_values["additive_density"]["unit"]))
    return{"additive": {"value": material_prefLabel[additive]}, 
           "additive_density": {
               "value": additive_density, 
               "unit": label_uri_dict[unit_prefLabel[additive_density_unit]]}}

def set_coating_properties(elde, coating_default_values):
    length_units = ['micron', 'mm']
    mass_loading_units = ['mg/cm2', 'kg/m2']
    dual_coated = st.checkbox('Dual-Coated', key = elde+"_dual_coated")
    am_mass_fraction = st.number_input(label='Active Material Mass Fraction', min_value=0.0, max_value=1.0, step =0.01, key=elde+"_input_am_mass_fraction", value = float(coating_default_values["am_mass_fraction"]["value"]))
    binder_mass_fraction = st.number_input(label='Binder Mass Fraction', min_value=0.0, max_value=1.0, step =0.01, key=elde+"_input_binder_mass_fraction", value = float(coating_default_values["binder_mass_fraction"]["value"]))
    additive_mass_fraction = st.number_input(label='Additive Mass Fraction', min_value=0.0, max_value=1.0, step =0.01, key=elde+"_input_additive_mass_fraction", value = float(coating_default_values["additive_mass_fraction"]["value"]))

    col1, col2 = st.columns(2)
    with col1:
        coating_thickness = st.number_input(label='Coating Thickness', step = 0.1, min_value=0.0, key=elde+"_coating_thickness", value = float(coating_default_values["coating_thickness"]["value"]))
        mass_loading = st.number_input(label='Mass Loading', step = 0.1, min_value=0.0, key=elde+"_mass_loading", value = float(coating_default_values["mass_loading"]["value"]))
    with col2:
        coating_thickness_unit = st.selectbox('',length_units, key=elde+"_selectbox_coating_thickness_unit", index=length_units.index(coating_default_values["coating_thickness"]["unit"]))
        mass_loading_unit = st.selectbox('',mass_loading_units, key=elde+"_selectbox_mass_loading_unit", index=mass_loading_units.index(coating_default_values["mass_loading"]["unit"]))
    return{"am_mass_fraction": {"value": am_mass_fraction}, 
           "binder_mass_fraction": {"value": binder_mass_fraction}, 
           "additive_mass_fraction": {"value": additive_mass_fraction}, 
           "coating_thickness": {
               "value": coating_thickness, 
               "unit": label_uri_dict[unit_prefLabel[coating_thickness_unit]]}, 
           "mass_loading": {
               "value": mass_loading, 
               "unit": label_uri_dict[unit_prefLabel[mass_loading_unit]]}}

def set_current_collector_properties(elde, current_collector_default_values):
    length_units = ['micron', 'mm']
    col1, col2 = st.columns(2)
    with col1:
        #pe_mass = st.number_input(label='Positive Electrode Mass', step = 0.1, min_value=0.0)
        current_collector_thickness = st.number_input(label='Current Collector Thickness', step = 0.1, min_value=0.0, key = elde+"_current_collector_thickness", value = float(current_collector_default_values["current_collector_thickness"]["value"]))
    with col2:
        #pe_mass_unit = st.selectbox('',('kg', 'g'), key="selectbox_pe_mass_unit")
        current_collector_thickness_unit = st.selectbox('',length_units, key=elde+"_selectbox_cc_thickness_unit", index=length_units.index(current_collector_default_values["current_collector_thickness"]["unit"]))
    return{"current_collector_thickness": {
                "value": current_collector_thickness, 
                "unit": label_uri_dict[unit_prefLabel[current_collector_thickness_unit]]}}

def set_rectangular_electrode_properties(elde, dimensions_default_values):
    length_units = ['mm', 'cm']
    thickness_units = ['micron', 'mm']
    layers = st.number_input(label='Electrode Layers Per Cell', step = 1, min_value=0, key=elde+"_layers", value = (dimensions_default_values["electrode_layers"]["value"]))
    col1, col2 = st.columns(2)
    with col1:
        #pe_mass = st.number_input(label='Electrode Mass', step = 0.1, min_value=0.0)
        #pe_volume = st.number_input(label='Electrode Volume', step = 0.1, min_value=0.0)
        electrode_width = st.number_input(label='Electrode Width', step = 0.1, min_value=0.0, key = elde + "_width", value = float(dimensions_default_values["electrode_width"]["value"]))
        electrode_height = st.number_input(label='Electrode Height', step = 0.1, min_value=0.0, key = elde + "_height", value = float(dimensions_default_values["electrode_height"]["value"]))
        electrode_thickness = st.number_input(label='Electrode Thickness', step = 0.1, min_value=0.0, key = elde + "_thickness", value = float(dimensions_default_values["electrode_thickness"]["value"]))
    with col2:
        #pe_mass_unit = st.selectbox('',('kg', 'g'), key="selectbox_pe_mass_unit")
        #pe_volume_unit = st.selectbox('',('L', 'mL'), key="selectbox_pe_volume_unit")
        electrode_width_unit = st.selectbox('',length_units, key=elde+"_selectbox_width_unit", index=length_units.index(dimensions_default_values["electrode_width"]["unit"]))
        electrode_height_unit = st.selectbox('',length_units, key=elde+"_selectbox_height_unit", index=length_units.index(dimensions_default_values["electrode_height"]["unit"]))
        electrode_thickness_unit = st.selectbox('',thickness_units, key=elde+"_selectbox_pe_thickness_unit", index=thickness_units.index(dimensions_default_values["electrode_thickness"]["unit"]))
    return{"electrode_layers": {"value":layers},
           "electrode_width": {
               "value": electrode_width, 
               "unit": label_uri_dict[unit_prefLabel[electrode_width_unit]]},
           "electrode_height": {
               "value": electrode_height, 
               "unit": label_uri_dict[unit_prefLabel[electrode_height_unit]]},
           "electrode_thickness": {
               "value": electrode_thickness, 
               "unit": label_uri_dict[unit_prefLabel[electrode_thickness_unit]]}}

def set_circular_electrode_properties(elde, dimensions_default_values):
    length_units = ['mm', 'cm']
    thickness_units = ['micron', 'mm']
    layers = st.number_input(label='Electrode Layers Per Cell', step = 1, min_value=0, key=elde+"_layers")
    col1, col2 = st.columns(2)
    with col1:
        #pe_mass = st.number_input(label='Electrode Mass', step = 0.1, min_value=0.0)
        #pe_volume = st.number_input(label='Electrode Volume', step = 0.1, min_value=0.0)
        electrode_diameter = st.number_input(label='Electrode Diameter', step = 0.1, min_value=0.0, key = elde+"_diameter", value = float(dimensions_default_values["electrode_diameter"]["value"]))
        electrode_thickness = st.number_input(label='Electrode Thickness', step = 0.1, min_value=0.0, key = elde + "_thickness", value = float(dimensions_default_values["electrode_thickness"]["value"]))
    with col2:
        #pe_mass_unit = st.selectbox('',('kg', 'g'), key="selectbox_pe_mass_unit")
        #pe_volume_unit = st.selectbox('',('L', 'mL'), key="selectbox_pe_volume_unit")
        electrode_diameter_unit = st.selectbox('',length_units, key=elde+"_selectbox_diameter_unit", index=length_units.index(dimensions_default_values["electrode_diameter"]["unit"]))
        electrode_thickness_unit = st.selectbox('',thickness_units, key=elde+"_selectbox_thickness_unit", index=thickness_units.index(dimensions_default_values["electrode_thickness"]["unit"]))
    return{"electrode_layers": {"value":layers},
           "electrode_diameter": {
               "value": electrode_diameter, 
               "unit": label_uri_dict[unit_prefLabel[electrode_diameter_unit]]},
           "electrode_thickness": {
               "value": electrode_thickness, 
               "unit": label_uri_dict[unit_prefLabel[electrode_thickness_unit]]}}

def set_rectangular_separator_properties(sep_default_values):
    mass_units = ['g', 'kg']
    length_units = ['mm', 'cm']
    thickness_units = ['micron', 'mm']
    col1, col2 = st.columns(2)
    with col1:
        separator_mass = st.number_input(label='Mass', step = 0.1, min_value=0.0, value = float(sep_default_values["separator_mass"]["value"]))
        separator_porosity = st.number_input(label='Porosity', step = 0.1, min_value=0.0, value = float(sep_default_values["separator_porosity"]["value"]))
        separator_width = st.number_input(label='Width', step = 0.1, min_value=0.0, key = "sep_width", value = float(sep_default_values["separator_width"]["value"]))
        separator_height = st.number_input(label='Height', step = 0.1, min_value=0.0, key = "sep_height", value = float(sep_default_values["separator_height"]["value"]))
        separator_thickness = st.number_input(label='Thickness', step = 0.1, min_value=0.0, key = "sep_thickness", value = float(sep_default_values["separator_thickness"]["value"]))
    with col2:
        separator_mass_unit = st.selectbox('',mass_units, key="selectbox_pe_mass_unit", index=mass_units.index(sep_default_values["separator_mass"]["unit"]))
        separator_porosity_unit = st.selectbox('',('-'), key="selectbox_pe_volume_unit")
        separator_width_unit = st.selectbox('',length_units, key="sep_selectbox_width_unit", index=length_units.index(sep_default_values["separator_width"]["unit"]))
        separator_height_unit = st.selectbox('',length_units, key="sep_selectbox_height_unit", index=length_units.index(sep_default_values["separator_height"]["unit"]))
        separator_thickness_unit = st.selectbox('',thickness_units, key="sep_selectbox_pe_thickness_unit", index=thickness_units.index(sep_default_values["separator_thickness"]["unit"]))
    return{"separator_mass": {
                "value": separator_mass, 
                "unit": label_uri_dict[unit_prefLabel[separator_mass_unit]]},
           "separator_porosity": {
               "value": separator_porosity},
           "separator_width": {
               "value": separator_width, 
               "unit": label_uri_dict[unit_prefLabel[separator_width_unit]]},
           "separator_height": {
               "value": separator_height, 
               "unit": label_uri_dict[unit_prefLabel[separator_height_unit]]},
           "separator_thickness": {
               "value": separator_thickness, 
               "unit": label_uri_dict[unit_prefLabel[separator_thickness_unit]]}}

def set_circular_separator_properties(sep_default_values):
    mass_units = ['g', 'kg']
    length_units = ['mm', 'cm']
    thickness_units = ['micron', 'mm']
    col1, col2 = st.columns(2)
    with col1:
        separator_mass = st.number_input(label='Mass', step = 0.1, min_value=0.0, value = float(sep_default_values["separator_mass"]["value"]))
        separator_porosity = st.number_input(label='Porosity', step = 0.1, min_value=0.0, value = float(sep_default_values["separator_mass"]["value"]))
        separator_diameter = st.number_input(label='Width', step = 0.1, min_value=0.0, key = "sep_diameter", value = float(sep_default_values["separator_diameter"]["value"]))
        separator_thickness = st.number_input(label='Thickness', step = 0.1, min_value=0.0, key = "sep_thickness", value = float(sep_default_values["separator_thickness"]["value"]))
    with col2:
        separator_mass_unit = st.selectbox('',mass_units, key="selectbox_pe_mass_unit", index=mass_units.index(sep_default_values["separator_mass"]["unit"]))
        separator_porosity_unit = st.selectbox('',('-'), key="selectbox_pe_volume_unit")
        separator_diameter_unit = st.selectbox('',length_units, key="sep_selectbox_width_unit", index=length_units.index(sep_default_values["separator_diameter"]["unit"]))
        separator_thickness_unit = st.selectbox('',thickness_units, key="sep_selectbox_pe_thickness_unit", index=thickness_units.index(sep_default_values["separator_thickness"]["unit"]))
    return{"separator_mass": {
                "value": separator_mass, 
                "unit": label_uri_dict[unit_prefLabel[separator_mass_unit]]},
           "separator_porosity": {
               "value": separator_porosity},
           "separator_diameter": {
               "value": separator_diameter, 
               "unit": label_uri_dict[unit_prefLabel[separator_diameter_unit]]},
           "separator_thickness": {
               "value": separator_thickness, 
               "unit": label_uri_dict[unit_prefLabel[separator_thickness_unit]]}}


def electrolyte():
    tab_labels = ["Properties", "Component 1", "Component 2", "--", "--", "--"]
    col1, col2 = st.columns(2)
    with col1:
        N_components = st.number_input(label='Number of Components', step = 1, min_value=0, value = 2)
        add_button = st.form_submit_button(label='Update Components')
    if add_button:
        for i in range(N_components+1):
            if i !=0:
                tab_labels[i] = "Component "+str(i)

    tabs = st.tabs(tab_labels)
    
    # Instantiate the lists in case they are not shown in the tabs
    material_1 = []
    component_amount_concentration_1 = []
    component_amount_concentration_unit_1 = "mol/L"
    quantity_type_1 = []
    material_2 = []
    component_amount_concentration_2 = []
    component_amount_concentration_unit_2 = "mol/L"
    quantity_type_2 = []
    material_3 = []
    component_amount_concentration_3 = []
    component_amount_concentration_unit_3 = "mol/L"
    quantity_type_3 = []
    material_4 = []
    component_amount_concentration_4 = []
    component_amount_concentration_unit_4 = "mol/L"
    quantity_type_4 = []
    material_5 = []
    component_amount_concentration_5 = []
    component_amount_concentration_unit_5 = "mol/L"
    quantity_type_5 = []

    materials = ['LiPF6', 'LiTFSI', "EC", "EMC", "DEC", "DMC", "FEC"]
    units = ['mol/L', 'mol/m3', 'mol/kg', 'mass fraction']

    with tabs[0]:
        col1, col2 = st.columns(2)
        with col1:
            electrolyte_volume = st.number_input(label='Volume', step = 0.1, min_value=0.0)
        with col2:
            electrolyte_volume_unit = st.selectbox('',('mL', 'microL'), key="elyte_selectbox_mass_unit")

    with tabs[1]:
        material_1 = st.selectbox('Material',materials, key="elyte_component_1")
        col1, col2 = st.columns(2)
        with col1:
            component_amount_concentration_1 = st.number_input(label='Quantity', step = 0.1, min_value=0.0, key = "amount_conc_input_1")
        with col2:
            component_amount_concentration_unit_1 = st.selectbox('',units, key="selectbox_amount_conc_unit_1")
        if component_amount_concentration_unit_1 == 'mass fraction':
            quantity_type_1 = "MassFraction"
        else:
            quantity_type_1 = "AmountConcentration"

    with tabs[2]:
        if N_components >= 2:
            material_2 = st.selectbox('Material',materials, key="elyte_component_2")
            col1, col2 = st.columns(2)
            with col1:
                component_amount_concentration_2 = st.number_input(label='Amount Concentration', step = 0.1, min_value=0.0, key = "amount_conc_input_2")
            with col2:
                component_amount_concentration_unit_2 = st.selectbox('',units, key="selectbox_amount_conc_unit_2")
            if component_amount_concentration_unit_2 == 'mass fraction':
                quantity_type_2 = "MassFraction"
            else:
                quantity_type_2 = "AmountConcentration"

    with tabs[3]:
        if N_components >= 3:
            material_3 = st.selectbox('Material',materials, key="elyte_component_3")
            col1, col2 = st.columns(2)
            with col1:
                component_amount_concentration_3 = st.number_input(label='Amount Concentration', step = 0.1, min_value=0.0, key = "amount_conc_input_3")
            with col2:
                component_amount_concentration_unit_3 = st.selectbox('',units, key="selectbox_amount_conc_unit_3")
            if component_amount_concentration_unit_3 == 'mass fraction':
                quantity_type_3 = "MassFraction"
            else:
                quantity_type_3 = "AmountConcentration"

    with tabs[4]:
        if N_components >= 4:
            material_4 = st.selectbox('Material',materials, key="elyte_component_4")
            col1, col2 = st.columns(2)
            with col1:
                component_amount_concentration_4 = st.number_input(label='Amount Concentration', step = 0.1, min_value=0.0, key = "amount_conc_input_4")
            with col2:
                component_amount_concentration_unit_4 = st.selectbox('',units, key="selectbox_amount_conc_unit_4")
            if component_amount_concentration_unit_4 == 'mass fraction':
                quantity_type_4 = "MassFraction"
            else:
                quantity_type_4 = "AmountConcentration"

    with tabs[5]:
        if N_components >= 5:
            material_5 = st.selectbox('Material',materials, key="elyte_component_5")
            col1, col2 = st.columns(2)
            with col1:
                component_amount_concentration_5 = st.number_input(label='Amount Concentration', step = 0.1, min_value=0.0, key = "amount_conc_input_5")
            with col2:
                component_amount_concentration_unit_5 = st.selectbox('',units, key="selectbox_amount_conc_unit_5")
            if component_amount_concentration_unit_5 == 'mass fraction':
                quantity_type_5 = "MassFraction"
            else:
                quantity_type_5 = "AmountConcentration"
    
    return{"electrolyte_volume": {
                "value": electrolyte_volume, 
                "unit": label_uri_dict[unit_prefLabel[electrolyte_volume_unit]]},
            "amount_list": [component_amount_concentration_1, 
                            component_amount_concentration_2,
                            component_amount_concentration_3,
                            component_amount_concentration_4,
                            component_amount_concentration_5],
            "quantity_type_list": [quantity_type_1,
                                   quantity_type_2,
                                   quantity_type_3,
                                   quantity_type_4,
                                   quantity_type_5],
            "material_list": [material_1,
                              material_2,
                              material_3,
                              material_4,
                              material_5],
            "quantity_value_list": [component_amount_concentration_1,
                                    component_amount_concentration_2,
                                    component_amount_concentration_3,
                                    component_amount_concentration_4,
                                    component_amount_concentration_5,],
            "quantity_unit_list": [label_uri_dict[unit_prefLabel[component_amount_concentration_unit_1]],
                                   label_uri_dict[unit_prefLabel[component_amount_concentration_unit_2]],
                                   label_uri_dict[unit_prefLabel[component_amount_concentration_unit_3]],
                                   label_uri_dict[unit_prefLabel[component_amount_concentration_unit_4]],
                                   label_uri_dict[unit_prefLabel[component_amount_concentration_unit_5]]],
           "material_1": {"value": material_1},
           "quantity_type_1": quantity_type_1,
           "amount_concentration_1": {
               "value": component_amount_concentration_1, 
               "unit": label_uri_dict[unit_prefLabel[component_amount_concentration_unit_1]]},
           "material_2": {"value": material_2},
           "amount_concentration_2": {
               "value": component_amount_concentration_2, 
               "unit": label_uri_dict[unit_prefLabel[component_amount_concentration_unit_2]]},
           "material_3": {"value": material_3},
           "amount_concentration_3": {
               "value": component_amount_concentration_3, 
               "unit": label_uri_dict[unit_prefLabel[component_amount_concentration_unit_3]]},
           "material_4": {"value": material_4},
           "amount_concentration_4": {
               "value": component_amount_concentration_4, 
               "unit": label_uri_dict[unit_prefLabel[component_amount_concentration_unit_4]]},
           "material_5": {"value": material_5},
           "amount_concentration_5": {
               "value": component_amount_concentration_5, 
               "unit": label_uri_dict[unit_prefLabel[component_amount_concentration_unit_5]]},}


def rectangular_electrode(elde, am_default_values, binder_default_values, additive_default_values, coating_default_values, current_collector_default_values, dimensions_default_values):
    tab_labels = ["Active Material", "Binder", "Additive", "Coating", "Current Collector", "Dimensions"]
    tabs = st.tabs(tab_labels)
    with tabs[0]:
        am_properties        = set_active_material(elde, am_default_values)
    with tabs[1]:
        binder_properties    = set_binder_material(elde, binder_default_values)
    with tabs[2]:
        additive_properties  = set_additive_material(elde, additive_default_values)
    with tabs[3]:
        coating_properties   = set_coating_properties(elde, coating_default_values)
    with tabs[4]:
        cc_properties        = set_current_collector_properties(elde, current_collector_default_values)
    with tabs[5]:
        dim_properties       = set_rectangular_electrode_properties(elde, dimensions_default_values)

    electrode_properties = {**am_properties, **binder_properties, **additive_properties, **coating_properties, **cc_properties, **dim_properties}
    return electrode_properties

def circular_electrode(elde, am_default_values, binder_default_values, additive_default_values, coating_default_values, current_collector_default_values, dimensions_default_values):
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Active Material", "Binder", "Additive", "Coating", "Current Collector", "Dimensions"])
    with tab1:
        am_properties        = set_active_material(elde, am_default_values)
    with tab2:
        binder_properties    = set_binder_material(elde, binder_default_values)
    with tab3:
        additive_properties  = set_additive_material(elde, additive_default_values)
    with tab4:
        coating_properties   = set_coating_properties(elde, coating_default_values)
    with tab5:
        cc_properties        = set_current_collector_properties(elde, current_collector_default_values)
    with tab6:
        dim_properties       = set_circular_electrode_properties(elde, dimensions_default_values)
        
    electrode_properties = {**am_properties, **binder_properties, **additive_properties, **coating_properties, **cc_properties, **dim_properties}
    return electrode_properties

def disperse_json_to_fields():
    cell_mass = 123


def disperse_fields_to_json(format_data, production_properties, physical_properties, electrical_properties, pe_properties, ne_properties, separator_properties, electrolyte_properties):
    with open('BatteryCell.jsonld') as f:
        jsonld_data = json.load(f)

    # Cell Production Properties
    jsonld_data["@id"]                      = namespace+str(uuid.uuid4())
    jsonld_data["schema:name"]              = production_properties["name"]
    jsonld_data["schema:productionDate"]    = production_properties["productionDate"]
    jsonld_data["schema:manufacturer"]      = production_properties["manufacturer"]
    jsonld_data["schema:creator"]           = production_properties["creator"]
    if format_data["cell_format"]["value"] == "Coin":
        jsonld_data["@type"] = "CoinCell"
    elif format_data["cell_format"]["value"] == "Pouch":
        jsonld_data["@type"] = "PouchCell"
    elif format_data["cell_format"]["value"] == "Prismatic":
        jsonld_data["@type"] = "PrismaticCell"
    elif format_data["cell_format"]["value"] == "Cylindrical":
        jsonld_data["@type"] = "CylindricalCell"
    

    if format_data["cell_format"]["value"] == "Coin" or format_data["cell_format"]["value"] == "Cylindrical":
        ## Cell Quantitative Property ID
        jsonld_data["hasQuantitativeProperty"][0]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasQuantitativeProperty"][1]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasQuantitativeProperty"][2]["@id"] = namespace+str(uuid.uuid4())
        del jsonld_data["hasQuantitativeProperty"][3]

        jsonld_data["hasQuantitativeProperty"][0]["@type"] = "Mass"
        jsonld_data["hasQuantitativeProperty"][1]["@type"] = "Diameter"
        jsonld_data["hasQuantitativeProperty"][2]["@type"] = "Height"

        ## Cell Quantitative Property Value ID
        jsonld_data["hasQuantitativeProperty"][0]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasQuantitativeProperty"][1]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasQuantitativeProperty"][2]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        ## Cell Quantitative Property Value Data
        jsonld_data["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"] = physical_properties["mass"]["value"]
        jsonld_data["hasQuantitativeProperty"][1]["hasQuantityValue"]["hasNumericalData"] = physical_properties["diameter"]["value"]
        jsonld_data["hasQuantitativeProperty"][2]["hasQuantityValue"]["hasNumericalData"] = physical_properties["height"]["value"]
        ## Cell Quantitative Property Value Unit
        jsonld_data["hasQuantitativeProperty"][0]["hasReferenceUnit"] = physical_properties["mass"]["unit"]
        jsonld_data["hasQuantitativeProperty"][1]["hasReferenceUnit"] = physical_properties["diameter"]["unit"]
        jsonld_data["hasQuantitativeProperty"][2]["hasReferenceUnit"] = physical_properties["height"]["unit"]
    else:
        ## Cell Quantitative Property ID
        jsonld_data["hasQuantitativeProperty"][0]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasQuantitativeProperty"][1]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasQuantitativeProperty"][2]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasQuantitativeProperty"][3]["@id"] = namespace+str(uuid.uuid4())
        ## Cell Quantitative Property Value ID
        jsonld_data["hasQuantitativeProperty"][0]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasQuantitativeProperty"][1]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasQuantitativeProperty"][2]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasQuantitativeProperty"][3]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        ## Cell Quantitative Property Value Data
        jsonld_data["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"] = physical_properties["mass"]["value"]
        jsonld_data["hasQuantitativeProperty"][1]["hasQuantityValue"]["hasNumericalData"] = physical_properties["width"]["value"]
        jsonld_data["hasQuantitativeProperty"][2]["hasQuantityValue"]["hasNumericalData"] = physical_properties["height"]["value"]
        jsonld_data["hasQuantitativeProperty"][3]["hasQuantityValue"]["hasNumericalData"] = physical_properties["thickness"]["value"]
        ## Cell Quantitative Property Value Unit
        jsonld_data["hasQuantitativeProperty"][0]["hasReferenceUnit"] = physical_properties["mass"]["unit"]
        jsonld_data["hasQuantitativeProperty"][1]["hasReferenceUnit"] = physical_properties["width"]["unit"]
        jsonld_data["hasQuantitativeProperty"][2]["hasReferenceUnit"] = physical_properties["height"]["unit"]
        jsonld_data["hasQuantitativeProperty"][3]["hasReferenceUnit"] = physical_properties["thickness"]["unit"]

    # Positive Electrode Properties
    jsonld_data["hasPositiveElectrode"]["@id"] = namespace+str(uuid.uuid4())
    if format_data["cell_format"]["value"] == "Coin":
        ## Positive Electrode Quantitiative Property ID
        del jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][3]
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][0]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][1]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][2]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][3]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][4]["@id"] = namespace+str(uuid.uuid4())

        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][0]["@type"] = "NumberOfEntities"
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][1]["@type"] = "MassLoading"
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][2]["@type"] = "Diameter"
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][3]["@type"] = "Thickness"
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][4]["@type"] = "Mass"

        ## Positive Electrode Quantitiative Property Value ID
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][0]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][1]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][2]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][3]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][4]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        ## Positive Electrode Quantitative Property Value Data
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"] = pe_properties["electrode_layers"]["value"]
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][1]["hasQuantityValue"]["hasNumericalData"] = pe_properties["mass_loading"]["value"]
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][2]["hasQuantityValue"]["hasNumericalData"] = pe_properties["electrode_diameter"]["value"]
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][3]["hasQuantityValue"]["hasNumericalData"] = pe_properties["electrode_thickness"]["value"]
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][4]["hasQuantityValue"]["hasNumericalData"] = []
        ## Positive Electrode Quantitative Property Value Unit
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][0]["hasReferenceUnit"] = "http://emmo.info/emmo#EMMO_41efdf5d_0c9c_4ea0_bb65_f8236e663be5"
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][1]["hasReferenceUnit"] = pe_properties["mass_loading"]["unit"]
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][2]["hasReferenceUnit"] = pe_properties["electrode_diameter"]["unit"]
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][3]["hasReferenceUnit"] = pe_properties["electrode_thickness"]["unit"]
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][4]["hasReferenceUnit"] = []
    else:
        ## Positive Electrode Quantitiative Property ID
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][0]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][1]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][2]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][3]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][4]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][5]["@id"] = namespace+str(uuid.uuid4())
        ## Positive Electrode Quantitiative Property Value ID
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][0]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][1]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][2]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][3]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][4]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][5]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        ## Positive Electrode Quantitative Property Value Data
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"] = pe_properties["electrode_layers"]["value"]
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][1]["hasQuantityValue"]["hasNumericalData"] = pe_properties["mass_loading"]["value"]
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][2]["hasQuantityValue"]["hasNumericalData"] = pe_properties["electrode_width"]["value"]
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][3]["hasQuantityValue"]["hasNumericalData"] = pe_properties["electrode_height"]["value"]
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][4]["hasQuantityValue"]["hasNumericalData"] = pe_properties["electrode_thickness"]["value"]
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][5]["hasQuantityValue"]["hasNumericalData"] = []
        ## Positive Electrode Quantitative Property Value Unit
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][0]["hasReferenceUnit"] = "http://emmo.info/emmo#EMMO_41efdf5d_0c9c_4ea0_bb65_f8236e663be5"
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][1]["hasReferenceUnit"] = pe_properties["mass_loading"]["unit"]
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][2]["hasReferenceUnit"] = pe_properties["electrode_width"]["unit"]
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][3]["hasReferenceUnit"] = pe_properties["electrode_height"]["unit"]
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][4]["hasReferenceUnit"] = pe_properties["electrode_thickness"]["unit"]
        jsonld_data["hasPositiveElectrode"]["hasQuantitativeProperty"][5]["hasReferenceUnit"] = []

    # Positive Electrode Current Collector
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][0]["@id"] = namespace+str(uuid.uuid4())
    ## Positive Electrode Current Collector Quantitative Property ID
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][0]["hasQuantitativeProperty"][0]["@id"] = namespace+str(uuid.uuid4())
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][0]["hasQuantitativeProperty"][0]["@id"] = namespace+str(uuid.uuid4())
    ## Positive Electrode Current Collector Quantitative Property Value ID
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][0]["hasQuantitativeProperty"][0]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][0]["hasQuantitativeProperty"][1]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
    ## Positive Electrode Current Collector Quantitative Property Value Data
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][0]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"] = pe_properties["current_collector_thickness"]["value"]
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][0]["hasQuantitativeProperty"][1]["hasQuantityValue"]["hasNumericalData"] = []
    ## Positive Electrode Current Collector Quantitative Property Value Unit
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][0]["hasQuantitativeProperty"][0]["hasReferenceUnit"] = pe_properties["current_collector_thickness"]["unit"]
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][0]["hasQuantitativeProperty"][1]["hasReferenceUnit"] = []
    
    # Positive Electrode Coating
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["@id"] = namespace+str(uuid.uuid4())
    ## Positive Electrode Coating Quantitiative Property ID
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasQuantitativeProperty"][0]["@id"] = namespace+str(uuid.uuid4())
    ## Positive Electrode Coating Quantitiative Property Value ID
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasQuantitativeProperty"][0]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
    ## Positive Electrode Coating Quantitiative Property Value Data
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"] = pe_properties["coating_thickness"]["value"]
    ## Positive Electrode Coating Quantitiative Property Value Unit
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasQuantitativeProperty"][0]["hasReferenceUnit"] = pe_properties["coating_thickness"]["unit"]
    
    # Positive Electrode Active Material
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][0]["@id"] = namespace+str(uuid.uuid4())
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][0]["@type"] = pe_properties["active_material"]["value"]
    ## Positive Electrode Active Material Quantitative Property ID
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][0]["@id"] = namespace+str(uuid.uuid4())
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][1]["@id"] = namespace+str(uuid.uuid4())
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][2]["@id"] = namespace+str(uuid.uuid4())
    ## Positive Electrode Active Material Quantitative Property Value ID
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][0]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][1]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][2]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
    ## Positive Electrode Active Material Quantitative Property Value Data
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"] = pe_properties["am_mass_fraction"]["value"]
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][1]["hasQuantityValue"]["hasNumericalData"] = pe_properties["am_density"]["value"]
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][2]["hasQuantityValue"]["hasNumericalData"] = pe_properties["specific_capacity"]["value"]
    ## Positive Electrode Active Material Quantitative Property Value Unit
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][0]["hasReferenceUnit"] = "http://emmo.info/emmo#EMMO_18448443_dcf1_49b8_a321_cf46e2c393e1"
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][1]["hasReferenceUnit"] = pe_properties["am_density"]["unit"]
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][2]["hasReferenceUnit"] = pe_properties["specific_capacity"]["unit"]
    
    # Positive Electrode Binder
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][1]["@id"] = namespace+str(uuid.uuid4())
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][1]["@type"] = pe_properties["binder"]["value"]
    ## Positive Electrode Binder Quantitative Property ID
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][1]["hasQuantitativeProperty"][0]["@id"] = namespace+str(uuid.uuid4())
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][1]["hasQuantitativeProperty"][1]["@id"] = namespace+str(uuid.uuid4())
    ## Positive Electrode Binder Quantitative Property Value ID
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][1]["hasQuantitativeProperty"][0]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][1]["hasQuantitativeProperty"][1]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
    ## Positive Electrode Binder Quantitative Property Value Data
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][1]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"] = pe_properties["binder_mass_fraction"]["value"]
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][1]["hasQuantitativeProperty"][1]["hasQuantityValue"]["hasNumericalData"] = pe_properties["binder_density"]["value"]
    ## Positive Electrode Binder Quantitative Property Value Unit
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][1]["hasQuantitativeProperty"][0]["hasReferenceUnit"] = "http://emmo.info/emmo#EMMO_18448443_dcf1_49b8_a321_cf46e2c393e1"
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][1]["hasQuantitativeProperty"][1]["hasReferenceUnit"] = pe_properties["binder_density"]["unit"]
    
    # Positive Electrode Additive
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][2]["@id"] = namespace+str(uuid.uuid4())
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][2]["@type"] = pe_properties["additive"]["value"]
    ## Positive Electrode Additive Quantitative Property ID
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][2]["hasQuantitativeProperty"][0]["@id"] = namespace+str(uuid.uuid4())
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][2]["hasQuantitativeProperty"][1]["@id"] = namespace+str(uuid.uuid4())
    ## Positive Electrode Additive Quantitative Property Value ID
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][2]["hasQuantitativeProperty"][0]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][2]["hasQuantitativeProperty"][1]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
    ## Positive Electrode Additive Quantitative Property Value Data
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][2]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"] = pe_properties["additive_mass_fraction"]["value"]    
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][2]["hasQuantitativeProperty"][1]["hasQuantityValue"]["hasNumericalData"] = pe_properties["additive_density"]["value"]
    ## Positive Electrode Additive Quantitative Property Value Unit
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][2]["hasQuantitativeProperty"][0]["hasReferenceUnit"] = "http://emmo.info/emmo#EMMO_18448443_dcf1_49b8_a321_cf46e2c393e1"
    jsonld_data["hasPositiveElectrode"]["hasConstituent"][1]["hasConstituent"][2]["hasQuantitativeProperty"][1]["hasReferenceUnit"] = pe_properties["additive_density"]["unit"]

    # Negative Electrode Properties
    jsonld_data["hasNegativeElectrode"]["@id"] = namespace+str(uuid.uuid4())
    if format_data["cell_format"]["value"] == "Coin":
        ## Negative Electrode Quantitiative Property ID
        del jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][3]
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][0]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][1]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][2]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][3]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][4]["@id"] = namespace+str(uuid.uuid4())

        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][0]["@type"] = "NumberOfEntities"
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][1]["@type"] = "MassLoading"
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][2]["@type"] = "Diameter"
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][3]["@type"] = "Thickness"
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][4]["@type"] = "Mass"
        ## Negative Electrode Quantitiative Property Value ID
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][0]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][1]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][2]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][3]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][4]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        ## Negative Electrode Quantitative Property Value Data
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"] = ne_properties["electrode_layers"]["value"]
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][1]["hasQuantityValue"]["hasNumericalData"] = ne_properties["mass_loading"]["value"]
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][2]["hasQuantityValue"]["hasNumericalData"] = ne_properties["electrode_diameter"]["value"]
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][3]["hasQuantityValue"]["hasNumericalData"] = ne_properties["electrode_thickness"]["value"]
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][4]["hasQuantityValue"]["hasNumericalData"] = []
        ## Negative Electrode Quantitative Property Value Unit
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][0]["hasReferenceUnit"] = "http://emmo.info/emmo#EMMO_41efdf5d_0c9c_4ea0_bb65_f8236e663be5"
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][1]["hasReferenceUnit"] = ne_properties["mass_loading"]["unit"]
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][2]["hasReferenceUnit"] = ne_properties["electrode_diameter"]["unit"]
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][3]["hasReferenceUnit"] = ne_properties["electrode_thickness"]["unit"]
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][4]["hasReferenceUnit"] = []
    else:
        ## Negative Electrode Quantitiative Property ID
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][0]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][1]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][2]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][3]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][4]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][5]["@id"] = namespace+str(uuid.uuid4())
        ## Negative Electrode Quantitiative Property Value ID
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][0]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][1]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][2]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][3]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][4]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][5]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        ## Negative Electrode Quantitative Property Value Data
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"] = ne_properties["electrode_layers"]["value"]
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][1]["hasQuantityValue"]["hasNumericalData"] = ne_properties["mass_loading"]["value"]
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][2]["hasQuantityValue"]["hasNumericalData"] = ne_properties["electrode_width"]["value"]
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][3]["hasQuantityValue"]["hasNumericalData"] = ne_properties["electrode_height"]["value"]
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][4]["hasQuantityValue"]["hasNumericalData"] = ne_properties["electrode_thickness"]["value"]
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][5]["hasQuantityValue"]["hasNumericalData"] = []
        ## Negative Electrode Quantitative Property Value Unit
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][0]["hasReferenceUnit"] = "http://emmo.info/emmo#EMMO_41efdf5d_0c9c_4ea0_bb65_f8236e663be5"
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][1]["hasReferenceUnit"] = ne_properties["mass_loading"]["unit"]
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][2]["hasReferenceUnit"] = ne_properties["electrode_width"]["unit"]
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][3]["hasReferenceUnit"] = ne_properties["electrode_height"]["unit"]
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][4]["hasReferenceUnit"] = ne_properties["electrode_thickness"]["unit"]
        jsonld_data["hasNegativeElectrode"]["hasQuantitativeProperty"][5]["hasReferenceUnit"] = []

    # Negative Electrode Current Collector
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][0]["@id"] = namespace+str(uuid.uuid4())
    ## Negative Electrode Current Collector Quantitative Property ID
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][0]["hasQuantitativeProperty"][0]["@id"] = namespace+str(uuid.uuid4())
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][0]["hasQuantitativeProperty"][0]["@id"] = namespace+str(uuid.uuid4())
    ## Negative Electrode Current Collector Quantitative Property Value ID
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][0]["hasQuantitativeProperty"][0]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][0]["hasQuantitativeProperty"][1]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
    ## Negative Electrode Current Collector Quantitative Property Value Data
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][0]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"] = ne_properties["current_collector_thickness"]["value"]
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][0]["hasQuantitativeProperty"][1]["hasQuantityValue"]["hasNumericalData"] = []
    ## Negative Electrode Current Collector Quantitative Property Value Unit
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][0]["hasQuantitativeProperty"][0]["hasReferenceUnit"] = ne_properties["current_collector_thickness"]["unit"]
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][0]["hasQuantitativeProperty"][1]["hasReferenceUnit"] = []
    
    # Negative Electrode Coating
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["@id"] = namespace+str(uuid.uuid4())
    ## Negative Electrode Coating Quantitiative Property ID
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasQuantitativeProperty"][0]["@id"] = namespace+str(uuid.uuid4())
    ## Negative Electrode Coating Quantitiative Property Value ID
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasQuantitativeProperty"][0]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
    ## Negative Electrode Coating Quantitiative Property Value Data
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"] = ne_properties["coating_thickness"]["value"]
    ## Negative Electrode Coating Quantitiative Property Value Unit
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasQuantitativeProperty"][0]["hasReferenceUnit"] = ne_properties["coating_thickness"]["unit"]
    
    # Negative Electrode Active Material
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][0]["@id"] = namespace+str(uuid.uuid4())
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][0]["@type"] = ne_properties["active_material"]["value"]
    ## Negative Electrode Active Material Quantitative Property ID
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][0]["@id"] = namespace+str(uuid.uuid4())
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][1]["@id"] = namespace+str(uuid.uuid4())
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][2]["@id"] = namespace+str(uuid.uuid4())
    ## Negative Electrode Active Material Quantitative Property Value ID
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][0]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][1]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][2]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
    ## Negative Electrode Active Material Quantitative Property Value Data
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"] = ne_properties["am_mass_fraction"]["value"]
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][1]["hasQuantityValue"]["hasNumericalData"] = ne_properties["am_density"]["value"]
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][2]["hasQuantityValue"]["hasNumericalData"] = ne_properties["specific_capacity"]["value"]
    ## Negative Electrode Active Material Quantitative Property Value Unit
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][0]["hasReferenceUnit"] = "http://emmo.info/emmo#EMMO_18448443_dcf1_49b8_a321_cf46e2c393e1"
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][1]["hasReferenceUnit"] = ne_properties["am_density"]["unit"]
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][0]["hasQuantitativeProperty"][2]["hasReferenceUnit"] = ne_properties["specific_capacity"]["unit"]
    
    # Negative Electrode Binder
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][1]["@id"] = namespace+str(uuid.uuid4())
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][1]["@type"] = ne_properties["binder"]["value"]
    ## Negative Electrode Binder Quantitative Property ID
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][1]["hasQuantitativeProperty"][0]["@id"] = namespace+str(uuid.uuid4())
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][1]["hasQuantitativeProperty"][1]["@id"] = namespace+str(uuid.uuid4())
    ## Negative Electrode Binder Quantitative Property Value ID
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][1]["hasQuantitativeProperty"][0]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][1]["hasQuantitativeProperty"][1]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
    ## Negative Electrode Binder Quantitative Property Value Data
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][1]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"] = ne_properties["binder_mass_fraction"]["value"]
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][1]["hasQuantitativeProperty"][1]["hasQuantityValue"]["hasNumericalData"] = ne_properties["binder_density"]["value"]
    ## Negative Electrode Binder Quantitative Property Value Unit
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][1]["hasQuantitativeProperty"][0]["hasReferenceUnit"] = "http://emmo.info/emmo#EMMO_18448443_dcf1_49b8_a321_cf46e2c393e1"
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][1]["hasQuantitativeProperty"][1]["hasReferenceUnit"] = ne_properties["binder_density"]["unit"]
    
    # Negative Electrode Additive
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][2]["@id"] = namespace+str(uuid.uuid4())
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][2]["@type"] = ne_properties["additive"]["value"]
    ## Negative Electrode Additive Quantitative Property ID
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][2]["hasQuantitativeProperty"][0]["@id"] = namespace+str(uuid.uuid4())
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][2]["hasQuantitativeProperty"][1]["@id"] = namespace+str(uuid.uuid4())
    ## Negative Electrode Additive Quantitative Property Value ID
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][2]["hasQuantitativeProperty"][0]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][2]["hasQuantitativeProperty"][1]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
    ## Negative Electrode Additive Quantitative Property Value Data
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][2]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"] = ne_properties["additive_mass_fraction"]["value"]    
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][2]["hasQuantitativeProperty"][1]["hasQuantityValue"]["hasNumericalData"] = ne_properties["additive_density"]["value"]
    ## Negative Electrode Additive Quantitative Property Value Unit
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][2]["hasQuantitativeProperty"][0]["hasReferenceUnit"] = "http://emmo.info/emmo#EMMO_18448443_dcf1_49b8_a321_cf46e2c393e1"
    jsonld_data["hasNegativeElectrode"]["hasConstituent"][1]["hasConstituent"][2]["hasQuantitativeProperty"][1]["hasReferenceUnit"] = ne_properties["additive_density"]["unit"]

    if format_data["cell_format"]["value"] == "Coin":
        # Separator Properties
        jsonld_data["hasSeparator"]["@id"] = namespace+str(uuid.uuid4())
        ## Separator Quantitiative Property ID
        del jsonld_data["hasSeparator"]["hasQuantitativeProperty"][2]

        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][0]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][1]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][2]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][3]["@id"] = namespace+str(uuid.uuid4())

        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][0]["@type"] = "Mass"
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][1]["@type"] = "Diameter"
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][2]["@type"] = "Thickness"
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][3]["@type"] = "Porosity"
        ## Separator Quantitiative Property Value ID
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][0]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][1]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][2]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][3]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        ## Separator Quantitative Property Value Data
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"] = separator_properties["separator_mass"]["value"]
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][1]["hasQuantityValue"]["hasNumericalData"] = separator_properties["separator_diameter"]["value"]
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][2]["hasQuantityValue"]["hasNumericalData"] = separator_properties["separator_thickness"]["value"]
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][3]["hasQuantityValue"]["hasNumericalData"] = separator_properties["separator_porosity"]["value"]
        ## Separator Quantitative Property Value Unit
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][0]["hasReferenceUnit"] = separator_properties["separator_mass"]["unit"]
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][1]["hasReferenceUnit"] = separator_properties["separator_diameter"]["unit"]
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][2]["hasReferenceUnit"] = separator_properties["separator_thickness"]["unit"]
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][3]["hasReferenceUnit"] = "http://emmo.info/emmo#EMMO_9fd1e79d_41d1_44f8_8142_66dbdf0fc7ad"
    else:
        # Separator Properties
        jsonld_data["hasSeparator"]["@id"] = namespace+str(uuid.uuid4())
        ## Separator Quantitiative Property ID
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][0]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][1]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][2]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][3]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][4]["@id"] = namespace+str(uuid.uuid4())
        ## Separator Quantitiative Property Value ID
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][0]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][1]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][2]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][3]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][4]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
        ## Separator Quantitative Property Value Data
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"] = separator_properties["separator_mass"]["value"]
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][1]["hasQuantityValue"]["hasNumericalData"] = separator_properties["separator_width"]["value"]
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][2]["hasQuantityValue"]["hasNumericalData"] = separator_properties["separator_height"]["value"]
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][3]["hasQuantityValue"]["hasNumericalData"] = separator_properties["separator_thickness"]["value"]
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][4]["hasQuantityValue"]["hasNumericalData"] = separator_properties["separator_porosity"]["value"]
        ## Separator Quantitative Property Value Unit
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][0]["hasReferenceUnit"] = separator_properties["separator_mass"]["unit"]
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][1]["hasReferenceUnit"] = separator_properties["separator_width"]["unit"]
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][2]["hasReferenceUnit"] = separator_properties["separator_height"]["unit"]
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][3]["hasReferenceUnit"] = separator_properties["separator_thickness"]["unit"]
        jsonld_data["hasSeparator"]["hasQuantitativeProperty"][4]["hasReferenceUnit"] = "http://emmo.info/emmo#EMMO_9fd1e79d_41d1_44f8_8142_66dbdf0fc7ad"


    # Electrolyte
    jsonld_data["hasElectrolyte"]["@id"] = namespace+str(uuid.uuid4())
    ## Electrolyte Quantitative Property ID
    jsonld_data["hasElectrolyte"]["hasQuantitativeProperty"][0]["@id"] = namespace+str(uuid.uuid4())
    ## Electrolyte Quantitative Property Value ID
    jsonld_data["hasElectrolyte"]["hasQuantitativeProperty"][0]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
    ## Electrolyte Quantitative Property Value Data
    jsonld_data["hasElectrolyte"]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"] = electrolyte_properties["electrolyte_volume"]["value"]
    ## Electrolyte Quantitative Property Value Unit
    jsonld_data["hasElectrolyte"]["hasQuantitativeProperty"][0]["hasReferenceUnit"] = electrolyte_properties["electrolyte_volume"]["unit"]

    for i, elem in enumerate(electrolyte_properties["amount_list"]):
        if elem != []:
            if i > 1:
                jsonld_data["hasElectrolyte"]["hasConstituent"].append({
                "@type": "ChemicalMaterial",
                "hasQuantitativeProperty": [
                    {
                        "@type": "AmountConcentration",
                        "hasReferenceUnit": "http://emmo.info/emmo#EMMO_630acb48_c5c8_4b11_9d76_1342d7ed946f",
                        "hasQuantityValue": {
                            "@type": "Real",
                            "hasNumericalData": []
                        }
                    }
                ]
            })
            # Electrolyte Constituent
            jsonld_data["hasElectrolyte"]["hasConstituent"][i]["@type"] = "ChemicalMaterial"
            jsonld_data["hasElectrolyte"]["hasConstituent"][i]["@id"] = namespace+str(uuid.uuid4())
            ## Electrolyte Constituent Quantitative Property ID
            jsonld_data["hasElectrolyte"]["hasConstituent"][i]["hasQuantitativeProperty"][0]["@type"] = electrolyte_properties["quantity_type_list"][i]
            jsonld_data["hasElectrolyte"]["hasConstituent"][i]["hasQuantitativeProperty"][0]["@id"] = namespace+str(uuid.uuid4())
            ## Electrolyte Constituent Quantitative Property Value ID
            jsonld_data["hasElectrolyte"]["hasConstituent"][i]["hasQuantitativeProperty"][0]["hasQuantityValue"]["@id"] = namespace+str(uuid.uuid4())
            ## Electrolyte Constituent Quantitative Property Value Data
            jsonld_data["hasElectrolyte"]["hasConstituent"][i]["hasQuantitativeProperty"][0]["hasQuantityValue"]["hasNumericalData"] = electrolyte_properties["quantity_value_list"][i]
            ## Electrolyte Constituent Quantitative Property Value Unit
            jsonld_data["hasElectrolyte"]["hasConstituent"][i]["hasQuantitativeProperty"][0]["hasReferenceUnit"] = electrolyte_properties["quantity_unit_list"][i]

    return jsonld_data