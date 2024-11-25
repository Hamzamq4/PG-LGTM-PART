/**
 * @name Method Call Relationships
 * @description Extracts caller and callee method pairs to build a call graph.
 * @kind path-problem
 * @problem.severity info
 * @tags call-graph
 */

import java

/**
 * Represents a call relationship between two methods.
 */
class MethodCall extends CallExpr {
  MethodCall() { this instanceof CallExpr }
}

from Method caller, Method callee, MethodCall call
where
  call.getMethod() = callee and
  call.getEnclosingCallable() = caller
select call, caller, callee, "Method " + caller.getName() + " calls " + callee.getName()
