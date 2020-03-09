from bs4 import BeautifulSoup


def my_add(x, y):
    """
    This functions adds x and y args

    Args:
        x: x parameter
        y: y parameter

    Returns:
        x+y

    Examples:
        >>> my_add(1,2)
    """
    return x + y


def parse_dobie_response(xml_response):
    """
    The following function is used to get DOBIE responses and parses annotated tools

    Args:
        xml_response: DOBIE response

    Returns:
        extracted_skills: list of dict
        >>> [{'string': 'CustomerSupport', 'frequencyOfMention': '1', 'kind': 'topic'}, {'string': 'Security', 'frequencyOfMention': '1', 'kind': 'topic'}]

    Examples:
        >>> parse_dobie_response(
        '''<Annotation Id="0" Type="Split" StartNode="42" EndNode="42">
            <Feature>
              <Name className="java.lang.String">kind</Name>
              <Value className="java.lang.String">external</Value>
            </Feature>
        </Annotation>'''
        )
    """
    soup = BeautifulSoup(xml_response, "xml")
    annotations = soup.find_all('Annotation')

    extracted_skills = []

    for annotation in annotations:
        features = annotation.select('Feature')
        skills = dict()

        for feature in features:
            name = feature.Name.text
            value = feature.Value.text

            if value != 'external':
                skills['{}'.format(name)] = value

            if skills:
                extracted_skills.append(skills)
    return skills