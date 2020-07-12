import re
import numpy as np
import constants
class DecisionTreeParser:

    def __init__(self,string_tree,features_names):
        self.tree = string_tree
        self.features_names_from_index = {int(i):name for i, name in enumerate(features_names)}
        self.class_to_target = {}

    def eval_comp(self,user_answer, sign, numb):
        if sign == '<=':
            return user_answer <= numb
        elif sign == '<':
            return user_answer < numb
        elif sign == '=':
            return user_answer == numb
        elif sign == '>':
            return user_answer > numb
        elif sign == '>=':
            return user_answer >= numb

    def get_first_question(self):

        listed = self.tree.split('\n')
        question_index = int(re.findall(r'feature_(\d)', listed[0])[0])
        question = self.features_names_from_index[question_index]

        return Tree_node(is_leaf=False,current_question=question)

    def update_classification(self, answer_sequence):
        class_lookup = '|--- class: '
        current_level = 0
        next_question=''
        current_question =''
        level_spacing = '|   '
        listed = self.tree.split('\n')
        next_line = 0

        next_question_index=0
        for i,user_answer in enumerate(answer_sequence):

            # if i!=0:
            #     question_index=next_question_index
            #     feature_decision='|--- feature_'+str(question_index)
            # else:
            question_index = int(re.findall(r'feature_(\d)', listed[0])[0])
            feature_decision = '|--- feature_' + str(question_index)
            #feature_decision = '|--- feature_'+re.findall(r'feature_(\d)',listed[0])[0]


            current_question = self.features_names_from_index[question_index]

            feature_rules_unparsed = [[i,x] for i,x in enumerate(listed) if feature_decision in x]
            [rule_line, rule] = feature_rules_unparsed[0]
            [alternative_rule_line, alternative_rule] = feature_rules_unparsed[1]

            threshold = float(re.findall('\d+\.\d+',rule)[0])
            operand = re.findall("([><=]{1,2})", rule)[0]
            condition = self.eval_comp(user_answer,operand,threshold)
            if condition:
                listed = listed[rule_line+1:alternative_rule_line]
                next_line = 0
            else:
                listed = listed[alternative_rule_line+1:]
                next_line = 0


            # parse if leaf
            if class_lookup in listed[next_line]:
                class_number = int(re.findall('class: (\d+)',listed[next_line])[0])
                target_name = constants.class_to_target[class_number]
                return Tree_node(is_leaf=True,target_name=target_name,current_question=current_question,next_question='endpoint')
            else:
                current_level+=1
                next_question_index = int(re.findall(r'feature_(\d)',listed[next_line])[0])
                next_question = self.features_names_from_index[next_question_index]

        return Tree_node(is_leaf=False,next_question=next_question,current_question=current_question)

class Tree_node:
    def __init__(self,is_leaf=False,target_name='unknown target',current_question ='unknown cq',next_question='unknown nq'):
        self.is_leaf = is_leaf
        self.target_name = target_name

        self.next_question = next_question
        self.current_question = current_question



