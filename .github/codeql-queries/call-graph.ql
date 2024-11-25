import java

from Method caller, MethodAccess call, Method callee
where
  // The method being called
  call.getCallee() = callee and
  // The method containing the call
  call.getEnclosingCallable() = caller
select caller, callee, call, "Call graph relationship found."
