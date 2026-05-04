-- Approach:
-- We categorize each node using a CASE statement based on the following conditions:
-- 1. If p_id is NULL, it's the Root.
-- 2. If the node's id exists in the p_id column of the table (meaning it is a parent to someone else)
--    and it's not the root, it's an Inner node.
-- 3. Otherwise, it's a Leaf node.

SELECT
    id,
    CASE
        WHEN p_id IS NULL THEN 'Root'
        WHEN id IN (SELECT p_id FROM Tree) THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM
    Tree;