import json
from colors import c
from alphabet import alphabet as abc
from tag_set import tags
from sys import argv

file = "15704546335_10156308025161336"
filename = "./data/{}.js".format(file)

js_data = open(filename).read()
data = json.loads(js_data)['data']

tags_dict = {}
tagged = []
untagged = []


def init():
    counter = 0
    for t in tags.list:
        tags_dict[abc.list[counter]] = t
        counter = counter + 1

    print tags_dict

    for d in data:
        if "tags" not in d.keys():
            untagged.append(d)
        else:
            tagged.append(d)

    print
    print c().printGreen(str(len(untagged))) + " comments left to tag out of " + c().printGreen(str(len(data)))
    print
    print "Begin tagging..."
    print "\n"*3


def prompt_msg(msg):
    print "id: " + c().printHeader(msg['id'])
    print "time: " + c().printBlue(msg['created_time'])
    print "message: " + c().printGreen(msg['message'])
    print


def instruct():
    counter = 0
    for i in range(0, len(abc.list)):
        if abc.list[i] in tags_dict.keys():
            key = abc.list[i]
            print "Enter " + c().printBlue(key) + " to tag as " + c().printGreen(tags_dict[key])
            counter = counter + 1
    print


def addTags(obj, tags):
    tags_list = []
    for t in tags:
        tags_list.append(tags_dict.get(t))
    obj['tags'] = tags_list


def edit_msg(u):
    prompt_msg(u)
    instruct()
    wait = raw_input().replace(" ", "")
    tags = list(set(wait))
    addTags(u, tags)
    print u['tags']
    print


def merge_data():

    merge = []
    for u in untagged:
        merge.append(u)
    for t in tagged:
        merge.append(t)
    obj = {"data": merge}
    # print c().printHeader(str(merge))

    print c().printGreen("Data merging...")
    name = './data/{}.js'.format(file)
    with open(name, 'wt') as out:
        res = json.dump(obj, out, sort_keys=True, indent=2, separators=(',', ': '))
    print c().printGreen("Data merged into ") + c().printHeader(name)


def main():
    init()
    print c().printBlue("This loop edits untagged comments.")
    for u in untagged:
        edit_msg(u)
        print c().printBlue("Enter \'q\' to exit.")
        print c().printHeader("Enter any key to continue.")
        print
        if raw_input().strip() == "q":
            merge_data()
            break


def edit():
    init()
    print c().printBlue("Edit message? Enter \'q\' to exit.")
    print c().printHeader("Enter any key to continue.")
    while raw_input().strip() != "q":
        print c().printHeader("Enter the ID of the message you want to edit.")
        search = raw_input().strip()
        relevant = []
        for u in untagged:
            relevant.append(u)
        for t in tagged:
            print t
            relevant.append(t)
        # print relevant
        find = [m for m in relevant if m['id'] == search]
        if len(find) > 0:
            edit_msg(find[0])
        print c().printBlue("Edit another? Enter \'q\' to exit.")
        print c().printHeader("Enter any key to continue.")
        print
    merge_data()


if __name__ == '__main__':
    if len(argv) == 1:
        main()
    elif len(argv) == 2:
        call = {"main": main, "edit": edit}
        call[argv[1]]()
