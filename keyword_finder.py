
# coding: utf-8

# In[ ]:


import re


def find_words(df_row,words,feature,flag):
    
    """Finds 'flag' of 'words' in 'df_row' for 'feature' :
    
    :param df_row:  dataframe, row (is 'x' from df.apply(lambda x:....))   
    :param words:   string,    keywords to search in 'df_row'    
    :param feature: string,    in which feature/column to search 'words'    
    :param flag:    string,    ['count', 'set', 'exist'] telling which of 
                               the returns should be triggered
    :return:        if 'count': integer, 
                    if 'set':   list
                    if 'exist': integer binary
    """  
    
    my_list = re.findall(words,df_row[feature],flags=re.IGNORECASE)
    if flag == 'count':
        return(len(set(my_list)))
    elif flag == 'set':
        return(list(set(my_list)))
    elif flag == 'exist':
        return 1 if len(my_list)>0 else 0


def doctors_identifier(df_gr,word_list:list,feat1_count:str, feat2_set:str,thresh:int,flag:bool):
    
    """Adding 1 to the 'oculist'|'doctor' columns based on 'flag' if the 'word_list' is found in feat2_set.
       Also adds 1 to 'doctor' if the value of 'feat1_count' is above threshold('thresh')
       
    :param df_gr:        dataframe,  dataframe   
    :param word_list:    list,       list of words to search in 'feat2_set' column  
    :param feat1_count:  str,        column name //count of words found after find_words() function   
    :param feat2_set:    str,        column name //set of words found after find_words() function
    :param thresh:       int,        minimum count of words needed to increase 'doctor' by 1
    :param flag:         bool,       flag for adding 1 to 'oculist'|'oculist'&'doctor' based on feat2_set input values 
    
    """
    
    doc_int_ind = df_gr[df_gr[feat1_count]>=thresh].index
    df_gr.loc[doc_int_ind,'doctor'] += 1
    
    for doct_words in word_list:
        df_words = df_gr[feat2_set].apply(lambda x :doct_words in ' '.join(x).lower())
        words_ind = df_words[df_words==True].index
        if flag == 0: 
            df_gr.loc[words_ind,'oculist'] += 1
            df_gr.loc[words_ind,'doctor'] += 1
        elif flag == 1:
            df_gr.loc[words_ind,'oculist'] += 1






def trash_identifier(df_gr,feat1_count:str,thresh:int):
    
    """Adding 1 to the 'oculist'|'doctor' columns based on 'flag' if the 'word_list' is found in feat2_set.
       Also adds 1 to 'doctor' if the value of 'feat1_count' is above threshold('thresh')
       
    :param df_gr:        dataframe,  dataframe   
    :param feat1_count:  str,        column name //count of words found after find_words() function   
    :param thresh:       int,        minimum count of words needed to increase 'doctor' by 1 
    
    """
    
    doc_int_ind = df_gr[df_gr[feat1_count]>=thresh].index
    df_gr.loc[doc_int_ind,'trash'] += 1
    
    doc_int_ind_1 = df_gr[df_gr[feat1_count]>=1].index
    df_gr.loc[doc_int_ind_1,'trash'] += 1













