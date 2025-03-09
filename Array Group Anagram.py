ana=defaultdict(list)

        for i in strs:
            sw=''.join(sorted(i))
            ana[sw].append(i)

        return list(ana.values())
