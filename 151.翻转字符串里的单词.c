/*
 * @lc app=leetcode.cn id=151 lang=c
 *
 * [151] 翻转字符串里的单词
 */

// @lc code=start


char * reverseWords(char * s){
    // strip
    int i, j, k, m;
    for (i = strlen(s) - 1; i >= 0; i--)
    {
        if (*(s + i) != ' ')
        {
            *(s + i + 1) = '\0';
            break;
        }
    }
    if (i == -1 && *(s + i + 1) != '\0')
        *s = '\0';
    for (i = 0; i < strlen(s); i++)
    {
        if (*(s + i) != ' ')
        {
            s += i;
            break;
        }
    }
    bool inword = true;
    for (i = 0, j = 0; *(s + j) != '\0'; )
    {
        if (*(s + j) == ' ')
        {
            if (inword)
            {
                *(s + i++) = *(s + j++);
                inword = false;
            }
            else
                j++;
        }
        else
        {
            *(s + i++) = *(s + j++);
            if (!inword)
                inword = true;
        }
    }
    *(s + i) = '\0';
    for (i = 0, j = strlen(s) - 1; i < j; i++, j--)
    {
        char tmp = *(s + i);
        *(s + i) = *(s + j);
        *(s + j) = tmp;
    }
    for (j = 0, k = 0; j < strlen(s) + 1; j++)
    {
        if (*(s + j) == ' ' || *(s + j) == '\0')
        {
            for (i = k, m = j - 1; i < m; i++, m--)
            {
                char tmp = *(s + i);
                *(s + i) = *(s + m);
                *(s + m) = tmp;
            }
            k = j + 1;
        }
    }
    return s;
}


// @lc code=end

