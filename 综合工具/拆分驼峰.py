import re

def replace_camel_case(strings):
    pattern = re.compile(r'(?<=\w)([A-Z])')
    new_strings = []
    for string in strings:
        new_string = pattern.sub(r' \1', string)
        new_strings.append(new_string)
    return new_strings

# 示例输入
strings = ['NewLine',
'UseTabs',
'TabSize',
'IndentationSize',
'SpacingAfterMethodDeclarationName',
'SpaceWithinMethodDeclarationParenthesis',
'SpaceBetweenEmptyMethodDeclarationParentheses',
'SpaceAfterMethodCallName',
'SpaceWithinMethodCallParentheses',
'SpaceBetweenEmptyMethodCallParentheses',
'SpaceAfterControlFlowStatementKeyword',
'SpaceWithinExpressionParentheses',
'SpaceWithinCastParentheses',
'SpaceWithinOtherParentheses',
'SpaceAfterCast',
'SpaceBeforeOpenSquareBracket',
'SpaceBetweenEmptySquareBrackets',
'SpaceWithinSquareBrackets',
'SpaceAfterColonInBaseTypeDeclaration',
'SpaceAfterComma',
'SpaceAfterDot',
'SpaceAfterSemicolonsInForStatement',
'SpaceBeforeColonInBaseTypeDeclaration',
'SpaceBeforeComma',
'SpaceBeforeDot',
'SpaceBeforeSemicolonsInForStatement',
'SpacingAroundBinaryOperator',
'IndentBraces',
'IndentBlock',
'IndentSwitchSection',
'IndentSwitchCaseSection',
'IndentSwitchCaseSectionWhenBlock',
'LabelPositioning',
'WrappingPreserveSingleLine',
'WrappingKeepStatementsOnSingleLine',
'NewLinesForBracesInTypes',
'NewLinesForBracesInMethods',
'NewLinesForBracesInProperties',
'NewLinesForBracesInAccessors',
'NewLinesForBracesInAnonymousMethods',
'NewLinesForBracesInControlBlocks',
'NewLinesForBracesInAnonymousTypes',
'NewLinesForBracesInObjectCollectionArrayInitializers',
'NewLinesForBracesInLambdaExpressionBody',
'NewLineForElse',
'NewLineForCatch',
'NewLineForFinally',
'NewLineForMembersInObjectInit',
'NewLineForMembersInAnonymousTypes',
'NewLineForClausesInQuery']

# 转换为带空格的字符串列表
new_strings = replace_camel_case(strings)

# 打印输出
print('\n'.join(new_strings))