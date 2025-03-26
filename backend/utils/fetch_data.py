import requests
import json
from pymongo import MongoClient
import random
from urllib.parse import quote_plus

# MongoDB connection
username = "tang0551"
password = "hUvvibJrWBYImwE0"
encoded_password = quote_plus(password)
client = MongoClient(f"mongodb+srv://{username}:{encoded_password}@cluster0.nl9y4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.get_database('SC2006_api_db')
institution_collection = db.Institution

# API endpoints
api_endpoints = {
    'general_info': 'https://data.gov.sg/api/action/datastore_search?resource_id=d_688b934f82c1059ed0a6993d2a829089&limit=1000',
    'subjects': 'https://data.gov.sg/api/action/datastore_search?resource_id=d_f1d144e423570c9d84dbc5102c2e664d&limit=1000',
    'distinctive_programs': 'https://data.gov.sg/api/action/datastore_search?resource_id=d_db1faeea02c646fa3abccfa5aba99214&limit=1000',
    'moe_programs': 'https://data.gov.sg/api/action/datastore_search?resource_id=d_b0697d22a7837a4eddf72efb66a36fc2&limit=1000',
    'cca': 'https://data.gov.sg/api/action/datastore_search?resource_id=d_9aba12b5527843afb0b2e8e4ed6ac6bd&limit=1000'
}

# Placeholder for school images (can be replaced with actual images)
school_images = [
    "https://images.unsplash.com/photo-1562774053-701939374585?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1186&q=80",
    "https://images.unsplash.com/photo-1562774053-701939374585?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1186&q=80",
    "https://images.unsplash.com/photo-1562774053-701939374585?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1186&q=80",
    "https://images.unsplash.com/photo-1562774053-701939374585?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1186&q=80",
    "https://images.unsplash.com/photo-1562774053-701939374585?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1186&q=80"
]

# Approximate coordinates for Singapore regions
region_coordinates = {
    'NORTH': {'lat': 0, 'lng': 0},
    'SOUTH': {'lat': 0, 'lng': 0},
    'EAST': {'lat': 0, 'lng': 0},
    'WEST': {'lat': 0, 'lng': 0},
    'CENTRAL': {'lat': 0, 'lng': 0}
}

def fetch_data(url):
    """Fetch data from API endpoint"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()['result']['records']
    except Exception as e:
        print(f"Error fetching data from {url}: {e}")
        return []

def get_coordinates(school_info):
    """Get approximate coordinates based on zone or add slight randomness"""
    zone = school_info.get('zone_code', 'CENTRAL')
    base_coords = region_coordinates.get(zone, region_coordinates['CENTRAL'])
    
    # Add some randomness to avoid all schools in a zone having the same coordinates
    lat_jitter = random.uniform(-0.02, 0.02)
    lng_jitter = random.uniform(-0.02, 0.02)
    
    return {
        'latitude': base_coords['lat'] + lat_jitter,
        'longitude': base_coords['lng'] + lng_jitter
    }

def generate_description(school_info):
    """Generate a description for the school"""
    name = school_info.get('school_name', '')
    type_code = school_info.get('type_code', '')
    nature_code = school_info.get('nature_code', '')
    session_code = school_info.get('session_code', '')
    level_code = school_info.get('mainlevel_code', '')
    
    description = f"{name} is a {nature_code.lower()} {type_code.lower()} offering {level_code.lower()} education. "
    description += f"It operates on a {session_code.lower()} basis. "
    
    if school_info.get('sap_ind', 'No') == 'Yes':
        description += "It is a Special Assistance Plan (SAP) school. "
    
    if school_info.get('autonomous_ind', 'No') == 'Yes':
        description += "It is an autonomous school. "
    
    if school_info.get('gifted_ind', 'No') == 'Yes':
        description += "It offers the Gifted Education Programme. "
    
    if school_info.get('ip_ind', 'No') == 'Yes':
        description += "It offers the Integrated Programme. "
    
    return description

def get_entry_requirements(level_code):
    """Determine entry requirements based on school level"""
    level_code = level_code.upper() if level_code else ""
    
    if "PRIMARY" in level_code:
        return ["Not Applicable"]
    elif "SECONDARY" in level_code:
        return ["PSLE"]
    elif "JUNIOR COLLEGE" in level_code or "JC" in level_code:
        return ["O-Levels"]
    else:
        return ["A-Levels"]

def main():
    # Fetch data from all endpoints
    print("Fetching data from APIs...")
    general_info_data = fetch_data(api_endpoints['general_info'])
    subjects_data = fetch_data(api_endpoints['subjects'])
    distinctive_programs_data = fetch_data(api_endpoints['distinctive_programs'])
    moe_programs_data = fetch_data(api_endpoints['moe_programs'])
    cca_data = fetch_data(api_endpoints['cca'])
    
    # Group data by school name
    print("Processing data...")
    
    # Group subjects by school
    school_subjects = {}
    for subject in subjects_data:
        school_name = subject.get('SCHOOL_NAME', '')
        if not school_name:
            continue
            
        if school_name not in school_subjects:
            school_subjects[school_name] = []
        
        subject_desc = subject.get('SUBJECT_DESC', '')
        if subject_desc and subject_desc not in school_subjects[school_name]:
            school_subjects[school_name].append(subject_desc)
    
    # Group distinctive programs by school
    school_programs = {}
    for program in distinctive_programs_data:
        school_name = program.get('school_name', '')
        if not school_name:
            continue
            
        if school_name not in school_programs:
            school_programs[school_name] = []
        
        alp_title = program.get('alp_title', '')
        llp_title1 = program.get('llp_title1', '')
        llp_title2 = program.get('llp_title2', '')
        
        if alp_title and alp_title != 'na' and alp_title not in school_programs[school_name]:
            school_programs[school_name].append(alp_title)
        
        if llp_title1 and llp_title1 != 'na' and llp_title1 not in school_programs[school_name]:
            school_programs[school_name].append(llp_title1)
        
        if llp_title2 and llp_title2 != 'na' and llp_title2 not in school_programs[school_name]:
            school_programs[school_name].append(llp_title2)
    
    # Group MOE programs by school
    for program in moe_programs_data:
        school_name = program.get('school_name', '')
        if not school_name:
            continue
            
        if school_name not in school_programs:
            school_programs[school_name] = []
        
        moe_program = program.get('moe_programme_desc', '')
        if moe_program and moe_program not in school_programs[school_name]:
            school_programs[school_name].append(moe_program)
    
    # Group CCAs by school
    school_ccas = {}
    for cca in cca_data:
        school_name = cca.get('school_name', '')
        if not school_name:
            continue
            
        if school_name not in school_ccas:
            school_ccas[school_name] = []
        
        cca_name = cca.get('cca_customized_name', '')
        if cca_name == 'na' or not cca_name:
            cca_name = cca.get('cca_generic_name', '')
        
        if cca_name and cca_name not in school_ccas[school_name]:
            school_ccas[school_name].append(cca_name)
    
    # Prepare data for MongoDB
    institutions = []
    
    for school in general_info_data:
        school_name = school.get('school_name', '')
        if not school_name:
            continue
        
        # Some school names might be in different formats in different datasets
        # Create variations to help with matching
        name_variations = [
            school_name,
            school_name.upper(),
            school_name.title(),
            ' '.join([word.capitalize() for word in school_name.split()])
        ]
        
        # Find matching subjects, programs, and CCAs
        courses_offered = []
        for name_var in name_variations:
            if name_var in school_subjects:
                courses_offered = school_subjects[name_var]
                break
        
        special_programs = []
        for name_var in name_variations:
            if name_var in school_programs:
                special_programs = school_programs[name_var]
                break
        
        ccas = []
        for name_var in name_variations:
            if name_var in school_ccas:
                ccas = school_ccas[name_var]
                break
        
        # Get coordinates
        coords = get_coordinates(school)
        
        # Prepare institution data
        institution = {
            'id': str(school.get('_id', '')),
            'name': school_name,
            'type': school.get('mainlevel_code', 'Unknown'),
            'location': f"{school.get('address', '')}, {school.get('postal_code', '')}, Singapore",
            'latitude': coords['latitude'],
            'longitude': coords['longitude'],
            'ranking': 0,  # Random ranking as placeholder
            'entryRequirements': get_entry_requirements(school.get('mainlevel_code', '')),
            'coursesOffered': courses_offered if courses_offered else [],
            'coCurricularActivities': ccas if ccas else [],  # No limit on CCAs
            'specialPrograms': special_programs if special_programs else [],  # No limit on special programs
            'description': generate_description(school),
            'imageUrl': random.choice(school_images)
        }
        
        institutions.append(institution)
    
    # Insert data into MongoDB
    if institutions:
        print(f"Inserting {len(institutions)} institutions into MongoDB...")
        
        # Drop existing collection if needed
        institution_collection.drop()
        
        # Insert new data
        institution_collection.insert_many(institutions)
        print(f"Successfully inserted {len(institutions)} institutions.")
    else:
        print("No institutions data to insert.")

if __name__ == "__main__":
    main()