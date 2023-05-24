def show_table(data, header, max_text_view=15):
    """Format the data type table

    Parameters
    ----------
        data: list
            The data to show in the table
        header: list
            The header of the table
        max_text_view: int
            The max length of the text. If the text is larger than the "max_text_view",
            it will display "..."

    Returns
    -------
        None
    """
    # Variables to make the header
    top_header_part = ""
    middle_header_part = ""
    down_header_part = ""

    for title in header:
        len_title = len(title) + 1
        top_header_part += "+" + "-" * len_title + max_text_view * "-"
        middle_header_part += "| " + title + max_text_view * " "
        down_header_part += "+" + "-" * len_title + max_text_view * "-"
    table_header = top_header_part + "+\n" + \
        middle_header_part + "|\n" + down_header_part + "+\n"
    
    # Variables to make the table 
    n = len(data)
    table = ""

    for i in range(n):
        m = len(data[i])
        table_part = "| "
        for j in range(m):
            item = data[i][j]
            len_title = len(header[j])
            len_item = len(item)
            if len_item > max_text_view:
                table_part += item[:max_text_view - 3] + \
                    "..." + len_title * " " + "| "
            else:
                table_part += item + \
                    (max_text_view + len_title - len_item) * " " + "| "
        table += table_part + "\n"
    # Complete string table
    final_table = table_header + table + down_header_part + "+"
    print(final_table)

def show_list(data):
    """Format the data type list

    Parameters
    ----------
        data: list
            The data to show type list

    Returns
    -------
        None
    """
    for idx, value in enumerate(data, start = 1):
        print(f"{idx}.{value[1]}")
    print("") 

def list_any2list_str(data):
    """Convert all element of a matrix in type str

    Parameters
    ----------
        data: list
            The matrix that will be transform

    Returns
    -------
        ans: list
            The matrix with all elements type str
    """
    return [[str(ele) for ele in item] for item in data]


