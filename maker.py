import os
import sys
class FileTreeMaker(object):

    def _recurse(self, parent_path, file_list, prefix, output_buf, level):
        if len(file_list) == 0:
            return
        else:
            file_list.sort(key=lambda f: os.path.isfile(os.path.join(parent_path, f)))
            for idx, sub_path in enumerate(file_list):

                full_path = os.path.join(parent_path, sub_path)
                idc = " ┣━ "
                if idx == len(file_list) - 1:
                    idc = " ┗━ "

                if os.path.isdir(full_path):
                    output_buf.append("%s%s[%s]" % (prefix, idc, sub_path))
                    if len(file_list) > 1 and idx != len(file_list) - 1:
                        tmp_prefix = prefix + " ┃  "
                    else:
                        tmp_prefix = prefix + "    "
                    self._recurse(full_path, os.listdir(full_path), tmp_prefix, output_buf, level + 1)
                elif os.path.isfile(full_path):
                    output_buf.append("%s%s%s" % (prefix, idc, sub_path))

    def make(self, mountedRoot):
        self.root = mountedRoot

        print("root:%s" % self.root)

        buf = []
        path_parts = self.root.rsplit(os.path.sep, 1)
        buf.append("[%s]" % (path_parts[-1],))
        self._recurse(self.root, os.listdir(self.root), "", buf, 0)

        output_str = "\n".join(buf)
        return output_str
        sys.exit(1)
