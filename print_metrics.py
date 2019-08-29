def get_extracted_text_file_path(chapter):
    extracted_text_file_path = {
         # Chapter 4 start #
         4: "ITIL Books/ITIL 3/Service operation chapter 4/Service operation chapter 4 - 4.txt",

         # Chapter 4 - 4.1 to 4.1.4 #
         4.1: "ITIL Books\ITIL 3\Service operation chapter 4\Automated concepts extracted\\4.1\Service operation chapter 4 - 4.1 to 4.1.4.txt",

         # Chapter 4 - 4.2 to 4.2.4 #
         4.2: "ITIL Books\ITIL 3\Service operation chapter 4\Automated concepts extracted\\4.2\Service operation chapter 4 - 4.2 to 4.2.4.txt",

         # Chapter 4 - 4.3 to 4.3.4 #
         4.3: "ITIL Books\ITIL 3\Service operation chapter 4\Automated concepts extracted\\4.3\Service operation chapter 4 - 4.3 to 4.3.4.txt",

         # Chapter 4 - 4.4 to 4.4.4 #
         4.4: "ITIL Books\ITIL 3\Service operation chapter 4\Automated concepts extracted\\4.4\Service operation chapter 4 - 4.4 to 4.4.4.txt",

         # Chapter 4 - 4.5 to 4.5.4 #
         4.5: "ITIL Books\ITIL 3\Service operation chapter 4\Automated concepts extracted\\4.5\Service operation chapter 4 - 4.5 to 4.5.4.txt",

         # Chapter 4 - 4.6 to 4.6.4 #
         4.6: "ITIL Books\ITIL 3\Service operation chapter 4\Automated concepts extracted\\4.6\Service operation chapter 4 - 4.6 to 4.6.4.txt"
    }

    return extracted_text_file_path[chapter]

def get_manual_concepts_file_path(chapter):
        manual_concepts_file_path = {
            # Chapter 4 start #
            4: "ITIL Books/ITIL 3/Service operation chapter 4/Automated concepts extracted/4/Manual concepts extracted 4.txt",

            # Chapter 4 - 4.1 to 4.1.4 #
            4.1: "ITIL Books/ITIL 3/Service operation chapter 4/Automated concepts extracted/4.1/Manual concepts extracted 4.1.txt",

            # Chapter 4 - 4.2 to 4.2.4 #
            4.2: "ITIL Books/ITIL 3/Service operation chapter 4/Automated concepts extracted/4.2/Manual concepts extracted 4.2.txt",

            # Chapter 4 - 4.3 to 4.3.4 #
            4.3: "ITIL Books/ITIL 3/Service operation chapter 4/Automated concepts extracted/4.3/Manual concepts extracted 4.3.txt",

            # Chapter 4 - 4.4 to 4.4.4 #
            4.4: "ITIL Books/ITIL 3/Service operation chapter 4/Automated concepts extracted/4.4/Manual concepts extracted 4.4.txt",

            # Chapter 4 - 4.5 to 4.5.4 #
            4.5: "ITIL Books/ITIL 3/Service operation chapter 4/Automated concepts extracted/4.5/Manual concepts extracted 4.5.txt",

            # Chapter 4 - 4.6 to 4.6.4 #
            4.6: "ITIL Books/ITIL 3/Service operation chapter 4/Automated concepts extracted/4.6/Manual concepts extracted 4.6.txt"
        }

        return manual_concepts_file_path[chapter]

def lemmatize_list(list):
    from nltk.stem import WordNetLemmatizer

    lemmatizer = WordNetLemmatizer()

    return [lemmatizer.lemmatize(element) for element in list]

def print_metrics(manual_concepts_file_path, all_noun_phrases, lemmatize_first=False, debug=False, remove_duplicates=True):
    with open(manual_concepts_file_path, 'r') as file:
        manual_concepts = file.read()

    manual_concepts_list = manual_concepts.split('\n')
    manual_concepts_list = [x.lower() for x in manual_concepts_list]

    if lemmatize_first:
        manual_concepts_list = lemmatize_list(manual_concepts_list)

    # automatic_concepts_list = ['Service Operation', 'processes', 'paragraph', 'detail', 'chapter', 'reference', 'structure', 'processes', 'detail', 'chapter', 'Please note', 'roles', 'process', 'tools', 'process', 'Chapters', 'Management', 'process', 'monitors', 'events', 'IT infrastructure', 'operation', 'exception conditions', 'Incident Management', 'service', 'users', 'order', 'business impact', 'Problem Management', 'root-cause analysis', 'cause', 'events', 'incidents', 'activities', 'problems/incidents', 'Known Error subprocess', 'quicker diagnosis', 'resolution', 'incidents', 'NOTE', 'distinction', 'incidents', 'problems', 'Incident', 'Problem Records', 'danger', 'Incidents', 'support cycle', 'actions', 'recurrence', 'incidents', 'Incidents', 'root cause analysis', 'visibility', 'user ’ s service', 'SLA targets', 'service', 'users', 'expectations', 'results', 'number', 'incidents', '‘ purge ’', 'visibility', 'issues', 'Request Fulfilment', 'management', 'customer', 'user requests', 'incident', 'service delay', 'disruption', 'organizations', 'requests', 'category ’', 'incidents', 'information', 'Incident Management system', 'others', 'volumes', 'business priority', 'requests', 'provision', 'Request Fulfilment', 'Request Fulfilment process', 'practice', 'Request Fulfilment process', 'customer', 'user requests', 'types', 'requests', 'facilities', 'moves', 'supplies', 'IT services', 'requests', 'SLA measures', 'records', 'process flow', 'practice', 'organizations', 'Access Management', 'process', 'users', 'right', 'service', 'access', 'users', 'users', 'ability', 'access services', 'stages', 'resources', 'HR', 'lifecycle', 'Access Management', 'Identity', 'Rights Management', 'organizations', 'addition', 'processes', 'Service Operation', 'phases', 'Service Management Lifecycle', 'aspects', 'processes', 'part', 'chapter', 'include', 'Change Management', 'process', 'Configuration Management', 'Release Management', 'topics', 'Service Transition publication', 'Capacity', 'Availability Management', 'aspects', 'publication', 'detail', 'Service Design publication', 'Financial Management', 'Service Strategy publication', 'Knowledge Management', 'Service Transition publication', 'IT Service Continuity', 'Service Design publication', 'Service Reporting', 'Measurement', 'Continual Service Improvement publication']
    automatic_concepts_list = all_noun_phrases
    automatic_concepts_list = [x.lower() for x in automatic_concepts_list]

    # Remove duplicates from lists
    if remove_duplicates:
        manual_concepts_list = list(dict.fromkeys(manual_concepts_list))
        automatic_concepts_list = list(dict.fromkeys(automatic_concepts_list))

    if debug:
        print(f"All noun phrases\n{all_noun_phrases}")
        print(f"manual concepts\n{manual_concepts_list}")

    count = 0
    for concept in manual_concepts_list:
        if concept in automatic_concepts_list:
            count = count + 1

    number_of_fully_correct_manual_concepts = count

    number_of_manual_concepts = len(manual_concepts_list)

    count = 0
    for concept in automatic_concepts_list:
        if concept in manual_concepts_list:
            count = count + 1

    number_of_fully_correct_automatic_concepts = count

    number_of_automatic_concepts = len(automatic_concepts_list)

    print(f"number_of_manual_concepts: {number_of_manual_concepts}")
    print(f"number_of_automatic_concepts: {number_of_automatic_concepts}")
    print(f"number_of_fully_correct_manual_concepts: {number_of_fully_correct_manual_concepts}")
    print(f"number_of_fully_correct_automatic_concepts: {number_of_fully_correct_automatic_concepts}")

    # Lists to words for partial matches
    automatic_concepts_list_single_words = [x.split() for x in automatic_concepts_list]
    # print(automatic_concepts_list_single_words)

    manual_concepts_list_single_words = [x.split() for x in manual_concepts_list]
    # print(manual_concepts_list_single_words)

    count = 0
    for concept in manual_concepts_list_single_words:
        for word in concept:
            if word in ' '.join(automatic_concepts_list).split():
                count = count + 1
                break

    number_of_full_and_partial_correct_manual_concepts = count
    print(f"number_of_full_and_partial_correct_manual_concepts: {number_of_full_and_partial_correct_manual_concepts}")

    count = 0
    for concept in automatic_concepts_list_single_words:
        for word in concept:
            if word in ' '.join(manual_concepts_list).split():
                count = count + 1
                break

    number_of_full_and_partial_correct_automatic_concepts = count
    print(f"number_of_full_and_partial_correct_automatic_concepts: {number_of_full_and_partial_correct_automatic_concepts}")