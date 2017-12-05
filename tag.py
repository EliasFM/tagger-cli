# Python v2.7.3

# Imports
import os
import json
from sys import argv

# Internal packages
from colors import c
from alphabet import alphabet as abc
from tag_set import tags


class tagger():

    file_path = ""
    directory = "./data/"
    tags_dict = {}
    data = []
    tagged = []
    untagged = []
    valid = []
    invalid = []

    def dict(self):
        # Set up tag dictionary
        counter = 0
        for t in tags.list:
            self.tags_dict[abc.list[counter]] = t
            counter = counter + 1

    def init(self):
        for d in self.data:
            if "tags" not in d.keys():
                self.untagged.append(d)
            else:
                self.tagged.append(d)

        print
        print c().printGreen(str(len(self.untagged))) + " comments left to tag out of " + c().printGreen(str(len(self.data)))
        print
        print "Begin tagging..."
        print "\n"*3

    def init_check(self):
        group1 = [tags.list[0], tags.list[1]]
        group2 = [tags.list[2], tags.list[3], tags.list[4], tags.list[5]]
        group3 = [tags.list[6], tags.list[7]]
        group4 = [tags.list[8], tags.list[9]]
        group5 = [tags.list[10], tags.list[11]]
        group6 = [tags.list[12], tags.list[13]]

        for d in self.data:
            is_valid = True
            if "tags" in d.keys():
                counts = [0, 0, 0, 0, 0, 0]
                for t in d["tags"]:
                    print t
                    if t in group1:
                        counts[0] = counts[0] + 1
                    if t in group2:
                        counts[1] = counts[1] + 1
                    if t in group3:
                        counts[2] = counts[2] + 1
                    if t in group4:
                        counts[3] = counts[3] + 1
                    if t in group5:
                        counts[4] = counts[4] + 1
                    if t in group6:
                        counts[5] = counts[5] + 1
                for i in counts:
                    if i > 1:
                        is_valid = False
            if is_valid:
                self.valid.append(d)
            else:
                self.invalid.append(d)

    def choose_file(self):
        # List data files in directory
        files = []
        for (dirpath, dirnames, filenames) in os.walk(self.directory):
            for f in filenames:
                if ".js" in f:
                    files.append(f)

        # Instruct user to choose a file
        for i, f in enumerate(files):
            print c().printHeader("Enter " + c().printBlue(str(i)) + " for file: ") + c().printBlue(f)

        # Allow user to enter number
        index = int(raw_input().strip())
        while index >= len(files):
            print c().printWarn("Index out of bounds. Enter a valid number.")
            index = int(raw_input().strip())

        # Open up data file and return
        self.file_path = self.directory + files[index]
        print self.file_path
        js_data = open(self.file_path).read()
        data = json.loads(js_data)['data']
        self.data = data

    def prompt_msg(self, msg):
        print "id: " + c().printHeader(msg['id'])
        print "time: " + c().printBlue(msg['created_time'])
        print "message: " + c().printGreen(msg['message'])
        print

    def instruct(self):
        counter = 0
        for i in range(0, len(abc.list)):
            if abc.list[i] in self.tags_dict.keys():
                key = abc.list[i]
                print "Enter " + c().printBlue(key) + " to tag as " + c().printGreen(self.tags_dict[key])
                counter = counter + 1
        print

    def addTags(self, obj, tags):
        tags_list = []
        for t in tags:
            tags_list.append(self.tags_dict.get(t))
        obj['tags'] = tags_list

    def edit_msg(self, u):
        self.prompt_msg(u)
        self.instruct()
        wait = raw_input().replace(" ", "")
        tags = list(set(wait))
        self.addTags(u, tags)
        print u['tags']
        print

    def get_merge(self, a_set, b_set):
        merge = []
        for u in a_set:
            merge.append(u)
        for t in b_set:
            merge.append(t)
        return merge

    def sort_date(self, data):
        return sorted(data, key=lambda k: k['created_time'])

    def write_data(self, obj):
        print c().printGreen("Data merging...")
        assert self.file_path is not None, "FILE NOT SET"
        with open(self.file_path, 'wt') as out:
            res = json.dump(obj, out, sort_keys=True, indent=2, separators=(',', ': '))
        print c().printGreen("Data merged into ") + c().printHeader(self.file_path)

    def merge_data(self):
        merge = self.get_merge(self.untagged, self.tagged)
        merge = self.sort_date(merge)
        obj = {"data": merge}
        self.write_data(obj)

    def merge_data_check(self):
        merge = self.get_merge(self.invalid, self.valid)
        merge = self.sort_date(merge)
        obj = {"data": merge}
        self.write_data(obj)

    def main(self):
        self.init()
        print c().printBlue("This loop edits untagged comments.")
        for u in self.untagged:
            self.edit_msg(u)
            print c().printBlue("Enter \'q\' to exit and save.")
            print c().printHeader("Enter any key to continue.")
            print
            if raw_input().strip() == "q":
                self.merge_data()
                break

    def edit(self):
        self.init()
        print c().printBlue("Edit message? Enter \'q\' to exit and save.")
        print c().printHeader("Enter any key to continue.")
        while raw_input().strip() != "q":
            print c().printHeader("Enter the ID of the message you want to edit.")
            search = raw_input().strip()
            relevant = []
            for u in self.untagged:
                relevant.append(u)
            for t in self.tagged:
                relevant.append(t)
            find = [m for m in relevant if m['id'] == search]
            if len(find) > 0:
                edit_msg(find[0])
            print c().printBlue("Edit another? Enter \'q\' to exit and save.")
            print c().printHeader("Enter any key to continue.")
            print
        self.merge_data()

    def clear_all_tags(self):
        self.init()
        print c().printBlue("Are you sure you want to clear all tags?")
        print c().printHeader("Type \'yes\' to clear all tags.")
        print c().printWarn("WARNING: This cannot be reverted.")
        print c().printHeader("Enter any other key to quit.")
        print
        if raw_input().strip() == "yes":
            for u in self.untagged:
                u.pop('tags', None)
            for t in self.tagged:
                t.pop('tags', None)
        else:
            return
        print c().printBlue("Ready to save. Are you sure?")
        print c().printHeader("Type \'yes\' to clear all tags.")
        print c().printWarn("WARNING: This cannot be reverted.")
        print c().printHeader("Enter any other key to quit.")
        print
        if raw_input().strip() == "yes":
            self.merge_data()
        else:
            return

    def check(self):
        self.init_check()
        print c().printBlue("This loop edits comments with invalid tagging.")
        for i in self.invalid:
            self.edit_msg(i)
            print c().printBlue("Enter \'q\' to exit and save.")
            print c().printHeader("Enter any key to continue.")
            print
            if raw_input().strip() == "q":
                self.merge_data_check()
                break


if __name__ == '__main__':
    tagger = tagger()
    tagger.dict()
    tagger.choose_file()
    if len(argv) == 1:
        tagger.main()
    elif len(argv) == 2:
        call = {"main": tagger.main, "edit": tagger.edit, "clear": tagger.clear_all_tags, "check": tagger.check}
        call[argv[1]]()
