import re
import numpy as np
class DecisionTreeParser:

    def __init__(self,string_tree,features_names):
        self.tree = string_tree
        self.features_names_from_index = {str(i):name for i, name in enumerate(features_names)}
        self.class_to_target = {};
    def eval_comp(self,user_answer, sign, numb):
        if sign == '<=':
            return user_answer <= numb;
        elif sign == '<':
            return user_answer < numb;
        elif sign == '=':
            return user_answer == numb
        elif sign == '>':
            return user_answer > numb;
        elif sign == '>=':
            return user_answer >= numb;

    def parse_tree(self):
        current_level = 0
        level_spacing = '|   '
        listed = self.tree.split('\n')
        while True:

            feature_decision = current_level*level_spacing +'|--- feature_'+re.findall(r'feature_(\d)',listed[0])[0]
            feature_index = re.findall(r'feature_(\d)',listed[0])[0]
            print('Question' + self.features_names_from_index[feature_index])
            feature_rules_unparsed = [[i,x] for i,x in enumerate(listed) if feature_decision in x]

            # get user answer
            user_answer = 1
            #parse if leave
            [rule_line, rule] = feature_rules_unparsed[0]
            [alternative_rule_line, alternative_rule] = feature_rules_unparsed[1]

            threshold = float(re.findall('\d+\.\d+',rule)[0])
            operand = re.findall("([><=]{1,2})", rule)[0]
            condition = self.eval_comp(user_answer,operand,threshold)
            if condition:
                listed = listed[rule_line+1:alternative_rule_line]
                next_line = rule_line+1
            else:
                listed = listed[alternative_rule_line:]
                next_line = 1
            class_lookup = (current_level+1)*level_spacing +'|--- class: '
            if class_lookup in listed[next_line]:
                class_number = int(re.findall('class: (\d+)',listed[next_line])[0])
                break
            else:
                current_level+=1
        print(class_number)
        # for [i,rule,next_i,next_rule_line] in feature_rules_unparsed:
        #     #evaluate_rule
        #     condition=True
        #     # if no - go to next level
        #     if 'class' not in next_rule_line and condition:
        #         current_level+=1
        #
        #         pass


