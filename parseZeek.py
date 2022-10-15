def print_ans(list, counter):
    for i in range(len(list)):
        if i >= counter:
            break
        print(str(i + 1) + ". " + list[i][0] + ", " + str(list[i][1]))
    print('-----------------------------------------------------')

def extract_and_sort(file, pos_list):
    dict = {}

    for line in file.readlines():
        # Skip the comment part
        if line.startswith('#') == True:
            continue
        
        # Split line by Tab ('\t')
        split_list = line.split("\t")
        
        # Get the first designate field
        data = split_list[pos_list[0]]

        # Concatenate multiple fields together
        if len(pos_list) >= 2:
            for i in range(1, len(pos_list)):
                data =  ", ".join([data, split_list[pos_list[i]]])

        # Data hasn't been recorded
        if dict.get(data, False) == False:
            # Record data to the dictionary in the form of "data - the number of data"
            dict[data] = 1
        else:
            # Update the number of data in the list 
            dict[data] = dict[data] + 1

    # Move the file descriptor back to the beginning of the file
    file.seek(0)

    # Sort the dictionary in descending order
    return sorted(dict.items(), key = lambda dict : dict[1], reverse=True)

def main():
    conn_log = open("conn.log", "r")
    originator_host = extract_and_sort(conn_log, [2])
    print("Top 10 most active originator host in the form of (host, times)")
    print_ans(originator_host, 10)

    http_log = open("http.log", "r")
    visited_host = extract_and_sort(http_log, [8])
    print("Top 10 most visited host in HTTP in the form of (host, times)")
    print_ans(visited_host, 10)

    dns_log = open("dns.log", "r")
    queried_host = extract_and_sort(dns_log, [9])
    dns_log.close()
    print("Top 10 most queried name in DNS in the form of (queried name, times)")
    print_ans(queried_host, 10)
    
    pair_host = extract_and_sort(conn_log, [2, 4])
    conn_log.close()
    print("Top 10 most pair of hosts in conn.log in the form of (pair, times)")
    print_ans(pair_host, 10)

    user_agent = extract_and_sort(http_log, [12])
    http_log.close()
    print("Top 10 most popular user agent in HTTP in the form of (user agent, times)")
    print_ans(user_agent, 10)

if __name__ == "__main__":
    main()