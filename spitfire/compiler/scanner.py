# Copyright 2007 The Spitfire Authors. All Rights Reserved.
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from spitfire.compiler import parser
from spitfire.third_party.yapps2 import yappsrt

# SpitfireScanner uses the order of the match, not the length of the match to
# determine what token to return. I'm not sure how fragille this is long-term,
# but it seems to have been the right solution for a number of small problems
# allong the way.
_restrict_cache = {}
human_patterns = dict([
            ('DOT', '.'),
            ('NUM', 'valid number'),
            ('ID', 'valid identifier'),
            ('SINGLE_QUOTE_STR', 'single quoted string literal'),
            ('DOUBLE_QUOTE_STR', 'single quoted string literal'),
            ('SINGLE_LINE_COMMENT', 'single line comment'),
            ('MULTI_LINE_COMMENT', 'multi line comment'),
            ('ASSIGN_OPERATOR', '='),
            ('COMP_OPERATOR', '"<=", ">=", "==", ">", "<", "!=", "in"'),
            ('OPEN_PAREN', '('),
            ('PLACEHOLDER_OPEN_PAREN', '('),
            ('CLOSE_PAREN', ')'),
            ('OPEN_BRACKET', '['),
            ('CLOSE_BRACKET', ']'),
            ('PLACEHOLDER_OPEN_BRACE', '{'),
            ('PLACEHOLDER_CLOSE_BRACE', '['),
            ('OPEN_BRACE', '{'),
            ('CLOSE_BRACE', '[ \t]*\\}[ \t]*'),
            ('PIPE', '|'),
            ('COMMA_DELIMITER', ','),
            ('COLON_DELIMITER', ':'),
            ('SPACE', '" "'),
            ('CLOSE_DIRECTIVE_TOKEN', 'either "\\n" or "#"'),
            ('END_DIRECTIVE', '#end'),
            ('START_DIRECTIVE', '#'),
            ('START_PLACEHOLDER', '\\$'),
            ('LITERAL_DOLLAR_SIGN', '\\\\\\$'),
            ('LITERAL_HASH', '\\\\#'),
            ('LITERAL_BACKSLASH', '\\\\'),
            ('NEWLINE', '\\n'),
            ('PYTHON_LINE', '.+'),
            ('END', '$'),
        ])

class SpitfireScanner(parser._SpitfireParserScanner):

    def token(self, i, restrict=0):
        """Get the i'th token, and if i is one past the end, then scan
        for another token; restrict is a list of tokens that
        are allowed, or 0 for any token."""
        if i == len(self.tokens):
            self.scan(restrict)
        if i < len(self.tokens):
            # Make sure the restriction is more restricted
            restriction = self.restrictions[i]
            if restrict and restriction:
                if not restriction.issuperset(restrict):
                    raise NotImplementedError(
                        "Unimplemented: restriction set changed", restrict,
                        self.restrictions[i])
                return self.tokens[i]
            elif not restrict and not restriction:
                return self.tokens[i]
        raise yappsrt.NoMoreTokens(i, len(self.tokens), self.tokens[i],
                                   restrict, self.restrictions[i], self.tokens)

    def scan(self, restrict):
        """Should scan another token and add it to the list, self.tokens,
        and add the restriction to self.restrictions"""
        # Cache the list of patterns we check to avoid unnecessary iteration
        restrict = frozenset(restrict)
        try:
            patterns = _restrict_cache[restrict]
        except KeyError:
            patterns = [pair
                        for pair in self.patterns
                        if not restrict or pair[0] in restrict]
            _restrict_cache[restrict] = patterns

        _input, _pos = self.input, self.pos
        for best_pat, regexp in patterns:
            m = regexp.match(_input, _pos)
            if m:
                tname = m.group(0)
                best_match = len(tname)
                # msolo: use the first match, not the 'best'
                break
        else:
            # If we didn't find anything, raise an error
            msg = "Bad Token"
            if restrict:
                msg = "\033[1;31m \n ==========ERROR=========: \n Expected "
                for r in restrict: 
                    msg += human_patterns.get(r, r) + ','

                msg+="\033[1;m "
            raise yappsrt.SyntaxError(self.pos, msg)

        # Create a token with this data
        end = _pos + best_match
        token = (_pos, end, best_pat, tname)
        self.pos = end
        # Only add this token if it's not in the list
        # (to prevent looping)
        if not self.tokens or token != self.tokens[-1]:
            self.tokens.append(token)
            self.restrictions.append(restrict)
        return
