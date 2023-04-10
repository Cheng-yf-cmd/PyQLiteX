/**
 * @kind problem
 * @id py/FunctionFind
 */

import python

from Function f
where f.getScope() instanceof Function
select f, f.getName()